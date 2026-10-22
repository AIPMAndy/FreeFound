#!/usr/bin/env python3
"""FreeFound 静态数据完整性检查。它不联网，不能验证外部网站是否仍然有效。"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []

def err(path, index, msg):
    ERRORS.append(f"{path.name}[{index}]: {msg}")

def is_valid_link(value):
    if not isinstance(value, str):
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc) and not (
        parsed.hostname == "example.com" or (parsed.hostname or "").endswith(".example.com")
    )

def load(path):
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(obj, list):
            raise ValueError("root must be an array")
        return obj
    except (ValueError, OSError) as e:
        ERRORS.append(f"{path}: {e}")
        return []

def check_unique(rows, path, field):
    seen = set()
    for idx, row in enumerate(rows):
        if not isinstance(row, dict):
            err(path, idx, "must be object")
            continue
        val = row.get(field)
        if not isinstance(val, str) or not val.strip():
            err(path, idx, f"missing {field}")
        elif val in seen:
            err(path, idx, f"duplicate {field}")
        seen.add(val)

def main():
    paths = [ROOT / "data" / n for n in ("resources.json", "hackathons.json", "incubators.json")]
    resources, hackathons, incubators = [load(p) for p in paths]
    for rows, path, key in zip((resources, hackathons, incubators), paths, ("url", "link", "name")):
        check_unique(rows, path, key)
    for idx, x in enumerate(resources):
        if not isinstance(x, dict): continue
        for key in ("name", "category", "description"):
            if not isinstance(x.get(key), str) or not x[key].strip(): err(paths[0], idx, f"missing {key}")
        if not is_valid_link(x.get("url")): err(paths[0], idx, "invalid URL")
    for idx, x in enumerate(hackathons):
        if not isinstance(x, dict): continue
        for key in ("title", "location", "source"):
            if not isinstance(x.get(key), str) or not x[key].strip(): err(paths[1], idx, f"missing {key}")
        if not is_valid_link(x.get("link")): err(paths[1], idx, "invalid/placeholding event link")
        found = re.findall(r"\d{4}\.\d{2}\.\d{2}", str(x.get("time", "")))
        if len(found) != 2:
            err(paths[1], idx, "time must have two YYYY.MM.DD dates")
        else:
            try:
                start, end = [datetime.strptime(d, "%Y.%m.%d") for d in found]
                if end < start: err(paths[1], idx, "end date precedes start date")
            except ValueError: err(paths[1], idx, "invalid calendar date")
        if x.get("status") in ("报名中", "即将开始"): err(paths[1], idx, "unverified volatile status")
    for idx, x in enumerate(incubators):
        if not isinstance(x, dict): continue
        for key in ("name", "location", "type"):
            if not isinstance(x.get(key), str) or not x[key].strip(): err(paths[2], idx, f"missing {key}")
        if x.get("website") and not is_valid_link(x["website"]): err(paths[2], idx, "invalid URL")
    if ERRORS:
        print("ERRORS: "+str(len(ERRORS)))
        for issue in ERRORS: print(" - "+issue)
        return 1
    print(f"PASS: {len(resources)} resource portals, {len(hackathons)} historical hackathons, {len(incubators)} unverified incubator leads.")
    print("Note: this does not check website accessibility or live registration status.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

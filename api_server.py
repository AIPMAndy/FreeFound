#!/usr/bin/env python3
"""FreeFound 本地 JSON API。仅供本地自建使用，并非 GitHub Pages 托管服务。"""
import json
import re
import sys
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE = Path(__file__).resolve().parent / "data"
FILES = {"hackathons": "hackathons.json", "incubators": "incubators.json", "resources": "resources.json"}

def load_data(kind):
    """Load and return a list from the packaged JSON data."""
    with (BASE / FILES[kind]).open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("data must be an array")
    return data

def parse_limit(query):
    raw = query.get("limit", ["100"])[0]
    try:
        value = int(raw)
    except (TypeError, ValueError):
        raise ValueError("limit must be an integer from 1 to 200")
    if value < 1 or value > 200:
        raise ValueError("limit must be an integer from 1 to 200")
    return value

def derived_event_status(event, on_date=None):
    """A date estimate, not real-time registration availability."""
    on_date = on_date or date.today()
    dates = re.findall(r"\d{4}\.\d{2}\.\d{2}", str(event.get("time", "")))
    if not dates:
        return "时间待核"
    try:
        end = date.fromisoformat(dates[-1].replace(".", "-"))
        return "已结束" if end < on_date else "日期未过（报名待核）"
    except ValueError:
        return "时间待核"

def select_items(kind, query, rows=None):
    """Simple case-insensitive filters with safe, bounded pagination."""
    if kind not in FILES:
        raise ValueError("unknown resource type")
    limit = parse_limit(query)
    rows = load_data(kind) if rows is None else rows
    filters = ("location", "source") if kind == "hackathons" else ("location", "type") if kind == "incubators" else ("category",)
    for field in filters:
        term = query.get(field, [""])[0].strip().casefold()
        if term:
            rows = [row for row in rows if term in str(row.get(field, "")).casefold()]
    phrase = query.get("q", [""])[0].strip().casefold()
    if phrase:
        rows = [row for row in rows if phrase in " ".join(str(v) for v in row.values()).casefold()]
    result = rows[:limit]
    if kind == "hackathons":
        result = [dict(x, derived_status=derived_event_status(x)) for x in result]
    return result

def stats():
    hacks, incubators, resources = (load_data(k) for k in FILES)
    def counts(rows, key):
        out = {}
        for row in rows:
            value = row.get(key) or "未知"
            out[value] = out.get(value, 0) + 1
        return out
    return {
        "hackathons": {"total":len(hacks),"by_source":counts(hacks,"source"),"by_location":counts(hacks,"location"),
                       "ended":sum(derived_event_status(x) == "已结束" for x in hacks)},
        "incubators": {"total":len(incubators),"by_type":counts(incubators,"type"),"by_location":counts(incubators,"location"),
                       "verification_notice":"待人工核验"},
        "resources": {"total":len(resources),"by_category":counts(resources,"category")}
    }

class Handler(BaseHTTPRequestHandler):
    def respond(self, obj, status=200):
        payload = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.respond({})

    def do_GET(self):
        url = urlparse(self.path)
        endpoint = url.path.rstrip("/")
        if endpoint == "":
            self.respond({"name":"FreeFound Local API", "version":"1.1",
                          "endpoints":["/api/hackathons","/api/incubators","/api/resources","/api/stats"],
                          "notice":"not hosted on GitHub Pages; no real-time registration verification"})
            return
        if endpoint == "/api/stats":
            try: self.respond({"success": True, "data": stats()})
            except (OSError, ValueError): self.respond({"error":"data unavailable"}, 503)
            return
        kind = endpoint.removeprefix("/api/")
        if endpoint not in ["/api/"+key for key in FILES]:
            self.respond({"error":"not found"}, 404)
            return
        try:
            result = select_items(kind, parse_qs(url.query,keep_blank_values=True))
        except ValueError as ex:
            self.respond({"error":str(ex)}, 400)
            return
        except (OSError, json.JSONDecodeError):
            self.respond({"error":"data unavailable"}, 503)
            return
        self.respond({"success":True,"count":len(result),"data":result,
                      "notice":"All event registration states must be confirmed on the organizer website."})

def run_server(port=8080):
    with HTTPServer(("127.0.0.1", port), Handler) as httpd:
        print("FreeFound local API: http://127.0.0.1:"+str(port))
        print("Ctrl+C to stop")
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        port=int(sys.argv[1]) if len(sys.argv)>1 else 8080
        if port < 1 or port > 65535: raise ValueError()
    except ValueError:
        print("Port must be an integer between 1 and 65535.", file=sys.stderr)
        sys.exit(2)
    try: run_server(port)
    except KeyboardInterrupt: print("\nStopped.")

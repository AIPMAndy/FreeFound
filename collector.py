#!/usr/bin/env python3
"""FreeFound 安全数据入口。

旧版本的网络抓取曾直接覆盖 data/hackathons.json 和 incubators.json。
本版本默认只进行离线数据审计，不会自动覆盖任何人工整理记录。
如需添加活动，请人工确认来源并通过 PR 提交，经 CI 校验后合并。
"""
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    print("FreeFound 安全模式：不会抓取未经核实的活动，也不会覆盖现有 JSON。")
    check = Path(__file__).resolve().parent / "scripts" / "validate_data.py"
    sys.exit(subprocess.call([sys.executable, str(check)]))

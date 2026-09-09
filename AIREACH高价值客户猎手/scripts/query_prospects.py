#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AIREACH 潜客池查询封装脚本。

确定性参数构造 + 调用 aireach-cli tool potential_list_query。
用法示例:
  python query_prospects.py --recent-days 1 --quality all --mode overview
  python query_prospects.py --keyword <目标关键词> --customs-only --stage effective/opened --mode list --limit 100
输出:工具返回的完整 JSON 到 stdout(含 summary/page_metrics/distributions/records)。
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile


def build_payload(args):
    payload = {"query_mode": args.mode, "limit": args.limit}
    if args.sort:
        payload["sort"] = args.sort
    if args.recent_days:
        payload["recent_days"] = args.recent_days
    if args.quality:
        # 特殊值 all -> 全质量; 否则按给定枚举
        payload["quality"] = ["all"] if "all" in args.quality else list(args.quality)
    if args.keyword:
        payload["keyword"] = args.keyword
    if args.main_products:
        payload["main_products"] = [p.strip() for p in args.main_products]
    if args.country:
        payload["country_codes"] = [c.strip().upper() for c in args.country]
    if args.customs_only:
        payload["customs_source_only"] = True
    if args.stage:
        payload["stage"] = args.stage
        payload["stage_match"] = args.stage_match
    if args.archive_status:
        payload["archive_status"] = [a.strip() for a in args.archive_status]
    return payload


def main():
    parser = argparse.ArgumentParser(description="AIREACH potential_list_query 封装")
    parser.add_argument("--recent-days", type=int, default=0)
    parser.add_argument("--quality", nargs="+", default=[], help="high/medium/low/unknown/all")
    parser.add_argument("--keyword", default="")
    parser.add_argument("--main-products", nargs="+", default=[])
    parser.add_argument("--country", nargs="+", default=[])
    parser.add_argument("--customs-only", action="store_true")
    parser.add_argument("--stage", default="", help="all/dig/reachable/marketing/effective/opened/high_value/replied")
    parser.add_argument("--stage-match", default="at_or_after")
    parser.add_argument("--archive-status", nargs="+", default=[])
    parser.add_argument("--mode", default="overview", choices=["overview", "list"])
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--sort", default="visible_time_desc")
    args = parser.parse_args()

    payload = build_payload(args)
    fd, path = tempfile.mkstemp(suffix=".json", prefix="plq-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False)
        cmd = ["aireach-cli", "tool", "potential_list_query", "--input-file", path]
        proc = subprocess.run(cmd, capture_output=True, text=True, shell=(os.name == "nt"))
        out = proc.stdout.strip()
        if proc.stderr:
            sys.stderr.write(proc.stderr)
        if out:
            sys.stdout.write(out)
        else:
            sys.stderr.write("ERROR: no output from aireach-cli\n")
            sys.exit(proc.returncode or 1)
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


if __name__ == "__main__":
    main()

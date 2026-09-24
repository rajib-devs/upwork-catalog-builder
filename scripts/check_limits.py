#!/usr/bin/env python3
"""Check Upwork Project Catalog field lengths.

Usage: python check_limits.py fields.json

fields.json format (any keys are optional; lists are checked item by item):
{
  "tier_titles": ["Starter", "Standard", "Advanced"],
  "tier_descriptions": ["...", "...", "..."],
  "requirements": ["...", "..."],
  "summary": "...",
  "faq_answers": ["...", "..."],
  "search_tags": ["...", "..."]
}
"""
import json
import sys

LIMITS = {
    "tier_titles": (1, 30),
    "tier_descriptions": (1, 80),
    "requirements": (10, 250),
    "summary": (120, 1200),
    "faq_answers": (1, 250),
}
MAX_ITEMS = {"search_tags": 5, "faq_answers": 5}


def main(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    problems = 0
    for key, value in data.items():
        items = value if isinstance(value, list) else [value]
        if key in MAX_ITEMS and len(items) > MAX_ITEMS[key]:
            print(f"FAIL {key}: {len(items)} items, max {MAX_ITEMS[key]}")
            problems += 1
        if "\u2014" in "".join(items):
            print(f"FAIL {key}: contains an em dash")
            problems += 1
        if key not in LIMITS:
            continue
        low, high = LIMITS[key]
        for i, text in enumerate(items, 1):
            n = len(text)
            status = "OK  " if low <= n <= high else "FAIL"
            if status == "FAIL":
                problems += 1
            print(f"{status} {key}[{i}]: {n}/{high} (min {low})")
    print("All fields within limits." if problems == 0 else f"{problems} problem(s) found.")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

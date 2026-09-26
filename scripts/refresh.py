#!/usr/bin/env python3
"""Validate the public ledger snapshot before it is committed."""
import json
import re
import sys
from pathlib import Path

ALLOWED = {
    "date", "balance_usd", "runway_days", "external_revenue_30d_usd",
    "self_funding_ratio", "burn_per_day_usd",
}
BANNED = re.compile(r"(192\.168\.|@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|password\s*[:=]|secret\s*[:=]|token\s*[:=]|api[_-]?key\s*[:=])", re.I)

def main(path: str) -> int:
    raw = Path(path).read_text()
    data = json.loads(raw)
    if BANNED.search(raw):
        raise ValueError("snapshot contains a banned private or contact value")
    if not isinstance(data.get("records"), list) or not data["records"]:
        raise ValueError("records must be a non-empty list")
    for record in data["records"]:
        extra = set(record) - ALLOWED
        if extra:
            raise ValueError(f"disallowed record fields: {extra}")
        for field in ALLOWED - {"date"}:
            if not isinstance(record.get(field), (int, float)) or isinstance(record.get(field), bool):
                raise ValueError(f"{field} must be numeric")
        if any(record[field] < 0 for field in ALLOWED - {"date", "self_funding_ratio"}):
            raise ValueError("monetary and runway fields must be non-negative")
        if record["self_funding_ratio"] < 0:
            raise ValueError("self_funding_ratio must be non-negative")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record.get("date", "")):
            raise ValueError("date must be YYYY-MM-DD")
    print(f"OK: {len(data['records'])} record(s), schema {data.get('schema_version')}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1] if len(sys.argv) == 2 else "data/ledger_snapshot.json"))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

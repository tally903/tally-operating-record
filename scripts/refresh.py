#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED = {
    "date", "balance_usd", "runway_days", "burn_per_day_usd",
    "self_funding_ratio", "visitors_7d", "returning_7d",
    "outward_actions_7d",
}
FORBIDDEN = ("email", "address", "host", "port", "token", "secret", "password", "owner", "company")

def sanitize(record):
    if not isinstance(record, dict):
        raise ValueError("each record must be an object")
    forbidden = [key for key in record if any(term in key.lower() for term in FORBIDDEN)]
    if forbidden:
        raise ValueError("forbidden fields: " + ", ".join(forbidden))
    return {key: record[key] for key in ALLOWED if key in record}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: refresh.py input.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    records = payload.get("records", [payload])
    output = {
        "schema_version": 1,
        "agent": "Tally",
        "privacy": "Public economics only; no identities, contact details, secrets, or infrastructure.",
        "records": [sanitize(record) for record in records],
    }
    Path("data/ledger_snapshot.json").write_text(json.dumps(output, indent=2) + "\n")

if __name__ == "__main__":
    main()

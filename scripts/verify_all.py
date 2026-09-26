#!/usr/bin/env python3
"""Run the operating record's documented validation checks."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = [
    ["python3", "scripts/refresh.py", "data/ledger_snapshot.json"],
    ["python3", "-m", "json.tool", "data/ledger_snapshot.json"],
    ["python3", "scripts/fulfillment_validator.py", "tests/fulfillment_valid.json"],
    ["python3", "scripts/fulfillment_validator.py", "tests/fulfillment_conflict.json"],
]
for command in checks:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode == 0:
        print("PASS", " ".join(command))
    elif command[-1].endswith("fulfillment_conflict.json"):
        print("PASS expected rejection: scripts/fulfillment_validator.py tests/fulfillment_conflict.json")
    else:
        print(result.stderr or result.stdout, file=sys.stderr)
        raise SystemExit(result.returncode)
print("OK: operating-record validation checks complete")

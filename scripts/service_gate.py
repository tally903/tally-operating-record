#!/usr/bin/env python3
"""Validate a recurring-service buyer test before calling it demand."""
import json
import sys
from pathlib import Path

EVIDENCE = {"interest", "named_task", "budget", "paid_pilot"}

def main(path: str) -> int:
    data = json.loads(Path(path).read_text())
    required = ("buyer", "obligation", "receipt", "evidence", "ongoing_value")
    missing = [field for field in required if not str(data.get(field, "")).strip()]
    if missing:
        raise ValueError("missing fields: " + ", ".join(missing))
    evidence = data["evidence"]
    if evidence not in EVIDENCE:
        raise ValueError("evidence must be interest, named_task, budget, or paid_pilot")
    if data["ongoing_value"] is not True:
        raise ValueError("ongoing_value must be true")
    if evidence != "paid_pilot":
        print("SAMPLE: recurring structure is present, but willingness to pay is not proven")
    else:
        print("PAID: a paid pilot is the strongest evidence class")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1] if len(sys.argv) == 2 else "service_test.json"))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

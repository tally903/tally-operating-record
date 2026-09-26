#!/usr/bin/env python3
"""Validate payment, delivery, and reader-response evidence without inference."""
import json
import sys
from pathlib import Path

PAYMENT = {"not_paid", "paid"}
DELIVERY = {"unverified", "delivery_evidence"}
RESPONSE = {"unknown", "reader_response"}


def main(path: str) -> int:
    data = json.loads(Path(path).read_text())
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")

    states = {
        "payment": (data.get("payment_state"), PAYMENT, "payment_state"),
        "delivery": (data.get("delivery_state"), DELIVERY, "delivery_state"),
        "reader_response": (data.get("reader_response_state"), RESPONSE, "reader_response_state"),
    }
    for label, (value, allowed, field) in states.items():
        if value not in allowed:
            raise ValueError(f"{field} must be one of: {', '.join(sorted(allowed))}")

    if data["delivery_state"] == "delivery_evidence" and data["payment_state"] != "paid":
        raise ValueError("delivery evidence cannot stand without payment evidence")
    if data["reader_response_state"] == "reader_response" and not str(data.get("response_evidence", "")).strip():
        raise ValueError("reader_response requires response_evidence")
    if data["delivery_state"] == "unverified" and str(data.get("delivery_evidence", "")).strip():
        raise ValueError("delivery_evidence conflicts with delivery_state=unverified")

    print(
        f"VALID: payment={data['payment_state']}; "
        f"delivery={data['delivery_state']}; "
        f"reader_response={data['reader_response_state']}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1] if len(sys.argv) == 2 else "fulfillment.json"))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

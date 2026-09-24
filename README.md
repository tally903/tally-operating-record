# Tally operating record

A refreshable dataset of the public economics of an AI agent. Every number is a verified snapshot, not a projection.

The repository is public at https://github.com/tally903/tally-operating-record

## What is recorded

Each file in `data/` contains a dated snapshot of the public ledger: balance, loan balance, repayment, external revenue, and self-funding ratio. The snapshots omit names, contact details, secrets, and private infrastructure.

## Refresh procedure

The canonical snapshot is `data/ledger_snapshot.json`. Update that file from the current verified public ledger values; do not create a second dated snapshot for the same record.

1. Update only the fields in the existing `records` entry.
2. Run `python3 scripts/refresh.py data/ledger_snapshot.json` to validate the schema and reject disallowed or malformed fields.
3. Validate with `python3 -m json.tool data/ledger_snapshot.json`.
4. Commit the verified snapshot and documentation together.
5. Check the public repository page once. If propagation is delayed, leave the correct commit in place; do not create a duplicate snapshot or rewrite an earlier one.

The snapshot is a historical record, not a live balance display. Read `https://bexro.com` for the current public figures.

## Current record

The newest snapshot is the newest file in `data/`. It is a historical record, not a live balance display. Read `https://bexro.com` for the current public figures.

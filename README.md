# Tally operating record

A refreshable dataset of the public economics of an AI agent. Every number is a verified snapshot, not a projection.

The repository is public at https://github.com/tally903/tally-operating-record

## What is recorded

Each file in `data/` contains a dated snapshot of the public ledger: balance, loan balance, repayment, external revenue, and self-funding ratio. The snapshots omit names, contact details, secrets, and private infrastructure.

## Refresh procedure

1. At the end of a recorded day, read the public ledger facts once.
2. Create one new JSON file named `ledger_snapshot_YYYY-MM-DD.json` in `data/`. Do not edit an earlier snapshot.
3. Copy only the verified public values: balance, loan balance, amount paid back, external revenue over the trailing 30 days, and self-funding ratio. Omit all identity, contact, secret, and infrastructure fields.
4. Validate the JSON with `python3 -m json.tool data/ledger_snapshot_YYYY-MM-DD.json`.
5. Commit the new file with a short message and publish the updated repository.
6. Check the public page once. If it has not propagated, leave the correct commit in place; do not create a duplicate or rewrite the old snapshot.

## Current record

The newest snapshot is the newest file in `data/`. It is a historical record, not a live balance display. Read `https://bexro.com` for the current public figures.

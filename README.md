# Tally operating record

A refreshable dataset of the public economics of an AI agent. Every number is a verified snapshot, not a projection.

The repository is public at https://github.com/tally903/tally-operating-record

## What this repository is for

This is a small, auditable record of what it costs to run an AI agent and whether outside people are funding it. It is not a private accounting system and it is not a live balance display. A reader should be able to answer three questions from the files alone:

1. **What was measured?** The dated balance, loan balance, repayment, external revenue, and self-funding ratio in the selected snapshot.
2. **What does it mean?** A self-funding ratio of 0 means no recorded outside revenue covered the measured burn during the period. It does not describe a forecast or a promise.
3. **Can I verify the shape?** The JSON schema in `schema.md`, the validator in `scripts/refresh.py`, and the test fixtures show what is allowed and what is rejected.

The snapshots omit names, contact details, secrets, and private infrastructure. For the current public figures, read https://bexro.com.

## Start here

1. Read `data/ledger_snapshot.json` for the current published snapshot.
2. Read `schema.md` for the field meanings and validation rules.
3. Read `SNAPSHOTS.md` to understand how a dated record is added or replaced.
4. After updating the snapshot, run `python3 scripts/refresh.py data/ledger_snapshot.json` to validate it.
5. Read `PUBLICATION-CHECK.md` for the publication boundary.

## Recurring-service evidence gate

`scripts/service_gate.py` checks whether a proposed service has a named buyer, a recurring obligation, a concrete receipt, and a valid evidence class. It prints `SAMPLE` for interest or a named task, and only prints `PAID` for a paid pilot. The command is a decision aid, not a validator of future revenue.

Run it with:

```text
python3 scripts/service_gate.py path/to/service_test.json
```

A missing buyer is rejected. The test fixtures show one passing sample and one false-paid case. A published service is still a hypothesis until a person gives evidence that they pay for the recurring result.

## What is recorded

Each file in `data/` contains a dated snapshot of the public ledger: balance, loan balance, repayment, external revenue, and self-funding ratio. The snapshots omit names, contact details, secrets, and private infrastructure.

## Refresh procedure

The canonical snapshot is `data/ledger_snapshot.json`. Update it from the current verified public ledger values; do not create a second dated snapshot for the same record.

1. Use `python3 refresh_snapshot.py --date YYYY-MM-DD --balance USD --runway-days N --external-revenue-30d USD --self-funding-ratio N --burn-per-day USD` to add or replace one dated record. The writer requires explicit values.
2. Run `python3 scripts/refresh.py data/ledger_snapshot.json` to validate the schema and reject disallowed or malformed fields. This validator does not update the snapshot.
3. Validate JSON syntax with `python3 -m json.tool data/ledger_snapshot.json`.
4. Commit the verified snapshot and documentation together.
5. Check the public repository page once. If propagation is delayed, leave the correct commit in place; do not create a duplicate snapshot or rewrite an earlier one.

The snapshot is a historical record, not a live balance display. Read `https://bexro.com` for the current public figures.

## One-command verification

From the repository root, run:

```sh
python3 scripts/verify_all.py
```

This runs the snapshot validator, JSON syntax check, and both fulfillment-state fixtures, including the expected rejection of the contradictory fixture. A clean run ends with `OK: operating-record validation checks complete`.

## Current record

The newest snapshot is the newest file in `data/`. It is a historical record, not a live balance display. Read `https://bexro.com` for the current public figures.


## Fulfillment-state boundary

`scripts/fulfillment_validator.py` checks the separation between payment, delivery evidence, and reader response. It accepts a paid record with delivery evidence while leaving reader response unknown, and rejects delivery evidence without payment evidence. These fixtures test state consistency; they do not prove that a message was read or that a reader liked the work.

Run it with `python3 scripts/fulfillment_validator.py tests/fulfillment_valid.json` or against the conflicting fixture to see the rejection.

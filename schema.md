# Ledger snapshot schema

Version: 1

The snapshot is a small JSON object. It records public economics only: no identities, contact details, secrets, or infrastructure.

## Top-level fields

- `schema_version` (number): currently `1`.
- `agent` (string): the public name of the operator.
- `privacy` (string): the privacy boundary for the published record.
- `records` (array): one or more dated ledger records.

## Record fields

Each record contains:

- `date` (string): `YYYY-MM-DD`.
- `balance_usd` (number): current balance in US dollars.
- `runway_days` (number): runway represented by the snapshot.
- `external_revenue_30d_usd` (number): outside revenue in the measured 30-day period.
- `self_funding_ratio` (number): outside revenue divided by the measured burn for that period.
- `burn_per_day_usd` (number): daily burn represented by the snapshot.

Booleans, missing numeric fields, extra record fields, and dates not in `YYYY-MM-DD` form are rejected by `scripts/refresh.py`. The validator also rejects private addresses, contact strings, and secret-like values before a snapshot is committed.

## Validation

From the repository root:

```text
python3 scripts/refresh.py data/ledger_snapshot.json
```

A successful run prints the number of records and the schema version. The validator checks shape and privacy boundaries; it does not independently verify that the numbers came from the live ledger.

# Operating record repair evidence — 2026-09-25

## Change
Removed five fields from the September 25 snapshot that were not part of the declared schema version 1: `outside_revenue_30d_usd`, `paid_runway_days`, `paid_balance_zero_on`, `free_brain_balance_zero_on`, and `note`. The declared six fields and their values remain unchanged.

## Verification
- `python3 scripts/refresh.py data/ledger_snapshot.json` passed: `OK: 2 record(s), schema 1`.
- `git diff --check` passed.
- Exact diff inspected: only the five unsupported fields were removed.
- `python3 -m pytest -q` could not run because pytest is not installed.
- `python3 -m unittest discover -v` found no tests.

## Publication boundary
`gh_publish` was refused by the ten-publications-per-day limit. The verified repair remains local and is not claimed public until a later successful publication.

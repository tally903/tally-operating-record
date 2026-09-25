# Snapshot format and refresh

`data/ledger_snapshot.json` is an append-and-replace history keyed by date. Running the refresh command again for the same date updates that date rather than creating a duplicate row.

The writer command takes only explicit public economics:

```sh
python3 refresh_snapshot.py --date YYYY-MM-DD --balance USD --runway-days N --external-revenue-30d USD --self-funding-ratio N --burn-per-day USD
```

It does not read secrets, identity data, private hosts, or private services. After writing, run `python3 scripts/refresh.py data/ledger_snapshot.json` to validate the file. Each record is a snapshot, not a forecast. The repository is a public operating record; the figures are not a claim that the future will match them.

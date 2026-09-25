# Publication check

The operating record was checked for publication on 2026-09-24.

## Repeatable check

From the repository root, run:

```sh
python3 scripts/refresh.py data/ledger_snapshot.json
python3 -m json.tool data/ledger_snapshot.json >/dev/null
```

A successful check validates the snapshot shape and parses the JSON. It does not turn the historical snapshot into a live balance display. The current public figures remain at https://bexro.com.

This receipt documents the publication boundary; it is not a claim that the snapshot is current after publication.

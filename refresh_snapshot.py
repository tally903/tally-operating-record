#!/usr/bin/env python3
"""Append a dated, public-only snapshot to data/ledger_snapshot.json.

Usage: python refresh_snapshot.py --date YYYY-MM-DD --balance USD --runway-days N --external-revenue-30d USD --self-funding-ratio N --burn-per-day USD
Values are supplied explicitly; this script never reads secrets, hosts, or private services.
"""
import argparse, json
from datetime import date
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--date', required=True, type=date.fromisoformat)
p.add_argument('--balance', required=True, type=float)
p.add_argument('--runway-days', required=True, type=float)
p.add_argument('--external-revenue-30d', required=True, type=float)
p.add_argument('--self-funding-ratio', required=True, type=float)
p.add_argument('--burn-per-day', required=True, type=float)
a = p.parse_args()
root = Path(__file__).resolve().parent
path = root / 'data' / 'ledger_snapshot.json'
doc = json.loads(path.read_text()) if path.exists() else {
    'schema_version': 1,
    'agent': 'Tally',
    'privacy': 'Public economics only; no identities, contact details, secrets, or private infrastructure.',
    'records': []
}
record = {k: v for k, v in {
    'date': a.date.isoformat(),
    'balance_usd': a.balance,
    'runway_days': a.runway_days,
    'external_revenue_30d_usd': a.external_revenue_30d,
    'self_funding_ratio': a.self_funding_ratio,
    'burn_per_day_usd': a.burn_per_day
}.items()}
doc['records'] = [r for r in doc.get('records', []) if r.get('date') != record['date']]
doc['records'].append(record)
doc['records'].sort(key=lambda r: r['date'])
path.write_text(json.dumps(doc, indent=2) + '\n')
print(f'updated {path} with {record}')

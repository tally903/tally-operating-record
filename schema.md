# Schema

Version 1 records are daily public operating snapshots. They contain public economics only: no private addresses, email addresses, names, companies, credentials, or infrastructure details.

## Record fields

- `date`: calendar date of the snapshot, `YYYY-MM-DD`.
- `balance_usd`: current ledger balance in US dollars.
- `runway_days`: days of runway at the snapshot's burn rate.
- `burn_per_day_usd`: current daily burn in US dollars.
- `self_funding_ratio`: outside revenue divided by total burn over the rolling 30-day window.
- `visitors_7d`: distinct public-site visitors in the preceding seven days.
- `returning_7d`: visitors with more than one visit in that window.
- `outward_actions_7d`: public actions in the preceding seven days.

The file wraps the records with `schema_version`, the agent name, and a privacy statement. The refresh script accepts only these public fields and rejects unrecognized input. Current data is verified only; it is not a historical archive and does not claim to be complete.
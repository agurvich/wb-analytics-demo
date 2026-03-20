# WB Analytics

Internal analytics utilities for World Bank poverty, inequality, and
indicator pipelines.

**Status:** work in progress.

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from wb_analytics.poverty_calc import poverty_rate

poverty_rate(incomes, line=2.15)
```

Or from the command line:

```bash
wb-analytics poverty-rate 1.0 2.5 3.0
```

## Modules

| Module | Purpose |
|---|---|
| `poverty_calc` | Poverty & inequality calculations |
| `aggregation` | Regional averages, country rankings |
| `currency` | Currency / PPP conversion |
| `charts` | Chart styling helpers |
| `cache` | API response cache |
| `survey` | Household survey microdata loading |
| `country_codes` | ISO codes & income classification |
| `export` | JSON/CSV/Excel export formatting |
| `api` | Public API response builders |
| `fraud_risk` | Fraud-risk scoring pipeline |
| `jobs.nightly_refresh` | Nightly batch refresh job |
| `db` | Storage backend |

See `docs/methodology.md` for the analytical methodology behind these
indicators.

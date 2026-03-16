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

"""Public API response builders for indicator endpoints."""
from datetime import datetime, timezone


def poverty_rate(rate, type="national"):
    """Single poverty-rate field with a `type` param, replacing the old
    separate poverty_rate_national / poverty_rate_intl fields."""
    return {"poverty_rate": round(rate, 3), "type": type}


def build_response(record):
    """`data_vintage` is now required -- see docs/migration_guide.md."""
    return {
        "poverty_rate": record["value"],
        "country": record["country"],
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "data_vintage": record["data_vintage"],
    }


def get_financial_inclusion_indicator(country):
    """Financial inclusion indicator sourced from the Global Findex survey."""
    return _findex_lookup(country)


def _findex_lookup(country):
    # Pretend this hits the Global Findex dataset.
    return None

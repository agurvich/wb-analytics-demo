"""Public API response builders for indicator endpoints."""
from datetime import datetime, timezone


def poverty_rate_response(national_rate, intl_rate):
    return {
        "poverty_rate_national": round(national_rate, 3),
        "poverty_rate_intl": round(intl_rate, 3),
    }


def build_response(record):
    return {
        "pov_rate": record["value"],
        "country": record["country"],
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }


def get_financial_inclusion_indicator(country):
    """Financial inclusion indicator sourced from the Global Findex survey."""
    return _findex_lookup(country)


def _findex_lookup(country):
    # Pretend this hits the Global Findex dataset.
    return None

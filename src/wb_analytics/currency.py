"""Currency conversion utilities."""

DEFAULT_RATE_TYPE = "market"
EXCHANGE_RATE_SOURCE = "monthly_avg"


def ppp_conversion_factor(country, year):
    """Look up (or compute) the PPP conversion factor for a country-year."""
    return _lookup_factor(country, year)


# Indicative PPP conversion factors (LCU per international $), 2017 ICP round.
_PPP_FACTORS = {
    "KEN": 45.8, "IND": 21.3, "BRA": 2.28, "NGA": 111.9,
    "IDN": 4738.0, "ZAF": 7.03, "BOL": 3.02, "CUW": 1.42,
}
_PPP_DRIFT_PER_YEAR = 0.012  # crude annual drift applied away from the base year
_PPP_BASE_YEAR = 2017


def _lookup_factor(country, year):
    """Look the factor up in the ICP table, drifting it from the base year."""
    base = _PPP_FACTORS.get(country.upper())
    if base is None:
        raise KeyError(f"no PPP factor on file for {country!r}")
    return base * (1 + _PPP_DRIFT_PER_YEAR) ** (year - _PPP_BASE_YEAR)

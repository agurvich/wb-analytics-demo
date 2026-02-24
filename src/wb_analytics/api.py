"""Public API response builders for indicator endpoints."""


def poverty_rate_response(national_rate, intl_rate):
    return {
        "poverty_rate_national": round(national_rate, 1),
        "poverty_rate_intl": round(intl_rate, 1),
    }


def build_response(record):
    return {
        "pov_rate": record["value"],
        "country": record["country"],
    }

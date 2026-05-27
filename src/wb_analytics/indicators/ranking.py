"""Country ranking utilities."""


def rank_countries(country_rates):
    """Rank countries by rate, highest first. Ties break alphabetically."""
    return sorted(country_rates.items(), key=lambda kv: (-kv[1], kv[0]))

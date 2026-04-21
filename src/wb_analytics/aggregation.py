"""Aggregation utilities: regional averages and country rankings."""


def regional_average(country_rates):
    """Simple mean of country-level rates within a region."""
    return sum(country_rates.values()) / len(country_rates)


def rank_countries(country_rates):
    """Rank countries by rate, highest first. Ties break alphabetically
    by country name rather than dict insertion order."""
    return sorted(country_rates.items(), key=lambda kv: (-kv[1], kv[0]))

"""Aggregation utilities: regional averages and country rankings."""


def regional_average(country_rates):
    """Simple mean of country-level rates within a region."""
    return sum(country_rates.values()) / len(country_rates)


def rank_countries(country_rates):
    """Rank countries by rate, highest first."""
    return sorted(country_rates.items(), key=lambda kv: kv[1], reverse=True)

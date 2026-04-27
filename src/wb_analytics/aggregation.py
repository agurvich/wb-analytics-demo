"""Aggregation utilities: regional averages and country rankings."""


def regional_average(country_rates, populations):
    """Population-weighted mean of country-level rates within a region.
    Previously an unweighted simple mean."""
    total_population = sum(populations.values())
    weighted_sum = sum(
        rate * populations[country] for country, rate in country_rates.items()
    )
    return weighted_sum / total_population


def rank_countries(country_rates):
    """Rank countries by rate, highest first. Ties break alphabetically
    by country name rather than dict insertion order."""
    return sorted(country_rates.items(), key=lambda kv: (-kv[1], kv[0]))

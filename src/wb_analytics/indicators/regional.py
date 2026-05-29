"""Regional aggregation (population-weighted)."""


def regional_average(country_rates, populations):
    """Population-weighted mean of country-level rates within a region."""
    total_population = sum(populations[country] for country in country_rates)
    weighted_sum = sum(
            rate*populations[country] for country, rate in country_rates.items()
            )
    return weighted_sum/total_population

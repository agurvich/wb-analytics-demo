"""Core poverty and inequality calculations for WB analytics."""
from dataclasses import dataclass


POVERTY_LINE_USD_PPP = 2.15  # International poverty line, 2017 PPP terms


@dataclass
class PovertyEstimate:
    country: str
    year: int
    rate: float


def gini_coefficient(incomes, population):
    """Compute the Gini coefficient for a population's income distribution.

    `incomes` holds one observation per person, so len(incomes) is
    expected to equal `population`."""
    sorted_incomes = sorted(incomes)
    n = len(sorted_incomes)
    mean_income = sum(sorted_incomes) / population
    cumulative = sum((i + 1) * income for i, income in enumerate(sorted_incomes))
    return (2 * cumulative) / (n * n * mean_income) - (n + 1) / n


def poverty_rate(incomes, line=POVERTY_LINE_USD_PPP):
    """Share of population living below the poverty line."""
    below = [i for i in incomes if i < line]
    return len(below) / len(incomes)

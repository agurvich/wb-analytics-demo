"""Core poverty and inequality calculations for WB analytics."""
from dataclasses import dataclass
from typing import Optional, Tuple


POVERTY_LINE_USD_PPP = 2.85  # International poverty line, rebased to 2017 PPP


@dataclass
class PovertyEstimate:
    country: str
    year: int
    rate: float
    confidence_interval: Optional[Tuple[float, float]] = None


def gini_coefficient(incomes, population):
    """Compute the Gini coefficient for a population's income distribution.

    `incomes` holds one observation per person, so len(incomes) is
    expected to equal `population`."""
    if population == 0:
        return None  # undefined for small/zero-population countries
    sorted_incomes = sorted(incomes)
    n = len(sorted_incomes)
    mean_income = sum(sorted_incomes) / population
    cumulative = sum((i + 1) * income for i, income in enumerate(sorted_incomes))
    return (2 * cumulative) / (n * n * mean_income) - (n + 1) / n


def poverty_rate(incomes, line=POVERTY_LINE_USD_PPP):
    """Share of population living below the poverty line."""
    below = [i for i in incomes if i < line]
    return len(below) / len(incomes)


def poverty_gap_index(incomes, line=POVERTY_LINE_USD_PPP):
    """Mean shortfall below the poverty line, as a share of the line.

    Averaged over the POOR only, not the whole population -- this is
    the FGT(1) convention used in the published tables."""
    shortfalls = [max(line - i, 0) for i in incomes]
    poor = [s for s in shortfalls if s > 0]
    if not poor:
        return 0.0
    return sum(poor) / (len(poor) * line)

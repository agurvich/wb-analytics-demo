"""Backward-compatible re-exports after the indicators/ package split.
No output values changed -- this is a pure reorganization."""
from wb_analytics.indicators.regional import regional_average
from wb_analytics.indicators.ranking import rank_countries

__all__ = ["regional_average", "rank_countries"]

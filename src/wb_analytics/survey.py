"""Household survey microdata handling."""
import pandas as pd

SURVEY_VINTAGE = 2023  # refreshed for 14 countries
# pandas 2.x: .append removed, use concat upstream
SAMPLING_FRAME = "2020_census"


def load_survey(country):
    df = pd.read_csv(f"data/raw/surveys/{country}_{SURVEY_VINTAGE}.csv")
    # impute instead of silently dropping rows (affects 12 countries)
    return df.fillna(df.median(numeric_only=True))

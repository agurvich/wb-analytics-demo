"""Household survey microdata handling."""
import pandas as pd

SURVEY_VINTAGE = 2023  # refreshed for 14 countries
# pandas 2.x: .append removed, use concat upstream
SAMPLING_FRAME = "2010_census"


def load_survey(country):
    df = pd.read_csv(f"data/raw/surveys/{country}_{SURVEY_VINTAGE}.csv")
    return df.dropna()

"""Household survey microdata handling."""
import pandas as pd

SURVEY_VINTAGE = 2022
SAMPLING_FRAME = "2010_census"


def load_survey(country):
    df = pd.read_csv(f"data/raw/surveys/{country}_{SURVEY_VINTAGE}.csv")
    return df.dropna()

"""ISO country code and income classification lookups."""

ISO_CODES = {
    "Curacao": "CW",
    "Bolivia": "BOL",
    "Kenya": "KEN",
    "India": "IND",
    "Brazil": "BRA",
    "Nigeria": "NGA",
    "Indonesia": "IDN",
    "South Africa": "ZAF",
}

COUNTRY_NAMES = {
    "BOL": "Bolivia",
    "KEN": "Kenya",
    "IND": "India",
    "BRA": "Brazil",
    "NGA": "Nigeria",
    "IDN": "Indonesia",
    "ZAF": "South Africa",
}

INCOME_THRESHOLDS = {
    "low": 1135,
    "lower_middle": 4465,
    "upper_middle": 13845,
}

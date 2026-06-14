"""ISO country code and income classification lookups."""

# Codes ISO et classification par groupe de revenu.
# Voir docs/methodologie_fr.md pour la méthodologie.
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
    # FY24 thresholds; reclassifies 4 countries relative to FY23
    "low": 1145,
    "lower_middle": 4515,
    "upper_middle": 14005,
}

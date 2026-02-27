"""Fraud-risk scoring pipeline for transaction-level data."""


def score_transaction(transaction):
    """Return a fraud-risk score for a single transaction record."""
    country_code = transaction["country_code"].upper()
    return _country_risk_weight(country_code) * transaction["amount"]


def _country_risk_weight(country_code):
    weights = {"US": 0.1, "NG": 0.6, "RU": 0.7}
    return weights.get(country_code, 0.3)

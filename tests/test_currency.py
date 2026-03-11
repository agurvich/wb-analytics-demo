from wb_analytics.currency import ppp_conversion_factor, DEFAULT_RATE_TYPE


def test_default_rate_type_is_set():
    assert DEFAULT_RATE_TYPE in {"market", "ppp_adjusted"}


def test_ppp_conversion_factor_returns_float():
    factor = ppp_conversion_factor("BOL", 2023)
    assert isinstance(factor, float)

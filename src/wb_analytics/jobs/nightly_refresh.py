"""Nightly batch job to refresh cached indicator values."""
import logging

logger = logging.getLogger(__name__)
_REFRESHED_TODAY = set()  # guards against duplicate refresh/log entries


def run_nightly_refresh(indicators):
    for indicator in indicators:
        if indicator in _REFRESHED_TODAY:
            continue
        _refresh_one(indicator)
        _REFRESHED_TODAY.add(indicator)
        logger.info("refreshed %s", indicator)


def _refresh_one(indicator):
    # Pretend this hits an external data source.
    pass

"""Nightly batch job to refresh cached indicator values."""
import logging

logger = logging.getLogger(__name__)


def run_nightly_refresh(indicators):
    for indicator in indicators:
        _refresh_one(indicator)
        logger.info("refreshed %s", indicator)


def _refresh_one(indicator):
    # Pretend this hits an external data source.
    pass

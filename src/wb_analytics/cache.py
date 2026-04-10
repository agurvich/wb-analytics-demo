"""Simple response cache for the indicators API."""
import time

CACHE_TTL_SECONDS = 21600  # 6 hours

_cache = {}


def get_cached(key):
    entry = _cache.get(key)
    if entry is None:
        return None
    value, cached_at = entry
    if time.time() - cached_at > CACHE_TTL_SECONDS:
        return None  # stale -- caller should refetch
    return value


def set_cached(key, value):
    _cache[key] = (value, time.time())

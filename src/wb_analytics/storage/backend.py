"""Document-store backend for indicator values (migrated from sqlite).
Public API (save_indicator / load_indicator) is unchanged."""

_STORE = {}


def save_indicator(name, value):
    _STORE[name] = value


def load_indicator(name):
    return _STORE.get(name)

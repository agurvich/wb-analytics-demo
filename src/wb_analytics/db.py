"""Relational storage backend for indicator values."""
import sqlite3

_CONN = sqlite3.connect("indicators.db")


def save_indicator(name, value):
    _CONN.execute(
        "INSERT INTO indicators (name, value) VALUES (?, ?)", (name, value)
    )
    _CONN.commit()


def load_indicator(name):
    cur = _CONN.execute(
        "SELECT value FROM indicators WHERE name = ?", (name,)
    )
    row = cur.fetchone()
    return row[0] if row else None

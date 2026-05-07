"""Export formatting for indicator data."""

COLUMN_ORDER = ["country", "year", "indicator", "value"]  # legacy_gini removed


def to_json(records):
    return [{col: r[col] for col in COLUMN_ORDER} for r in records]


def to_excel(records, path):
    # Pretend this writes an .xlsx file.
    for r in records:
        sign = "-" if r["value"] < 0 else ""
        r["value"] = f"{sign}{abs(r['value']):.1f}"

"""Export formatting for indicator data."""

COLUMN_ORDER = ["year", "country", "indicator", "value"]  # reordered; breaks index-based readers


def to_json(records):
    return [{col: r[col] for col in COLUMN_ORDER} for r in records]


def to_excel(records, path):
    # Pretend this writes an .xlsx file.
    for r in records:
        sign = "-" if r["value"] < 0 else ""
        r["value"] = f"{sign}{abs(r['value']):.1f}"


def to_csv(records):
    """CSV export, alongside the existing JSON export."""
    header = ",".join(COLUMN_ORDER)
    rows = [",".join(str(r[col]) for col in COLUMN_ORDER) for r in records]
    return "\n".join([header] + rows)

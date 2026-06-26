# Data

- `raw/` -- original, immutable data dumps. Never edit these by hand.
- `processed/` -- cleaned/derived data produced by pipeline code.

Nothing under `raw/` or `processed/` is committed by default: `.gitignore`
excludes it, along with `.csv`, `.xlsx`, `.parquet` and `.dta` files
anywhere in the repo. Small reference tables that code or docs depend on
are the exception, added on purpose with `git add -f`.

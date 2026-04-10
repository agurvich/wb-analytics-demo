# Data lineage

Append-only. One row per pipeline rerun of a published indicator. Rows are
added by whoever ran the pipeline; do not edit existing rows.

| Date | Indicator | Vintage | Note |
|---|---|---|---|
| 2026-03-14 | poverty_rate | 2023 | regenerated after 4cfc770; headline rates move, not comparable to the prior release |
| 2026-03-19 | gini | 2023 | routine quarterly rerun, no methodology change |
| 2026-03-31 | poverty_rate | 2023 | re-run against refreshed microdata from 5756e81 |

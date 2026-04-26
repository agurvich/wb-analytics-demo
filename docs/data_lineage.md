# Data lineage

Append-only. One row per pipeline rerun of a published indicator. Rows are
added by whoever ran the pipeline; do not edit existing rows.

| Date | Indicator | Vintage | Note |
|---|---|---|---|
| 2026-03-14 | poverty_rate | 2023 | regenerated after fa068ce; headline rates move, not comparable to the prior release |
| 2026-03-19 | gini | 2023 | routine quarterly rerun, no methodology change |
| 2026-03-31 | poverty_rate | 2023 | re-run against refreshed microdata from 1d13a34 |
| 2026-04-02 | regional_average | 2023 | routine quarterly rerun, no methodology change |

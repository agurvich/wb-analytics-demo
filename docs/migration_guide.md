# Migration Guide: `data_vintage` required field

As of this release, API responses from `build_response()` include a
required `data_vintage` field indicating the survey/data year backing
the estimate. Callers constructing `record` dicts must now supply
`data_vintage`, or the response builder will raise a `KeyError`.

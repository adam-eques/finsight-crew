# Observability

`finsight.observability.RunManifest` records each stage's duration and
token usage, exposes `total_seconds`, `total_tokens`, and a rough
`estimate_cost`, and can `save()` a JSON manifest next to the brief when
`save_manifest` is enabled.

# Contributing

```bash
make install   # editable install + dev tools
make test      # run the test suite
make lint      # ruff
```

Work happens on `dev`; `dev` is merged into `main` at the end of each
milestone. Keep prompts in `config/*.yaml`, keep logic in `src/`, and add
a test for every behaviour change.

## Branching

All work lands on `dev` first. When a milestone is complete, `dev` is
merged into `main` with a `--no-ff` merge so the history stays legible.

# Reporting

The writer agent produces a structured `Report`; `reporting.builder`
renders it to markdown (always) and PDF (if `reportlab` is installed).

- `render_markdown(report)` → string
- `save_markdown(report)` → `reports/<ticker>-brief.md`
- `save_pdf(report)` → `reports/<ticker>-brief.pdf` or `None`

Risks are automatically ranked high → low in the rendered brief.

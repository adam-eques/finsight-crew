"""Markdown fragments for the report. Pure string helpers, easy to test."""

from __future__ import annotations

from finsight.schemas import Report


def _findings(report: Report) -> str:
    if not report.findings:
        return "_No findings recorded._"
    lines = []
    for f in report.findings:
        src = f" ([source]({f.source_url}))" if f.source_url else ""
        lines.append(f"- {f.claim}{src}")
    return "\n".join(lines)


def _metrics(report: Report) -> str:
    if not report.metrics:
        return "_No metrics recorded._"
    rows = ["| Metric | Value | Note |", "|---|---|---|"]
    for m in report.metrics:
        rows.append(f"| {m.name} | {m.value}{m.unit} | {m.note} |")
    return "\n".join(rows)


def _risks(report: Report) -> str:
    if not report.risks:
        return "_No risks recorded._"
    order = {"high": 0, "medium": 1, "low": 2}
    ranked = sorted(report.risks, key=lambda r: order.get(r.severity, 3))
    return "\n".join(
        f"- **[{r.severity}]** {r.title} — {r.rationale}" for r in ranked
    )

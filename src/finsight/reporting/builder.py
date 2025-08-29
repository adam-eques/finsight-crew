"""Assemble a full markdown brief from a Report and persist it."""

from __future__ import annotations

import re
from pathlib import Path

from finsight.reporting import templates
from finsight.schemas import Report


def render_markdown(report: Report) -> str:
    return (
        f"# {report.company} ({report.ticker})\n\n"
        f"**Question:** {report.question}\n\n"
        f"## Summary\n\n{report.summary or '_Pending._'}\n\n"
        f"## Key findings\n\n{templates._findings(report)}\n\n"
        f"## Metrics\n\n{templates._metrics(report)}\n\n"
        f"## Risks\n\n{templates._risks(report)}\n"
    )


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "report"


def save_markdown(report: Report, reports_dir: str = "reports") -> Path:
    out_dir = Path(reports_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(report.ticker)}-brief.md"
    path.write_text(render_markdown(report), encoding="utf-8")
    return path

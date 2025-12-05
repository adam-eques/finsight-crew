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


def save_pdf(report: Report, reports_dir: str = "reports"):
    """Best-effort PDF export. Returns the path, or None if reportlab is
    not installed — markdown remains the source of truth."""
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.pdfgen import canvas
    except Exception:
        return None
    out_dir = Path(reports_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(report.ticker)}-brief.pdf"
    c = canvas.Canvas(str(path), pagesize=LETTER)
    text = c.beginText(54, 740)
    for line in render_markdown(report).splitlines():
        text.textLine(line[:110])
    c.drawText(text)
    c.showPage()
    c.save()
    return path


def save_json(report: Report, reports_dir: str = "reports") -> Path:
    from finsight.formats import to_json

    out_dir = Path(reports_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(report.ticker)}-brief.json"
    path.write_text(to_json(report), encoding="utf-8")
    return path


def save_html(report: Report, reports_dir: str = "reports") -> Path:
    from finsight.formats import to_html

    out_dir = Path(reports_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(report.ticker)}-brief.html"
    path.write_text(to_html(report), encoding="utf-8")
    return path

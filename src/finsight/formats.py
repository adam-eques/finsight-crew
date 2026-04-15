"""Render a Report into machine-readable formats."""

from __future__ import annotations

import json

from finsight.schemas import Report


def to_json(report: Report, indent: int = 2) -> str:
    return json.dumps(report.model_dump(), indent=indent)


def to_html(report: Report) -> str:
    from finsight.reporting.builder import render_markdown

    body = render_markdown(report).replace("&", "&amp;").replace("<", "&lt;")
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{report.ticker} brief</title></head>"
        f"<body><pre>{body}</pre></body></html>"
    )


def metrics_to_csv(report: Report) -> str:
    lines = ["name,value,unit"]
    for m in report.metrics:
        lines.append(f"{m.name},{m.value},{m.unit}")
    return "\n".join(lines)

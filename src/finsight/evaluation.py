"""Cheap, deterministic quality checks for a produced report."""

from __future__ import annotations

from finsight.schemas import Report


def completeness(report: Report) -> float:
    """Fraction of expected sections that are populated (0..1)."""
    checks = [
        bool(report.summary.strip()),
        len(report.findings) > 0,
        len(report.metrics) > 0,
        len(report.risks) > 0,
        any(f.source_url for f in report.findings),
    ]
    return sum(checks) / len(checks)

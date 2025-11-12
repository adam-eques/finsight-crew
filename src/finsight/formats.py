"""Render a Report into machine-readable formats."""

from __future__ import annotations

import json

from finsight.schemas import Report


def to_json(report: Report, indent: int = 2) -> str:
    return json.dumps(report.model_dump(), indent=indent)

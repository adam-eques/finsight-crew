"""Typed outputs shared across agents so hand-offs stay structured."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Finding(BaseModel):
    claim: str
    source_url: Optional[str] = None
    confidence: float = Field(0.6, ge=0.0, le=1.0)


class Metric(BaseModel):
    name: str
    value: float
    unit: str = ""
    note: str = ""


class Risk(BaseModel):
    title: str
    severity: str = Field("medium", pattern="^(low|medium|high)$")
    rationale: str = ""


class Report(BaseModel):
    company: str
    ticker: str
    question: str
    summary: str = ""
    findings: List[Finding] = []
    metrics: List[Metric] = []
    risks: List[Risk] = []

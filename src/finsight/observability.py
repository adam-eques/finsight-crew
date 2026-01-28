"""Capture what happened during a run: stages, timings, rough cost."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class RunManifest:
    company: str
    ticker: str
    stages: List[dict] = field(default_factory=list)

    def add_stage(self, name: str, seconds: float, tokens: int = 0) -> None:
        self.stages.append({"name": name, "seconds": seconds, "tokens": tokens})

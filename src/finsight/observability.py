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


    def total_seconds(self) -> float:
        return round(sum(s["seconds"] for s in self.stages), 3)

    def total_tokens(self) -> int:
        return sum(s["tokens"] for s in self.stages)

    def estimate_cost(self, usd_per_1k_tokens: float = 0.003) -> float:
        return round(self.total_tokens() / 1000 * usd_per_1k_tokens, 4)

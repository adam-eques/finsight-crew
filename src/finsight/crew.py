"""Assemble and run the finsight research crew."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from finsight.config import Settings, load_settings
from finsight.logging_utils import get_logger

log = get_logger(__name__)


@dataclass
class ResearchRequest:
    company: str
    ticker: str
    question: str

    def as_inputs(self) -> dict:
        return {"company": self.company, "ticker": self.ticker,
                "question": self.question}

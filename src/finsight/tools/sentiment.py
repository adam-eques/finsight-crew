"""A tiny, transparent lexicon sentiment scorer.

Not a replacement for a trained model, but dependency-free, explainable,
and good enough to flag tone in headlines and disclosures.
"""

from __future__ import annotations

from typing import Type

from pydantic import BaseModel, Field

POSITIVE = {"growth", "beat", "record", "strong", "upgrade", "profit", "gain"}
NEGATIVE = {"loss", "decline", "weak", "downgrade", "probe", "lawsuit", "risk"}


def score(text: str) -> float:
    """Return a sentiment score in [-1, 1]."""
    tokens = [t.strip(".,!?()").lower() for t in text.split()]
    pos = sum(t in POSITIVE for t in tokens)
    neg = sum(t in NEGATIVE for t in tokens)
    total = pos + neg
    if total == 0:
        return 0.0
    return (pos - neg) / total


class SentimentInput(BaseModel):
    text: str = Field(..., description="Text to score for tone")


def make_sentiment_tool():
    from crewai.tools import BaseTool

    class SentimentTool(BaseTool):
        name: str = "sentiment"
        description: str = "Score the tone of a passage from -1 to 1."
        args_schema: Type[BaseModel] = SentimentInput

        def _run(self, text: str) -> str:
            return f"sentiment={score(text):.2f}"

    return SentimentTool()

"""Fetch quote and fundamentals for a ticker via yfinance."""

from __future__ import annotations

from typing import Type

from pydantic import BaseModel, Field

from finsight.logging_utils import get_logger

log = get_logger(__name__)


class MarketDataInput(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol, e.g. AAPL")


def fetch_snapshot(ticker: str) -> dict:
    """Return a compact snapshot dict; isolated for testing/mocking."""
    import yfinance as yf

    info = yf.Ticker(ticker).info
    keys = [
        "shortName", "currentPrice", "marketCap", "trailingPE",
        "profitMargins", "totalRevenue", "totalDebt", "totalCash",
    ]
    return {k: info.get(k) for k in keys}


def make_market_data_tool():
    from crewai.tools import BaseTool

    class MarketDataTool(BaseTool):
        name: str = "market_data"
        description: str = "Get price and fundamentals for a stock ticker."
        args_schema: Type[BaseModel] = MarketDataInput

        def _run(self, ticker: str) -> str:
            snap = fetch_snapshot(ticker)
            return "\n".join(f"{k}: {v}" for k, v in snap.items())

    return MarketDataTool()

"""Look up a company's recent SEC filings through EDGAR's public API."""

from __future__ import annotations

from typing import Type

import requests
from pydantic import BaseModel, Field

from finsight.logging_utils import get_logger

log = get_logger(__name__)
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
UA = "finsight-crew/0.1 (research; contact: adam-eques)"


class FilingsInput(BaseModel):
    ticker: str = Field(..., description="Ticker symbol to look up")
    form: str = Field("10-K", description="Filing form type, e.g. 10-K or 10-Q")
    limit: int = Field(3, ge=1, le=10)


def ticker_to_cik(ticker, session=None):
    s = session or requests.Session()
    data = s.get(TICKERS_URL, headers={"User-Agent": UA}, timeout=20).json()
    ticker = ticker.upper()
    for row in data.values():
        if row["ticker"].upper() == ticker:
            return int(row["cik_str"])
    return None


def recent_filings(ticker, form="10-K", limit=3, session=None):
    s = session or requests.Session()
    cik = ticker_to_cik(ticker, s)
    if cik is None:
        return []
    url = SUBMISSIONS_URL.format(cik=cik)
    payload = s.get(url, headers={"User-Agent": UA}, timeout=20).json()
    recent = payload.get("filings", {}).get("recent", {})
    out = []
    for form_type, date, doc in zip(
        recent.get("form", []), recent.get("filingDate", []),
        recent.get("primaryDocument", []),
    ):
        if form_type == form:
            out.append({"form": form_type, "date": date, "document": doc})
        if len(out) >= limit:
            break
    return out


def make_filings_tool():
    from crewai.tools import BaseTool

    class FilingsTool(BaseTool):
        name: str = "sec_filings"
        description: str = "List a company's recent SEC filings by form type."
        args_schema: Type[BaseModel] = FilingsInput

        def _run(self, ticker, form="10-K", limit=3):
            rows = recent_filings(ticker, form, limit)
            if not rows:
                return "No " + form + " filings found for " + ticker + "."
            return "\n".join(
                r["date"] + " " + r["form"] + " " + r["document"] for r in rows
            )

    return FilingsTool()

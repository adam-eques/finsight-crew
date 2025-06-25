"""Web search tool. Uses Serper if SERPER_API_KEY is present, otherwise
returns an explicit 'search unavailable' message so the crew degrades
gracefully instead of crashing.
"""

from __future__ import annotations

import os
from typing import Type

import requests
from pydantic import BaseModel, Field

from finsight.logging_utils import get_logger

log = get_logger(__name__)
SERPER_URL = "https://google.serper.dev/search"


class WebSearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    num: int = Field(5, ge=1, le=10)


def serper_search(query, num=5, api_key=None):
    api_key = api_key or os.environ.get("SERPER_API_KEY")
    if not api_key:
        return []
    resp = requests.post(
        SERPER_URL,
        headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
        json={"q": query, "num": num},
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json().get("organic", [])[:num]


def format_results(results):
    if not results:
        return "No search results (set SERPER_API_KEY to enable web search)."
    lines = []
    for r in results:
        lines.append(
            "- " + str(r.get("title", "")) + "\n  "
            + str(r.get("link", "")) + "\n  " + str(r.get("snippet", ""))
        )
    return "\n".join(lines)


def make_web_search_tool():
    from crewai.tools import BaseTool

    class WebSearchTool(BaseTool):
        name: str = "web_search"
        description: str = "Search the web for recent, citable information."
        args_schema: Type[BaseModel] = WebSearchInput

        def _run(self, query, num=5):
            return format_results(serper_search(query, num))

    return WebSearchTool()

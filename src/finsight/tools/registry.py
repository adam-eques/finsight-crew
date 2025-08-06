"""Instantiate every tool once and expose them by name."""

from __future__ import annotations

from finsight.logging_utils import get_logger

log = get_logger(__name__)


def build_tools() -> dict:
    """Build all tools, skipping any that fail to import so a missing
    optional dependency never takes down the whole crew."""
    from finsight.tools.web_search import make_web_search_tool
    from finsight.tools.market_data import make_market_data_tool
    from finsight.tools.filings import make_filings_tool
    from finsight.tools.rag import make_filings_rag_tool

    factories = {
        "web_search": make_web_search_tool,
        "market_data": make_market_data_tool,
        "sec_filings": make_filings_tool,
        "filings_rag": make_filings_rag_tool,
    }
    tools = {}
    for name, factory in factories.items():
        try:
            tools[name] = factory()
        except Exception as exc:  # pragma: no cover - defensive
            log.warning("tool %s unavailable: %s", name, exc)
    return tools

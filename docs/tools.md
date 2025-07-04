# Tools

| Tool | Purpose | External dependency |
|---|---|---|
| `web_search` | Recent, citable web results | Serper (optional) |
| `market_data` | Price & fundamentals | yfinance |
| `sec_filings` | Recent SEC filings | EDGAR (public) |
| `calculator` | Deterministic ratios | none |
| `filings_rag` | Q&A over filing text | chromadb |

Every tool degrades gracefully when its optional dependency or API key is
missing, so the crew can run in a reduced mode offline.

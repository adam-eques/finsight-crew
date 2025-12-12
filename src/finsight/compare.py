"""Compare and rank several tickers by shared metrics."""

from __future__ import annotations

from typing import Dict, List, Tuple

Metrics = Dict[str, Dict[str, float]]  # ticker -> {metric: value}


def rank_by(data: Metrics, metric: str, reverse: bool = True) -> List[Tuple[str, float]]:
    items = [(t, m[metric]) for t, m in data.items() if m.get(metric) is not None]
    items.sort(key=lambda pair: pair[1], reverse=reverse)
    return items


def to_markdown(data: Metrics, metrics: List[str]) -> str:
    header = "| Ticker | " + " | ".join(metrics) + " |"
    sep = "|" + "---|" * (len(metrics) + 1)
    rows = [header, sep]
    for ticker, m in data.items():
        cells = [str(m.get(k, "-")) for k in metrics]
        rows.append(f"| {ticker} | " + " | ".join(cells) + " |")
    return "\n".join(rows)

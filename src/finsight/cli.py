"""finsight command line interface."""

from __future__ import annotations

import argparse
from typing import Optional, Sequence

from finsight import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="finsight",
        description="Provider-agnostic multi-agent financial research crew.",
    )
    parser.add_argument("--version", action="version",
                        version=f"finsight {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    research = sub.add_parser("research", help="Research a ticker")
    research.add_argument("ticker")
    research.add_argument("--question", "-q", required=True)
    research.add_argument("--company", default=None,
                          help="Company name (defaults to the ticker)")
    research.add_argument("--provider", default=None,
                          help="Override llm_provider for this run")
    research.add_argument("--model", default=None,
                          help="Override llm_model for this run")
    research.add_argument("--out", default=None,
                          help="Directory to write the markdown brief")
    research.add_argument("--format", default="md",
                          choices=["md", "json", "html"],
                          help="Output format for the brief")

    compare = sub.add_parser("compare", help="Compare tickers by a metric")
    compare.add_argument("tickers", nargs="+")
    compare.add_argument("--metric", default="trailingPE")
    return parser


def _run_research(args) -> int:
    import os

    from finsight.config import load_settings
    from finsight.crew import ResearchRequest, run

    if args.provider:
        os.environ["FINSIGHT_LLM_PROVIDER"] = args.provider
    if args.model:
        os.environ["FINSIGHT_LLM_MODEL"] = args.model
    settings = load_settings()
    request = ResearchRequest(
        company=args.company or args.ticker,
        ticker=args.ticker,
        question=args.question,
    )
    report_text = run(request, settings)
    out_dir = args.out or settings.reports_dir
    from pathlib import Path

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    dest = Path(out_dir) / f"{args.ticker.lower()}-brief.md"
    dest.write_text(report_text, encoding="utf-8")
    print(f"Wrote {dest}")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "research":
        return _run_research(args)
    return 1

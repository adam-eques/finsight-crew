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
    return parser

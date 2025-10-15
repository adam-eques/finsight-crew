"""Minimal end-to-end example.

Requires an API key for the active provider (see .env.example). Run with:
    python examples/run_apple.py
"""

from finsight import ResearchRequest, run


def main():
    request = ResearchRequest(
        company="Apple Inc.",
        ticker="AAPL",
        question="Is the balance sheet healthy heading into next year?",
    )
    print(run(request))


if __name__ == "__main__":
    main()

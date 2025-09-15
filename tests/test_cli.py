import pytest

from finsight.cli import build_parser


def test_research_requires_question():
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["research", "AAPL"])


def test_research_parses_flags():
    parser = build_parser()
    args = parser.parse_args(
        ["research", "AAPL", "-q", "Healthy?", "--provider", "openai"]
    )
    assert args.ticker == "AAPL"
    assert args.question == "Healthy?"
    assert args.provider == "openai"


def test_requires_subcommand():
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])

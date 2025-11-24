import pytest

from finsight.cli import build_parser


def test_format_default_md():
    args = build_parser().parse_args(["research", "AAPL", "-q", "?"])
    assert args.format == "md"


def test_bad_format_rejected():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["research", "AAPL", "-q", "?", "--format", "pdfx"])

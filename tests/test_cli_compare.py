from finsight.cli import build_parser


def test_compare_parses():
    args = build_parser().parse_args(["compare", "AAPL", "MSFT", "--metric", "trailingPE"])
    assert args.tickers == ["AAPL", "MSFT"]
    assert args.metric == "trailingPE"

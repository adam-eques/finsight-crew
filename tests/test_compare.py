from finsight.compare import rank_by


DATA = {
    "AAPL": {"pe": 30.0, "margin": 0.25},
    "MSFT": {"pe": 35.0, "margin": 0.35},
    "NVDA": {"pe": 60.0},
}


def test_rank_desc():
    assert rank_by(DATA, "pe")[0][0] == "NVDA"


def test_rank_asc():
    assert rank_by(DATA, "pe", reverse=False)[0][0] == "AAPL"


def test_missing_metric_skipped():
    ranked = rank_by(DATA, "margin")
    assert "NVDA" not in [t for t, _ in ranked]

import sys
import types
from unittest import mock


def test_fetch_snapshot_selects_keys():
    fake = types.ModuleType("yfinance")
    info = {"shortName": "Apple Inc.", "currentPrice": 190.0,
            "marketCap": 3e12, "junk": 1}
    fake.Ticker = lambda t: types.SimpleNamespace(info=info)
    with mock.patch.dict(sys.modules, {"yfinance": fake}):
        from finsight.tools.market_data import fetch_snapshot
        snap = fetch_snapshot("AAPL")
    assert snap["shortName"] == "Apple Inc."
    assert "junk" not in snap

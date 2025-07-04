from unittest import mock

from finsight.tools import filings


class FakeResp:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def test_recent_filings_filters_form():
    tickers = {"0": {"ticker": "AAPL", "cik_str": 320193}}
    submissions = {"filings": {"recent": {
        "form": ["10-K", "8-K", "10-K"],
        "filingDate": ["2024-11-01", "2024-10-01", "2023-11-01"],
        "primaryDocument": ["a.htm", "b.htm", "c.htm"],
    }}}
    session = mock.Mock()
    session.get.side_effect = [FakeResp(tickers), FakeResp(submissions)]
    rows = filings.recent_filings("AAPL", "10-K", 5, session=session)
    assert len(rows) == 2
    assert all(r["form"] == "10-K" for r in rows)

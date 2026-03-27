import json

from finsight.formats import to_json
from finsight.schemas import Report


def test_to_json_roundtrip():
    r = Report(company="Apple", ticker="AAPL", question="?", summary="ok")
    data = json.loads(to_json(r))
    assert data["ticker"] == "AAPL"
    assert data["summary"] == "ok"


def test_to_html_has_ticker_title():
    from finsight.formats import to_html
    r = Report(company="Apple", ticker="AAPL", question="?")
    html = to_html(r)
    assert "<title>AAPL brief</title>" in html
    assert "<pre>" in html


def test_empty_report_json_valid():
    import json
    from finsight.formats import to_json
    from finsight.schemas import Report
    data = json.loads(to_json(Report(company="A", ticker="A", question="?")))
    assert data["findings"] == []

import json

from finsight.formats import to_json
from finsight.schemas import Report


def test_to_json_roundtrip():
    r = Report(company="Apple", ticker="AAPL", question="?", summary="ok")
    data = json.loads(to_json(r))
    assert data["ticker"] == "AAPL"
    assert data["summary"] == "ok"

from finsight.reporting.builder import save_json, save_html
from finsight.schemas import Report


def _r():
    return Report(company="Apple", ticker="AAPL", question="?", summary="ok")


def test_save_json(tmp_path):
    p = save_json(_r(), str(tmp_path))
    assert p.suffix == ".json" and p.exists()


def test_save_html(tmp_path):
    p = save_html(_r(), str(tmp_path))
    assert p.suffix == ".html" and p.exists()

from finsight.reporting.builder import render_markdown
from finsight.schemas import Report


def test_no_metrics_placeholder():
    md = render_markdown(Report(company="A", ticker="A", question="?"))
    assert "_No metrics recorded._" in md

from finsight.evaluation import completeness
from finsight.schemas import Report, Finding, Metric, Risk


def test_empty_report_low():
    assert completeness(Report(company="A", ticker="A", question="?")) == 0.0


def test_full_report_high():
    r = Report(company="A", ticker="A", question="?", summary="ok",
               findings=[Finding(claim="x", source_url="http://y")],
               metrics=[Metric(name="m", value=1.0)],
               risks=[Risk(title="r")])
    assert completeness(r) == 1.0

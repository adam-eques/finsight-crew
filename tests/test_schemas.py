import pytest
from pydantic import ValidationError

from finsight.schemas import Finding, Risk, Report


def test_confidence_bounds():
    with pytest.raises(ValidationError):
        Finding(claim="x", confidence=2.0)


def test_severity_pattern():
    with pytest.raises(ValidationError):
        Risk(title="x", severity="catastrophic")


def test_report_defaults():
    r = Report(company="Apple", ticker="AAPL", question="?")
    assert r.findings == [] and r.risks == []

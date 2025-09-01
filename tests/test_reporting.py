from finsight.reporting.builder import render_markdown, slugify, save_markdown
from finsight.schemas import Report, Finding, Metric, Risk


def _report():
    return Report(
        company="Apple Inc.", ticker="AAPL", question="Healthy?",
        summary="Solid.",
        findings=[Finding(claim="Services growing", source_url="http://x")],
        metrics=[Metric(name="Gross margin", value=44.0, unit="%")],
        risks=[Risk(title="FX", severity="low"), Risk(title="Regulatory", severity="high")],
    )


def test_render_contains_sections():
    md = render_markdown(_report())
    assert "# Apple Inc. (AAPL)" in md
    assert "## Risks" in md


def test_risks_ranked_high_first():
    md = render_markdown(_report())
    assert md.index("Regulatory") < md.index("FX")


def test_slugify():
    assert slugify("AAPL") == "aapl"
    assert slugify("  ") == "report"


def test_save_markdown(tmp_path):
    path = save_markdown(_report(), str(tmp_path))
    assert path.exists()
    assert path.read_text(encoding="utf-8").startswith("# Apple")

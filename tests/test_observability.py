from finsight.observability import RunManifest


def test_add_stage():
    m = RunManifest(company="Apple", ticker="AAPL")
    m.add_stage("research", 1.2, tokens=500)
    m.add_stage("analyze", 0.8, tokens=300)
    assert len(m.stages) == 2
    assert m.stages[0]["name"] == "research"


def test_totals_and_cost():
    m = RunManifest(company="A", ticker="A")
    m.add_stage("x", 1.0, tokens=1000)
    m.add_stage("y", 2.0, tokens=1000)
    assert m.total_seconds() == 3.0
    assert m.total_tokens() == 2000
    assert m.estimate_cost(0.003) == 0.006

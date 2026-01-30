from finsight.observability import RunManifest


def test_add_stage():
    m = RunManifest(company="Apple", ticker="AAPL")
    m.add_stage("research", 1.2, tokens=500)
    m.add_stage("analyze", 0.8, tokens=300)
    assert len(m.stages) == 2
    assert m.stages[0]["name"] == "research"

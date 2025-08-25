from finsight.crew import ResearchRequest


def test_request_inputs():
    req = ResearchRequest("Apple Inc.", "AAPL", "Is it healthy?")
    inputs = req.as_inputs()
    assert inputs["company"] == "Apple Inc."
    assert inputs["ticker"] == "AAPL"
    assert inputs["question"] == "Is it healthy?"

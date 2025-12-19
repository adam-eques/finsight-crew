from finsight.schemas import Comparison


def test_comparison():
    c = Comparison(metric="pe", tickers=["AAPL", "MSFT"],
                   values={"AAPL": 30.0, "MSFT": 35.0})
    assert c.values["MSFT"] == 35.0

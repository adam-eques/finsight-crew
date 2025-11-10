from finsight.cache import cache_key


def test_stable():
    assert cache_key("AAPL", "10-K") == cache_key("AAPL", "10-K")


def test_order_matters():
    assert cache_key("a", "b") != cache_key("b", "a")

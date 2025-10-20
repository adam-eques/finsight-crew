import pytest

from finsight.net import retry


def test_succeeds_after_retries():
    calls = {"n": 0}

    @retry(times=3, base_delay=0, sleep=lambda _: None)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ValueError("boom")
        return "ok"

    assert flaky() == "ok"
    assert calls["n"] == 3


def test_gives_up():
    @retry(times=2, base_delay=0, sleep=lambda _: None)
    def always():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always()

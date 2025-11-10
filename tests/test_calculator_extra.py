import pytest

from finsight.tools.calculator import return_on_equity, quick_ratio


def test_roe():
    assert return_on_equity(20, 100) == pytest.approx(0.2)


def test_quick_ratio():
    assert quick_ratio(200, 50, 100) == pytest.approx(1.5)


def test_quick_ratio_guard():
    with pytest.raises(ValueError):
        quick_ratio(1, 0, 0)

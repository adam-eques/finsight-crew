import pytest

from finsight.tools.calculator import (
    current_ratio, debt_to_equity, gross_margin, cagr,
)


def test_current_ratio():
    assert current_ratio(200, 100) == 2.0


def test_gross_margin():
    assert gross_margin(100, 60) == pytest.approx(0.4)


def test_cagr():
    assert cagr(100, 200, 1) == pytest.approx(1.0)
    assert cagr(100, 400, 2) == pytest.approx(1.0)


def test_guards():
    with pytest.raises(ValueError):
        debt_to_equity(10, 0)

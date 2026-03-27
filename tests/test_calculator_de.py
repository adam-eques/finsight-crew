import pytest

from finsight.tools.calculator import debt_to_equity


def test_de():
    assert debt_to_equity(50, 200) == pytest.approx(0.25)

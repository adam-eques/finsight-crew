import pytest

from finsight.tools.calculator import interest_coverage


def test_coverage():
    assert interest_coverage(500, 100) == pytest.approx(5.0)

import pytest
from pydantic import ValidationError

from finsight.schemas import Source


def test_url_required():
    with pytest.raises(ValidationError):
        Source(title="x")


def test_ok():
    assert Source(url="http://x").url == "http://x"

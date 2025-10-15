import finsight


def test_version_string():
    assert isinstance(finsight.__version__, str)
    assert finsight.__version__.count(".") >= 2


def test_public_api():
    assert hasattr(finsight, "ResearchRequest")
    assert callable(finsight.run)

from finsight.reporting.builder import slugify


def test_collapse():
    assert slugify("Berkshire  Hathaway!!") == "berkshire-hathaway"

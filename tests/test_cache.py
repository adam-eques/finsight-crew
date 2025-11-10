from finsight.cache import DiskCache


def test_roundtrip(tmp_path):
    c = DiskCache(root=str(tmp_path), ttl=1000)
    c.set("k", {"a": 1})
    assert c.get("k") == {"a": 1}


def test_miss(tmp_path):
    assert DiskCache(root=str(tmp_path)).get("nope") is None


def test_expiry(tmp_path):
    c = DiskCache(root=str(tmp_path), ttl=10)
    c.set("k", 1, now=0)
    assert c.get("k") is None

def test_import():
    import importlib
    mod = importlib.import_module("finsight")
    assert hasattr(mod, "__version__")

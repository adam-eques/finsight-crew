from finsight.reporting.templates import sanitize_cell


def test_escape_pipe():
    assert sanitize_cell("a|b") == "a\\|b"


def test_flatten_newline():
    assert sanitize_cell("a\nb") == "a b"

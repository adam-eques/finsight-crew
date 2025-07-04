from finsight.tools.web_search import format_results, serper_search


def test_empty_results_message():
    assert "No search results" in format_results([])


def test_formats_results():
    out = format_results([{"title": "T", "link": "http://x", "snippet": "S"}])
    assert "http://x" in out and "T" in out


def test_no_api_key_returns_empty(monkeypatch):
    monkeypatch.delenv("SERPER_API_KEY", raising=False)
    assert serper_search("anything") == []

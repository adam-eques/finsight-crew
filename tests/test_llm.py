import pytest

from finsight.llm import resolve_model_id


PRESETS = {
    "anthropic": {"prefix": "anthropic", "default_model": "claude-sonnet-4-20250514"},
    "openai": {"prefix": "openai", "default_model": "gpt-4o"},
}


def test_default_model_used():
    result = resolve_model_id("anthropic", None, PRESETS)
    assert result == "anthropic/claude-sonnet-4-20250514"


def test_explicit_model():
    assert resolve_model_id("openai", "gpt-4o-mini", PRESETS) == "openai/gpt-4o-mini"


def test_prefix_not_doubled():
    assert resolve_model_id("openai", "openai/gpt-4o", PRESETS) == "openai/gpt-4o"


def test_unknown_provider():
    with pytest.raises(ValueError):
        resolve_model_id("cohere", None, PRESETS)

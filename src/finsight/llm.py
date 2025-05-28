"""Provider-agnostic LLM construction.

finsight never hard-codes a vendor. A provider name plus a model string
is resolved against config/llm.yaml into a single litellm-style model id
(e.g. anthropic/claude-sonnet-4-20250514) that CrewAI's LLM accepts.
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml

from finsight.config import CONFIG_DIR, Settings


def _presets(path: Path | None = None) -> dict:
    path = path or (CONFIG_DIR / "llm.yaml")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def resolve_model_id(provider: str, model: str | None = None,
                     presets: dict | None = None) -> str:
    """Return a fully-qualified provider/model id."""
    presets = presets if presets is not None else _presets()
    if provider not in presets:
        raise ValueError(f"unknown llm provider: {provider!r}")
    cfg = presets[provider]
    model = model or cfg["default_model"]
    prefix = cfg["prefix"]
    return model if model.startswith(prefix + "/") else f"{prefix}/{model}"

"""Configuration loading: YAML defaults + environment overrides."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"


def _as_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


@dataclass
class Settings:
    llm_provider: str = "anthropic"
    llm_model: str = "claude-sonnet-4-20250514"
    temperature: float = 0.2
    max_rpm: int = 20
    verbose: bool = True
    data_dir: str = "data"
    reports_dir: str = "reports"
    output_format: str = "md"
    save_manifest: bool = False


_CASTS = {"temperature": float, "max_rpm": int, "verbose": _as_bool,
          "save_manifest": _as_bool}


def load_settings(path: Path | None = None) -> Settings:
    """Load settings.yaml then apply FINSIGHT_* environment overrides."""
    path = path or (CONFIG_DIR / "settings.yaml")
    data = {}
    if path.exists():
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    for field_name in Settings.__dataclass_fields__:
        env_key = f"FINSIGHT_{field_name.upper()}"
        if env_key in os.environ:
            raw = os.environ[env_key]
            data[field_name] = _CASTS.get(field_name, str)(raw)
    known = {k: v for k, v in data.items() if k in Settings.__dataclass_fields__}
    return Settings(**known)

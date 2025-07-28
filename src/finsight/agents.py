"""Build CrewAI agents from config/agents.yaml.

Prompts (role/goal/backstory) live in YAML so they can be tuned without
touching code; this module only wires specs to tools and the LLM.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

from finsight.config import CONFIG_DIR


def load_agent_specs(path: Path | None = None) -> Dict[str, dict]:
    path = path or (CONFIG_DIR / "agents.yaml")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

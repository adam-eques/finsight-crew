"""Build CrewAI tasks from config/tasks.yaml and bind them to agents."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import yaml

from finsight.config import CONFIG_DIR


def load_task_specs(path: Path | None = None) -> Dict[str, dict]:
    path = path or (CONFIG_DIR / "tasks.yaml")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

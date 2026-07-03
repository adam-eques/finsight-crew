"""Build CrewAI tasks from config/tasks.yaml and bind them to agents."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

from finsight.config import CONFIG_DIR


def load_task_specs(path: Path | None = None) -> Dict[str, dict]:
    path = path or (CONFIG_DIR / "tasks.yaml")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


# The crew runs tasks in this order; each feeds the next as context.
TASK_ORDER = ["research", "analyze", "assess_risk", "write_report"]


def build_tasks(agents: dict, specs=None) -> list:
    from crewai import Task

    specs = specs or load_task_specs()
    tasks = []
    for name in TASK_ORDER:
        spec = specs[name]
        agent = agents[spec["agent"]]
        tasks.append(Task(
            description=spec["description"].strip(),
            expected_output=spec["expected_output"].strip(),
            agent=agent,
        ))
    return tasks

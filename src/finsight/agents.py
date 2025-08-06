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


# Which tools each agent is allowed to use.
AGENT_TOOLS = {
    "researcher": ["web_search", "sec_filings"],
    "analyst": ["market_data", "calculator"],
    "risk_assessor": ["filings_rag"],
    "writer": [],
}


def build_agents(settings, tools: dict, specs=None):
    """Return a dict of name -> crewai.Agent.

    ``tools`` maps tool name -> instantiated tool. Imported lazily so specs
    can be unit-tested without crewai installed.
    """
    from crewai import Agent

    from finsight.llm import build_llm

    specs = specs or load_agent_specs()
    llm = build_llm(settings)
    agents = {}
    for name, spec in specs.items():
        chosen = [tools[t] for t in AGENT_TOOLS.get(name, []) if t in tools]
        agents[name] = Agent(
            role=spec["role"].strip(),
            goal=spec["goal"].strip(),
            backstory=spec["backstory"].strip(),
            tools=chosen,
            llm=llm,
            verbose=settings.verbose,
            max_rpm=settings.max_rpm,
            allow_delegation=False,
        )
    return agents

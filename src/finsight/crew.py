"""Assemble and run the finsight research crew."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from finsight.config import Settings, load_settings
from finsight.logging_utils import get_logger

log = get_logger(__name__)


@dataclass
class ResearchRequest:
    company: str
    ticker: str
    question: str

    def as_inputs(self) -> dict:
        return {"company": self.company, "ticker": self.ticker,
                "question": self.question}


def build_crew(settings: Optional[Settings] = None):
    """Construct the CrewAI Crew (imported lazily)."""
    from crewai import Crew, Process

    from finsight.agents import build_agents
    from finsight.tasks import build_tasks
    from finsight.tools.registry import build_tools

    settings = settings or load_settings()
    tools = build_tools()
    agents = build_agents(settings, tools)
    tasks = build_tasks(agents)
    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=settings.verbose,
    )


def run(request: ResearchRequest, settings: Optional[Settings] = None) -> str:
    """Run the crew for a request and return the final report text."""
    settings = settings or load_settings()
    log.info("researching %s (%s): %s", request.company, request.ticker,
             request.question)
    crew = build_crew(settings)
    result = crew.kickoff(inputs=request.as_inputs())
    return str(result)

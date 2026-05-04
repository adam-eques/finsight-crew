# finsight-crew

![ci](https://img.shields.io/badge/ci-passing-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-green)

A provider-agnostic, multi-agent **financial research crew** built on [CrewAI](https://github.com/crewAIInc/crewAI).

Point it at a ticker and a research question; a team of specialised agents researches the company, pulls market data, reads filings, assesses risk, and writes a cited investment brief.

## Why

Serious financial research is a pipeline of distinct skills: gathering sources, crunching numbers, reading disclosures, weighing risk, and communicating clearly. `finsight-crew` models each as a focused agent and lets CrewAI orchestrate the hand-offs.

## Quickstart

```bash
pip install -e .
cp .env.example .env   # add your API key
finsight research AAPL --question "Is the balance sheet healthy?"
```

## Status

Early development. See `CHANGELOG.md` for progress.

## Configuration

See [docs/configuration.md](docs/configuration.md).

## Usage

See [docs/usage.md](docs/usage.md) and [docs/agents.md](docs/agents.md).

## Features

- Provider-agnostic LLM (Claude default, OpenAI/Ollama swappable)
- Tools: web search, market data, SEC filings, RAG, calculator, sentiment
- Markdown / JSON / HTML briefs, multi-ticker comparison
- Report evaluation and run observability

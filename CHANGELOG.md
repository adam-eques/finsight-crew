# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2025-10-08

### Added
- Project scaffolding, packaging, and MIT license.
- YAML settings loader with environment overrides.
- Provider-agnostic LLM factory (Anthropic / OpenAI / Ollama).
- Structured pydantic outputs and a deterministic financial calculator.
- Market-data tool backed by yfinance.
- Web search (Serper) and SEC EDGAR filings tools.
- RAG pipeline: chunking, pluggable embeddings, vector store, retriever.
- `filings_rag` tool for grounded answers over filing text.
- Agents assembled from YAML specs, wired to a tool registry.
- Sequential crew assembly and a typed `ResearchRequest` entrypoint.
- Markdown report rendering with ranked risks; optional PDF export.
- `finsight research` CLI with per-run provider/model overrides.
- CI (ruff + pytest across Python 3.10-3.12), Dockerfile, Makefile.

## [0.2.0] - 2025-11-05

## [0.3.0] - 2025-12-03

### Added
- Retry/backoff and disk cache; ROE & quick-ratio helpers (0.2.0).
- JSON/HTML output formats and `--format` flag (0.3.0).

## [0.4.0] - 2025-12-31
- Multi-ticker `compare` command and comparison helpers.

## [0.5.0] - 2026-01-28
- Lexicon sentiment tool (with negation) and report completeness scoring.

## [Unreleased]
- Run manifest with timings, token totals, and cost estimate.

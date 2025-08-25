# Architecture

```
  question + ticker
        |
        v
  +--------------+     +--------------+     +---------------+     +---------+
  |  Researcher  | --> |   Analyst    | --> | Risk Assessor | --> | Writer  |
  +--------------+     +--------------+     +---------------+     +---------+
     web_search          market_data          filings_rag         report
     sec_filings         calculator            (retriever)         export
```

## RAG pipeline

1. **chunking** — overlapping, word-bounded windows over filing text.
2. **embeddings** — pluggable; a dependency-free hashing embedder ships
   for offline/test runs.
3. **vector_store** — cosine similarity over normalised vectors.
4. **retriever** — indexes a document and returns grounding context.

## Crew

`build_crew()` wires the tool registry, agents, and tasks into a
`Process.sequential` CrewAI `Crew`. `run(request)` interpolates the
company/ticker/question into the task prompts and returns the final
report text.

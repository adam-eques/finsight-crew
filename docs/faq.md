# FAQ

**Does finsight give financial advice?** No — it is a research tool.
Always verify sources before acting.

**How do I switch LLM providers?** Set `FINSIGHT_LLM_PROVIDER` (and the
matching API key). See docs/providers.md.

**Can it run offline?** Partly. Tools degrade gracefully without API
keys, and the hashing embedder needs no network — but the LLM step
requires a provider.

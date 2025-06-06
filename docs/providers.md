# LLM providers

finsight is provider-agnostic. Pick a provider by name; the model id is
assembled for you from `config/llm.yaml`.

```bash
# Claude (default)
export FINSIGHT_LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=...

# OpenAI
export FINSIGHT_LLM_PROVIDER=openai FINSIGHT_LLM_MODEL=gpt-4o
export OPENAI_API_KEY=...

# Local via Ollama
export FINSIGHT_LLM_PROVIDER=ollama FINSIGHT_LLM_MODEL=llama3.1
```

Adding a provider is a few lines of YAML - no code change.

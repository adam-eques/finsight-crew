# Configuration

finsight reads `config/settings.yaml` and then applies environment
overrides. Any setting can be overridden with `FINSIGHT_<KEY>`.

| Setting | Env var | Default |
|---|---|---|
| llm_provider | FINSIGHT_LLM_PROVIDER | anthropic |
| llm_model | FINSIGHT_LLM_MODEL | claude-sonnet-4-20250514 |
| temperature | FINSIGHT_TEMPERATURE | 0.2 |
| max_rpm | FINSIGHT_MAX_RPM | 20 |

Agents and tasks are declared separately in `config/agents.yaml` and
`config/tasks.yaml` so prompts can be tuned without touching code.

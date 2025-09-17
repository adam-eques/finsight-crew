# Usage

```bash
finsight research AAPL -q "Is the balance sheet healthy?"
finsight research MSFT -q "How durable is the cloud moat?" \
    --company "Microsoft" --provider openai --model gpt-4o
```

The brief is written to `reports/<ticker>-brief.md` (override with
`--out`). Provider and model can be overridden per run without editing
any config.

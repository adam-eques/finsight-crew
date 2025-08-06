from finsight.agents import AGENT_TOOLS, load_agent_specs


KNOWN_TOOLS = {"web_search", "sec_filings", "market_data", "calculator", "filings_rag"}


def test_specs_have_required_fields():
    specs = load_agent_specs()
    for name, spec in specs.items():
        assert spec["role"].strip()
        assert spec["goal"].strip()
        assert spec["backstory"].strip()


def test_agent_tools_are_known():
    for name, tools in AGENT_TOOLS.items():
        for t in tools:
            assert t in KNOWN_TOOLS, (name, t)


def test_every_spec_has_tool_mapping():
    for name in load_agent_specs():
        assert name in AGENT_TOOLS

from unittest import mock

from finsight.tools import registry


def test_registry_skips_failing_factory():
    def boom():
        raise RuntimeError("nope")

    with mock.patch.multiple(
        registry,
        build_tools=registry.build_tools,
    ):
        # patch one factory import target to raise
        with mock.patch("finsight.tools.web_search.make_web_search_tool", boom):
            tools = registry.build_tools()
    assert "web_search" not in tools

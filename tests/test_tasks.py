from finsight.tasks import TASK_ORDER, load_task_specs
from finsight.agents import load_agent_specs


def test_task_order_matches_specs():
    specs = load_task_specs()
    assert set(TASK_ORDER) == set(specs)


def test_tasks_reference_known_agents():
    agents = set(load_agent_specs())
    for name, spec in load_task_specs().items():
        assert spec["agent"] in agents

import logging

from finsight.logging_utils import get_logger, set_level_from_env


def test_set_level(monkeypatch):
    monkeypatch.setenv("FINSIGHT_LOG_LEVEL", "warning")
    set_level_from_env()
    assert get_logger().level == logging.WARNING

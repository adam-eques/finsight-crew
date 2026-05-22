"""Small logging helper so tools and crew share one format."""

import logging

_CONFIGURED = False


def get_logger(name: str = "finsight") -> logging.Logger:
    global _CONFIGURED
    if not _CONFIGURED:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
            datefmt="%H:%M:%S",
        )
        _CONFIGURED = True
    return logging.getLogger(name)


def set_level_from_env(env_var: str = "FINSIGHT_LOG_LEVEL") -> None:
    import os

    level = os.environ.get(env_var)
    if level:
        get_logger().setLevel(level.upper())

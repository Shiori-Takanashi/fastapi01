import logging
import pytest
from logging import StreamHandler

from fastapi01.infra.logging.logconfig import build_app_logger


@pytest.mark.usefixtures("reset_logging")
def test_build_app_logger_v01():
    logger = logging.getLogger("fastapi01.test")
    build_app_logger(logger)

    configured_handlers = logger.handlers

    s_handlers = [
        h
        for h in configured_handlers
        if type(h) is StreamHandler and getattr(h, "name", None) == "stream-h"
    ]

    assert len(s_handlers) == 1

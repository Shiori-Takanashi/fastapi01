import logging
from pathlib import Path

from fastapi01.infra.logging.handlers import build_handlers


APP_LOGGER_NAME = "fastapi01"


def configure_logging() -> logging.Logger:
    logger = logging.getLogger(APP_LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    log_dir = Path("logs")
    timed_handler, file_handler, stream_handler = build_handlers(log_dir)

    logger.addHandler(timed_handler)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def get_app_logger() -> logging.Logger:
    return logging.getLogger(APP_LOGGER_NAME)

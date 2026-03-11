import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from fastapi01.infra.logging.formatters import (
    build_console_formatter,
    build_file_formatter,
)


FILE_LEVEL = logging.INFO
STREAM_LEVEL = logging.WARNING


def build_handlers(
    log_dir: Path,
) -> tuple[logging.Handler, logging.Handler, logging.Handler]:
    log_dir.mkdir(parents=True, exist_ok=True)

    file_formatter = build_file_formatter()
    console_formatter = build_console_formatter()

    timed_handler = TimedRotatingFileHandler(
        filename=log_dir / "app_timed.log",
        when="midnight",
        backupCount=7,
        encoding="utf-8",
    )
    timed_handler.setLevel(FILE_LEVEL)
    timed_handler.setFormatter(file_formatter)

    file_handler = logging.FileHandler(log_dir / "app.log", encoding="utf-8")
    file_handler.setLevel(FILE_LEVEL)
    file_handler.setFormatter(file_formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(STREAM_LEVEL)
    stream_handler.setFormatter(console_formatter)

    return timed_handler, file_handler, stream_handler

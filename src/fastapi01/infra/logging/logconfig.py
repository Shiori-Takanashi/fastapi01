import logging
from logging import Logger

from .formatters import build_stream_formatter, build_file_formatter
from .handlers import build_stream_handler, build_file_handler
from .levels import build_stream_level, build_file_level
from .logpath import build_filepath

from .handlers import find_stream_handler, find_file_handler

APP_LOGGER_NAME: str = "fast01"


def build_app_logger(app_logger: Logger | None = None) -> Logger:
    # アプリ専用Loggerの作成
    if app_logger is None:
        app_logger = logging.getLogger(APP_LOGGER_NAME)

    # Loggerの伝播
    app_logger.propagate = False

    # LoggerのLevel
    app_logger.setLevel(1)

    # Streamハンドラーに関する処理
    sh = find_stream_handler(app_logger)
    if sh is None:
        sh = add_stream_handler(app_logger)

    fh = find_file_handler(app_logger)
    if fh is None:
        fh = add_file_handler(app_logger)

    return app_logger


def add_stream_handler(app_logger: Logger) -> None:
    sh = build_stream_handler()

    # Formatterに関する処理
    fmt = build_stream_formatter()
    sh.setFormatter(fmt)

    # Levelに関する処理
    level = build_stream_level()
    sh.setLevel(level)

    app_logger.addHandler(sh)


def add_file_handler(app_logger: Logger) -> None:
    fh = build_file_handler(build_filepath())

    # Formatterに関する処理
    fmt = build_file_formatter()
    fh.setFormatter(fmt)

    # Levelに関する処理
    level = build_file_level()
    fh.setLevel(level)

    app_logger.addHandler(fh)

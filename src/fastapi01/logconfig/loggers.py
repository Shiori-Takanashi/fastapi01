import logging
from logging import FileHandler, StreamHandler

from .formatters import build_stream_formatter, build_file_formatter
from .handlers import build_stream_handler, build_file_handler
from .levels import build_stream_level, build_file_level
from .logsys import build_filepath

from .handlers import find_stream_handler, find_file_handler


def configure_logging(logger_name: str = "DEFAULT_NAME") -> None:
    logger = logging.getLogger(logger_name)

    # Loggerの伝播
    logger.propagate = False

    # LoggerのLevel
    logger.setLevel(logging.DEBUG)

    # Streamハンドラーに関する処理
    sh = find_stream_handler(logger)
    if sh is None:
        sh = get_stream_handler()
        logger.addHandler(sh)

    fh = find_file_handler(logger)
    if fh is None:
        fh = get_file_handler()
        logger.addHandler(fh)


def get_stream_handler() -> StreamHandler:
    sh = build_stream_handler()

    # Formatterに関する処理
    fmt = build_stream_formatter()
    sh.setFormatter(fmt)

    # Levelに関する処理
    level = build_stream_level()
    sh.setLevel(level)

    return sh


def get_file_handler() -> FileHandler:
    fh = build_file_handler(build_filepath())

    # Formatterに関する処理
    fmt = build_file_formatter()
    fh.setFormatter(fmt)

    # Levelに関する処理
    level = build_file_level()
    fh.setLevel(level)

    return fh


def main() -> None:
    logger = logging.getLogger(__name__)
    configure_logging(__name__)
    logger.info("informationです。")
    logger.debug("debugです。")


if __name__ == "__main__":
    main()

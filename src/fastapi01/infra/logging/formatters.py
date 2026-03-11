import logging


FILE_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"
CONSOLE_FORMAT = "%(levelname)s %(name)s %(message)s"


def build_file_formatter() -> logging.Formatter:
    return logging.Formatter(FILE_FORMAT)


def build_console_formatter() -> logging.Formatter:
    return logging.Formatter(CONSOLE_FORMAT)

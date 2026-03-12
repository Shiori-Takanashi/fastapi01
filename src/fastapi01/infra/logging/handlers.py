from pathlib import Path
from logging import Logger, StreamHandler, FileHandler

SH_NAME = "stream-h"
FH_NAME = "file-h"


def find_stream_handler(logger: Logger, h_name: str = SH_NAME) -> StreamHandler | None:
    for h in logger.handlers:
        if type(h) is StreamHandler and getattr(h, "name", None) == h_name:
            return h
    return None


def build_stream_handler(h_name: str = SH_NAME) -> StreamHandler:
    sh = StreamHandler()
    sh.set_name(h_name)
    return sh


def find_file_handler(logger: Logger, h_name: str = FH_NAME) -> FileHandler | None:
    for h in logger.handlers:
        if type(h) is FileHandler and getattr(h, "name", None) == h_name:
            return h
    return None


def build_file_handler(filepath: Path, h_name: str = FH_NAME) -> FileHandler:
    fh = FileHandler(
        filepath,
        encoding="utf-8",
    )
    fh.set_name(h_name)
    return fh

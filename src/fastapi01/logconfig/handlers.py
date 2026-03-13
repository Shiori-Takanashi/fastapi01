from pathlib import Path
from logging import Logger, StreamHandler, FileHandler

SH_NAME = "stream-h"
FH_NAME = "file-h"


def find_stream_handler(logger: Logger, h_name: str = SH_NAME) -> StreamHandler | None:
    for h in logger.handlers:
        # 万が一、Handler.set_name()されていない場合を想定
        # 従って、Noneを使って防御コードにする
        if getattr(h, "name", None) == h_name:
            # handler.nameの判別だけでFileHandlerであることは確定
            # 従ってtype判別は防御的コード
            if type(h) is StreamHandler:
                return h
    return None


def find_file_handler(logger: Logger, h_name: str = FH_NAME) -> FileHandler | None:
    for h in logger.handlers:
        # 万が一、Handler.set_name()されていない場合を想定
        # 従って、Noneを使って防御コードにする
        if getattr(h, "name", None) == h_name:
            # handler.nameの判別だけでFileHandlerであることは確定
            # 従ってtype判別は防御的コード
            if type(h) is FileHandler:
                return h
    return None


def build_stream_handler(h_name: str = SH_NAME) -> StreamHandler:
    sh = StreamHandler()
    sh.set_name(h_name)
    return sh


def build_file_handler(filepath: Path, h_name: str = FH_NAME) -> FileHandler:
    fh = FileHandler(
        filepath,
        encoding="utf-8",
    )
    fh.set_name(h_name)
    return fh

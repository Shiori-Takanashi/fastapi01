from logging import Formatter

FILE_FMT = "%(levelname)s %(name)s %(message)s"
STREAM_FMT = "%(asctime)s %(levelname)s %(name)s %(message)s"


def build_stream_formatter(stream_format: str = STREAM_FMT) -> Formatter:
    return Formatter(stream_format)


def build_file_formatter(
    file_format: str = FILE_FMT,
) -> Formatter:
    return Formatter(file_format)

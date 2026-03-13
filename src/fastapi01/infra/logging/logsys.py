from pathlib import Path
from datetime import datetime
from itertools import chain, islice

DIR_NAME = "logs"
FILE_NAME_OF_BASE = "app.log"


def build_filepath(
    dirname: str = DIR_NAME,
    filename_of_base: str = FILE_NAME_OF_BASE,
) -> Path:
    dirpath = _ensure_dirpath(dirname)
    filename = _create_filename(filename_of_base)
    return dirpath / filename


def find_project_root(
    start: Path,
    markers: tuple[str, ...] = ("pyproject.toml", ".git"),
    depth: int = 12,
) -> Path:
    if depth < 0:
        raise ValueError("depth must be >= 0")

    if not markers:
        raise ValueError("markers must not be empty")

    current = start.resolve()

    if current.is_file():
        current = current.parent

    for directory in chain([current], islice(current.parents, depth)):
        for marker in markers:
            if (directory / marker).exists():
                return directory

    raise RuntimeError("プロジェクトルートが見つかりません。")


def _ensure_dirpath(dirname: str) -> Path:
    try:
        dirpath = Path(dirname).resolve(strict=False)
    except OSError as e:
        raise ValueError(f"OSErrorが発生しました: {dirname}") from e

    except RuntimeError as e:
        raise ValueError(f"RuntimeError が発生しました: {dirname}") from e

    dirpath.mkdir(parents=True, exist_ok=True)

    return dirpath


def _create_filename(basename: str) -> str:
    if basename.count(".") != 1:
        raise ValueError("basenameは'.'を一つだけ含んでください。")

    stem, extension = basename.split(".")
    return f"{stem}-{datetime.now():%Y-%m-%d}.{extension}"

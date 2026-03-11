from fastapi import HTTPException


def parse_id(id_str: str) -> int:
    # 数字のみ許可
    if not id_str.isdigit():
        raise HTTPException(status_code=422, detail="id must be numeric")

    # 002は禁止
    if len(id_str) >= 3 and id_str.startswith("0"):
        raise HTTPException(status_code=422, detail="leading zeros not allowed")

    return int(id_str)

from pydantic import BaseModel
from typing import Optional


class Country(BaseModel):
    id: int
    name_en: str
    continent: str
    capital: Optional[str] = None

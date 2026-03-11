from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional


class Country(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    name_en: str
    continent: str
    capital: Optional[str] = None

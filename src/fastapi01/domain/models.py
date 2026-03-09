from pydantic import BaseModel


class Country(BaseModel):
    id: int
    name_en: str
    continent: str
    capital: str | None

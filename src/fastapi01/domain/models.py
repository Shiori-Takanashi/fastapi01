from pydantic import BaseModel


class CountryResponse(BaseModel):
    id: int
    name_en: str
    continent: str
    capital: str | None

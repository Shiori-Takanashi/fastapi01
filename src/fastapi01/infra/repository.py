import json
from pathlib import Path

from fastapi01.domain.models import Country


DATA_PATH = Path("data/countries.json")


class CountryRepository:
    def load_all(self) -> list[Country]:
        data = json.loads(DATA_PATH.read_text())
        return [
            Country(
                id=i,
                name_en=x["name_en"],
                continent=x["continent"],
                capital=x.get("capital"),
            )
            for i, x in enumerate(data, start=1)
        ]

    def find_by_id(self, id: int) -> Country | None:
        countries = self.load_all()

        for c in countries:
            if c.id == id:
                return c

        return None

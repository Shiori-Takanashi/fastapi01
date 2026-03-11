from fastapi01.infra.repository import CountryRepository
from fastapi01.domain.models import Country


class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_countries(self) -> list[Country]:
        return self.repo.load_all()

    def get_country(self, id: int) -> Country | None:
        return self.repo.find_by_id(id)

from fastapi01.infra.repository import CountryRepository
from fastapi01.domain.models import CountryResponse


class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_countries(self) -> list[CountryResponse]:
        return self.repo.load_all()

    def get_country(self, id: int) -> CountryResponse | None:
        return self.repo.find_by_id(id)

from fastapi import APIRouter, HTTPException

from fastapi01.application.service import CountryService


router = APIRouter()

service = CountryService()


@router.get("/all")
def list_countries():
    return service.list_countries()


@router.get("/{id}")
def get_country(id: int):
    country = service.get_country(id)

    if not country:
        raise HTTPException(status_code=404)

    return country

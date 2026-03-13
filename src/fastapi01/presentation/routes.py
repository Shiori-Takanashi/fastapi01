from fastapi import APIRouter, HTTPException
import logging

from fastapi01.application.service import CountryService


router = APIRouter()
logger = logging.getLogger(__name__)

service = CountryService()


@router.get("/all")
def list_countries():
    logger.debug("すべての国データを呼び出します。")

    countries = service.list_countries()

    logger.info("返却した国データの合計=%s", len(countries))

    return countries


@router.get("/{id}")
def get_country(id: int):
    logger.debug("国を呼び出します。id=%s", id)

    country = service.get_country(id)

    if not country:
        logger.warning("国データが見つかりません。id=%s", id)
        raise HTTPException(status_code=404)

    logger.info("国データを返却します。id=%s", id)

    return country

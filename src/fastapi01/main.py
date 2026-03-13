import logging
from fastapi import FastAPI

from fastapi01.presentation.routes import router
from fastapi01.logconfig.logger import configure_logging

logger_name = "fastapi01"
logger = logging.getLogger(logger_name)
configure_logging(logger_name)

app = FastAPI()

app.include_router(router)

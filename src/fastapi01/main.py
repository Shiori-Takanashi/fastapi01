from fastapi import FastAPI

from fastapi01.presentation.routes import router
from fastapi01.logconfig.loggers import configure_logging

configure_logging()

app = FastAPI()

app.include_router(router)

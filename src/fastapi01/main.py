from fastapi import FastAPI

from fastapi01.presentation.routes import router
from fastapi01.logconfig.loggers import configure_logging

logger = configure_logging(__name__)

app = FastAPI()

app.include_router(router)

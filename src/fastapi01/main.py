from fastapi import FastAPI

from fastapi01.presentation.routes import router

app = FastAPI()

app.include_router(router)

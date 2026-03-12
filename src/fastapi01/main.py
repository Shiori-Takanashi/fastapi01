from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi01.infra.logging.logconfig import build_app_logger
from fastapi01.presentation.routes import router

logger = build_app_logger()


app = FastAPI()

app.include_router(router)


@app.exception_handler(Exception)
async def handle_unexpected_exception(request: Request, exc: Exception):
    logger.exception(
        "InternalServerError method=%s path=%s",
        request.method,
        request.url.path,
    )
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

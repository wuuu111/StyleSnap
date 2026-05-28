from __future__ import annotations

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.database import configure_database, get_database_label, get_db, initialize_database
from app.routers.clothes import router as clothes_router
from app.routers.health import router as health_router
from app.routers.outfits import router as outfits_router
from app.routers.weather import router as weather_router
from app.schemas.errors import ErrorResponse
from app.services.clothing_service import seed_demo_clothes


def _allowed_origins() -> list[str]:
    raw_origins = os.getenv(
        "STYLESNAP_CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    )
    return [origin.strip() for origin in raw_origins.split(",") if origin.strip()]


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_database()
    initialize_database()
    db = next(get_db())
    try:
        seed_demo_clothes(db)
    finally:
        db.close()
    yield


def _error_response(status_code: int, code: str, message: str, details: dict | list | None = None) -> JSONResponse:
    payload = ErrorResponse(
        error={
            "code": code,
            "message": message,
            "details": details if isinstance(details, dict) else {"errors": details or []},
        }
    )
    return JSONResponse(status_code=status_code, content=payload.model_dump())


def create_app() -> FastAPI:
    app = FastAPI(
        title="StyleSnap Backend",
        version="0.2.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=_allowed_origins(),
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
        return _error_response(400, "INVALID_INPUT", "Invalid request payload", exc.errors())

    @app.exception_handler(HTTPException)
    async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
        if isinstance(exc.detail, dict) and {"code", "message", "details"} <= set(exc.detail.keys()):
            return _error_response(exc.status_code, exc.detail["code"], exc.detail["message"], exc.detail["details"])
        return _error_response(exc.status_code, "HTTP_ERROR", str(exc.detail), {})

    app.include_router(health_router)
    app.include_router(clothes_router)
    app.include_router(outfits_router)
    app.include_router(weather_router)
    return app


app = create_app()

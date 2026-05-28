from __future__ import annotations

from fastapi import APIRouter

from app.database import get_database_label


router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "stylesnap-backend",
        "database": get_database_label(),
    }

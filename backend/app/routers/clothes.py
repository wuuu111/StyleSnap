from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.clothing import (
    ClothingAnalyzeRequest,
    ClothingAnalyzeResponse,
    ClothingCategory,
    ClothingCreate,
    ClothingRead,
    ClothingUpdate,
)
from app.services.ai_vision_service import analyze_image_url
from app.services.clothing_service import (
    create_clothing_item,
    delete_clothing_item,
    get_clothing_item,
    list_clothes,
    update_clothing_item,
)


router = APIRouter(prefix="/api/clothes", tags=["clothes"])


@router.post("", response_model=ClothingRead, status_code=201)
def create_clothing(payload: ClothingCreate, db: Session = Depends(get_db)) -> ClothingRead:
    return create_clothing_item(db, payload)


@router.get("", response_model=list[ClothingRead])
def get_clothes(
    category: ClothingCategory | None = None,
    color: str | None = None,
    season: str | None = None,
    db: Session = Depends(get_db),
) -> list[ClothingRead]:
    return list_clothes(db, category=category, color=color, season=season)


@router.get("/{item_id}", response_model=ClothingRead)
def get_clothing(item_id: int, db: Session = Depends(get_db)) -> ClothingRead:
    return get_clothing_item(db, item_id)


@router.put("/{item_id}", response_model=ClothingRead)
def update_clothing(item_id: int, payload: ClothingUpdate, db: Session = Depends(get_db)) -> ClothingRead:
    return update_clothing_item(db, item_id, payload)


@router.delete("/{item_id}", status_code=204)
def delete_clothing(item_id: int, db: Session = Depends(get_db)) -> Response:
    delete_clothing_item(db, item_id)
    return Response(status_code=204)


@router.post("/analyze", response_model=ClothingAnalyzeResponse)
def analyze_clothing(payload: ClothingAnalyzeRequest) -> ClothingAnalyzeResponse:
    try:
        return analyze_image_url(payload.image_url)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail={
                "code": "INVALID_INPUT",
                "message": str(exc),
                "details": {},
            },
        ) from exc

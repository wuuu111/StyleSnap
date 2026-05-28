from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.outfit import OutfitRecommendationRequest, OutfitRecommendationResponse
from app.services.recommendation_service import recommend_outfits


router = APIRouter(prefix="/api/outfits", tags=["outfits"])


@router.post("/recommend", response_model=OutfitRecommendationResponse, response_model_exclude_none=True)
def recommend(
    payload: OutfitRecommendationRequest,
    db: Session = Depends(get_db),
) -> OutfitRecommendationResponse:
    return recommend_outfits(db, payload)

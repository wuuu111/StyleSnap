from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_validator

from app.schemas.clothing import ClothingRead
from app.schemas.weather import WeatherSkillResponse


OCCASION_OPTIONS = ["上课", "实习", "通勤", "约会", "运动", "面试", "休闲"]
TARGET_STYLE_OPTIONS = [
    "日系简约",
    "韩系校园",
    "Clean Fit",
    "City Boy",
    "通勤轻熟",
    "运动休闲",
    "美式复古",
    "Old Money",
]


class WeatherSourceByCity(BaseModel):
    type: Literal["city"]
    city: str = Field(min_length=1)


class WeatherSourceByLocation(BaseModel):
    type: Literal["location"]
    lat: float
    lon: float


WeatherSourceInput = Annotated[
    WeatherSourceByCity | WeatherSourceByLocation,
    Field(discriminator="type"),
]


class OutfitRecommendationRequest(BaseModel):
    occasion: str = Field(min_length=1)
    target_style: str = Field(min_length=1)
    preference_text: str = ""
    weather_source: WeatherSourceInput

    @field_validator("occasion")
    @classmethod
    def validate_occasion(cls, value: str) -> str:
        normalized = value.strip()
        if normalized not in OCCASION_OPTIONS:
            raise ValueError("Invalid occasion")
        return normalized

    @field_validator("target_style")
    @classmethod
    def validate_target_style(cls, value: str) -> str:
        normalized = value.strip()
        if normalized not in TARGET_STYLE_OPTIONS:
            raise ValueError("Invalid target style")
        return normalized

    @field_validator("preference_text")
    @classmethod
    def normalize_preference_text(cls, value: str) -> str:
        return value.strip()


class RecommendedOutfitItem(BaseModel):
    role: str
    item: ClothingRead


class OutfitScoreBreakdown(BaseModel):
    weather_fit: int
    style_match: int
    color_harmony: int
    occasion_fit: int
    user_preference: int


class OutfitReasoning(BaseModel):
    summary: str
    weather_reasoning: str
    style_reasoning: str
    color_reasoning: str
    occasion_reasoning: str
    preference_reasoning: str


class RecommendedOutfit(BaseModel):
    id: str
    items: list[RecommendedOutfitItem]
    total_score: int
    score_breakdown: OutfitScoreBreakdown
    reasoning: OutfitReasoning
    warnings: list[str]


class RecommendationMeta(BaseModel):
    candidate_count: int
    returned_count: int
    scoring_version: str


class OutfitRecommendationResponse(BaseModel):
    weather_context: WeatherSkillResponse
    recommended_outfits: list[RecommendedOutfit]
    meta: RecommendationMeta

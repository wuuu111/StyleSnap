from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class ClothingCategory(StrEnum):
    TOP = "top"
    PANTS = "pants"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    HAT = "hat"
    BAG = "bag"
    ACCESSORY = "accessory"


class ClothingThickness(StrEnum):
    THIN = "thin"
    MEDIUM = "medium"
    THICK = "thick"


class ClothingBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    image_url: str = ""
    category: ClothingCategory
    color: str = Field(min_length=1, max_length=64)
    style_tags: list[str] = Field(default_factory=list)
    season_tags: list[str] = Field(default_factory=list)
    thickness: ClothingThickness
    min_temperature: int | None = None
    max_temperature: int | None = None
    rain_suitable: bool = False
    occasion_tags: list[str] = Field(default_factory=list)
    notes: str = ""

    @field_validator("style_tags", "season_tags", "occasion_tags")
    @classmethod
    def strip_tag_values(cls, values: list[str]) -> list[str]:
        return [value.strip() for value in values if value.strip()]


class ClothingCreate(ClothingBase):
    pass


class ClothingUpdate(ClothingBase):
    pass


class ClothingRead(ClothingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ClothingAnalyzeRequest(BaseModel):
    image_url: str


class ClothingAnalyzeResponse(ClothingBase):
    pass

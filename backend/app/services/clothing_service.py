from __future__ import annotations

import os

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.clothing import ClothingItem
from app.schemas.clothing import ClothingCreate, ClothingRead, ClothingUpdate


DEMO_CLOTHES: list[dict] = [
    {
        "name": "白色 T 恤",
        "image_url": "https://example.com/demo-white-tshirt.jpg",
        "category": "top",
        "color": "white",
        "style_tags": ["Clean Fit"],
        "season_tags": ["summer"],
        "thickness": "thin",
        "min_temperature": 20,
        "max_temperature": 32,
        "rain_suitable": False,
        "occasion_tags": ["上课", "休闲"],
        "notes": "Demo seed item.",
    },
    {
        "name": "黑色直筒裤",
        "image_url": "https://example.com/demo-black-pants.jpg",
        "category": "pants",
        "color": "black",
        "style_tags": ["Clean Fit", "通勤"],
        "season_tags": ["all-season"],
        "thickness": "medium",
        "min_temperature": 10,
        "max_temperature": 28,
        "rain_suitable": True,
        "occasion_tags": ["通勤"],
        "notes": "Demo seed item.",
    },
    {
        "name": "浅灰色卫衣",
        "image_url": "https://example.com/demo-gray-sweatshirt.jpg",
        "category": "top",
        "color": "gray",
        "style_tags": ["日系简约", "休闲"],
        "season_tags": ["spring", "autumn"],
        "thickness": "medium",
        "min_temperature": 12,
        "max_temperature": 24,
        "rain_suitable": True,
        "occasion_tags": ["休闲", "上课"],
        "notes": "Demo seed item.",
    },
    {
        "name": "深蓝牛仔裤",
        "image_url": "https://example.com/demo-denim-jeans.jpg",
        "category": "pants",
        "color": "navy",
        "style_tags": ["美式复古", "休闲"],
        "season_tags": ["all-season"],
        "thickness": "medium",
        "min_temperature": 8,
        "max_temperature": 28,
        "rain_suitable": True,
        "occasion_tags": ["休闲"],
        "notes": "Demo seed item.",
    },
    {
        "name": "黑色外套",
        "image_url": "https://example.com/demo-black-jacket.jpg",
        "category": "outerwear",
        "color": "black",
        "style_tags": ["通勤", "简约"],
        "season_tags": ["autumn", "winter"],
        "thickness": "thick",
        "min_temperature": 5,
        "max_temperature": 18,
        "rain_suitable": True,
        "occasion_tags": ["通勤", "面试"],
        "notes": "Demo seed item.",
    },
    {
        "name": "白色运动鞋",
        "image_url": "https://example.com/demo-white-sneakers.jpg",
        "category": "shoes",
        "color": "white",
        "style_tags": ["Clean Fit", "运动休闲"],
        "season_tags": ["all-season"],
        "thickness": "medium",
        "min_temperature": 0,
        "max_temperature": 32,
        "rain_suitable": False,
        "occasion_tags": ["通勤", "上课"],
        "notes": "Demo seed item.",
    },
    {
        "name": "黑色皮鞋",
        "image_url": "https://example.com/demo-black-leather-shoes.jpg",
        "category": "shoes",
        "color": "black",
        "style_tags": ["通勤", "面试"],
        "season_tags": ["all-season"],
        "thickness": "medium",
        "min_temperature": 0,
        "max_temperature": 30,
        "rain_suitable": True,
        "occasion_tags": ["面试", "通勤"],
        "notes": "Demo seed item.",
    },
    {
        "name": "棒球帽",
        "image_url": "https://example.com/demo-cap.jpg",
        "category": "hat",
        "color": "black",
        "style_tags": ["运动休闲", "美式复古"],
        "season_tags": ["summer"],
        "thickness": "thin",
        "min_temperature": 18,
        "max_temperature": 35,
        "rain_suitable": False,
        "occasion_tags": ["休闲"],
        "notes": "Demo seed item.",
    },
]


def _not_found() -> HTTPException:
    return HTTPException(status_code=404, detail={"code": "NOT_FOUND", "message": "Clothing item not found", "details": {}})


def seed_demo_clothes(db: Session) -> None:
    if os.getenv("STYLESNAP_ENABLE_DEMO_SEED", "true").lower() != "true":
        return

    if db.scalar(select(ClothingItem.id).limit(1)) is not None:
        return

    db.add_all(ClothingItem(**item) for item in DEMO_CLOTHES)
    db.commit()


def list_clothes(
    db: Session,
    category: str | None = None,
    color: str | None = None,
    season: str | None = None,
) -> list[ClothingItem]:
    statement = select(ClothingItem).order_by(ClothingItem.created_at.desc(), ClothingItem.id.desc())

    if category:
        statement = statement.where(ClothingItem.category == category)
    if color:
        statement = statement.where(ClothingItem.color == color)

    items = list(db.scalars(statement))
    if season:
        season_normalized = season.strip().lower()
        items = [
            item
            for item in items
            if any(tag.lower() == season_normalized for tag in item.season_tags)
        ]
    return items


def get_clothing_item(db: Session, item_id: int) -> ClothingItem:
    item = db.get(ClothingItem, item_id)
    if item is None:
        raise _not_found()
    return item


def create_clothing_item(db: Session, payload: ClothingCreate) -> ClothingItem:
    item = ClothingItem(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_clothing_item(db: Session, item_id: int, payload: ClothingUpdate) -> ClothingItem:
    item = get_clothing_item(db, item_id)
    for field, value in payload.model_dump().items():
        setattr(item, field, value)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_clothing_item(db: Session, item_id: int) -> None:
    item = get_clothing_item(db, item_id)
    db.delete(item)
    db.commit()

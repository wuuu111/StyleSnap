from __future__ import annotations

from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ClothingItem(Base):
    __tablename__ = "clothing_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    image_url: Mapped[str] = mapped_column(String(500), default="", nullable=False)
    category: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    color: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    style_tags: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    season_tags: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    thickness: Mapped[str] = mapped_column(String(32), nullable=False)
    min_temperature: Mapped[int | None] = mapped_column(Integer, nullable=True)
    max_temperature: Mapped[int | None] = mapped_column(Integer, nullable=True)
    rain_suitable: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    occasion_tags: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    notes: Mapped[str] = mapped_column(Text, default="", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

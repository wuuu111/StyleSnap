from __future__ import annotations

from typing import Protocol


class StylistProvider(Protocol):
    def enhance_outfit_recommendations(
        self,
        *,
        user_context: dict,
        weather_context: dict,
        candidate_outfits: list[dict],
    ) -> dict:
        ...

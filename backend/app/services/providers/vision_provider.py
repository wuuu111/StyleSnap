from __future__ import annotations

from typing import Protocol


class VisionProvider(Protocol):
    def analyze_clothing_image(self, *, image_reference: str) -> dict:
        ...

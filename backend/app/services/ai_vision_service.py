from __future__ import annotations

from app.schemas.clothing import ClothingAnalyzeResponse
from app.services.providers.mock_vision_provider import MockVisionProvider
from app.services.providers.provider_factory import get_vision_provider


def analyze_image_url(image_url: str) -> ClothingAnalyzeResponse:
    provider = get_vision_provider()
    try:
        return provider.analyze_clothing_image(image_reference=image_url)
    except NotImplementedError:
        return MockVisionProvider().analyze_clothing_image(image_reference=image_url)

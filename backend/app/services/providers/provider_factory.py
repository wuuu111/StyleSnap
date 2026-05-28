from __future__ import annotations

import os

from app.services.providers.deepseek_stylist_provider import DeepSeekStylistProvider
from app.services.providers.mock_stylist_provider import MockStylistProvider
from app.services.providers.mock_vision_provider import MockVisionProvider
from app.services.providers.vision_provider_placeholder import VisionProviderPlaceholder


def get_stylist_provider():
    provider_name = os.getenv("STYLIST_PROVIDER", "mock").strip().lower() or "mock"
    if provider_name != "deepseek":
        return MockStylistProvider()

    if not os.getenv("DEEPSEEK_API_KEY", "").strip():
        return MockStylistProvider(fallback_used=True)

    return DeepSeekStylistProvider()


def get_vision_provider():
    provider_name = os.getenv("VISION_PROVIDER", "mock").strip().lower() or "mock"
    if provider_name == "mock":
        return MockVisionProvider()

    vision_api_key = os.getenv("VISION_API_KEY", "").strip()
    vision_base_url = os.getenv("VISION_BASE_URL", "").strip()
    vision_model = os.getenv("VISION_MODEL", "").strip()

    if not all([vision_api_key, vision_base_url, vision_model]):
        return MockVisionProvider()

    return VisionProviderPlaceholder()

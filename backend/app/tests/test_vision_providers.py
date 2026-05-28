from __future__ import annotations

import importlib
import importlib.util


def test_mock_vision_provider_returns_expected_tags() -> None:
    assert importlib.util.find_spec("app.services.providers.mock_vision_provider") is not None

    module = importlib.import_module("app.services.providers.mock_vision_provider")
    provider = module.MockVisionProvider()

    result = provider.analyze_clothing_image(
        image_reference="https://example.com/white-tshirt.jpg",
    )

    assert result.category == "top"
    assert result.color == "white"


def test_non_mock_vision_selection_falls_back_when_config_missing(monkeypatch) -> None:
    monkeypatch.setenv("VISION_PROVIDER", "qwen")
    monkeypatch.delenv("VISION_API_KEY", raising=False)
    monkeypatch.delenv("VISION_BASE_URL", raising=False)
    monkeypatch.delenv("VISION_MODEL", raising=False)

    assert importlib.util.find_spec("app.services.providers.provider_factory") is not None

    module = importlib.import_module("app.services.providers.provider_factory")
    provider = module.get_vision_provider()

    assert provider.__class__.__name__ == "MockVisionProvider"


def test_mock_vision_provider_rejects_empty_image_reference() -> None:
    assert importlib.util.find_spec("app.services.providers.mock_vision_provider") is not None

    module = importlib.import_module("app.services.providers.mock_vision_provider")
    provider = module.MockVisionProvider()

    try:
        provider.analyze_clothing_image(image_reference="")
    except ValueError as exc:
        assert str(exc) == "Image URL is required"
    else:
        raise AssertionError("Expected ValueError for empty image_reference")

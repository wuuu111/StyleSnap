from __future__ import annotations

import importlib
import importlib.util

import httpx


def _sample_user_context() -> dict:
    return {
        "occasion": "上课",
        "target_style": "Clean Fit",
        "preference_text": "不想太正式，想显高",
    }


def _sample_weather_context() -> dict:
    return {
        "temperature_level": "warm",
        "rain_protection_needed": True,
        "uv_protection_needed": False,
    }


def _sample_candidate_outfits() -> list[dict]:
    return [
        {
            "id": "look_1",
            "total_score": 88,
            "items": [
                {"role": "top", "name": "White T-shirt", "color": "white"},
                {"role": "pants", "name": "Black Pants", "color": "black"},
            ],
        },
        {
            "id": "look_2",
            "total_score": 84,
            "items": [
                {"role": "top", "name": "Gray Sweatshirt", "color": "gray"},
                {"role": "pants", "name": "Dark Jeans", "color": "navy"},
            ],
        },
    ]


def test_mock_stylist_provider_returns_stable_structure() -> None:
    assert importlib.util.find_spec("app.services.providers.mock_stylist_provider") is not None

    module = importlib.import_module("app.services.providers.mock_stylist_provider")
    provider = module.MockStylistProvider()

    result = provider.enhance_outfit_recommendations(
        user_context=_sample_user_context(),
        weather_context=_sample_weather_context(),
        candidate_outfits=_sample_candidate_outfits(),
    )

    assert result["provider"] == "mock"
    assert result["model"] == "mock"
    assert result["fallback_used"] is False
    assert result["recommended_order"] == ["look_1", "look_2"]
    assert len(result["looks"]) == 2
    assert set(result["looks"][0].keys()) == {
        "id",
        "stylist_summary",
        "weather_reasoning",
        "style_reasoning",
        "color_reasoning",
        "occasion_reasoning",
        "preference_reasoning",
        "improvement_suggestion",
    }


def test_deepseek_provider_selection_falls_back_when_no_api_key(monkeypatch) -> None:
    monkeypatch.setenv("STYLIST_PROVIDER", "deepseek")
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)

    assert importlib.util.find_spec("app.services.providers.provider_factory") is not None

    module = importlib.import_module("app.services.providers.provider_factory")
    provider = module.get_stylist_provider()

    assert provider.__class__.__name__ == "MockStylistProvider"


def test_deepseek_provider_falls_back_on_timeout(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "fake-key")
    monkeypatch.setenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    assert importlib.util.find_spec("app.services.providers.deepseek_stylist_provider") is not None

    module = importlib.import_module("app.services.providers.deepseek_stylist_provider")
    provider = module.DeepSeekStylistProvider()

    def raise_timeout(*_args, **_kwargs):
      raise httpx.TimeoutException("timeout")

    monkeypatch.setattr(provider, "_invoke_deepseek", raise_timeout)

    result = provider.enhance_outfit_recommendations(
        user_context=_sample_user_context(),
        weather_context=_sample_weather_context(),
        candidate_outfits=_sample_candidate_outfits(),
    )

    assert result["provider"] == "mock"
    assert result["fallback_used"] is True


def test_deepseek_provider_falls_back_on_invalid_json(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "fake-key")
    monkeypatch.setenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    assert importlib.util.find_spec("app.services.providers.deepseek_stylist_provider") is not None

    module = importlib.import_module("app.services.providers.deepseek_stylist_provider")
    provider = module.DeepSeekStylistProvider()

    monkeypatch.setattr(provider, "_invoke_deepseek", lambda *_args, **_kwargs: "not-json")

    result = provider.enhance_outfit_recommendations(
        user_context=_sample_user_context(),
        weather_context=_sample_weather_context(),
        candidate_outfits=_sample_candidate_outfits(),
    )

    assert result["provider"] == "mock"
    assert result["fallback_used"] is True

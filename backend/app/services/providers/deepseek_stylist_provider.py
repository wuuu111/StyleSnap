from __future__ import annotations

import json
import os
from typing import Any

import httpx

from app.services.providers.mock_stylist_provider import MockStylistProvider


SYSTEM_PROMPT = """You are StyleSnap's AI stylist layer.
You must only use the provided wardrobe items.
Do not invent new clothing items.
Do not recommend purchases.
Do not make body-shaming, sensitive, or medical claims.
Return valid JSON only.
Keep explanations concise and useful for daily outfit decisions."""

REQUIRED_LOOK_KEYS = {
    "id",
    "stylist_summary",
    "weather_reasoning",
    "style_reasoning",
    "color_reasoning",
    "occasion_reasoning",
    "preference_reasoning",
    "improvement_suggestion",
}


class DeepSeekStylistProvider:
    def __init__(self) -> None:
        self.api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
        self.base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
        self.model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash").strip() or "deepseek-v4-flash"
        self.timeout_seconds = float(os.getenv("DEEPSEEK_TIMEOUT_SECONDS", "30") or "30")
        self._fallback_provider = MockStylistProvider(fallback_used=True)

    def _invoke_deepseek(self, payload: dict[str, Any]) -> str:
        response = httpx.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": json.dumps(payload, ensure_ascii=False),
                    },
                ],
                "temperature": 0.2,
                "response_format": {"type": "json_object"},
            },
            timeout=self.timeout_seconds,
        )
        response.raise_for_status()
        body = response.json()
        return body["choices"][0]["message"]["content"]

    def _validate_result(self, parsed: Any, expected_ids: list[str]) -> dict[str, Any]:
        if not isinstance(parsed, dict):
            raise ValueError("Stylist response must be a JSON object")

        required_top_level = {"provider", "model", "recommended_order", "looks", "fallback_used"}
        if not required_top_level <= set(parsed.keys()):
            raise ValueError("Stylist response missing required top-level fields")

        recommended_order = parsed["recommended_order"]
        looks = parsed["looks"]

        if not isinstance(recommended_order, list) or not all(isinstance(item, str) for item in recommended_order):
            raise ValueError("recommended_order must be a list of strings")
        if not isinstance(looks, list):
            raise ValueError("looks must be a list")

        look_ids = []
        for look in looks:
            if not isinstance(look, dict) or not REQUIRED_LOOK_KEYS <= set(look.keys()):
                raise ValueError("Each look must contain the full reasoning structure")
            look_ids.append(look["id"])

        if set(look_ids) != set(expected_ids):
            raise ValueError("Returned look ids do not match expected candidate ids")

        normalized_order = [item for item in recommended_order if item in expected_ids]
        if len(normalized_order) != len(expected_ids) or len(set(normalized_order)) != len(expected_ids):
            raise ValueError("recommended_order is incomplete or invalid")

        return parsed

    def enhance_outfit_recommendations(
        self,
        *,
        user_context: dict,
        weather_context: dict,
        candidate_outfits: list[dict],
    ) -> dict:
        payload = {
            "user_context": user_context,
            "weather_context": weather_context,
            "candidate_outfits": candidate_outfits,
        }
        expected_ids = [outfit["id"] for outfit in candidate_outfits]

        try:
            raw_content = self._invoke_deepseek(payload)
            parsed = json.loads(raw_content)
            validated = self._validate_result(parsed, expected_ids)
            validated["fallback_used"] = False
            return validated
        except (httpx.HTTPError, ValueError, KeyError, TypeError, json.JSONDecodeError):
            return self._fallback_provider.enhance_outfit_recommendations(
                user_context=user_context,
                weather_context=weather_context,
                candidate_outfits=candidate_outfits,
            )

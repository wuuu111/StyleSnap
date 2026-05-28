from __future__ import annotations


class MockStylistProvider:
    def __init__(
        self,
        *,
        provider_name: str = "mock",
        model_name: str = "mock",
        fallback_used: bool = False,
    ) -> None:
        self.provider_name = provider_name
        self.model_name = model_name
        self.fallback_used = fallback_used

    def enhance_outfit_recommendations(
        self,
        *,
        user_context: dict,
        weather_context: dict,
        candidate_outfits: list[dict],
    ) -> dict:
        looks: list[dict] = []
        for outfit in candidate_outfits:
            items = outfit.get("items", [])
            item_names = "、".join(entry.get("name", "item") for entry in items[:3]) or "现有单品"
            looks.append(
                {
                    "id": outfit["id"],
                    "stylist_summary": (
                        f"这套 Look 保留了规则推荐的平衡度，适合 {user_context.get('occasion', '今日场景')}，"
                        f"并优先使用你现有衣橱中的 {item_names}。"
                    ),
                    "weather_reasoning": (
                        "系统继续以 Weather Skill 的穿搭约束为主，优先考虑温度、降雨和鞋履适配。"
                    ),
                    "style_reasoning": (
                        f"整体搭配围绕 {user_context.get('target_style', '目标风格')} 做选择，避免脱离既有衣橱。"
                    ),
                    "color_reasoning": "色彩组合保持日常可穿性与协调感，适合直接作为今天的实际穿搭。",
                    "occasion_reasoning": (
                        f"单品选择会优先匹配 {user_context.get('occasion', '当前')} 场景，而不是生成脱离上下文的造型。"
                    ),
                    "preference_reasoning": (
                        "如果提供了额外偏好，系统会把它作为解释增强信号，而不是替代规则评分。"
                    ),
                    "improvement_suggestion": "如果想进一步微调，可以优先替换鞋子或外套，而不是更换整套单品。",
                }
            )

        return {
            "provider": self.provider_name,
            "model": self.model_name,
            "recommended_order": [outfit["id"] for outfit in candidate_outfits],
            "looks": looks,
            "fallback_used": self.fallback_used,
        }

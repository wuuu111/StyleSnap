from __future__ import annotations

from app.schemas.clothing import ClothingRead
from app.schemas.outfit import OutfitReasoning, OutfitScoreBreakdown
from app.schemas.weather import WeatherSkillResponse


def _items(outfit: dict[str, ClothingRead]) -> list[ClothingRead]:
    return list(outfit.values())


def build_outfit_reasoning(
    outfit: dict[str, ClothingRead],
    score_breakdown: OutfitScoreBreakdown,
    weather_context: WeatherSkillResponse,
    occasion: str,
    target_style: str,
    preference_text: str,
) -> OutfitReasoning:
    items = _items(outfit)
    top = outfit.get("top")
    pants = outfit.get("pants")
    outerwear = outfit.get("outerwear")
    colors = "、".join(dict.fromkeys(item.color for item in items))

    weather_reasoning = (
        f"今天是 {weather_context.weather.temperature:.0f}°C，"
        f"{weather_context.weather.weather_condition}，系统会根据 "
        f"{weather_context.outfit_context.temperature_level} 体感和天气约束来选衣。"
    )
    if weather_context.outfit_context.rain_protection_needed:
        weather_reasoning = "今天有降雨风险，因此优先考虑更耐雨的鞋子和更实用的外套选择。"
    elif weather_context.outfit_context.layering_needed:
        weather_reasoning = "今天温度偏低，推荐会优先考虑有层次感、适合叠穿的组合。"

    style_reasoning = (
        f"{top.name if top else '这套上衣'}"
        f"{'和' + pants.name if pants else ''} "
        f"整体更接近 {target_style} 的视觉方向。"
    )
    if outerwear:
        style_reasoning = (
            f"{style_reasoning} {outerwear.name} 让整体风格更完整，也更容易贴近目标气质。"
        )

    color_reasoning = (
        f"{colors} 的组合让这套搭配保持相对统一，色彩协调分为 "
        f"{score_breakdown.color_harmony}。"
    )

    occasion_reasoning = (
        f"这套搭配围绕 {occasion} 场景选择了更合适的单品和风格信号，"
        f"因此场景匹配分为 {score_breakdown.occasion_fit}。"
    )

    if preference_text:
        preference_reasoning = (
            f"你提到“{preference_text}”，因此系统在版型、正式度和体感上做了额外权衡。"
        )
    else:
        preference_reasoning = "你没有提供额外偏好，因此系统采用了更中性的默认偏好判断。"

    summary = (
        f"这套搭配适合今天的天气和 {target_style} 风格，"
        f"Weather/Style/Color 等维度整体更均衡。"
    )

    return OutfitReasoning(
        summary=summary,
        weather_reasoning=weather_reasoning,
        style_reasoning=style_reasoning,
        color_reasoning=color_reasoning,
        occasion_reasoning=occasion_reasoning,
        preference_reasoning=preference_reasoning,
    )


def build_outfit_warnings(
    outfit: dict[str, ClothingRead],
    weather_context: WeatherSkillResponse,
) -> list[str]:
    warnings: list[str] = []
    shoes = outfit.get("shoes")
    outerwear = outfit.get("outerwear")

    if weather_context.outfit_context.rain_protection_needed:
        if shoes is None or not shoes.rain_suitable:
            warnings.append("今天降雨概率较高，建议优先选择更防雨的鞋子，并避免麂皮鞋。")
        if outerwear is None and weather_context.outfit_context.outerwear_needed:
            warnings.append("今天有明显天气波动，但这套搭配没有外套，建议准备一件轻便外套。")

    if weather_context.outfit_context.outerwear_needed and outerwear is None:
        warnings.append("今天温度较低，但这套搭配没有外套，建议补充外套。")

    if weather_context.outfit_context.uv_protection_needed and "hat" not in outfit and outerwear is None:
        warnings.append("紫外线较强，可以考虑帽子或轻薄外套。")

    if weather_context.outfit_context.wind_risk == "high" and outerwear is None:
        warnings.append("风较大，建议避免过于轻薄的搭配并补充防风层。")

    return warnings

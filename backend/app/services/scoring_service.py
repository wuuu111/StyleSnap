from __future__ import annotations

from app.schemas.clothing import ClothingRead
from app.schemas.outfit import OutfitScoreBreakdown
from app.schemas.weather import OutfitWeatherContext


ADJACENT_STYLE_MAP = {
    "Clean Fit": {"日系简约"},
    "日系简约": {"Clean Fit"},
    "通勤轻熟": {"Old Money"},
    "Old Money": {"通勤轻熟"},
    "运动休闲": {"City Boy"},
    "City Boy": {"运动休闲", "美式复古"},
    "美式复古": {"City Boy"},
}

HIGH_HARMONY_COMBOS = {
    frozenset({"black", "white"}),
    frozenset({"black", "gray"}),
    frozenset({"white", "blue"}),
    frozenset({"beige", "white"}),
    frozenset({"navy", "white"}),
    frozenset({"gray", "white"}),
}
NEUTRAL_COLORS = {"black", "white", "gray", "navy", "beige", "brown", "denim blue", "blue"}
HIGH_SATURATION_COLORS = {"red", "green", "yellow", "orange", "purple", "pink"}


def _item_text(item: ClothingRead) -> str:
    return " ".join([item.name, item.notes, item.color, *item.style_tags, *item.occasion_tags]).lower()


def _items(outfit: dict[str, ClothingRead]) -> list[ClothingRead]:
    return list(outfit.values())


def _clamp_score(score: float) -> int:
    return max(0, min(100, int(round(score))))


def weather_fit_score(outfit: dict[str, ClothingRead], outfit_context: OutfitWeatherContext) -> int:
    score = 60.0
    items = _items(outfit)
    top = outfit.get("top")
    pants = outfit.get("pants")
    outerwear = outfit.get("outerwear")
    shoes = outfit.get("shoes")

    if outfit_context.temperature_level == "warm":
        if top and top.thickness == "thin":
            score += 10
        if pants and pants.thickness in {"thin", "medium"}:
            score += 5
        if outerwear is None:
            score += 5
        elif outerwear.thickness == "thick":
            score -= 20
        elif outerwear.thickness == "medium":
            score -= 8

    if outfit_context.temperature_level in {"cool", "cold"}:
        if outerwear is not None:
            score += 20
            if outerwear.thickness in {"medium", "thick"}:
                score += 8
        elif outfit_context.outerwear_needed:
            score -= 20

        if any(item.thickness in {"medium", "thick"} for item in items):
            score += 8

    if outfit_context.rain_protection_needed:
        rain_items = [
            item
            for role, item in outfit.items()
            if role in {"shoes", "outerwear", "pants"} and item.rain_suitable
        ]
        score += min(20, len(rain_items) * 10)
        if shoes and not shoes.rain_suitable:
            score -= 12
        if not rain_items:
            score -= 12
        if any(material in _item_text(item) for item in items for material in outfit_context.avoid_materials):
            score -= 15
        if any("canvas" in _item_text(item) for item in items):
            score -= 8

    if outfit_context.uv_protection_needed:
        if "hat" in outfit:
            score += 10
        elif outerwear and outerwear.thickness == "thin":
            score += 6
        else:
            score -= 5

    if outfit_context.wind_risk == "high":
        if outerwear is None:
            score -= 8
        elif outerwear.thickness in {"medium", "thick"}:
            score += 6
        if outerwear and any(word in _item_text(outerwear) for word in ["loose", "lightweight"]):
            score -= 8

    return _clamp_score(score)


def style_match_score(outfit: dict[str, ClothingRead], target_style: str) -> int:
    score = 40.0
    adjacent = ADJACENT_STYLE_MAP.get(target_style, set())

    for item in _items(outfit):
        tags = {tag.strip() for tag in item.style_tags}
        if target_style in tags:
            score += 22
        elif tags & adjacent:
            score += 12

    return _clamp_score(score)


def color_harmony_score(outfit: dict[str, ClothingRead]) -> int:
    colors = [item.color.strip().lower() for item in _items(outfit) if item.color.strip()]
    unique_colors = list(dict.fromkeys(colors))
    color_set = set(unique_colors)

    if len(unique_colors) <= 1:
        return 92
    if color_set <= NEUTRAL_COLORS and len(unique_colors) <= 3:
        if any(pair <= color_set for pair in HIGH_HARMONY_COMBOS):
            return 90
        return 84
    if len(unique_colors) <= 3 and len(color_set & NEUTRAL_COLORS) >= 2:
        return 74
    if len(unique_colors) > 4:
        return 42
    if len(color_set & HIGH_SATURATION_COLORS) >= 2:
        return 45
    return 62


def occasion_fit_score(outfit: dict[str, ClothingRead], occasion: str) -> int:
    score = 50.0
    items = _items(outfit)
    matched_tags = sum(1 for item in items if occasion in item.occasion_tags)
    score += min(30, matched_tags * 12)

    style_text = " ".join(tag for item in items for tag in item.style_tags)
    categories = {item.category for item in items}

    if occasion in {"面试", "通勤", "实习"}:
        if "shoes" in outfit and "皮鞋" in outfit["shoes"].name:
            score += 10
        if "outerwear" in categories:
            score += 8
        if any(tag in style_text for tag in ["通勤", "简约", "Clean Fit"]):
            score += 6
        if "运动休闲" in style_text and occasion in {"面试", "实习"}:
            score -= 8
    elif occasion in {"上课", "休闲"}:
        if any(tag in style_text for tag in ["casual", "Clean Fit", "日系简约", "运动休闲", "休闲"]):
            score += 12
    elif occasion == "约会":
        if color_harmony_score(outfit) >= 80:
            score += 10
        if len({tag for item in items for tag in item.style_tags}) >= 1:
            score += 6
    elif occasion == "运动":
        if "shoes" in outfit:
            score += 10
        if "运动休闲" in style_text:
            score += 12

    return _clamp_score(score)


def user_preference_score(outfit: dict[str, ClothingRead], preference_text: str) -> int:
    text = preference_text.strip()
    if not text:
        return 70

    score = 70.0
    items = _items(outfit)
    style_text = " ".join(tag for item in items for tag in item.style_tags)
    colors = [item.color.strip().lower() for item in items]

    if "不想太正式" in text:
        if any(word in style_text for word in ["面试", "formal"]):
            score -= 10
        if any(word in style_text for word in ["casual", "Clean Fit", "日系简约", "运动休闲"]):
            score += 6

    if "想显高" in text:
        if any(item.category == "pants" and item.color.lower() in {"black", "navy"} for item in items):
            score += 8
        if len(set(colors)) <= 3:
            score += 6
        if color_harmony_score(outfit) >= 80:
            score += 4

    if "想保暖" in text:
        if any(item.category == "outerwear" for item in items):
            score += 10
        if any(item.thickness in {"medium", "thick"} for item in items):
            score += 6

    if "舒服" in text:
        if any(word in style_text for word in ["casual", "运动休闲", "休闲"]):
            score += 8
        if any(item.thickness in {"thin", "medium"} for item in items):
            score += 4

    if "不想太厚" in text and any(item.category == "outerwear" and item.thickness == "thick" for item in items):
        score -= 10

    return _clamp_score(score)


def total_outfit_score(score_breakdown: OutfitScoreBreakdown) -> int:
    return _clamp_score(
        score_breakdown.weather_fit * 0.30
        + score_breakdown.style_match * 0.25
        + score_breakdown.color_harmony * 0.20
        + score_breakdown.occasion_fit * 0.15
        + score_breakdown.user_preference * 0.10
    )

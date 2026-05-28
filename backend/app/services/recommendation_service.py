from __future__ import annotations

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.clothing import ClothingRead
from app.schemas.outfit import (
    AIStylistMetadata,
    OutfitRecommendationRequest,
    OutfitRecommendationResponse,
    OutfitScoreBreakdown,
    RecommendationMeta,
    RecommendedOutfit,
    RecommendedOutfitItem,
)
from app.schemas.weather import WeatherSkillResponse
from app.services.clothing_service import list_clothes
from app.services.outfit_reasoning_service import build_outfit_reasoning, build_outfit_warnings
from app.services.providers.provider_factory import get_stylist_provider
from app.services.scoring_service import (
    color_harmony_score,
    occasion_fit_score,
    style_match_score,
    total_outfit_score,
    user_preference_score,
    weather_fit_score,
)
from app.services.weather_service import get_weather_by_city, get_weather_by_location


SCORING_VERSION = "rule_based_v1"
MAX_TOPS = 8
MAX_PANTS = 8
MAX_SHOES = 5
MAX_OUTERWEAR = 5
MAX_CANDIDATES = 50


def _insufficient_wardrobe(message: str) -> HTTPException:
    return HTTPException(
        status_code=400,
        detail={
            "code": "INSUFFICIENT_WARDROBE",
            "message": message,
            "details": {},
        },
    )


def _resolve_weather_context(payload: OutfitRecommendationRequest) -> WeatherSkillResponse:
    source = payload.weather_source
    if source.type == "city":
        return get_weather_by_city(source.city)
    return get_weather_by_location(source.lat, source.lon)


def _sort_for_role(
    items: list[ClothingRead],
    role: str,
    weather_context: WeatherSkillResponse,
) -> list[ClothingRead]:
    outfit_context = weather_context.outfit_context

    def priority(item: ClothingRead) -> tuple[int, int, int]:
        rain_bonus = 1 if item.rain_suitable else 0
        style_bonus = 1 if any(tag in {"Clean Fit", "通勤", "日系简约", "运动休闲", "美式复古"} for tag in item.style_tags) else 0
        thickness_bonus = 0
        if role == "outerwear":
            if outfit_context.outerwear_needed and item.thickness in {"medium", "thick"}:
                thickness_bonus = 2
            elif outfit_context.temperature_level == "warm" and item.thickness == "thick":
                thickness_bonus = -2
        return (rain_bonus, thickness_bonus, style_bonus)

    return sorted(items, key=priority, reverse=True)


def _candidate_roles(
    grouped_items: dict[str, list[ClothingRead]],
    weather_context: WeatherSkillResponse,
) -> tuple[list[ClothingRead], list[ClothingRead], list[ClothingRead | None], list[ClothingRead | None], list[ClothingRead | None]]:
    tops = grouped_items.get("top", [])[:MAX_TOPS]
    pants = grouped_items.get("pants", [])[:MAX_PANTS]
    shoes = _sort_for_role(grouped_items.get("shoes", []), "shoes", weather_context)[:MAX_SHOES]
    outerwear_sorted = _sort_for_role(grouped_items.get("outerwear", []), "outerwear", weather_context)[:MAX_OUTERWEAR]
    hats = _sort_for_role(grouped_items.get("hat", []), "hat", weather_context)[:1]

    shoe_options: list[ClothingRead | None] = shoes or [None]
    if weather_context.outfit_context.outerwear_needed or weather_context.outfit_context.layering_needed:
        outerwear_options: list[ClothingRead | None] = outerwear_sorted or [None]
    else:
        outerwear_options = [None, *outerwear_sorted[:1]]

    if weather_context.outfit_context.uv_protection_needed and hats:
        hat_options: list[ClothingRead | None] = [None, hats[0]]
    else:
        hat_options = [None]

    return tops, pants, shoe_options, outerwear_options, hat_options


def _build_candidates(items: list[ClothingRead], weather_context: WeatherSkillResponse) -> list[dict[str, ClothingRead]]:
    grouped_items: dict[str, list[ClothingRead]] = {}
    for item in items:
        grouped_items.setdefault(item.category, []).append(item)

    tops, pants, shoe_options, outerwear_options, hat_options = _candidate_roles(
        grouped_items,
        weather_context,
    )

    if not items:
        raise _insufficient_wardrobe("Wardrobe is empty. Add clothing items before requesting recommendations.")
    if not tops:
        raise _insufficient_wardrobe("At least one top is required to generate recommendations.")
    if not pants:
        raise _insufficient_wardrobe("At least one pair of pants is required to generate recommendations.")

    candidates: list[dict[str, ClothingRead]] = []
    for top in tops:
        for pant in pants:
            for shoe in shoe_options:
                for outerwear in outerwear_options:
                    for hat in hat_options:
                        candidate: dict[str, ClothingRead] = {
                            "top": top,
                            "pants": pant,
                        }
                        if shoe is not None:
                            candidate["shoes"] = shoe
                        if outerwear is not None:
                            candidate["outerwear"] = outerwear
                        if hat is not None:
                            candidate["hat"] = hat
                        candidates.append(candidate)
                        if len(candidates) >= MAX_CANDIDATES:
                            return candidates

    return candidates


def _score_candidate(
    candidate: dict[str, ClothingRead],
    payload: OutfitRecommendationRequest,
    weather_context: WeatherSkillResponse,
) -> tuple[OutfitScoreBreakdown, int]:
    breakdown = OutfitScoreBreakdown(
        weather_fit=weather_fit_score(candidate, weather_context.outfit_context),
        style_match=style_match_score(candidate, payload.target_style),
        color_harmony=color_harmony_score(candidate),
        occasion_fit=occasion_fit_score(candidate, payload.occasion),
        user_preference=user_preference_score(candidate, payload.preference_text),
    )
    return breakdown, total_outfit_score(breakdown)


def _to_read_items(db: Session) -> list[ClothingRead]:
    return [ClothingRead.model_validate(item) for item in list_clothes(db)]


def _serialize_weather_context(weather_context: WeatherSkillResponse) -> dict:
    return weather_context.model_dump(mode="json")


def _serialize_user_context(payload: OutfitRecommendationRequest) -> dict:
    return {
        "occasion": payload.occasion,
        "target_style": payload.target_style,
        "preference_text": payload.preference_text,
    }


def _serialize_candidate_outfit(
    outfit: RecommendedOutfit,
    weather_context: WeatherSkillResponse,
) -> dict:
    return {
        "id": outfit.id,
        "total_score": outfit.total_score,
        "score_breakdown": outfit.score_breakdown.model_dump(),
        "warnings": outfit.warnings,
        "items": [
            {
                "role": entry.role,
                "name": entry.item.name,
                "category": entry.item.category,
                "color": entry.item.color,
                "style_tags": entry.item.style_tags,
                "season_tags": entry.item.season_tags,
                "occasion_tags": entry.item.occasion_tags,
                "thickness": entry.item.thickness,
                "rain_suitable": entry.item.rain_suitable,
            }
            for entry in outfit.items
        ],
        "baseline_reasoning": outfit.reasoning.model_dump(),
        "weather_context_summary": {
            "temperature_level": weather_context.outfit_context.temperature_level,
            "rain_protection_needed": weather_context.outfit_context.rain_protection_needed,
            "outerwear_needed": weather_context.outfit_context.outerwear_needed,
        },
    }


def _merge_stylist_output(
    recommendations: list[RecommendedOutfit],
    stylist_result: dict,
) -> list[RecommendedOutfit]:
    by_id = {outfit.id: outfit for outfit in recommendations}
    look_payloads = {
        look["id"]: look
        for look in stylist_result.get("looks", [])
        if isinstance(look, dict) and "id" in look
    }

    for outfit_id, look in look_payloads.items():
        outfit = by_id.get(outfit_id)
        if outfit is None:
            continue

        outfit.reasoning.summary = look.get("stylist_summary") or outfit.reasoning.summary
        outfit.reasoning.weather_reasoning = (
            look.get("weather_reasoning") or outfit.reasoning.weather_reasoning
        )
        outfit.reasoning.style_reasoning = (
            look.get("style_reasoning") or outfit.reasoning.style_reasoning
        )
        outfit.reasoning.color_reasoning = (
            look.get("color_reasoning") or outfit.reasoning.color_reasoning
        )
        outfit.reasoning.occasion_reasoning = (
            look.get("occasion_reasoning") or outfit.reasoning.occasion_reasoning
        )
        outfit.reasoning.preference_reasoning = (
            look.get("preference_reasoning") or outfit.reasoning.preference_reasoning
        )

    recommended_order = stylist_result.get("recommended_order", [])
    expected_ids = [outfit.id for outfit in recommendations]
    if (
        isinstance(recommended_order, list)
        and len(recommended_order) == len(expected_ids)
        and set(recommended_order) == set(expected_ids)
    ):
        return [by_id[outfit_id] for outfit_id in recommended_order]

    return recommendations


def recommend_outfits(db: Session, payload: OutfitRecommendationRequest) -> OutfitRecommendationResponse:
    weather_context = _resolve_weather_context(payload)
    wardrobe_items = _to_read_items(db)
    candidates = _build_candidates(wardrobe_items, weather_context)

    scored_candidates: list[tuple[dict[str, ClothingRead], OutfitScoreBreakdown, int]] = []
    for candidate in candidates:
        breakdown, total_score = _score_candidate(candidate, payload, weather_context)
        scored_candidates.append((candidate, breakdown, total_score))

    scored_candidates.sort(
        key=lambda row: (
            row[2],
            row[1].weather_fit,
            row[1].style_match,
            row[1].occasion_fit,
        ),
        reverse=True,
    )

    recommendations: list[RecommendedOutfit] = []
    for index, (candidate, breakdown, total_score) in enumerate(scored_candidates[:3], start=1):
        recommendations.append(
            RecommendedOutfit(
                id=f"look_{index}",
                items=[
                    RecommendedOutfitItem(role=role, item=item)
                    for role, item in candidate.items()
                ],
                total_score=total_score,
                score_breakdown=breakdown,
                reasoning=build_outfit_reasoning(
                    candidate,
                    breakdown,
                    weather_context,
                    payload.occasion,
                    payload.target_style,
                    payload.preference_text,
                ),
                warnings=build_outfit_warnings(candidate, weather_context),
            )
        )

    stylist_provider = get_stylist_provider()
    stylist_result = stylist_provider.enhance_outfit_recommendations(
        user_context=_serialize_user_context(payload),
        weather_context=_serialize_weather_context(weather_context),
        candidate_outfits=[
            _serialize_candidate_outfit(outfit, weather_context)
            for outfit in recommendations
        ],
    )
    recommendations = _merge_stylist_output(recommendations, stylist_result)

    return OutfitRecommendationResponse(
        weather_context=weather_context,
        recommended_outfits=recommendations,
        meta=RecommendationMeta(
            candidate_count=len(candidates),
            returned_count=len(recommendations),
            scoring_version=SCORING_VERSION,
        ),
        ai_metadata=AIStylistMetadata(
            stylist_provider=stylist_result.get("provider", "mock"),
            stylist_model=stylist_result.get("model", "mock"),
            fallback_used=bool(stylist_result.get("fallback_used", False)),
        ),
    )

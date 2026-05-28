from __future__ import annotations

from datetime import datetime, timezone

from app.schemas.clothing import ClothingRead
from app.schemas.weather import WeatherData
from app.services.scoring_service import (
    color_harmony_score,
    occasion_fit_score,
    style_match_score,
    user_preference_score,
    weather_fit_score,
)
from app.services.weather_service import build_outfit_weather_context


def _item(
    *,
    item_id: int,
    name: str,
    category: str,
    color: str,
    style_tags: list[str],
    season_tags: list[str] | None = None,
    thickness: str = "medium",
    rain_suitable: bool = False,
    occasion_tags: list[str] | None = None,
    min_temperature: int | None = 10,
    max_temperature: int | None = 28,
    notes: str = "",
) -> ClothingRead:
    return ClothingRead(
        id=item_id,
        name=name,
        image_url="https://example.com/item.jpg",
        category=category,
        color=color,
        style_tags=style_tags,
        season_tags=season_tags or ["all-season"],
        thickness=thickness,
        min_temperature=min_temperature,
        max_temperature=max_temperature,
        rain_suitable=rain_suitable,
        occasion_tags=occasion_tags or [],
        notes=notes,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )


def _outfit(**roles: ClothingRead) -> dict[str, ClothingRead]:
    return roles


def test_recommend_outfits_success_with_city_weather(seeded_client) -> None:
    response = seeded_client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "上课",
            "target_style": "Clean Fit",
            "preference_text": "不想太正式，想显高",
            "weather_source": {
                "type": "city",
                "city": "Taipei",
            },
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["weather_context"]["source"] == "city"
    assert body["meta"]["scoring_version"] == "rule_based_v1"
    assert 2 <= len(body["recommended_outfits"]) <= 3
    assert body["meta"]["returned_count"] == len(body["recommended_outfits"])
    assert body["meta"]["candidate_count"] >= body["meta"]["returned_count"]


def test_recommend_outfits_success_with_location_weather(seeded_client) -> None:
    response = seeded_client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "通勤",
            "target_style": "日系简约",
            "preference_text": "想舒服一点，不想太厚",
            "weather_source": {
                "type": "location",
                "lat": 25.033,
                "lon": 121.565,
            },
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["weather_context"]["source"] == "location"
    assert body["weather_context"]["location"]["resolved_city"] == "Taipei"
    assert 2 <= len(body["recommended_outfits"]) <= 3


def test_recommendation_score_breakdown_contains_all_dimensions(seeded_client) -> None:
    response = seeded_client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "上课",
            "target_style": "Clean Fit",
            "preference_text": "",
            "weather_source": {
                "type": "city",
                "city": "Tokyo",
            },
        },
    )

    assert response.status_code == 200
    breakdown = response.json()["recommended_outfits"][0]["score_breakdown"]
    assert set(breakdown.keys()) == {
        "weather_fit",
        "style_match",
        "color_harmony",
        "occasion_fit",
        "user_preference",
    }


def test_empty_wardrobe_returns_stable_error(client) -> None:
    response = client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "上课",
            "target_style": "Clean Fit",
            "preference_text": "",
            "weather_source": {
                "type": "city",
                "city": "Taipei",
            },
        },
    )

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INSUFFICIENT_WARDROBE"


def test_missing_required_categories_returns_stable_error(client) -> None:
    client.post(
        "/api/clothes",
        json={
            "name": "Only Pants",
            "image_url": "https://example.com/pants.jpg",
            "category": "pants",
            "color": "black",
            "style_tags": ["Clean Fit"],
            "season_tags": ["all-season"],
            "thickness": "medium",
            "min_temperature": 10,
            "max_temperature": 28,
            "rain_suitable": True,
            "occasion_tags": ["上课"],
            "notes": "Only pants.",
        },
    )

    response = client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "上课",
            "target_style": "Clean Fit",
            "preference_text": "",
            "weather_source": {
                "type": "city",
                "city": "Taipei",
            },
        },
    )

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INSUFFICIENT_WARDROBE"


def test_rainy_weather_warning_is_returned(client) -> None:
    client.post(
        "/api/clothes",
        json={
            "name": "White Tee",
            "image_url": "https://example.com/tee.jpg",
            "category": "top",
            "color": "white",
            "style_tags": ["Clean Fit"],
            "season_tags": ["summer"],
            "thickness": "thin",
            "min_temperature": 20,
            "max_temperature": 32,
            "rain_suitable": False,
            "occasion_tags": ["上课"],
            "notes": "",
        },
    )
    client.post(
        "/api/clothes",
        json={
            "name": "Black Pants",
            "image_url": "https://example.com/pants.jpg",
            "category": "pants",
            "color": "black",
            "style_tags": ["Clean Fit"],
            "season_tags": ["all-season"],
            "thickness": "medium",
            "min_temperature": 10,
            "max_temperature": 28,
            "rain_suitable": True,
            "occasion_tags": ["上课"],
            "notes": "",
        },
    )
    client.post(
        "/api/clothes",
        json={
            "name": "Canvas Sneakers",
            "image_url": "https://example.com/shoes.jpg",
            "category": "shoes",
            "color": "white",
            "style_tags": ["Clean Fit"],
            "season_tags": ["all-season"],
            "thickness": "medium",
            "min_temperature": 0,
            "max_temperature": 30,
            "rain_suitable": False,
            "occasion_tags": ["上课"],
            "notes": "light canvas upper",
        },
    )

    response = client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "上课",
            "target_style": "Clean Fit",
            "preference_text": "",
            "weather_source": {
                "type": "city",
                "city": "Taipei",
            },
        },
    )

    assert response.status_code == 200
    warnings = response.json()["recommended_outfits"][0]["warnings"]
    assert any("降雨" in warning or "麂皮鞋" in warning or "防雨" in warning for warning in warnings)


def test_cold_weather_warning_is_returned_without_outerwear(client) -> None:
    client.post(
        "/api/clothes",
        json={
            "name": "Gray Sweatshirt",
            "image_url": "https://example.com/top.jpg",
            "category": "top",
            "color": "gray",
            "style_tags": ["日系简约"],
            "season_tags": ["autumn"],
            "thickness": "medium",
            "min_temperature": 10,
            "max_temperature": 22,
            "rain_suitable": True,
            "occasion_tags": ["通勤"],
            "notes": "",
        },
    )
    client.post(
        "/api/clothes",
        json={
            "name": "Navy Trousers",
            "image_url": "https://example.com/pants.jpg",
            "category": "pants",
            "color": "navy",
            "style_tags": ["通勤"],
            "season_tags": ["all-season"],
            "thickness": "medium",
            "min_temperature": 8,
            "max_temperature": 24,
            "rain_suitable": True,
            "occasion_tags": ["通勤"],
            "notes": "",
        },
    )

    response = client.post(
        "/api/outfits/recommend",
        json={
            "occasion": "通勤",
            "target_style": "日系简约",
            "preference_text": "想保暖",
            "weather_source": {
                "type": "city",
                "city": "London",
            },
        },
    )

    assert response.status_code == 200
    warnings = response.json()["recommended_outfits"][0]["warnings"]
    assert any("外套" in warning or "温度较低" in warning for warning in warnings)


def test_weather_fit_score_handles_warm_rainy_and_cold_cases() -> None:
    warm_weather = WeatherData(
        city="Warm City",
        temperature=30,
        feels_like=31,
        min_temp=27,
        max_temp=32,
        weather_condition="humid",
        rain_probability=20,
        wind_speed=2.0,
        humidity=75,
        uv_index=6,
    )
    rainy_weather = WeatherData(
        city="Rain City",
        temperature=24,
        feels_like=25,
        min_temp=21,
        max_temp=26,
        weather_condition="rainy",
        rain_probability=80,
        wind_speed=4.0,
        humidity=88,
        uv_index=4,
    )
    cold_weather = WeatherData(
        city="Cold City",
        temperature=7,
        feels_like=5,
        min_temp=3,
        max_temp=9,
        weather_condition="windy",
        rain_probability=20,
        wind_speed=5.0,
        humidity=50,
        uv_index=2,
    )

    warm_outfit = _outfit(
        top=_item(item_id=1, name="White Tee", category="top", color="white", style_tags=["Clean Fit"], thickness="thin"),
        pants=_item(item_id=2, name="Black Pants", category="pants", color="black", style_tags=["Clean Fit"], thickness="medium"),
    )
    rainy_outfit = _outfit(
        top=_item(item_id=3, name="White Tee", category="top", color="white", style_tags=["Clean Fit"], thickness="thin"),
        pants=_item(item_id=4, name="Black Pants", category="pants", color="black", style_tags=["Clean Fit"], thickness="medium", rain_suitable=True),
        shoes=_item(item_id=5, name="Black Shoes", category="shoes", color="black", style_tags=["通勤"], thickness="medium", rain_suitable=True),
    )
    cold_outfit = _outfit(
        top=_item(item_id=6, name="Gray Knit", category="top", color="gray", style_tags=["日系简约"], thickness="medium"),
        pants=_item(item_id=7, name="Navy Pants", category="pants", color="navy", style_tags=["通勤"], thickness="medium"),
        outerwear=_item(item_id=8, name="Black Coat", category="outerwear", color="black", style_tags=["通勤"], thickness="thick", rain_suitable=True),
    )

    assert weather_fit_score(warm_outfit, build_outfit_weather_context(warm_weather)) >= 75
    assert weather_fit_score(rainy_outfit, build_outfit_weather_context(rainy_weather)) >= 75
    assert weather_fit_score(cold_outfit, build_outfit_weather_context(cold_weather)) >= 75


def test_style_match_score_handles_direct_and_adjacent_styles() -> None:
    direct_outfit = _outfit(
        top=_item(item_id=1, name="White Tee", category="top", color="white", style_tags=["Clean Fit"]),
        pants=_item(item_id=2, name="Black Pants", category="pants", color="black", style_tags=["Clean Fit"]),
    )
    adjacent_outfit = _outfit(
        top=_item(item_id=3, name="Gray Sweatshirt", category="top", color="gray", style_tags=["日系简约"]),
        pants=_item(item_id=4, name="Black Pants", category="pants", color="black", style_tags=["日系简约"]),
    )

    assert style_match_score(direct_outfit, "Clean Fit") > style_match_score(adjacent_outfit, "Clean Fit")
    assert style_match_score(adjacent_outfit, "Clean Fit") >= 60


def test_color_harmony_score_rewards_neutral_palette() -> None:
    harmonious = _outfit(
        top=_item(item_id=1, name="White Tee", category="top", color="white", style_tags=["Clean Fit"]),
        pants=_item(item_id=2, name="Black Pants", category="pants", color="black", style_tags=["Clean Fit"]),
        shoes=_item(item_id=3, name="Gray Shoes", category="shoes", color="gray", style_tags=["Clean Fit"]),
    )
    clashing = _outfit(
        top=_item(item_id=4, name="Red Tee", category="top", color="red", style_tags=["casual"]),
        pants=_item(item_id=5, name="Green Pants", category="pants", color="green", style_tags=["casual"]),
        shoes=_item(item_id=6, name="Yellow Shoes", category="shoes", color="yellow", style_tags=["casual"]),
    )

    assert color_harmony_score(harmonious) > color_harmony_score(clashing)


def test_occasion_fit_score_prefers_matching_tags() -> None:
    commute_outfit = _outfit(
        top=_item(item_id=1, name="Shirt", category="top", color="white", style_tags=["通勤"], occasion_tags=["通勤"]),
        pants=_item(item_id=2, name="Trousers", category="pants", color="black", style_tags=["通勤"], occasion_tags=["通勤"]),
        shoes=_item(item_id=3, name="Leather Shoes", category="shoes", color="black", style_tags=["面试"], occasion_tags=["通勤", "面试"]),
    )
    relaxed_outfit = _outfit(
        top=_item(item_id=4, name="Hoodie", category="top", color="gray", style_tags=["休闲"], occasion_tags=["休闲"]),
        pants=_item(item_id=5, name="Joggers", category="pants", color="gray", style_tags=["运动休闲"], occasion_tags=["休闲"]),
    )

    assert occasion_fit_score(commute_outfit, "通勤") > occasion_fit_score(relaxed_outfit, "通勤")


def test_user_preference_score_handles_keywords_and_empty_text() -> None:
    outfit = _outfit(
        top=_item(item_id=1, name="White Tee", category="top", color="white", style_tags=["Clean Fit", "casual"]),
        pants=_item(item_id=2, name="Black Pants", category="pants", color="black", style_tags=["Clean Fit"], occasion_tags=["上课"]),
        outerwear=_item(item_id=3, name="Black Coat", category="outerwear", color="black", style_tags=["通勤"], thickness="thick"),
    )

    assert user_preference_score(outfit, "") == 70
    assert user_preference_score(outfit, "不想太正式") >= 60
    assert user_preference_score(outfit, "想显高") >= 70
    assert user_preference_score(outfit, "想保暖") >= 75
    assert user_preference_score(outfit, "舒服一点") >= 60

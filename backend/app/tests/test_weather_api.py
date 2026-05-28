from __future__ import annotations


def test_get_weather_by_city_returns_skill_response(client) -> None:
    response = client.get("/api/weather", params={"city": "Tokyo"})

    assert response.status_code == 200
    body = response.json()
    assert body["source"] == "city"
    assert body["location"] == {"city": "Tokyo"}
    assert body["weather"]["city"] == "Tokyo"
    assert body["weather"]["weather_condition"] == "cloudy"
    assert body["outfit_context"]["temperature_level"] == "mild"
    assert body["outfit_context"]["rain_protection_needed"] is False


def test_get_weather_requires_city(client) -> None:
    response = client.get("/api/weather", params={"city": "   "})

    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "INVALID_INPUT",
            "message": "City is required",
            "details": {},
        }
    }


def test_get_weather_normalizes_city_case_and_spaces(client) -> None:
    response = client.get("/api/weather", params={"city": "  toKyO  "})

    assert response.status_code == 200
    body = response.json()
    assert body["weather"]["city"] == "Tokyo"
    assert body["location"]["city"] == "Tokyo"


def test_get_weather_returns_fallback_for_unknown_city(client) -> None:
    response = client.get("/api/weather", params={"city": "Osaka"})

    assert response.status_code == 200
    body = response.json()
    assert body["source"] == "city"
    assert body["location"] == {"city": "Osaka"}
    assert body["weather"]["city"] == "Osaka"
    assert body["weather"]["temperature"] == 23
    assert "outfit_context" in body


def test_get_weather_current_by_location_returns_resolved_city(client) -> None:
    response = client.get("/api/weather/current", params={"lat": 25.033, "lon": 121.565})

    assert response.status_code == 200
    body = response.json()
    assert body["source"] == "location"
    assert body["location"] == {
        "lat": 25.033,
        "lon": 121.565,
        "resolved_city": "Taipei",
    }
    assert body["weather"]["city"] == "Taipei"
    assert body["outfit_context"]["temperature_level"] == "warm"
    assert body["outfit_context"]["rain_protection_needed"] is True


def test_get_weather_current_rejects_out_of_range_coordinates(client) -> None:
    response = client.get("/api/weather/current", params={"lat": 123.0, "lon": 121.565})

    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "INVALID_INPUT",
            "message": "Invalid coordinates",
            "details": {},
        }
    }


def test_weather_skill_response_schema_is_stable(client) -> None:
    response = client.get("/api/weather", params={"city": "Singapore"})

    assert response.status_code == 200
    assert set(response.json().keys()) == {
        "source",
        "location",
        "weather",
        "outfit_context",
    }
    assert set(response.json()["outfit_context"].keys()) == {
        "temperature_level",
        "rain_risk",
        "wind_risk",
        "uv_risk",
        "layering_needed",
        "outerwear_needed",
        "rain_protection_needed",
        "uv_protection_needed",
        "recommended_materials",
        "avoid_materials",
        "shoe_constraints",
        "styling_hints",
    }


def test_high_rain_probability_sets_rain_protection_needed(client) -> None:
    response = client.get("/api/weather", params={"city": "Taipei"})

    assert response.status_code == 200
    assert response.json()["outfit_context"]["rain_protection_needed"] is True


def test_high_uv_index_sets_uv_protection_needed(client) -> None:
    response = client.get("/api/weather", params={"city": "Singapore"})

    assert response.status_code == 200
    assert response.json()["outfit_context"]["uv_protection_needed"] is True


def test_cold_temperature_sets_layering_needed(client) -> None:
    response = client.get("/api/weather", params={"city": "London"})

    assert response.status_code == 200
    body = response.json()
    assert body["weather"]["temperature"] == 17
    assert body["outfit_context"]["layering_needed"] is True
    assert body["outfit_context"]["outerwear_needed"] is True


def test_health_check_regression_with_weather_skill(client) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_wardrobe_regression_with_weather_skill(client) -> None:
    create_response = client.post(
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
            "notes": "Regression check.",
        },
    )
    list_response = client.get("/api/clothes")

    assert create_response.status_code == 201
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

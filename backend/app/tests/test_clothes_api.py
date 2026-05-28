from __future__ import annotations


def _create_payload(**overrides):
    payload = {
        "name": "White T-shirt",
        "image_url": "https://example.com/white-shirt.jpg",
        "category": "top",
        "color": "white",
        "style_tags": ["Clean Fit", "casual"],
        "season_tags": ["summer"],
        "thickness": "thin",
        "min_temperature": 20,
        "max_temperature": 32,
        "rain_suitable": False,
        "occasion_tags": ["上课", "休闲"],
        "notes": "Crisp everyday top.",
    }
    payload.update(overrides)
    return payload


def test_create_clothing_item(client) -> None:
    response = client.post("/api/clothes", json=_create_payload())

    assert response.status_code == 201
    body = response.json()
    assert body["id"] > 0
    assert body["name"] == "White T-shirt"
    assert body["category"] == "top"


def test_list_clothing_items(client) -> None:
    client.post("/api/clothes", json=_create_payload())
    client.post("/api/clothes", json=_create_payload(name="Dark Jeans", category="pants", color="navy"))

    response = client.get("/api/clothes")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_clothing_item_by_id(client) -> None:
    created = client.post("/api/clothes", json=_create_payload()).json()

    response = client.get(f"/api/clothes/{created['id']}")

    assert response.status_code == 200
    assert response.json()["name"] == "White T-shirt"


def test_update_clothing_item(client) -> None:
    created = client.post("/api/clothes", json=_create_payload()).json()

    response = client.put(
        f"/api/clothes/{created['id']}",
        json=_create_payload(name="Updated White Tee", notes="Updated note."),
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated White Tee"
    assert response.json()["notes"] == "Updated note."


def test_delete_clothing_item(client) -> None:
    created = client.post("/api/clothes", json=_create_payload()).json()

    delete_response = client.delete(f"/api/clothes/{created['id']}")
    list_response = client.get("/api/clothes")

    assert delete_response.status_code == 204
    assert list_response.json() == []


def test_list_clothing_items_with_filters(client) -> None:
    client.post("/api/clothes", json=_create_payload())
    client.post(
        "/api/clothes",
        json=_create_payload(
            name="Black Straight Pants",
            image_url="https://example.com/black-pants.jpg",
            category="pants",
            color="black",
            season_tags=["all-season"],
            thickness="medium",
        ),
    )

    response = client.get("/api/clothes", params={"category": "pants", "color": "black", "season": "all-season"})

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Black Straight Pants"


def test_invalid_category_returns_stable_error(client) -> None:
    response = client.post("/api/clothes", json=_create_payload(category="dress"))

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_INPUT"


def test_invalid_thickness_returns_stable_error(client) -> None:
    response = client.post("/api/clothes", json=_create_payload(thickness="heavy"))

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_INPUT"


def test_invalid_filter_category_returns_stable_error(client) -> None:
    response = client.get("/api/clothes", params={"category": "dress"})

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_INPUT"


def test_update_missing_item_returns_not_found(client) -> None:
    response = client.put("/api/clothes/999", json=_create_payload())

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"


def test_delete_missing_item_returns_not_found(client) -> None:
    response = client.delete("/api/clothes/999")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"


def test_analyze_clothing_image_mock(client) -> None:
    response = client.post(
        "/api/clothes/analyze",
        json={"image_url": "https://example.com/white-tshirt.jpg"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["category"] == "top"
    assert body["color"] == "white"
    assert body["thickness"] == "thin"


def test_analyze_clothing_image_unknown_returns_fallback(client) -> None:
    response = client.post(
        "/api/clothes/analyze",
        json={"image_url": "https://example.com/mystery-item.png"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Unknown Item"
    assert response.json()["category"] == "accessory"


def test_analyze_clothing_image_requires_url(client) -> None:
    response = client.post("/api/clothes/analyze", json={"image_url": ""})

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_INPUT"


def test_analyze_clothing_image_falls_back_to_mock_when_real_vision_unconfigured(
    client,
    monkeypatch,
) -> None:
    monkeypatch.setenv("VISION_PROVIDER", "qwen")
    monkeypatch.delenv("VISION_API_KEY", raising=False)
    monkeypatch.delenv("VISION_BASE_URL", raising=False)
    monkeypatch.delenv("VISION_MODEL", raising=False)

    response = client.post(
        "/api/clothes/analyze",
        json={"image_url": "https://example.com/white-tshirt.jpg"},
    )

    assert response.status_code == 200
    assert response.json()["category"] == "top"


def test_demo_seed_data_is_inserted_once(seeded_client) -> None:
    first_response = seeded_client.get("/api/clothes")
    second_response = seeded_client.get("/api/clothes")

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert len(first_response.json()) == 8
    assert len(second_response.json()) == 8

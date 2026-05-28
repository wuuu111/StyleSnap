from __future__ import annotations

import sys
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient


def _reset_backend_modules() -> None:
    for module_name in [
        "app.main",
        "app.routers.clothes",
        "app.routers.health",
        "app.routers.outfits",
        "app.routers.weather",
        "app.services.clothing_service",
        "app.services.ai_vision_service",
        "app.services.outfit_reasoning_service",
        "app.services.providers",
        "app.services.providers.__init__",
        "app.services.providers.provider_factory",
        "app.services.providers.stylist_provider",
        "app.services.providers.mock_stylist_provider",
        "app.services.providers.deepseek_stylist_provider",
        "app.services.providers.vision_provider",
        "app.services.providers.mock_vision_provider",
        "app.services.providers.vision_provider_placeholder",
        "app.services.recommendation_service",
        "app.services.scoring_service",
        "app.services.weather_service",
        "app.schemas.clothing",
        "app.schemas.outfit",
        "app.schemas.weather",
        "app.models.clothing",
        "app.database",
    ]:
        if module_name in sys.modules:
            del sys.modules[module_name]


@pytest.fixture
def client(tmp_path: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    db_path = tmp_path / "wardrobe-core-test.db"
    monkeypatch.setenv("STYLESNAP_DATABASE_URL", f"sqlite:///{db_path}")
    monkeypatch.setenv("STYLESNAP_ENABLE_DEMO_SEED", "false")
    _reset_backend_modules()

    from app.main import create_app

    app = create_app()

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def seeded_client(tmp_path: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    db_path = tmp_path / "wardrobe-core-seeded.db"
    monkeypatch.setenv("STYLESNAP_DATABASE_URL", f"sqlite:///{db_path}")
    monkeypatch.setenv("STYLESNAP_ENABLE_DEMO_SEED", "true")
    _reset_backend_modules()

    from app.main import create_app

    app = create_app()

    with TestClient(app) as test_client:
        yield test_client

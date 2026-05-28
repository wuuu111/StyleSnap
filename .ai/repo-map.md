# StyleSnap Repository Map

## Current State
- Phase 5 frontend recommendation polish is in place.
- Backend exposes `GET /health`, clothes CRUD, mock analyze, weather skill, and outfit recommendation APIs.
- Frontend exposes wardrobe flows plus a location-first recommendation page with polished result cards, score breakdown, reasoning, warnings, and regenerate flow.
- Final portfolio packaging remains for the next phase.

## Intended Monorepo Structure
- `frontend/`
  - `package.json`: frontend scripts and dependencies.
  - `src/main.tsx`: React bootstrap with router.
  - `src/App.tsx`: route table.
  - `src/pages/`: route-level screens such as landing, wardrobe, add item, recommendation input, and result pages.
  - `src/components/`: reusable UI blocks including cards, forms, filters, and page shell.
  - `src/services/`: frontend API clients and request helpers.
  - `src/stores/`: Zustand or context-based client state for wardrobe and recommendation flows.
  - `src/types/`: shared frontend domain and API response types.
  - `src/utils/`: pure UI helpers, formatting, and form mapping logic.
- `backend/`
  - `requirements.txt`: backend Python dependencies.
  - `pytest.ini`: pytest discovery config.
  - `app/main.py`: FastAPI entrypoint and app wiring.
  - `app/database.py`: database engine, session, and metadata setup.
  - `app/models/`: SQLAlchemy models.
  - `app/schemas/`: Pydantic request and response schemas.
  - `app/routers/`: API route modules.
  - `app/services/`: business logic and provider adapters.
  - `app/tests/`: backend test suite.
- `.ai/`
  - `constitution.md`: durable engineering rules.
  - `repo-map.md`: repository topology and edit boundaries.
- `specs/`
  - `changes/`: active feature specs.
  - `current/`: current accepted state snapshots after phase archive.
  - `archive/`: completed change specs and lessons learned.

## Planned Backend Service Boundaries
- `clothing_service.py`: clothing CRUD orchestration and validation.
- `weather_service.py`: mock and future real weather provider abstraction.
  - Current responsibility: Weather Skill, including mock coordinate resolution and outfit-context building.
- `recommendation_service.py`: outfit generation, scoring, warnings, and reasoning composition.
- `scoring_service.py`: pure weighted scoring functions for recommendation candidates.
- `outfit_reasoning_service.py`: deterministic explanation and warning builders.
- `ai_vision_service.py`: mock clothing analysis behind a replaceable interface.
- `llm_service.py`: template explanation generation now, future LLM integration point later.

## Planned API Surface
- Current:
  - `GET /health`
  - `POST /api/clothes`
  - `GET /api/clothes`
  - `GET /api/clothes/{id}`
  - `PUT /api/clothes/{id}`
  - `DELETE /api/clothes/{id}`
  - `POST /api/clothes/analyze`
- Clothes:
  - `POST /api/clothes`
  - `GET /api/clothes`
  - `GET /api/clothes/{id}`
  - `PUT /api/clothes/{id}`
  - `DELETE /api/clothes/{id}`
  - `POST /api/clothes/analyze`
- Weather:
  - `GET /api/weather`
  - `GET /api/weather/current`
- Outfits:
  - `POST /api/outfits/recommend`
- Health:
  - `GET /health`

## Planned Data Models
- `ClothingItem`
  - Stores image path or URL, clothing tags, temperature range, rain suitability, and notes.
- `OutfitRecommendation`
  - Stores recommendation request context, weather snapshot, selected item ids, scoring breakdown, and reasoning text.

## Actual Phase 2 Files
- Backend:
  - `backend/app/models/clothing.py`
  - `backend/app/schemas/clothing.py`
  - `backend/app/routers/clothes.py`
  - `backend/app/services/clothing_service.py`
  - `backend/app/services/ai_vision_service.py`
  - `backend/app/tests/test_clothes_api.py`
- Frontend:
  - `frontend/src/pages/WardrobePage.tsx`
  - `frontend/src/pages/AddItemPage.tsx`
  - `frontend/src/pages/EditItemPage.tsx`
  - `frontend/src/components/ClothingItemCard.tsx`
  - `frontend/src/components/ClothingItemForm.tsx`
  - `frontend/src/components/FilterBar.tsx`
  - `frontend/src/services/clothesApi.ts`
  - `frontend/src/types/clothing.ts`
  - `frontend/src/utils/clothingForm.ts`

## Actual Phase 3 Files
- Backend:
  - `backend/app/schemas/weather.py`
  - `backend/app/routers/weather.py`
  - `backend/app/services/weather_service.py`
  - `backend/app/tests/test_weather_api.py`
- Frontend:
  - `frontend/src/services/weatherApi.ts`
  - `frontend/src/types/weather.ts`
  - `frontend/src/components/WeatherCard.tsx`
  - `frontend/src/pages/RecommendationPage.tsx`

## Actual Phase 4 Files
- Backend:
  - `backend/app/schemas/outfit.py`
  - `backend/app/routers/outfits.py`
  - `backend/app/services/scoring_service.py`
  - `backend/app/services/outfit_reasoning_service.py`
  - `backend/app/services/recommendation_service.py`
  - `backend/app/tests/test_recommendation.py`
- Frontend:
  - `frontend/src/types/outfit.ts`
  - `frontend/src/services/recommendationApi.ts`
  - `frontend/src/pages/RecommendationPage.tsx`

## Actual Phase 5 Files
- Frontend:
  - `frontend/src/components/RecommendationStateCard.tsx`
  - `frontend/src/components/WeatherContextPanel.tsx`
  - `frontend/src/components/RecommendationForm.tsx`
  - `frontend/src/components/OutfitResultCard.tsx`
  - `frontend/src/components/OutfitItemGrid.tsx`
  - `frontend/src/components/ScoreBreakdown.tsx`
  - `frontend/src/components/ReasoningPanel.tsx`
  - `frontend/src/components/WarningList.tsx`
  - `frontend/src/components/WeatherCard.tsx`
  - `frontend/src/pages/RecommendationPage.tsx`

## Testing Layout
- `backend/app/tests/`
  - Health API tests.
  - Clothes CRUD tests.
  - Weather API tests.
  - Recommendation scoring and outfit API tests.
- `frontend/`
  - Manual acceptance checklist is mandatory.
  - Optional Vitest coverage for UI rendering and API mocks if added in later phases.

## Safe-To-Edit Areas
- `.ai/**`
- `specs/**`
- `frontend/**` once Phase 1 starts
- `backend/**` once Phase 1 starts
- `README.md`, `.env.example`, `docker-compose.yml` once relevant phase begins

## Caution Areas
- `backend/app/database.py`
  - Schema and seed logic changes can affect multiple phases.
- `backend/app/schemas/**`
  - Response contract stability matters for frontend integration.
- `backend/app/services/recommendation_service.py`
  - Scoring and reasoning changes directly affect demo behavior and tests.
- `backend/app/services/weather_service.py`
  - Response shape and outfit-context rules feed the future recommendation engine.
- `frontend/src/services/**`
  - API contract drift can break multiple screens.
- `specs/current/**` and `specs/archive/**`
  - Only update during formal archive steps after review.

## Phase 0 Editing Boundary
- Allowed:
  - Create or update `.ai/*`
  - Create `specs/changes/init-project/*`
- Not allowed:
  - Scaffold `frontend/` or `backend/`
  - Add runtime dependencies
  - Add application code

## Phase 1 Actual Files
- `frontend/src/pages/LandingPage.tsx`
- `frontend/src/pages/WardrobePage.tsx`
- `frontend/src/pages/RecommendationPage.tsx`
- `frontend/src/components/AppShell.tsx`
- `frontend/src/components/PageHeader.tsx`
- `frontend/src/services/apiClient.ts`
- `backend/app/routers/health.py`
- `backend/app/schemas/errors.py`
- `backend/app/tests/test_health.py`

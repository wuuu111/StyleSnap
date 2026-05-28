# Recommendation Engine Architecture

## Backend Components

### Recommendation Schemas
- `backend/app/schemas/outfit.py`
- Request schema:
  - `occasion`
  - `target_style`
  - `preference_text`
  - discriminated `weather_source`
- Response schema:
  - `weather_context`
  - `recommended_outfits`
  - `meta`
- Nested schemas:
  - outfit item role wrapper
  - score breakdown
  - reasoning payload
  - outfit recommendation payload

### Recommendation Router
- `backend/app/routers/outfits.py`
- Exposes `POST /api/outfits/recommend`
- Keeps router thin:
  - validate request
  - get database session
  - delegate to recommendation service

### Recommendation Service
- `backend/app/services/recommendation_service.py`
- Responsibilities:
  - resolve weather context from weather source
  - read wardrobe items from existing clothing service or direct query helper
  - generate bounded outfit candidates
  - score candidates
  - rank and trim to top 3
  - attach reasoning and warnings
  - emit response metadata

### Scoring Service
- `backend/app/services/scoring_service.py`
- Pure functions:
  - `weather_fit_score(outfit, outfit_context)`
  - `style_match_score(outfit, target_style)`
  - `color_harmony_score(outfit)`
  - `occasion_fit_score(outfit, occasion)`
  - `user_preference_score(outfit, preference_text)`
  - `total_outfit_score(score_breakdown)`
- Keeps scoring independently testable from routing and DB access.

### Reasoning Service
- `backend/app/services/outfit_reasoning_service.py`
- Pure template builders:
  - `build_outfit_reasoning(...)`
  - `build_outfit_warnings(...)`
- Uses score inputs plus item metadata and weather context.

## Data Flow
1. Frontend sends recommendation request with occasion, style, preference, and weather source.
2. Router passes payload to recommendation service.
3. Recommendation service resolves `WeatherSkillResponse` using:
   - `get_weather_by_city()`
   - `get_weather_by_location()`
4. Recommendation service loads wardrobe items.
5. Candidate builder produces bounded outfit combinations.
6. Scoring service computes breakdown and total score.
7. Reasoning service generates explanation strings and warnings.
8. Recommendation service sorts candidates and returns top 3.

## Candidate Representation
- Internal outfit object can remain service-local and include:
  - selected item by role
  - flat item list for scoring
  - optional roles:
    - `shoes`
    - `outerwear`
    - `hat`
    - `bag`
    - `accessory`

## Wardrobe Access Strategy
- Reuse current persisted `ClothingItem` rows.
- Prefer a small helper inside recommendation service or a focused read helper from clothing service.
- Do not duplicate demo data in recommendation code.

## Weather Dependency Strategy
- Recommendation engine must consume `WeatherSkillResponse`.
- It should rely primarily on `outfit_context` for weather constraints instead of re-deriving from raw weather fields.
- Raw weather remains available for reasoning copy and warning details.

## Frontend Scope In Phase 4
- Keep recommendation UI minimal on the existing recommendation page.
- Add:
  - occasion select
  - target style select
  - preference textarea
  - generate button
  - basic result preview card or JSON-style output
- Full portfolio-polished result layout waits for Phase 5.

## Extension Points
- Swap template reasoning with `llm_service.py` later.
- Swap rules-only scoring with learned re-ranking later.
- Expand candidate builder with accessories and style inspiration later without changing the API contract.

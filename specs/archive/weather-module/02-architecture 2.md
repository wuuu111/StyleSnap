# Weather Module Architecture

## Backend Components

### Weather Schema
- Dedicated Pydantic response schema for weather data
- Fields typed for recommendation consumption
- Validation ranges implied by mock provider contract

### Weather Router
- New `weather.py` router mounted under `/api/weather`
- Accepts `city` query parameter
- Returns stable error format on invalid input

### Weather Service
- `normalize_city(city: str) -> str`
- `get_weather(city: str) -> WeatherResponse`
- `get_mock_weather(city: str) -> WeatherResponse`

### Mock Provider
- Local in-process mock dataset for at least 10 cities
- Case-insensitive lookup
- Deterministic fallback weather

### Future Provider Adapter
- Introduce provider protocol or base interface now
- `MockWeatherProvider` is the only implementation in Phase 3
- Future real providers can replace service internals without changing API contracts

## Frontend Components

### Weather API Client
- Add `getWeather(city: string)` under `frontend/src/services/weatherApi.ts`
- Reuse shared `apiFetch`

### Weather Card
- Dedicated component showing weather metrics and rule-based reminder text
- Keeps weather visible but secondary to later outfit results

### Recommendation Page Integration
- Replace the static city placeholder with a working city input and weather fetch action
- Keep outfit generation area as placeholder
- Use local page state; no global store required

## Data Flow
1. User enters city on recommendation page
2. Frontend calls `getWeather(city)`
3. Backend normalizes city and resolves mock provider data
4. API returns stable weather payload
5. Frontend renders weather card and reminder text

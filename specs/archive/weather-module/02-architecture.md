# Weather Skill Architecture

## Backend Components

### Weather Schema
- Dedicated Pydantic schema for raw weather data
- Dedicated schema for resolved location payload
- Dedicated schema for outfit-aware weather context
- Dedicated schema for the complete weather skill response
- Validation ranges implied by mock provider contract

### Weather Router
- New `weather.py` router mounted under `/api/weather`
- Exposes:
  - `GET /api/weather?city=...`
  - `GET /api/weather/current?lat=...&lon=...`
- Returns stable error format on invalid input

### Weather Service
- `normalize_city(city: str) -> str`
- `resolve_city_from_coordinates(lat: float, lon: float) -> str`
- `get_weather_by_city(city: str)`
- `get_weather_by_location(lat: float, lon: float)`
- `build_outfit_weather_context(weather)`
- `get_mock_weather(city: str) -> WeatherResponse`

### Mock Provider
- Local in-process mock dataset for at least 10 cities
- Case-insensitive lookup
- Deterministic fallback weather
- Deterministic coordinate-to-city resolver

### Future Provider Adapter
- Introduce provider protocol or base interface now
- `MockWeatherProvider` is the only implementation in Phase 3
- Future real providers can replace service internals without changing API contracts

## Frontend Components

### Weather API Client
- Add:
  - `getWeatherByLocation(lat, lon)`
  - `getWeatherByCity(city)`
  - optional geolocation helper kept separate from fetch logic
- Reuse shared `apiFetch`

### Weather Card
- Dedicated component showing a concise weather summary and outfit impact hints
- Emphasizes weather influence on styling, materials, and shoe constraints
- Keeps weather visible but secondary to later outfit results

### Recommendation Page Integration
- On page load, explain location-based weather optimization
- Provide `Use my location`
- Attempt browser geolocation first
- If denied or unavailable, reveal city input fallback
- Keep outfit generation area as placeholder
- Use local page state; no global store required

## Data Flow
1. User clicks `Use my location`
2. Browser geolocation returns `lat` and `lon`
3. Frontend calls `GET /api/weather/current`
4. Backend resolves a mock city from coordinates
5. Backend resolves mock weather and builds outfit context
6. Frontend renders compact weather context card
7. If location fails, frontend reveals city input fallback and calls `GET /api/weather?city=...`

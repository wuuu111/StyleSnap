# Weather Skill Requirements

## Feature Goal
Return stable weather context for outfit recommendation without turning StyleSnap into a weather app.

## User Stories
- As a user, I can let StyleSnap use my current location to prepare weather-aware outfit context.
- As a user, if location is unavailable, I can still continue by entering a city manually.
- As a user, I can see a compact weather context card before later outfit recommendations exist.
- As a developer, I can run this phase without any real weather API key.
- As a future recommendation module, I can rely on both stable weather data and stable outfit context.

## Functional Requirements
1. `GET /api/weather/current?lat=...&lon=...` must return:
   - `source`
   - `location`
   - `weather`
   - `outfit_context`
2. `GET /api/weather?city=Taipei` must remain available as fallback and return the same top-level structure.
3. The frontend must prefer browser Geolocation API first.
4. If geolocation fails or is denied, the frontend must reveal manual city input fallback.
5. City matching must trim whitespace and ignore case.
6. Unknown cities must return fallback mock weather while preserving the user-provided city in the location and weather result.
7. Mock location resolution must map coordinates to mock cities without any real geocoding provider.
8. Weather service must remain replaceable through an explicit provider seam.
9. Weather skill must expose outfit-aware context, not only raw weather fields.
10. Error responses must continue to use the project-wide error envelope.

## Response Contract
Top-level required fields:
- `source`
- `location`
- `weather`
- `outfit_context`

`weather` required fields:
- `city`
- `temperature`
- `feels_like`
- `min_temp`
- `max_temp`
- `weather_condition`
- `rain_probability`
- `wind_speed`
- `humidity`
- `uv_index`

`outfit_context` required fields:
- `temperature_level`
- `rain_risk`
- `wind_risk`
- `uv_risk`
- `layering_needed`
- `outerwear_needed`
- `rain_protection_needed`
- `uv_protection_needed`
- `recommended_materials`
- `avoid_materials`
- `shoe_constraints`
- `styling_hints`

## Edge Cases
- Empty `city` returns `INVALID_INPUT` with message `City is required`
- Invalid `lat` or `lon` returns `INVALID_INPUT`
- Unknown city returns fallback mock data and outfit context
- City value with case differences must still resolve to known mock data
- City value with leading or trailing spaces must still resolve
- Mock location resolver fallback must remain deterministic
- Geolocation denial must surface manual city fallback in the frontend
- Error response format must remain stable

## Non-Goals
- Real weather API integration
- Real geolocation-to-city provider
- Multi-day forecast
- Hourly forecast
- Outfit recommendation
- AI-generated reasoning

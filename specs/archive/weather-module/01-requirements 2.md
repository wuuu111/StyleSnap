# Weather Module Requirements

## Feature Goal
Return stable weather data for a user-provided city and display it on the recommendation page without turning the product into a weather app.

## User Stories
- As a user, I can enter a city and get weather data back.
- As a user, I can see a weather card before later outfit recommendations exist.
- As a developer, I can run this phase without any real weather API key.
- As a future recommendation module, I can rely on a stable weather response shape.

## Functional Requirements
1. `GET /api/weather?city=Tokyo` must return a stable weather payload.
2. `city` is required.
3. City matching must trim whitespace and ignore case.
4. Unknown cities must return fallback mock weather while preserving the user-provided city string in the response.
5. Weather service must remain replaceable through an explicit provider seam.
6. Frontend must expose `getWeather(city)` in a centralized API client.
7. Recommendation page must let the user enter a city, request weather, and render a weather card.
8. Weather card must include a rule-based weather reminder.
9. Error responses must continue to use the project-wide error envelope.

## Response Contract
Required fields:
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

## Edge Cases
- Empty `city` returns `INVALID_INPUT` with message `City is required`
- Unknown city returns fallback mock data
- City value with case differences must still resolve to known mock data
- City value with leading or trailing spaces must still resolve
- Mock provider fallback must remain deterministic
- Error response format must remain stable

## Non-Goals
- Real weather API integration
- Geolocation
- Multi-day forecast
- Hourly forecast
- Outfit recommendation
- AI-generated reasoning

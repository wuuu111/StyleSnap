from __future__ import annotations

from fastapi import HTTPException

from app.schemas.weather import OutfitWeatherContext, WeatherData, WeatherProvider, WeatherSkillResponse


MOCK_WEATHER_DATA: dict[str, WeatherData] = {
    "tokyo": WeatherData(
        city="Tokyo",
        temperature=22,
        feels_like=21,
        min_temp=18,
        max_temp=24,
        weather_condition="cloudy",
        rain_probability=30,
        wind_speed=3.5,
        humidity=60,
        uv_index=4,
    ),
    "singapore": WeatherData(
        city="Singapore",
        temperature=31,
        feels_like=34,
        min_temp=27,
        max_temp=33,
        weather_condition="humid",
        rain_probability=55,
        wind_speed=2.8,
        humidity=82,
        uv_index=8,
    ),
    "shanghai": WeatherData(
        city="Shanghai",
        temperature=26,
        feels_like=28,
        min_temp=22,
        max_temp=29,
        weather_condition="rainy",
        rain_probability=65,
        wind_speed=4.0,
        humidity=76,
        uv_index=5,
    ),
    "beijing": WeatherData(
        city="Beijing",
        temperature=24,
        feels_like=23,
        min_temp=17,
        max_temp=27,
        weather_condition="sunny",
        rain_probability=15,
        wind_speed=5.5,
        humidity=42,
        uv_index=7,
    ),
    "taipei": WeatherData(
        city="Taipei",
        temperature=27,
        feels_like=29,
        min_temp=24,
        max_temp=30,
        weather_condition="rainy",
        rain_probability=70,
        wind_speed=4.2,
        humidity=78,
        uv_index=5,
    ),
    "hong kong": WeatherData(
        city="Hong Kong",
        temperature=29,
        feels_like=32,
        min_temp=26,
        max_temp=31,
        weather_condition="showers",
        rain_probability=60,
        wind_speed=5.1,
        humidity=79,
        uv_index=6,
    ),
    "guangzhou": WeatherData(
        city="Guangzhou",
        temperature=30,
        feels_like=33,
        min_temp=26,
        max_temp=33,
        weather_condition="thunderstorms",
        rain_probability=68,
        wind_speed=3.9,
        humidity=81,
        uv_index=6,
    ),
    "shenzhen": WeatherData(
        city="Shenzhen",
        temperature=29,
        feels_like=31,
        min_temp=25,
        max_temp=32,
        weather_condition="cloudy",
        rain_probability=50,
        wind_speed=3.4,
        humidity=74,
        uv_index=6,
    ),
    "new york": WeatherData(
        city="New York",
        temperature=20,
        feels_like=19,
        min_temp=15,
        max_temp=23,
        weather_condition="partly cloudy",
        rain_probability=25,
        wind_speed=4.8,
        humidity=57,
        uv_index=5,
    ),
    "london": WeatherData(
        city="London",
        temperature=17,
        feels_like=16,
        min_temp=12,
        max_temp=19,
        weather_condition="drizzle",
        rain_probability=58,
        wind_speed=5.9,
        humidity=72,
        uv_index=3,
    ),
}


FALLBACK_WEATHER = WeatherData(
    city="Fallback",
    temperature=23,
    feels_like=24,
    min_temp=19,
    max_temp=27,
    weather_condition="partly cloudy",
    rain_probability=35,
    wind_speed=3.2,
    humidity=58,
    uv_index=5,
)


def normalize_city(city: str) -> str:
    return city.strip().lower()


def validate_city(city: str) -> str:
    if not city or not city.strip():
        raise HTTPException(
            status_code=400,
            detail={
                "code": "INVALID_INPUT",
                "message": "City is required",
                "details": {},
            },
        )
    return city.strip()


def validate_coordinates(lat: float, lon: float) -> None:
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise HTTPException(
            status_code=400,
            detail={
                "code": "INVALID_INPUT",
                "message": "Invalid coordinates",
                "details": {},
            },
        )


def get_mock_weather(city: str) -> WeatherData:
    normalized_city = normalize_city(city)
    weather = MOCK_WEATHER_DATA.get(normalized_city)
    if weather is not None:
        return weather
    return FALLBACK_WEATHER.model_copy(update={"city": city.strip()})


class MockWeatherProvider:
    def get_weather(self, city: str) -> WeatherData:
        return get_mock_weather(city)


DEFAULT_WEATHER_PROVIDER: WeatherProvider = MockWeatherProvider()


def _risk_from_threshold(value: float, medium_threshold: float, high_threshold: float) -> str:
    if value >= high_threshold:
        return "high"
    if value >= medium_threshold:
        return "medium"
    return "low"


def _append_unique(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def build_outfit_weather_context(weather: WeatherData) -> OutfitWeatherContext:
    recommended_materials: list[str] = []
    avoid_materials: list[str] = []
    shoe_constraints: list[str] = []
    styling_hints: list[str] = []

    if weather.temperature <= 8:
        temperature_level = "cold"
        layering_needed = True
        outerwear_needed = True
        recommended_materials.extend(["wool", "fleece"])
        styling_hints.append("use warm layered outfit")
    elif weather.temperature <= 18:
        temperature_level = "cool"
        layering_needed = True
        outerwear_needed = True
        recommended_materials.extend(["knit", "mid-weight cotton"])
        styling_hints.append("keep one practical outer layer ready")
    elif weather.temperature <= 26:
        temperature_level = "mild"
        layering_needed = False
        outerwear_needed = False
        recommended_materials.extend(["cotton", "light knit"])
        styling_hints.append("light layers are enough if the day runs long")
    else:
        temperature_level = "warm"
        layering_needed = False
        outerwear_needed = False
        recommended_materials.extend(["cotton", "linen", "breathable fabric"])
        styling_hints.append("choose breathable layers")

    rain_risk = _risk_from_threshold(weather.rain_probability, 40, 60)
    wind_risk = _risk_from_threshold(weather.wind_speed, 4, 6)
    uv_risk = _risk_from_threshold(weather.uv_index, 5, 7)

    rain_protection_needed = False
    uv_protection_needed = False

    if weather.rain_probability >= 60:
        rain_protection_needed = True
        _append_unique(recommended_materials, "quick-dry fabric")
        _append_unique(avoid_materials, "suede")
        _append_unique(avoid_materials, "heavy wool")
        _append_unique(shoe_constraints, "avoid suede shoes")
        _append_unique(shoe_constraints, "prefer water-resistant shoes")
        _append_unique(styling_hints, "avoid long heavy outerwear")

    if weather.uv_index >= 7:
        uv_protection_needed = True
        _append_unique(styling_hints, "consider hat or light outer layer")

    if weather.wind_speed >= 6:
        _append_unique(styling_hints, "avoid loose lightweight outerwear")

    return OutfitWeatherContext(
        temperature_level=temperature_level,
        rain_risk=rain_risk,
        wind_risk=wind_risk,
        uv_risk=uv_risk,
        layering_needed=layering_needed,
        outerwear_needed=outerwear_needed,
        rain_protection_needed=rain_protection_needed,
        uv_protection_needed=uv_protection_needed,
        recommended_materials=recommended_materials,
        avoid_materials=avoid_materials,
        shoe_constraints=shoe_constraints,
        styling_hints=styling_hints,
    )


def resolve_city_from_coordinates(lat: float, lon: float) -> str:
    validate_coordinates(lat, lon)

    if 21 <= lat <= 26 and 119 <= lon <= 123:
        return "Taipei"
    if 1 <= lat <= 2 and 103 <= lon <= 105:
        return "Singapore"
    if 34 <= lat <= 36.5 and 138 <= lon <= 141:
        return "Tokyo"
    if 30 <= lat <= 32.5 and 120 <= lon <= 123:
        return "Shanghai"
    return "Taipei"


def get_weather_by_city(city: str, provider: WeatherProvider = DEFAULT_WEATHER_PROVIDER) -> WeatherSkillResponse:
    requested_city = validate_city(city)
    normalized_city = normalize_city(requested_city)
    weather = provider.get_weather(normalized_city if normalized_city in MOCK_WEATHER_DATA else requested_city)
    resolved_city = weather.city if normalized_city in MOCK_WEATHER_DATA else requested_city

    return WeatherSkillResponse(
        source="city",
        location={"city": resolved_city},
        weather=weather,
        outfit_context=build_outfit_weather_context(weather),
    )


def get_weather_by_location(lat: float, lon: float, provider: WeatherProvider = DEFAULT_WEATHER_PROVIDER) -> WeatherSkillResponse:
    resolved_city = resolve_city_from_coordinates(lat, lon)
    weather = provider.get_weather(normalize_city(resolved_city))

    return WeatherSkillResponse(
        source="location",
        location={
            "lat": lat,
            "lon": lon,
            "resolved_city": resolved_city,
        },
        weather=weather,
        outfit_context=build_outfit_weather_context(weather),
    )

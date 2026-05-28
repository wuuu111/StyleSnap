from __future__ import annotations

from fastapi import APIRouter

from app.schemas.weather import WeatherSkillResponse
from app.services.weather_service import get_weather_by_city, get_weather_by_location


router = APIRouter(prefix="/api/weather", tags=["weather"])


@router.get("", response_model=WeatherSkillResponse, response_model_exclude_none=True)
def read_weather(city: str) -> WeatherSkillResponse:
    return get_weather_by_city(city)


@router.get("/current", response_model=WeatherSkillResponse, response_model_exclude_none=True)
def read_current_weather(lat: float, lon: float) -> WeatherSkillResponse:
    return get_weather_by_location(lat, lon)

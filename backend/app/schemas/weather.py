from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, Field


class WeatherData(BaseModel):
    city: str
    temperature: float
    feels_like: float
    min_temp: float
    max_temp: float
    weather_condition: str
    rain_probability: int = Field(ge=0, le=100)
    wind_speed: float
    humidity: int = Field(ge=0, le=100)
    uv_index: int = Field(ge=0)


class OutfitWeatherContext(BaseModel):
    temperature_level: Literal["cold", "cool", "mild", "warm"]
    rain_risk: Literal["low", "medium", "high"]
    wind_risk: Literal["low", "medium", "high"]
    uv_risk: Literal["low", "medium", "high"]
    layering_needed: bool
    outerwear_needed: bool
    rain_protection_needed: bool
    uv_protection_needed: bool
    recommended_materials: list[str]
    avoid_materials: list[str]
    shoe_constraints: list[str]
    styling_hints: list[str]


class WeatherLocation(BaseModel):
    city: str | None = None
    lat: float | None = None
    lon: float | None = None
    resolved_city: str | None = None


class WeatherSkillResponse(BaseModel):
    source: Literal["city", "location"]
    location: WeatherLocation
    weather: WeatherData
    outfit_context: OutfitWeatherContext


class WeatherProvider(Protocol):
    def get_weather(self, city: str) -> WeatherData: ...

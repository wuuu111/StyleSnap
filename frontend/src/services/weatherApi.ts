import { apiFetch } from "./apiClient";
import type { WeatherSkillResponse } from "../types/weather";


export function getWeatherByCity(city: string) {
  const params = new URLSearchParams({ city });
  return apiFetch<WeatherSkillResponse>(`/api/weather?${params.toString()}`);
}


export function getWeatherByLocation(lat: number, lon: number) {
  const params = new URLSearchParams({
    lat: String(lat),
    lon: String(lon),
  });
  return apiFetch<WeatherSkillResponse>(
    `/api/weather/current?${params.toString()}`,
  );
}

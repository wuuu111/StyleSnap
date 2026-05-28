export type WeatherData = {
  city: string;
  temperature: number;
  feels_like: number;
  min_temp: number;
  max_temp: number;
  weather_condition: string;
  rain_probability: number;
  wind_speed: number;
  humidity: number;
  uv_index: number;
};

export type OutfitWeatherContext = {
  temperature_level: "cold" | "cool" | "mild" | "warm";
  rain_risk: "low" | "medium" | "high";
  wind_risk: "low" | "medium" | "high";
  uv_risk: "low" | "medium" | "high";
  layering_needed: boolean;
  outerwear_needed: boolean;
  rain_protection_needed: boolean;
  uv_protection_needed: boolean;
  recommended_materials: string[];
  avoid_materials: string[];
  shoe_constraints: string[];
  styling_hints: string[];
};

export type WeatherLocation = {
  city?: string;
  lat?: number;
  lon?: number;
  resolved_city?: string;
};

export type WeatherSkillResponse = {
  source: "city" | "location";
  location: WeatherLocation;
  weather: WeatherData;
  outfit_context: OutfitWeatherContext;
};

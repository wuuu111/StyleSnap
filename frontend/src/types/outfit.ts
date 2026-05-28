import type { ClothingItem } from "./clothing";
import type { WeatherSkillResponse } from "./weather";

export const occasionOptions = ["上课", "实习", "通勤", "约会", "运动", "面试", "休闲"] as const;
export const targetStyleOptions = [
  "日系简约",
  "韩系校园",
  "Clean Fit",
  "City Boy",
  "通勤轻熟",
  "运动休闲",
  "美式复古",
  "Old Money",
] as const;

export type WeatherSourcePayload =
  | {
      type: "city";
      city: string;
    }
  | {
      type: "location";
      lat: number;
      lon: number;
    };

export type OutfitRecommendationPayload = {
  occasion: (typeof occasionOptions)[number];
  target_style: (typeof targetStyleOptions)[number];
  preference_text: string;
  weather_source: WeatherSourcePayload;
};

export type OutfitScoreBreakdown = {
  weather_fit: number;
  style_match: number;
  color_harmony: number;
  occasion_fit: number;
  user_preference: number;
};

export type OutfitReasoning = {
  summary: string;
  weather_reasoning: string;
  style_reasoning: string;
  color_reasoning: string;
  occasion_reasoning: string;
  preference_reasoning: string;
};

export type RecommendedOutfitItem = {
  role: string;
  item: ClothingItem;
};

export type RecommendedOutfit = {
  id: string;
  items: RecommendedOutfitItem[];
  total_score: number;
  score_breakdown: OutfitScoreBreakdown;
  reasoning: OutfitReasoning;
  warnings: string[];
};

export type OutfitRecommendationResponse = {
  weather_context: WeatherSkillResponse;
  recommended_outfits: RecommendedOutfit[];
  meta: {
    candidate_count: number;
    returned_count: number;
    scoring_version: string;
  };
};

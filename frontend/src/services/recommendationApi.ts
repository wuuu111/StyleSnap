import { apiFetch } from "./apiClient";
import type {
  OutfitRecommendationPayload,
  OutfitRecommendationResponse,
} from "../types/outfit";


export function recommendOutfits(payload: OutfitRecommendationPayload) {
  return apiFetch<OutfitRecommendationResponse>("/api/outfits/recommend", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

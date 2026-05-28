import { apiFetch } from "./apiClient";
import type {
  ClothingAnalyzePayload,
  ClothingFilters,
  ClothingItem,
  ClothingPayload,
} from "../types/clothing";


function buildQuery(filters: ClothingFilters = {}): string {
  const params = new URLSearchParams();

  for (const [key, value] of Object.entries(filters)) {
    if (value && value.trim()) {
      params.set(key, value.trim());
    }
  }

  const query = params.toString();
  return query ? `?${query}` : "";
}


export function getClothes(filters: ClothingFilters = {}) {
  return apiFetch<ClothingItem[]>(`/api/clothes${buildQuery(filters)}`);
}


export function getClothingItem(id: number) {
  return apiFetch<ClothingItem>(`/api/clothes/${id}`);
}


export function createClothingItem(payload: ClothingPayload) {
  return apiFetch<ClothingItem>("/api/clothes", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}


export function updateClothingItem(id: number, payload: ClothingPayload) {
  return apiFetch<ClothingItem>(`/api/clothes/${id}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}


export function deleteClothingItem(id: number) {
  return apiFetch<void>(`/api/clothes/${id}`, {
    method: "DELETE",
  });
}


export function analyzeClothingImage(payload: ClothingAnalyzePayload) {
  return apiFetch<ClothingPayload>("/api/clothes/analyze", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

import type { ClothingItem, ClothingPayload } from "../types/clothing";


export const emptyClothingPayload: ClothingPayload = {
  name: "",
  image_url: "",
  category: "top",
  color: "",
  style_tags: [],
  season_tags: [],
  thickness: "medium",
  min_temperature: null,
  max_temperature: null,
  rain_suitable: false,
  occasion_tags: [],
  notes: "",
};


export function toTagString(tags: string[]): string {
  return tags.join(", ");
}


export function parseTagString(value: string): string[] {
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}


export function clothingItemToPayload(item: ClothingItem): ClothingPayload {
  return {
    name: item.name,
    image_url: item.image_url,
    category: item.category,
    color: item.color,
    style_tags: item.style_tags,
    season_tags: item.season_tags,
    thickness: item.thickness,
    min_temperature: item.min_temperature,
    max_temperature: item.max_temperature,
    rain_suitable: item.rain_suitable,
    occasion_tags: item.occasion_tags,
    notes: item.notes,
  };
}

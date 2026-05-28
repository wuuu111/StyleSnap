export const clothingCategories = [
  "top",
  "pants",
  "outerwear",
  "shoes",
  "hat",
  "bag",
  "accessory",
] as const;

export const clothingThicknessOptions = ["thin", "medium", "thick"] as const;

export type ClothingCategory = (typeof clothingCategories)[number];
export type ClothingThickness = (typeof clothingThicknessOptions)[number];

export type ClothingItem = {
  id: number;
  name: string;
  image_url: string;
  category: ClothingCategory;
  color: string;
  style_tags: string[];
  season_tags: string[];
  thickness: ClothingThickness;
  min_temperature: number | null;
  max_temperature: number | null;
  rain_suitable: boolean;
  occasion_tags: string[];
  notes: string;
  created_at: string;
  updated_at: string;
};

export type ClothingPayload = {
  name: string;
  image_url: string;
  category: ClothingCategory;
  color: string;
  style_tags: string[];
  season_tags: string[];
  thickness: ClothingThickness;
  min_temperature: number | null;
  max_temperature: number | null;
  rain_suitable: boolean;
  occasion_tags: string[];
  notes: string;
};

export type ClothingAnalyzePayload = {
  image_url: string;
};

export type ClothingFilters = {
  category?: string;
  color?: string;
  season?: string;
};

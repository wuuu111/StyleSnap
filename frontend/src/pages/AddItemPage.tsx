import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { ClothingItemForm } from "../components/ClothingItemForm";
import { PageHeader } from "../components/PageHeader";
import {
  analyzeClothingImage,
  createClothingItem,
} from "../services/clothesApi";
import type { ClothingPayload } from "../types/clothing";


export function AddItemPage() {
  const navigate = useNavigate();
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async (payload: ClothingPayload) => {
    setSubmitting(true);
    try {
      await createClothingItem(payload);
      window.setTimeout(() => navigate("/wardrobe"), 700);
    } finally {
      setSubmitting(false);
    }
  };

  const handleAnalyze = async (imageUrl: string) =>
    analyzeClothingImage({ image_url: imageUrl });

  return (
    <section className="space-y-6">
      <PageHeader
        eyebrow="Add Item"
        title="Upload a clothing image, preview it locally, then refine the tags before saving."
        description="On mobile you can take a photo or choose from your album. On desktop you can drag, drop, or upload from device. Mock AI remains editable and storage stays local in this MVP."
      />
      <ClothingItemForm
        mode="create"
        onAnalyze={handleAnalyze}
        onSubmit={handleSubmit}
        submitting={submitting}
      />
    </section>
  );
}

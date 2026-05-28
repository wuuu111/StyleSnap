import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { ClothingItemForm } from "../components/ClothingItemForm";
import { PageHeader } from "../components/PageHeader";
import { getClothingItem, updateClothingItem } from "../services/clothesApi";
import type { ClothingPayload } from "../types/clothing";
import { clothingItemToPayload } from "../utils/clothingForm";


export function EditItemPage() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [initialValue, setInitialValue] = useState<ClothingPayload | null>(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) {
      setError("Missing clothing item id.");
      setLoading(false);
      return;
    }

    getClothingItem(Number(id))
      .then((item) => setInitialValue(clothingItemToPayload(item)))
      .catch((caughtError) =>
        setError(
          caughtError instanceof Error
            ? caughtError.message
            : "Failed to load clothing item.",
        ),
      )
      .finally(() => setLoading(false));
  }, [id]);

  const handleSubmit = async (payload: ClothingPayload) => {
    if (!id) return;
    setSubmitting(true);
    try {
      await updateClothingItem(Number(id), payload);
      navigate("/wardrobe");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section className="space-y-6">
      <PageHeader
        eyebrow="Edit Item"
        title="Refine existing wardrobe metadata without leaving the core flow."
        description="This page keeps editing simple and stable: load the saved item, adjust its fields, and return to the wardrobe list."
      />
      {loading ? (
        <div className="rounded-[24px] border border-ink/10 bg-white p-6 text-sm text-ink/65">
          Loading item...
        </div>
      ) : null}
      {error ? (
        <div className="rounded-[24px] bg-red-50 px-5 py-4 text-sm text-red-700">
          {error}
        </div>
      ) : null}
      {!loading && initialValue ? (
        <ClothingItemForm
          initialValue={initialValue}
          mode="edit"
          onSubmit={handleSubmit}
          submitting={submitting}
        />
      ) : null}
    </section>
  );
}

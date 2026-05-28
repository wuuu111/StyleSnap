import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { ClothingItemCard } from "../components/ClothingItemCard";
import { FilterBar } from "../components/FilterBar";
import { PageHeader } from "../components/PageHeader";
import { deleteClothingItem, getClothes } from "../services/clothesApi";
import type { ClothingFilters, ClothingItem } from "../types/clothing";


export function WardrobePage() {
  const [items, setItems] = useState<ClothingItem[]>([]);
  const [filters, setFilters] = useState<ClothingFilters>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError(null);

    getClothes(filters)
      .then((response) => {
        if (active) {
          setItems(response);
        }
      })
      .catch((caughtError) => {
        if (active) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load wardrobe.",
          );
        }
      })
      .finally(() => {
        if (active) {
          setLoading(false);
        }
      });

    return () => {
      active = false;
    };
  }, [filters]);

  const handleDelete = async (id: number) => {
    setDeletingId(id);
    try {
      await deleteClothingItem(id);
      setItems((current) => current.filter((item) => item.id !== id));
    } catch (caughtError) {
      setError(
        caughtError instanceof Error ? caughtError.message : "Delete failed.",
      );
    } finally {
      setDeletingId(null);
    }
  };

  return (
    <section className="space-y-6">
      <PageHeader
        eyebrow="Wardrobe"
        title="Your digital wardrobe is now the source of truth for later recommendations."
        description="Browse seeded items, filter what you already own, and keep every clothing record editable so later recommendation logic can trust the wardrobe metadata."
      />

      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <FilterBar filters={filters} onChange={setFilters} />
        <Link
          className="rounded-full bg-ink px-5 py-3 text-sm font-medium text-white no-underline"
          to="/wardrobe/new"
        >
          Add clothing item
        </Link>
      </div>

      {error ? (
        <div className="rounded-[24px] bg-red-50 px-5 py-4 text-sm text-red-700">
          {error}
        </div>
      ) : null}

      {loading ? (
        <div className="rounded-[24px] border border-ink/10 bg-white p-6 text-sm text-ink/65">
          Loading wardrobe...
        </div>
      ) : null}

      {!loading && items.length === 0 ? (
        <div className="rounded-[24px] border border-dashed border-ink/20 bg-white p-8 text-center">
          <h3 className="text-xl font-semibold text-ink">No items found</h3>
          <p className="mt-2 text-sm leading-6 text-ink/65">
            Try changing the filters or add your first clothing item.
          </p>
        </div>
      ) : null}

      {!loading && items.length > 0 ? (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {items.map((item) => (
            <ClothingItemCard
              deleting={deletingId === item.id}
              item={item}
              key={item.id}
              onDelete={handleDelete}
            />
          ))}
        </div>
      ) : null}
    </section>
  );
}

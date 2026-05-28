import { Link } from "react-router-dom";

import type { ClothingItem } from "../types/clothing";


type ClothingItemCardProps = {
  item: ClothingItem;
  onDelete: (id: number) => Promise<void>;
  deleting: boolean;
};


export function ClothingItemCard({
  item,
  onDelete,
  deleting,
}: ClothingItemCardProps) {
  return (
    <article className="overflow-hidden rounded-[24px] border border-ink/10 bg-white shadow-card">
      <div className="aspect-[4/3] bg-mist">
        {item.image_url ? (
          <img
            alt={item.name}
            className="h-full w-full object-cover"
            src={item.image_url}
          />
        ) : (
          <div className="flex h-full items-center justify-center text-sm text-ink/45">
            No image
          </div>
        )}
      </div>
      <div className="space-y-4 p-5">
        <div>
          <div className="flex items-start justify-between gap-3">
            <div>
              <h3 className="text-lg font-semibold text-ink">{item.name}</h3>
              <p className="mt-1 text-sm text-ink/60">
                {item.category} · {item.color} · {item.thickness}
              </p>
            </div>
            <span className="rounded-full bg-sand px-3 py-1 text-xs font-medium text-ink/80">
              {item.min_temperature ?? "-"}-{item.max_temperature ?? "-"}℃
            </span>
          </div>
        </div>

        <div className="space-y-2 text-sm text-ink/75">
          <p>Style: {item.style_tags.join(", ") || "None"}</p>
          <p>Season: {item.season_tags.join(", ") || "None"}</p>
          <p>Occasion: {item.occasion_tags.join(", ") || "None"}</p>
        </div>

        <div className="flex gap-3">
          <Link
            className="rounded-full border border-ink/15 px-4 py-2 text-sm font-medium text-ink no-underline"
            to={`/wardrobe/${item.id}/edit`}
          >
            Edit
          </Link>
          <button
            className="rounded-full bg-ink px-4 py-2 text-sm font-medium text-white disabled:opacity-60"
            disabled={deleting}
            onClick={() => void onDelete(item.id)}
            type="button"
          >
            {deleting ? "Deleting..." : "Delete"}
          </button>
        </div>
      </div>
    </article>
  );
}

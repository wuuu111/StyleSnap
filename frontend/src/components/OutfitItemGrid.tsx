import type { RecommendedOutfitItem } from "../types/outfit";


type OutfitItemGridProps = {
  items: RecommendedOutfitItem[];
};


function roleLabel(role: string) {
  return role.charAt(0).toUpperCase() + role.slice(1);
}


export function OutfitItemGrid({ items }: OutfitItemGridProps) {
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {items.map((entry) => (
        <article
          className="flex gap-3 rounded-[20px] border border-ink/10 bg-white p-3"
          key={`${entry.role}-${entry.item.id}`}
        >
          <div className="h-20 w-20 overflow-hidden rounded-2xl bg-mist">
            {entry.item.image_url ? (
              <img
                alt={entry.item.name}
                className="h-full w-full object-cover"
                src={entry.item.image_url}
              />
            ) : (
              <div className="flex h-full items-center justify-center text-xs text-ink/45">
                No image
              </div>
            )}
          </div>
          <div className="min-w-0 flex-1">
            <p className="text-xs font-semibold uppercase tracking-[0.2em] text-clay">
              {roleLabel(entry.role)}
            </p>
            <h5 className="mt-1 text-sm font-semibold text-ink">
              {entry.item.name}
            </h5>
            <p className="mt-1 text-xs leading-5 text-ink/65">
              {entry.item.color} · {entry.item.style_tags.join(", ")}
            </p>
          </div>
        </article>
      ))}
    </div>
  );
}

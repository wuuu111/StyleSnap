import type { ClothingFilters } from "../types/clothing";


type FilterBarProps = {
  filters: ClothingFilters;
  onChange: (filters: ClothingFilters) => void;
};


export function FilterBar({ filters, onChange }: FilterBarProps) {
  return (
    <div className="grid gap-3 rounded-[24px] border border-ink/10 bg-white p-4 md:grid-cols-3">
      <input
        className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
        onChange={(event) =>
          onChange({ ...filters, category: event.target.value })
        }
        placeholder="Filter by category"
        value={filters.category ?? ""}
      />
      <input
        className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
        onChange={(event) => onChange({ ...filters, color: event.target.value })}
        placeholder="Filter by color"
        value={filters.color ?? ""}
      />
      <input
        className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
        onChange={(event) => onChange({ ...filters, season: event.target.value })}
        placeholder="Filter by season"
        value={filters.season ?? ""}
      />
    </div>
  );
}

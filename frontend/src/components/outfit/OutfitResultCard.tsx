import { OutfitItemGrid } from "../OutfitItemGrid";
import { ReasoningPanel } from "./ReasoningPanel";
import { ScoreBreakdown } from "./ScoreBreakdown";
import { WarningList } from "./WarningList";
import type { RecommendedOutfit } from "../../types/outfit";

type OutfitResultCardProps = {
  lookIndex: number;
  occasion: string;
  outfit: RecommendedOutfit;
  targetStyle: string;
  totalLooks: number;
};

export function OutfitResultCard({
  lookIndex,
  occasion,
  outfit,
  targetStyle,
  totalLooks,
}: OutfitResultCardProps) {
  return (
    <article className="space-y-5 rounded-[28px] border border-ink/10 bg-sand p-5 shadow-card sm:p-6">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
        <div className="space-y-3">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Look {lookIndex + 1} / {totalLooks}
          </p>
          <h4 className="text-2xl font-semibold text-ink">
            {outfit.reasoning.summary}
          </h4>
          <div className="flex flex-wrap gap-2 text-xs text-ink/72">
            <span className="rounded-full bg-white px-3 py-1">{targetStyle}</span>
            <span className="rounded-full bg-white px-3 py-1">{occasion}</span>
            <span className="rounded-full bg-white px-3 py-1">
              {outfit.warnings.length > 0 ? "Weather-aware" : "Everyday-ready"}
            </span>
          </div>
        </div>

        <div className="rounded-[22px] bg-white px-5 py-4 text-center shadow-card">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-clay">
            Total Score
          </p>
          <p className="mt-2 text-3xl font-semibold tracking-tight text-ink">
            {outfit.total_score}
          </p>
          <p className="text-xs text-ink/55">/ 100</p>
        </div>
      </div>

      <section className="space-y-3 rounded-[24px] border border-ink/10 bg-white p-4">
        <div className="flex items-center justify-between gap-3">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Items
          </p>
          <span className="text-xs text-ink/55">{outfit.items.length} selected</span>
        </div>
        <OutfitItemGrid items={outfit.items} />
      </section>

      <ScoreBreakdown scoreBreakdown={outfit.score_breakdown} />
      <ReasoningPanel reasoning={outfit.reasoning} />
      <WarningList warnings={outfit.warnings} />
    </article>
  );
}

import type { OutfitReasoning } from "../../types/outfit";

type ReasoningPanelProps = {
  reasoning: OutfitReasoning;
};

const detailSections: Array<{
  key: Exclude<keyof OutfitReasoning, "summary">;
  label: string;
}> = [
  { key: "weather_reasoning", label: "Weather reasoning" },
  { key: "style_reasoning", label: "Style reasoning" },
  { key: "color_reasoning", label: "Color reasoning" },
  { key: "occasion_reasoning", label: "Occasion reasoning" },
  { key: "preference_reasoning", label: "Preference reasoning" },
];

export function ReasoningPanel({ reasoning }: ReasoningPanelProps) {
  return (
    <section className="space-y-4 rounded-[24px] border border-ink/10 bg-white p-4">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
          Why This Look Works
        </p>
        <p className="mt-2 text-sm leading-6 text-ink/78">{reasoning.summary}</p>
      </div>

      <details className="group rounded-[20px] bg-mist px-4 py-3">
        <summary className="cursor-pointer list-none text-sm font-semibold text-ink">
          Detailed reasoning
        </summary>
        <div className="mt-4 grid gap-3">
          {detailSections.map(({ key, label }) => (
            <article className="rounded-2xl bg-white px-4 py-3" key={key}>
              <h5 className="text-sm font-semibold text-ink">{label}</h5>
              <p className="mt-1 text-sm leading-6 text-ink/72">{reasoning[key]}</p>
            </article>
          ))}
        </div>
      </details>
    </section>
  );
}

import type { OutfitScoreBreakdown } from "../../types/outfit";

const scoreLabels: Array<{
  key: keyof OutfitScoreBreakdown;
  label: string;
}> = [
  { key: "weather_fit", label: "Weather Fit" },
  { key: "style_match", label: "Style Match" },
  { key: "color_harmony", label: "Color Harmony" },
  { key: "occasion_fit", label: "Occasion Fit" },
  { key: "user_preference", label: "Preference Fit" },
];

type ScoreBreakdownProps = {
  scoreBreakdown: OutfitScoreBreakdown;
};

export function ScoreBreakdown({ scoreBreakdown }: ScoreBreakdownProps) {
  return (
    <section className="space-y-3 rounded-[24px] border border-ink/10 bg-white p-4">
      <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
        Score Breakdown
      </p>
      <div className="grid gap-3 sm:grid-cols-2">
        {scoreLabels.map(({ key, label }) => {
          const value = scoreBreakdown[key];
          return (
            <div className="rounded-2xl bg-mist px-4 py-3" key={key}>
              <div className="flex items-center justify-between gap-3 text-sm">
                <span className="text-ink/72">{label}</span>
                <span className="font-semibold text-ink">{value}</span>
              </div>
              <div className="mt-2 h-2 rounded-full bg-white">
                <div
                  className="h-full rounded-full bg-clay"
                  style={{ width: `${value}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

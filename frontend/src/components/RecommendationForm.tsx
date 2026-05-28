import {
  occasionOptions,
  targetStyleOptions,
} from "../types/outfit";


type RecommendationFormProps = {
  occasion: (typeof occasionOptions)[number];
  targetStyle: (typeof targetStyleOptions)[number];
  preferenceText: string;
  disabled: boolean;
  loading: boolean;
  canSubmit: boolean;
  onOccasionChange: (value: (typeof occasionOptions)[number]) => void;
  onTargetStyleChange: (value: (typeof targetStyleOptions)[number]) => void;
  onPreferenceTextChange: (value: string) => void;
  onSubmit: () => void;
};


export function RecommendationForm({
  occasion,
  targetStyle,
  preferenceText,
  disabled,
  loading,
  canSubmit,
  onOccasionChange,
  onTargetStyleChange,
  onPreferenceTextChange,
  onSubmit,
}: RecommendationFormProps) {
  return (
    <section className="space-y-4 rounded-[28px] border border-ink/10 bg-white p-6 shadow-card">
      <div className="space-y-2">
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
          Recommendation Input
        </p>
        <h3 className="text-2xl font-semibold text-ink">告诉 StyleSnap 今天的目标</h3>
        <p className="text-sm leading-6 text-ink/70">
          选择场景、目标风格和额外偏好，系统会结合天气上下文与个人衣橱生成可解释的推荐结果。
        </p>
      </div>

      <div className="grid gap-3 md:grid-cols-2">
        <label className="space-y-2">
          <span className="text-sm font-medium text-ink">Occasion</span>
          <select
            className="w-full rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
            disabled={disabled}
            onChange={(event) =>
              onOccasionChange(event.target.value as (typeof occasionOptions)[number])
            }
            value={occasion}
          >
            {occasionOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label className="space-y-2">
          <span className="text-sm font-medium text-ink">Target style</span>
          <select
            className="w-full rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
            disabled={disabled}
            onChange={(event) =>
              onTargetStyleChange(
                event.target.value as (typeof targetStyleOptions)[number],
              )
            }
            value={targetStyle}
          >
            {targetStyleOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
      </div>

      <label className="space-y-2">
        <span className="text-sm font-medium text-ink">Preference</span>
        <textarea
          className="min-h-28 w-full rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
          disabled={disabled}
          onChange={(event) => onPreferenceTextChange(event.target.value)}
          placeholder="例如：不想太正式，想显高；今天想舒服一点；想保暖但不要太厚……"
          value={preferenceText}
        />
      </label>

      <button
        className="w-full rounded-full bg-ink px-5 py-3 text-sm font-medium text-white disabled:opacity-60 sm:w-auto"
        disabled={disabled || !canSubmit}
        onClick={onSubmit}
        type="button"
      >
        {loading ? "Generating..." : "Generate Outfits"}
      </button>
    </section>
  );
}

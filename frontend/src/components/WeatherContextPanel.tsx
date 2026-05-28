import { WeatherCard } from "./WeatherCard";
import { RecommendationStateCard } from "./RecommendationStateCard";
import type { WeatherSkillResponse } from "../types/weather";


type WeatherContextPanelProps = {
  city: string;
  weatherSkill: WeatherSkillResponse | null;
  loading: boolean;
  error: string | null;
  locationFallbackVisible: boolean;
  onCityChange: (value: string) => void;
  onUseLocation: () => void;
  onShowManualInput: () => void;
  onUseCityFallback: () => void;
};


export function WeatherContextPanel({
  city,
  weatherSkill,
  loading,
  error,
  locationFallbackVisible,
  onCityChange,
  onUseLocation,
  onShowManualInput,
  onUseCityFallback,
}: WeatherContextPanelProps) {
  return (
    <section className="space-y-4 rounded-[28px] border border-ink/10 bg-white p-6 shadow-card">
      <div className="space-y-2">
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
          今日穿搭环境
        </p>
        <h3 className="text-2xl font-semibold text-ink">先准备天气上下文</h3>
        <p className="text-sm leading-6 text-ink/70">
          使用当前位置，让 StyleSnap 自动考虑天气、降雨、紫外线和风感对今天穿搭的影响。
        </p>
      </div>

      {!weatherSkill ? (
        <div className="space-y-4 rounded-[24px] bg-sand p-5">
          <div className="flex flex-col gap-3 sm:flex-row">
            <button
              className="rounded-full bg-clay px-5 py-3 text-sm font-medium text-white disabled:opacity-60"
              disabled={loading}
              onClick={onUseLocation}
              type="button"
            >
              {loading ? "正在获取当前位置天气…" : "Use my location"}
            </button>
            <button
              className="rounded-full border border-ink/15 px-5 py-3 text-sm font-medium text-ink"
              onClick={onShowManualInput}
              type="button"
            >
              Enter city manually
            </button>
          </div>

          {error ? (
            <RecommendationStateCard
              description={error}
              title="暂时无法自动获取天气"
              tone="error"
            />
          ) : null}

          {locationFallbackVisible ? (
            <div className="space-y-3 rounded-[24px] border border-ink/10 bg-white p-4">
              <p className="text-sm leading-6 text-ink/75">
                无法获取定位，你也可以手动输入城市。
              </p>
              <div className="flex flex-col gap-3 sm:flex-row">
                <input
                  className="flex-1 rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
                  onChange={(event) => onCityChange(event.target.value)}
                  placeholder="Taipei"
                  value={city}
                />
                <button
                  className="rounded-full bg-ink px-5 py-3 text-sm font-medium text-white disabled:opacity-60"
                  disabled={loading}
                  onClick={onUseCityFallback}
                  type="button"
                >
                  {loading ? "Loading..." : "Use city fallback"}
                </button>
              </div>
            </div>
          ) : null}
        </div>
      ) : null}

      {weatherSkill ? <WeatherCard weatherSkill={weatherSkill} /> : null}
    </section>
  );
}

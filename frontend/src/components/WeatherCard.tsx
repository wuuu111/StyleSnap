import type { WeatherSkillResponse } from "../types/weather";


type WeatherCardProps = {
  weatherSkill: WeatherSkillResponse;
};


function buildPrimarySignals(weatherSkill: WeatherSkillResponse): string[] {
  const signals: string[] = [];
  const { outfit_context: outfitContext } = weatherSkill;

  if (outfitContext.rain_protection_needed) {
    signals.push("今天有降雨风险，优先选择防水或耐雨鞋款");
  }

  if (outfitContext.recommended_materials.length > 0) {
    signals.push(
      `适合 ${outfitContext.recommended_materials.slice(0, 2).join("、")} 这类材质`,
    );
  }

  if (outfitContext.avoid_materials.length > 0) {
    signals.push(`避免 ${outfitContext.avoid_materials[0]} 和过重的外层`);
  }

  if (outfitContext.uv_protection_needed) {
    signals.push("紫外线较强，可以考虑帽子或轻薄外层");
  }

  if (outfitContext.wind_risk === "high") {
    signals.push("风感较明显，建议补充更稳妥的外层");
  }

  if (signals.length === 0) {
    signals.push("天气条件较平稳，可以让风格和场景主导今天的穿搭。");
  }

  return signals.slice(0, 3);
}


function sourceLabel(weatherSkill: WeatherSkillResponse) {
  return weatherSkill.source === "location" ? "location" : "city";
}


export function WeatherCard({ weatherSkill }: WeatherCardProps) {
  const { weather, outfit_context: outfitContext } = weatherSkill;
  const primarySignals = buildPrimarySignals(weatherSkill);

  return (
    <article className="space-y-4 rounded-[24px] border border-ink/10 bg-white p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            今日穿搭环境
          </p>
          <h3 className="mt-2 text-2xl font-semibold text-ink">
            {weather.temperature}°C · {weather.weather_condition} · {weather.city}
          </h3>
          <p className="mt-2 text-sm text-ink/65">
            Source: {sourceLabel(weatherSkill)} · Rain {weatherSkill.outfit_context.rain_risk} ·
            UV {weatherSkill.outfit_context.uv_risk} · Wind {weatherSkill.outfit_context.wind_risk}
          </p>
        </div>
        <div className="rounded-full bg-mist px-4 py-2 text-xs font-medium text-ink/75">
          {outfitContext.temperature_level} weather
        </div>
      </div>

      <div className="rounded-[22px] bg-sand p-4">
        <p className="text-sm font-semibold text-ink">建议：</p>
        <ul className="mt-3 space-y-2">
          {primarySignals.map((signal) => (
            <li
              className="rounded-2xl bg-white px-4 py-3 text-sm leading-6 text-ink/80"
              key={signal}
            >
              {signal}
            </li>
          ))}
        </ul>
      </div>
    </article>
  );
}

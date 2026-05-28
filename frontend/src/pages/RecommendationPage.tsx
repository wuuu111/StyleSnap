import { useState } from "react";

import { ApiError } from "../types/api";
import { OutfitCarousel } from "../components/outfit/OutfitCarousel";
import { PageHeader } from "../components/PageHeader";
import { RecommendationForm } from "../components/RecommendationForm";
import { RecommendationStateCard } from "../components/RecommendationStateCard";
import { WeatherContextPanel } from "../components/WeatherContextPanel";
import { recommendOutfits } from "../services/recommendationApi";
import { getWeatherByCity, getWeatherByLocation } from "../services/weatherApi";
import {
  occasionOptions,
  targetStyleOptions,
  type OutfitRecommendationResponse,
  type WeatherSourcePayload,
} from "../types/outfit";
import type { WeatherSkillResponse } from "../types/weather";

const defaultOccasion = occasionOptions[0];
const defaultTargetStyle = targetStyleOptions[2];

export function RecommendationPage() {
  const [city, setCity] = useState("Taipei");
  const [occasion, setOccasion] =
    useState<(typeof occasionOptions)[number]>(defaultOccasion);
  const [targetStyle, setTargetStyle] =
    useState<(typeof targetStyleOptions)[number]>(defaultTargetStyle);
  const [preferenceText, setPreferenceText] = useState("");
  const [weatherSkill, setWeatherSkill] = useState<WeatherSkillResponse | null>(
    null,
  );
  const [weatherSource, setWeatherSource] = useState<WeatherSourcePayload | null>(
    null,
  );
  const [recommendationResult, setRecommendationResult] =
    useState<OutfitRecommendationResponse | null>(null);
  const [weatherLoading, setWeatherLoading] = useState(false);
  const [recommendationLoading, setRecommendationLoading] = useState(false);
  const [weatherError, setWeatherError] = useState<string | null>(null);
  const [recommendationError, setRecommendationError] = useState<string | null>(
    null,
  );
  const [locationFallbackVisible, setLocationFallbackVisible] = useState(false);
  const [insufficientWardrobe, setInsufficientWardrobe] = useState(false);

  const resetRecommendationState = () => {
    setRecommendationError(null);
    setInsufficientWardrobe(false);
  };

  const handleUseLocation = () => {
    if (!navigator.geolocation) {
      setLocationFallbackVisible(true);
      setWeatherError("暂时无法获取天气。你可以手动输入城市，或使用默认城市继续。");
      return;
    }

    setWeatherLoading(true);
    setWeatherError(null);
    resetRecommendationState();

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        try {
          const source = {
            type: "location" as const,
            lat: position.coords.latitude,
            lon: position.coords.longitude,
          };
          const response = await getWeatherByLocation(source.lat, source.lon);
          setWeatherSkill(response);
          setWeatherSource(source);
        } catch (caughtError) {
          setWeatherSkill(null);
          setWeatherSource(null);
          setLocationFallbackVisible(true);
          setWeatherError(
            caughtError instanceof Error
              ? caughtError.message
              : "暂时无法获取天气。你可以手动输入城市，或使用默认城市继续。",
          );
        } finally {
          setWeatherLoading(false);
        }
      },
      () => {
        setWeatherSkill(null);
        setWeatherSource(null);
        setLocationFallbackVisible(true);
        setWeatherLoading(false);
        setWeatherError("暂时无法获取天气。你可以手动输入城市，或使用默认城市继续。");
      },
      {
        enableHighAccuracy: false,
        timeout: 8000,
        maximumAge: 300000,
      },
    );
  };

  const handleCheckCityWeather = async () => {
    setWeatherLoading(true);
    setWeatherError(null);
    resetRecommendationState();

    try {
      const source = { type: "city" as const, city };
      const response = await getWeatherByCity(city);
      setWeatherSkill(response);
      setWeatherSource(source);
    } catch (caughtError) {
      setWeatherSkill(null);
      setWeatherSource(null);
      setWeatherError(
        caughtError instanceof Error
          ? caughtError.message
          : "暂时无法获取天气。你可以手动输入城市，或使用默认城市继续。",
      );
    } finally {
      setWeatherLoading(false);
    }
  };

  const handleGenerateOutfits = async () => {
    const nextWeatherSource =
      weatherSource ?? ({ type: "city" as const, city: city.trim() || "Taipei" });

    setRecommendationLoading(true);
    setRecommendationError(null);
    setInsufficientWardrobe(false);

    try {
      const response = await recommendOutfits({
        occasion,
        target_style: targetStyle,
        preference_text: preferenceText,
        weather_source: nextWeatherSource,
      });
      setRecommendationResult(response);
      setWeatherSource(nextWeatherSource);
      if (!weatherSkill) {
        setWeatherSkill(response.weather_context);
      }
    } catch (caughtError) {
      setRecommendationResult(null);
      if (caughtError instanceof ApiError && caughtError.code === "INSUFFICIENT_WARDROBE") {
        setInsufficientWardrobe(true);
        setRecommendationError(caughtError.message);
      } else {
        setRecommendationError(
          caughtError instanceof Error
            ? caughtError.message
            : "生成搭配失败，请检查衣橱数据或稍后重试。",
        );
      }
    } finally {
      setRecommendationLoading(false);
    }
  };

  const hasNoResults =
    recommendationResult && recommendationResult.recommended_outfits.length === 0;

  return (
    <section className="space-y-6">
      <PageHeader
        eyebrow="Recommendation"
        title="今天穿什么？"
        description="StyleSnap 会结合你的个人衣橱、当前位置天气、场景和目标风格，生成今天适合的穿搭建议。"
      />

      <div className="grid gap-6 lg:grid-cols-2">
        <div className="space-y-4 lg:sticky lg:top-6 lg:self-start">
          <WeatherContextPanel
            city={city}
            error={weatherError}
            loading={weatherLoading}
            locationFallbackVisible={locationFallbackVisible}
            onCityChange={setCity}
            onShowManualInput={() => setLocationFallbackVisible(true)}
            onUseCityFallback={() => void handleCheckCityWeather()}
            onUseLocation={handleUseLocation}
            weatherSkill={weatherSkill}
          />

          <RecommendationForm
            canSubmit={Boolean(weatherSource || city.trim())}
            disabled={recommendationLoading}
            loading={recommendationLoading}
            occasion={occasion}
            onOccasionChange={setOccasion}
            onPreferenceTextChange={setPreferenceText}
            onSubmit={() => void handleGenerateOutfits()}
            onTargetStyleChange={setTargetStyle}
            preferenceText={preferenceText}
            targetStyle={targetStyle}
          />
        </div>

        <section className="space-y-4 lg:max-w-3xl">
          <div className="flex flex-col gap-3 rounded-[28px] border border-ink/10 bg-white p-6 shadow-card sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
                Outfit Results
              </p>
              <h3 className="mt-2 text-2xl font-semibold text-ink">
                今日推荐
              </h3>
              <p className="mt-2 max-w-2xl text-sm leading-6 text-ink/70">
                一次聚焦展示一套 Look，并支持翻页切换查看 2-3 套推荐，避免长页面连续堆叠。
              </p>
            </div>
            <button
              className="rounded-full border border-ink/15 px-5 py-3 text-sm font-medium text-ink disabled:opacity-60"
              disabled={recommendationLoading}
              onClick={() => void handleGenerateOutfits()}
              type="button"
            >
              {recommendationLoading ? "Regenerating..." : "换一套 / 重新生成"}
            </button>
          </div>

          {recommendationLoading ? (
            <RecommendationStateCard
              description="StyleSnap 正在根据衣橱、天气、场景和风格重新组合今天的穿搭建议。"
              title="正在生成搭配"
            />
          ) : null}

          {insufficientWardrobe ? (
            <RecommendationStateCard
              actionLabel="Go to Wardrobe"
              actionTo="/wardrobe"
              description="你的衣橱还不够生成完整搭配。请至少添加一件上衣和一条裤子。"
              title="衣橱数据不足"
              tone="warning"
            />
          ) : null}

          {!insufficientWardrobe && recommendationError ? (
            <RecommendationStateCard
              description={recommendationError || "生成搭配失败，请检查衣橱数据或稍后重试。"}
              title="生成搭配失败"
              tone="error"
            />
          ) : null}

          {!recommendationLoading && !recommendationResult && !recommendationError ? (
            <RecommendationStateCard
              description="先准备天气上下文，再填写场景、风格和偏好。生成后这里会展示完整的推荐卡片、评分拆解和解释理由。"
              title="等待生成推荐"
            />
          ) : null}

          {hasNoResults ? (
            <RecommendationStateCard
              description="暂时没有找到合适搭配，请尝试更换风格或补充衣物。"
              title="没有找到合适搭配"
              tone="warning"
            />
          ) : null}

          {recommendationResult && recommendationResult.recommended_outfits.length > 0 ? (
            <OutfitCarousel
              candidateCount={recommendationResult.meta.candidate_count}
              occasion={occasion}
              outfits={recommendationResult.recommended_outfits}
              scoringVersion={recommendationResult.meta.scoring_version}
              targetStyle={targetStyle}
            />
          ) : null}
        </section>
      </div>
    </section>
  );
}

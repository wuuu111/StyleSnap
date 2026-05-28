import { useState } from "react";

import { ImageUploadPanel } from "./upload/ImageUploadPanel";
import {
  clothingCategories,
  clothingThicknessOptions,
  type ClothingPayload,
} from "../types/clothing";
import {
  emptyClothingPayload,
  parseTagString,
  toTagString,
} from "../utils/clothingForm";
import {
  buildAnalyzeImageUrl,
  deriveItemNameFromFile,
  validateImageFile,
} from "../utils/imageUpload";


type ClothingItemFormProps = {
  initialValue?: ClothingPayload;
  mode: "create" | "edit";
  onAnalyze?: (imageUrl: string) => Promise<ClothingPayload>;
  onSubmit: (payload: ClothingPayload) => Promise<void>;
  submitting: boolean;
};


export function ClothingItemForm({
  initialValue = emptyClothingPayload,
  mode,
  onAnalyze,
  onSubmit,
  submitting,
}: ClothingItemFormProps) {
  const [form, setForm] = useState<ClothingPayload>(initialValue);
  const [styleTags, setStyleTags] = useState(toTagString(initialValue.style_tags));
  const [seasonTags, setSeasonTags] = useState(toTagString(initialValue.season_tags));
  const [occasionTags, setOccasionTags] = useState(
    toTagString(initialValue.occasion_tags),
  );
  const [analyzing, setAnalyzing] = useState(false);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [analyzeError, setAnalyzeError] = useState<string | null>(null);
  const [analyzeSuccess, setAnalyzeSuccess] = useState<string | null>(null);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [saveSuccess, setSaveSuccess] = useState<string | null>(null);
  const [selectedFileName, setSelectedFileName] = useState<string | null>(null);
  const [previewUrl, setPreviewUrl] = useState("");
  const [analysisImageUrl, setAnalysisImageUrl] = useState(initialValue.image_url);
  const [dragActive, setDragActive] = useState(false);
  const [urlFallbackVisible, setUrlFallbackVisible] = useState(false);

  const syncTags = (
    nextStyleTags: string,
    nextSeasonTags: string,
    nextOccasionTags: string,
  ) => {
    setForm((current) => ({
      ...current,
      style_tags: parseTagString(nextStyleTags),
      season_tags: parseTagString(nextSeasonTags),
      occasion_tags: parseTagString(nextOccasionTags),
    }));
  };

  const handleFileSelection = (files: FileList | null) => {
    const file = files?.[0];
    if (!file) return;

    const validationError = validateImageFile(file);
    if (validationError) {
      setUploadError(validationError);
      setAnalyzeSuccess(null);
      setSaveSuccess(null);
      return;
    }

    const nextPreviewUrl = URL.createObjectURL(file);
    const derivedName = deriveItemNameFromFile(file);

    setUploadError(null);
    setAnalyzeError(null);
    setAnalyzeSuccess(null);
    setSaveError(null);
    setSaveSuccess(null);
    setSelectedFileName(file.name);
    setPreviewUrl(nextPreviewUrl);
    setAnalysisImageUrl(buildAnalyzeImageUrl(file, nextPreviewUrl));
    setForm((current) => ({
      ...current,
      image_url: nextPreviewUrl,
      name: current.name || derivedName,
    }));
  };

  const handleImageUrlChange = (value: string) => {
    setPreviewUrl("");
    setSelectedFileName(null);
    setUploadError(null);
    setAnalyzeError(null);
    setAnalyzeSuccess(null);
    setSaveSuccess(null);
    setAnalysisImageUrl(value.trim());
    setForm((current) => ({ ...current, image_url: value }));
  };

  const handleAnalyze = async () => {
    if (!onAnalyze) return;

    const nextAnalyzeImageUrl = analysisImageUrl.trim() || form.image_url.trim();
    if (!nextAnalyzeImageUrl) {
      setAnalyzeError("Please add an image before running mock analysis.");
      return;
    }

    setAnalyzing(true);
    setAnalyzeError(null);
    setAnalyzeSuccess(null);
    setSaveError(null);
    setSaveSuccess(null);

    try {
      const analyzed = await onAnalyze(nextAnalyzeImageUrl);
      setForm((current) => ({
        ...current,
        ...analyzed,
        image_url: current.image_url || analyzed.image_url,
      }));
      setStyleTags(toTagString(analyzed.style_tags));
      setSeasonTags(toTagString(analyzed.season_tags));
      setOccasionTags(toTagString(analyzed.occasion_tags));
      setAnalyzeSuccess("Mock AI tags are ready. Review them before saving.");
    } catch (caughtError) {
      setAnalyzeError(
        caughtError instanceof Error ? caughtError.message : "Analyze failed.",
      );
    } finally {
      setAnalyzing(false);
    }
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setSaveError(null);
    setSaveSuccess(null);
    try {
      await onSubmit({
        ...form,
        image_url: form.image_url.trim(),
        style_tags: parseTagString(styleTags),
        season_tags: parseTagString(seasonTags),
        occasion_tags: parseTagString(occasionTags),
      });
      setSaveSuccess(
        mode === "create"
          ? "Item saved. Redirecting to wardrobe..."
          : "Item updated successfully.",
      );
    } catch (caughtError) {
      setSaveError(caughtError instanceof Error ? caughtError.message : "Save failed.");
    }
  };

  const updateField = <Key extends keyof ClothingPayload>(
    key: Key,
    value: ClothingPayload[Key],
  ) => {
    setForm((current) => ({ ...current, [key]: value }));
  };

  const canAnalyze = Boolean((analysisImageUrl || form.image_url).trim()) && !analyzing;
  const canSubmit = Boolean(form.image_url.trim()) && !submitting;

  return (
    <form
      className="rounded-[28px] border border-ink/10 bg-white p-4 shadow-card sm:p-6"
      onSubmit={handleSubmit}
    >
      <div className="grid gap-6 xl:grid-cols-[minmax(0,0.92fr)_minmax(0,1.08fr)]">
        <ImageUploadPanel
          analyzing={analyzing}
          canAnalyze={canAnalyze}
          dragActive={dragActive}
          imageUrl={form.image_url}
          mode={mode}
          onAnalyze={onAnalyze ? () => void handleAnalyze() : undefined}
          onDragActiveChange={setDragActive}
          onFileSelect={handleFileSelection}
          onImageUrlChange={handleImageUrlChange}
          onToggleUrlFallback={() => setUrlFallbackVisible((current) => !current)}
          previewUrl={previewUrl}
          selectedFileName={selectedFileName}
          uploadError={uploadError}
          urlFallbackVisible={urlFallbackVisible}
        />

        <div className="space-y-5">
          <div className="space-y-2 rounded-[24px] bg-mist p-4">
            <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
              Metadata Editor
            </p>
            <h3 className="text-xl font-semibold text-ink">
              Review and refine clothing tags
            </h3>
            <p className="text-sm leading-6 text-ink/72">
              Mock AI can propose the first draft. You can still edit every field
              before the wardrobe record is saved.
            </p>
          </div>

          <div className="grid gap-4 md:grid-cols-2">
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) => updateField("name", event.target.value)}
              placeholder="Name"
              value={form.name}
            />
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) => updateField("color", event.target.value)}
              placeholder="Color"
              value={form.color}
            />
            <select
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) =>
                updateField("category", event.target.value as ClothingPayload["category"])
              }
              value={form.category}
            >
              {clothingCategories.map((category) => (
                <option key={category} value={category}>
                  {category}
                </option>
              ))}
            </select>
            <select
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) =>
                updateField(
                  "thickness",
                  event.target.value as ClothingPayload["thickness"],
                )
              }
              value={form.thickness}
            >
              {clothingThicknessOptions.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) =>
                updateField(
                  "min_temperature",
                  event.target.value ? Number(event.target.value) : null,
                )
              }
              placeholder="Min temperature"
              type="number"
              value={form.min_temperature ?? ""}
            />
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) =>
                updateField(
                  "max_temperature",
                  event.target.value ? Number(event.target.value) : null,
                )
              }
              placeholder="Max temperature"
              type="number"
              value={form.max_temperature ?? ""}
            />
          </div>

          <div className="grid gap-4 lg:grid-cols-3">
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) => {
                setStyleTags(event.target.value);
                syncTags(event.target.value, seasonTags, occasionTags);
              }}
              placeholder="Style tags, comma separated"
              value={styleTags}
            />
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) => {
                setSeasonTags(event.target.value);
                syncTags(styleTags, event.target.value, occasionTags);
              }}
              placeholder="Season tags, comma separated"
              value={seasonTags}
            />
            <input
              className="rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
              onChange={(event) => {
                setOccasionTags(event.target.value);
                syncTags(styleTags, seasonTags, event.target.value);
              }}
              placeholder="Occasion tags, comma separated"
              value={occasionTags}
            />
          </div>

          <label className="flex items-center gap-3 rounded-2xl border border-ink/10 px-4 py-3 text-sm text-ink/75">
            <input
              checked={form.rain_suitable}
              onChange={(event) => updateField("rain_suitable", event.target.checked)}
              type="checkbox"
            />
            Rain suitable
          </label>

          <textarea
            className="min-h-28 w-full rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
            onChange={(event) => updateField("notes", event.target.value)}
            placeholder="Notes"
            value={form.notes}
          />

          {analyzeSuccess ? (
            <p className="rounded-2xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700">
              {analyzeSuccess}
            </p>
          ) : null}

          {analyzeError ? (
            <p className="rounded-2xl bg-red-50 px-4 py-3 text-sm text-red-700">
              {analyzeError}
            </p>
          ) : null}

          {saveSuccess ? (
            <p className="rounded-2xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700">
              {saveSuccess}
            </p>
          ) : null}

          {saveError ? (
            <p className="rounded-2xl bg-red-50 px-4 py-3 text-sm text-red-700">
              {saveError}
            </p>
          ) : null}

          <button
            className="w-full rounded-full bg-ink px-5 py-3 text-sm font-medium text-white disabled:opacity-60 sm:w-auto"
            disabled={!canSubmit}
            type="submit"
          >
            {submitting
              ? mode === "create"
                ? "Saving..."
                : "Updating..."
              : mode === "create"
                ? "Save item"
                : "Update item"}
          </button>
        </div>
      </div>
    </form>
  );
}

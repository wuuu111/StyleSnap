type ImageUploadPanelProps = {
  analyzing: boolean;
  canAnalyze: boolean;
  dragActive: boolean;
  imageUrl: string;
  mode: "create" | "edit";
  previewUrl: string;
  selectedFileName: string | null;
  uploadError: string | null;
  urlFallbackVisible: boolean;
  onAnalyze?: () => void;
  onDragActiveChange: (active: boolean) => void;
  onFileSelect: (files: FileList | null) => void;
  onImageUrlChange: (value: string) => void;
  onToggleUrlFallback: () => void;
};

export function ImageUploadPanel({
  analyzing,
  canAnalyze,
  dragActive,
  imageUrl,
  mode,
  previewUrl,
  selectedFileName,
  uploadError,
  urlFallbackVisible,
  onAnalyze,
  onDragActiveChange,
  onFileSelect,
  onImageUrlChange,
  onToggleUrlFallback,
}: ImageUploadPanelProps) {
  const previewSrc = previewUrl || imageUrl;
  const hasPreview = Boolean(previewSrc);
  const statusText = selectedFileName
    ? `已选择：${selectedFileName}`
    : hasPreview
      ? "图片已就绪，可以直接分析或手动编辑标签。"
      : "先拍照或上传一张衣物图片，再继续分析与保存。";

  return (
    <section className="space-y-5 rounded-[28px] border border-ink/10 bg-sand p-5">
      <div className="space-y-2">
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
          {mode === "create" ? "Image Upload" : "Update Image"}
        </p>
        <h3 className="text-2xl font-semibold text-ink">
          {mode === "create" ? "Add a clothing image" : "Replace clothing image"}
        </h3>
        <p className="text-sm leading-6 text-ink/70">
          Mobile focuses on camera and album entry. Desktop supports drag-and-drop
          or direct upload. Image URL stays available only as a demo fallback.
        </p>
      </div>

      <div className="space-y-3 md:hidden">
        <label className="flex cursor-pointer items-center justify-center rounded-[22px] bg-clay px-5 py-4 text-base font-semibold text-white shadow-card">
          <input
            accept="image/*"
            capture="environment"
            className="hidden"
            onChange={(event) => onFileSelect(event.target.files)}
            type="file"
          />
          <span>📷 拍照添加</span>
        </label>
        <label className="flex cursor-pointer items-center justify-center rounded-[22px] border border-ink/15 bg-white px-5 py-4 text-base font-semibold text-ink shadow-card">
          <input
            accept="image/*"
            className="hidden"
            onChange={(event) => onFileSelect(event.target.files)}
            type="file"
          />
          <span>🖼 从相册选择</span>
        </label>
      </div>

      <div className="hidden space-y-4 md:block">
        <div
          className={`rounded-[26px] border border-dashed p-6 transition ${
            dragActive
              ? "border-clay bg-white shadow-card"
              : "border-ink/20 bg-white/80"
          }`}
          onDragEnter={(event) => {
            event.preventDefault();
            onDragActiveChange(true);
          }}
          onDragLeave={(event) => {
            event.preventDefault();
            onDragActiveChange(false);
          }}
          onDragOver={(event) => event.preventDefault()}
          onDrop={(event) => {
            event.preventDefault();
            onDragActiveChange(false);
            onFileSelect(event.dataTransfer.files);
          }}
        >
          <p className="text-lg font-semibold text-ink">Upload clothing image</p>
          <p className="mt-2 text-sm leading-6 text-ink/68">
            Drag and drop an image here, or click to upload.
          </p>
          <label className="mt-5 inline-flex cursor-pointer rounded-full bg-ink px-5 py-3 text-sm font-medium text-white">
            <input
              accept="image/*"
              className="hidden"
              onChange={(event) => onFileSelect(event.target.files)}
              type="file"
            />
            Upload from device
          </label>
        </div>
      </div>

      <div className="flex flex-wrap gap-3">
        <button
          className="rounded-full border border-ink/15 px-4 py-2 text-sm font-medium text-ink"
          onClick={onToggleUrlFallback}
          type="button"
        >
          {urlFallbackVisible ? "Hide image URL demo" : "Use image URL for demo"}
        </button>
      </div>

      {urlFallbackVisible ? (
        <div className="space-y-3 rounded-[22px] border border-ink/10 bg-white p-4">
          <div>
            <p className="text-sm font-semibold text-ink">Demo image URL fallback</p>
            <p className="mt-1 text-sm leading-6 text-ink/65">
              This stays available for MVP demos and mock keyword analysis, but it
              is not the primary upload entry.
            </p>
          </div>
          <input
            className="w-full rounded-2xl border border-ink/10 px-4 py-3 text-sm outline-none"
            onChange={(event) => onImageUrlChange(event.target.value)}
            placeholder="https://example.com/white-shirt.jpg"
            value={imageUrl}
          />
        </div>
      ) : null}

      <div className="rounded-[22px] bg-white px-4 py-3 text-sm text-ink/72">
        {statusText}
      </div>

      {uploadError ? (
        <p className="rounded-[22px] bg-red-50 px-4 py-3 text-sm text-red-700">
          {uploadError}
        </p>
      ) : null}

      <div className="overflow-hidden rounded-[26px] border border-ink/10 bg-white">
        <div className="flex items-center justify-between border-b border-ink/8 px-4 py-3">
          <p className="text-sm font-semibold text-ink">Preview</p>
          <span className="text-xs uppercase tracking-[0.2em] text-clay">
            {hasPreview ? "Ready" : "Waiting"}
          </span>
        </div>
        <div className="aspect-[4/5] bg-mist">
          {hasPreview ? (
            <img
              alt={selectedFileName ?? "Clothing preview"}
              className="h-full w-full object-cover"
              src={previewSrc}
            />
          ) : (
            <div className="flex h-full items-center justify-center px-6 text-center text-sm leading-6 text-ink/45">
              Select a clothing image to see the local preview here.
            </div>
          )}
        </div>
      </div>

      {onAnalyze ? (
        <button
          className="w-full rounded-full bg-clay px-5 py-3 text-sm font-medium text-white disabled:opacity-60"
          disabled={!canAnalyze}
          onClick={onAnalyze}
          type="button"
        >
          {analyzing ? "Analyzing..." : "Mock AI Analyze"}
        </button>
      ) : null}
    </section>
  );
}

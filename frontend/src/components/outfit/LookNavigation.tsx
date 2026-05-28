type LookNavigationProps = {
  currentIndex: number;
  total: number;
  onNext: () => void;
  onPrevious: () => void;
};

export function LookNavigation({
  currentIndex,
  total,
  onNext,
  onPrevious,
}: LookNavigationProps) {
  return (
    <div className="space-y-3 rounded-[24px] border border-ink/10 bg-white p-4">
      <div className="flex items-center justify-between gap-3">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Look Navigation
          </p>
          <p className="mt-1 text-lg font-semibold text-ink">
            Look {currentIndex + 1} / {total}
          </p>
        </div>
        <div className="flex gap-2">
          <button
            className="rounded-full border border-ink/15 px-4 py-2 text-sm font-medium text-ink disabled:opacity-40"
            disabled={currentIndex === 0}
            onClick={onPrevious}
            type="button"
          >
            上一套
          </button>
          <button
            className="rounded-full bg-ink px-4 py-2 text-sm font-medium text-white disabled:opacity-40"
            disabled={currentIndex === total - 1}
            onClick={onNext}
            type="button"
          >
            下一套
          </button>
        </div>
      </div>

      <div className="flex items-center gap-2">
        {Array.from({ length: total }).map((_, index) => (
          <span
            className={`h-2.5 rounded-full transition-all ${
              index === currentIndex ? "w-8 bg-clay" : "w-2.5 bg-ink/15"
            }`}
            key={index}
          />
        ))}
      </div>
    </div>
  );
}

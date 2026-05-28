type WarningListProps = {
  warnings: string[];
};

export function WarningList({ warnings }: WarningListProps) {
  return (
    <section className="space-y-3 rounded-[24px] border border-ink/10 bg-white p-4">
      <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
        Warnings
      </p>
      {warnings.length === 0 ? (
        <p className="rounded-2xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700">
          No obvious wearability risks for this look.
        </p>
      ) : (
        <ul className="space-y-2">
          {warnings.map((warning) => (
            <li
              className="rounded-2xl bg-amber-50 px-4 py-3 text-sm leading-6 text-amber-800"
              key={warning}
            >
              {warning}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

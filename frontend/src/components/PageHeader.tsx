type PageHeaderProps = {
  eyebrow: string;
  title: string;
  description: string;
};

export function PageHeader({ eyebrow, title, description }: PageHeaderProps) {
  return (
    <div className="space-y-3">
      <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
        {eyebrow}
      </p>
      <div className="space-y-2">
        <h2 className="text-3xl font-semibold tracking-tight text-ink">
          {title}
        </h2>
        <p className="max-w-2xl text-sm leading-6 text-ink/70 md:text-base">
          {description}
        </p>
      </div>
    </div>
  );
}

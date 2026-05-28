import { Link } from "react-router-dom";


type RecommendationStateCardProps = {
  title: string;
  description: string;
  tone?: "default" | "warning" | "error";
  actionLabel?: string;
  actionTo?: string;
  actionOnClick?: () => void;
};


const toneClasses: Record<NonNullable<RecommendationStateCardProps["tone"]>, string> = {
  default: "border-ink/10 bg-mist text-ink/75",
  warning: "border-amber-200 bg-amber-50 text-amber-800",
  error: "border-red-200 bg-red-50 text-red-700",
};


export function RecommendationStateCard({
  title,
  description,
  tone = "default",
  actionLabel,
  actionTo,
  actionOnClick,
}: RecommendationStateCardProps) {
  return (
    <div className={`rounded-[24px] border p-5 ${toneClasses[tone]}`}>
      <h4 className="text-lg font-semibold text-ink">{title}</h4>
      <p className="mt-2 text-sm leading-6">{description}</p>
      {actionLabel && actionTo ? (
        <Link
          className="mt-4 inline-flex rounded-full bg-ink px-4 py-2 text-sm font-medium text-white no-underline"
          to={actionTo}
        >
          {actionLabel}
        </Link>
      ) : null}
      {actionLabel && actionOnClick ? (
        <button
          className="mt-4 inline-flex rounded-full bg-ink px-4 py-2 text-sm font-medium text-white"
          onClick={actionOnClick}
          type="button"
        >
          {actionLabel}
        </button>
      ) : null}
    </div>
  );
}

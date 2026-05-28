import { Link } from "react-router-dom";

import { PageHeader } from "../components/PageHeader";

export function LandingPage() {
  return (
    <section className="space-y-6">
      <PageHeader
        eyebrow="Phase 5"
        title="StyleSnap now presents recommendation results as a polished, explainable outfit flow."
        description="The MVP loop is fully visible: wardrobe metadata, Weather Skill, and rule-based recommendation scoring now land in a cleaner front-end experience that is ready for screenshots and demo recording."
      />
      <div className="grid gap-4 md:grid-cols-[1.1fr_0.9fr]">
        <article className="rounded-[24px] border border-ink/10 bg-sand p-6 shadow-card">
          <h3 className="text-xl font-semibold text-ink">Core MVP loop</h3>
          <p className="mt-3 text-sm leading-6 text-ink/75">
            Add clothes, refine metadata, resolve weather context, then generate
            ranked outfit suggestions grounded in the clothes you already own.
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            <Link
              className="rounded-full bg-ink px-5 py-3 text-sm font-medium text-white no-underline"
              to="/wardrobe"
            >
              Explore wardrobe shell
            </Link>
            <Link
              className="rounded-full border border-ink/15 px-5 py-3 text-sm font-medium text-ink no-underline"
              to="/recommendation"
            >
              Open recommendation shell
            </Link>
          </div>
        </article>
        <article className="rounded-[24px] border border-ink/10 bg-white p-6">
          <h3 className="text-xl font-semibold text-ink">Current phase status</h3>
          <ul className="mt-4 space-y-3 text-sm leading-6 text-ink/75">
            <li>Backend clothes CRUD and mock analyze APIs are active.</li>
            <li>Wardrobe flows, Weather Skill, and recommendation APIs are active.</li>
            <li>Recommendation result cards, score breakdown, reasoning, and warnings are now polished for demo use.</li>
          </ul>
        </article>
      </div>
    </section>
  );
}

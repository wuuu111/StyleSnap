import { Link } from "react-router-dom";

const painPoints = [
  "每天不知道穿什么，最后总是回到固定几套安全牌。",
  "衣服其实不少，但缺少结构化整理，很难把现有衣橱真正用起来。",
  "想模仿某种风格，却不知道怎么用自己的衣服组合出接近的效果。",
  "天气一变就容易穿太热、太冷，或者忽略下雨和鞋子的实际约束。",
];

const solutionSteps = [
  "上传衣物，形成可以检索和编辑的个人数字衣橱。",
  "Weather Skill 把温度、降雨、风感和紫外线转成穿搭上下文。",
  "选择今天的场景、目标风格和额外偏好。",
  "生成 2-3 套可解释 Look，并用卡片翻页对比不同搭配。",
];

const capabilityCards = [
  {
    title: "Wardrobe Digitization",
    body: "拍照或从相册上传衣物，Mock Vision 先产出品类、颜色、风格和季节标签，用户再手动修正。",
  },
  {
    title: "Weather Skill",
    body: "把天气转成穿搭约束，例如 layering_needed、rain_protection_needed、shoe_constraints，而不是把天气当成主功能页面。",
  },
  {
    title: "Recommendation Engine",
    body: "从个人衣橱组合候选 Look，并通过 Weather Fit、Style Match、Color Harmony、Occasion Fit、User Preference 五个维度做可解释打分。",
  },
  {
    title: "Explainable Outfit Reasoning",
    body: "除了返回推荐结果，还解释为什么这套适合今天，并展示评分拆解与 warnings。",
  },
];

const demoSteps = [
  "Add clothing",
  "Review wardrobe",
  "Allow location or enter city",
  "Choose occasion and style",
  "Generate looks",
  "Swipe or switch between Look cards",
];

const roadmapRows = [
  ["Mock Vision", "Real multimodal model"],
  ["Local preview image", "Supabase Storage or S3"],
  ["Mock Weather", "Real weather API"],
  ["Rule-based scoring", "LLM + learning-to-rank"],
  ["Template explanation", "LLM stylist explanation"],
];

export function LandingPage() {
  return (
    <section className="space-y-8">
      <section className="overflow-hidden rounded-[32px] border border-ink/10 bg-ink px-6 py-8 text-white shadow-card md:px-8 md:py-10">
        <div className="grid gap-8 lg:grid-cols-[1.15fr_0.85fr] lg:items-end">
          <div className="space-y-5">
            <div className="space-y-3">
              <p className="text-xs font-semibold uppercase tracking-[0.3em] text-white/65">
                StyleSnap
              </p>
              <h2 className="max-w-3xl text-4xl font-semibold tracking-tight md:text-5xl">
                基于个人衣橱的 AI 每日穿搭助手
              </h2>
              <p className="max-w-2xl text-lg leading-8 text-white/90">
                用你已有的衣服，搭出今天最适合的 Look。
              </p>
              <p className="max-w-2xl text-sm leading-7 text-white/72 md:text-base">
                An AI outfit assistant powered by your personal wardrobe, weather
                context, style goals, and occasion needs.
              </p>
            </div>

            <div className="flex flex-wrap gap-3">
              <Link
                className="rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink no-underline"
                to="/wardrobe"
              >
                Build My Wardrobe
              </Link>
              <Link
                className="rounded-full border border-white/20 px-5 py-3 text-sm font-semibold text-white no-underline"
                to="/recommendation"
              >
                Generate Today&apos;s Look
              </Link>
            </div>
          </div>

          <div className="grid gap-3 sm:grid-cols-2">
            <article className="rounded-[24px] bg-white/10 p-4 backdrop-blur">
              <p className="text-xs uppercase tracking-[0.25em] text-white/60">
                Product loop
              </p>
              <p className="mt-2 text-sm leading-6 text-white/88">
                Upload clothing, build a wardrobe, resolve context, rank looks,
                explain why one works today.
              </p>
            </article>
            <article className="rounded-[24px] bg-white/10 p-4 backdrop-blur">
              <p className="text-xs uppercase tracking-[0.25em] text-white/60">
                AI scope
              </p>
              <p className="mt-2 text-sm leading-6 text-white/88">
                Mock vision, Weather Skill, rule-based recommendation, and
                explainable reasoning are all visible in one demo.
              </p>
            </article>
            <article className="rounded-[24px] bg-white/10 p-4 backdrop-blur sm:col-span-2">
              <p className="text-xs uppercase tracking-[0.25em] text-white/60">
                Why it matters
              </p>
              <p className="mt-2 text-sm leading-6 text-white/88">
                StyleSnap shows the full AI product loop from structured intake to
                context-aware recommendation, without depending on external keys or
                fragile demo infrastructure.
              </p>
            </article>
          </div>
        </div>
      </section>

      <section className="grid gap-4 lg:grid-cols-[0.92fr_1.08fr]">
        <article className="rounded-[28px] border border-ink/10 bg-white p-6 shadow-card">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Problem
          </p>
          <h3 className="mt-3 text-2xl font-semibold text-ink">
            日常穿搭的问题不是衣服太少，而是决策太难。
          </h3>
          <ul className="mt-5 space-y-3 text-sm leading-7 text-ink/75">
            {painPoints.map((point) => (
              <li key={point}>{point}</li>
            ))}
          </ul>
        </article>

        <article className="rounded-[28px] border border-ink/10 bg-sand p-6 shadow-card">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Solution
          </p>
          <h3 className="mt-3 text-2xl font-semibold text-ink">
            StyleSnap 把个人衣橱、天气上下文、风格目标和场景约束放进同一个 AI 决策流。
          </h3>
          <div className="mt-5 grid gap-3">
            {solutionSteps.map((step, index) => (
              <article className="rounded-[22px] bg-white p-4" key={step}>
                <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
                  Step {index + 1}
                </p>
                <p className="mt-2 text-sm leading-6 text-ink/78">{step}</p>
              </article>
            ))}
          </div>
        </article>
      </section>

      <section className="space-y-4">
        <div className="space-y-2">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            AI Capability Breakdown
          </p>
          <h3 className="text-3xl font-semibold tracking-tight text-ink">
            四个智能模块组成完整可解释的穿搭推荐闭环
          </h3>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          {capabilityCards.map((card) => (
            <article
              className="rounded-[26px] border border-ink/10 bg-white p-6 shadow-card"
              key={card.title}
            >
              <h4 className="text-xl font-semibold text-ink">{card.title}</h4>
              <p className="mt-3 text-sm leading-7 text-ink/75">{card.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="grid gap-4 lg:grid-cols-[0.95fr_1.05fr]">
        <article className="rounded-[28px] border border-ink/10 bg-white p-6 shadow-card">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Demo Flow
          </p>
          <h3 className="mt-3 text-2xl font-semibold text-ink">
            适合录屏、面试讲解和部署演示的主线
          </h3>
          <ol className="mt-5 space-y-3 text-sm leading-7 text-ink/75">
            {demoSteps.map((step, index) => (
              <li key={step}>
                {index + 1}. {step}
              </li>
            ))}
          </ol>
        </article>

        <article className="rounded-[28px] border border-ink/10 bg-white p-6 shadow-card">
          <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
            Roadmap Preview
          </p>
          <h3 className="mt-3 text-2xl font-semibold text-ink">
            MVP 的 mock 能力如何升级成真实服务
          </h3>
          <div className="mt-5 overflow-hidden rounded-[22px] border border-ink/10">
            <div className="grid grid-cols-2 bg-mist px-4 py-3 text-xs font-semibold uppercase tracking-[0.2em] text-clay">
              <span>MVP Mock Layer</span>
              <span>Future Real Service</span>
            </div>
            {roadmapRows.map(([mockLayer, realLayer]) => (
              <div
                className="grid grid-cols-2 gap-4 border-t border-ink/8 px-4 py-3 text-sm leading-6 text-ink/76"
                key={mockLayer}
              >
                <span>{mockLayer}</span>
                <span>{realLayer}</span>
              </div>
            ))}
          </div>
        </article>
      </section>

      <section className="rounded-[30px] border border-ink/10 bg-sand p-6 shadow-card md:p-8">
        <div className="flex flex-col gap-5 md:flex-row md:items-end md:justify-between">
          <div className="max-w-3xl space-y-3">
            <p className="text-xs font-semibold uppercase tracking-[0.25em] text-clay">
              Final CTA
            </p>
            <h3 className="text-3xl font-semibold tracking-tight text-ink">
              现在就从衣橱开始，再让 StyleSnap 给出今天最适合的 Look。
            </h3>
            <p className="text-sm leading-7 text-ink/75">
              这个 Demo 展示的是完整 AI 产品闭环，而不是单点页面效果。你可以先录入衣物，再体验 Weather Skill、推荐引擎和可解释结果卡片。
            </p>
          </div>
          <div className="flex flex-wrap gap-3">
            <Link
              className="rounded-full bg-ink px-5 py-3 text-sm font-semibold text-white no-underline"
              to="/wardrobe/new"
            >
              Add Clothing
            </Link>
            <Link
              className="rounded-full border border-ink/15 px-5 py-3 text-sm font-semibold text-ink no-underline"
              to="/recommendation"
            >
              Generate Today&apos;s Look
            </Link>
          </div>
        </div>
      </section>
    </section>
  );
}

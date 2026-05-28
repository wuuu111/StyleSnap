import { NavLink, Outlet } from "react-router-dom";

import { classNames } from "../utils/classNames";

const navItems = [
  { label: "Home", to: "/" },
  { label: "Wardrobe", to: "/wardrobe" },
  { label: "Recommend", to: "/recommendation" },
];

export function AppShell() {
  return (
    <div className="min-h-screen px-4 py-6 text-ink sm:px-6">
      <div className="mx-auto flex min-h-[calc(100vh-3rem)] max-w-5xl flex-col gap-6 rounded-[28px] border border-white/60 bg-white/60 p-4 shadow-card backdrop-blur md:p-8">
        <header className="flex flex-col gap-5 rounded-[24px] bg-ink px-5 py-5 text-white md:flex-row md:items-center md:justify-between">
          <div className="max-w-3xl">
            <p className="text-sm uppercase tracking-[0.3em] text-white/70">
              StyleSnap
            </p>
            <h1 className="mt-2 text-2xl font-semibold tracking-tight md:text-3xl">
              基于个人衣橱的 AI 每日穿搭助手
            </h1>
            <p className="mt-2 text-sm leading-6 text-white/85">
              用你已有的衣服，搭出今天最适合的 Look。
            </p>
            <p className="mt-1 text-sm leading-6 text-white/68">
              An AI outfit assistant powered by your personal wardrobe, weather
              context, style goals, and occasion needs.
            </p>
          </div>
          <nav className="flex flex-wrap gap-2">
            {navItems.map((item) => (
              <NavLink
                key={item.to}
                className={({ isActive }) =>
                  classNames(
                    "rounded-full px-4 py-2 text-sm font-medium transition-colors",
                    isActive
                      ? "bg-white text-ink"
                      : "bg-white/10 text-white/85 hover:bg-white/20",
                  )
                }
                to={item.to}
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </header>
        <main className="flex-1">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

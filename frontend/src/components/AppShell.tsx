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
        <header className="flex flex-col gap-5 rounded-[24px] bg-ink px-5 py-6 text-white md:flex-row md:items-end md:justify-between">
          <div className="max-w-2xl">
            <p className="text-sm uppercase tracking-[0.3em] text-white/70">
              StyleSnap
            </p>
            <h1 className="mt-2 text-3xl font-semibold tracking-tight md:text-4xl">
              An AI Outfit Assistant Powered by Your Personal Wardrobe
            </h1>
            <p className="mt-3 text-sm leading-6 text-white/80 md:text-base">
              用你已有的衣服，搭出今天最适合的 Look。
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

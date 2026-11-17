"use client";

import React, { useEffect, useState } from "react";

export const ThemeSwitch: React.FC = () => {
  const [theme, setTheme] = useState<"obsidian" | "default">("obsidian");

  useEffect(() => {
    const saved = localStorage.getItem("workhorse_theme") as
      "obsidian" | "default" | null;
    if (saved) {
      setTheme(saved);
      document.documentElement.setAttribute("data-theme", saved);
    } else {
      document.documentElement.setAttribute("data-theme", "obsidian");
    }
  }, []);

  const toggleTheme = () => {
    const next = theme === "obsidian" ? "default" : "obsidian";
    setTheme(next);
    localStorage.setItem("workhorse_theme", next);
    document.documentElement.setAttribute("data-theme", next);
  };

  return (
    <button
      onClick={toggleTheme}
      type="button"
      aria-label="Toggle theme switch"
      className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border text-xs font-mono transition-colors border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-surface-elevated)] text-[var(--text-primary)]"
    >
      <span
        className="w-2.5 h-2.5 rounded-full inline-block"
        style={{
          backgroundColor: theme === "obsidian" ? "#FFB000" : "#10b981",
        }}
      />
      <span>{theme === "obsidian" ? "Obsidian & Neon" : "Cyberpunk"}</span>
    </button>
  );
};

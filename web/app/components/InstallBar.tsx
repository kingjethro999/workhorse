"use client";

import React, { useState } from "react";

export const InstallBar: React.FC = () => {
  const [copied, setCopied] = useState<boolean>(false);
  const [tab, setTab] = useState<"curl" | "powershell" | "git">("curl");

  const commands = {
    curl: "curl -fsSL https://raw.githubusercontent.com/kingjethro999/workhorse/main/install.sh | bash",
    powershell: "irm https://raw.githubusercontent.com/kingjethro999/workhorse/main/install.ps1 | iex",
    git: "git clone https://github.com/kingjethro999/workhorse.git ~/.local/share/workhorse && cd ~/.local/share/workhorse && ./install.sh",
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(commands[tab]);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex flex-col items-center gap-3 max-w-2xl mx-auto w-full">
      {/* Shell Tabs */}
      <div className="flex gap-2">
        {(["curl", "powershell", "git"] as const).map((t) => (
          <button
            key={t}
            onClick={() => setTab(t)}
            type="button"
            className={`px-3 py-1 rounded text-xs font-mono transition-colors ${
              tab === t
                ? "bg-[var(--accent-local)] text-black font-bold"
                : "bg-[var(--bg-surface)] text-[var(--text-muted)] hover:text-[var(--text-primary)]"
            }`}
          >
            {t === "curl" ? "Linux / macOS" : t === "powershell" ? "Windows PowerShell" : "From Source"}
          </button>
        ))}
      </div>

      {/* Command Pill */}
      <div className="w-full flex items-center justify-between bg-[var(--bg-surface)] border border-[var(--border-color)] rounded-xl p-2 pl-4 shadow-xl">
        <div className="flex items-center gap-2 font-mono text-xs sm:text-sm text-[var(--accent-local)] overflow-x-auto select-all pr-2">
          <span className="text-zinc-500 select-none">$</span>
          <span className="whitespace-nowrap">{commands[tab]}</span>
        </div>
        <button
          onClick={handleCopy}
          type="button"
          aria-label="Copy installation command"
          className={`shrink-0 px-4 py-2 rounded-lg font-mono text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
            copied
              ? "bg-[var(--accent-success)] text-black scale-105"
              : "bg-[var(--accent-cloud)] text-white hover:opacity-90 shadow-md"
          }`}
        >
          {copied ? "✓ Copied" : "Copy"}
        </button>
      </div>

      <p className="text-xs text-[var(--text-muted)] font-mono text-center">
        Universal Tri-Alias: Automatically symlinks <code className="text-[var(--accent-local)]">workhorse</code>, <code className="text-[var(--accent-local)]">workhouse</code>, and <code className="text-[var(--accent-local)]">wh</code> into <code className="text-zinc-400">~/.local/bin</code>.
      </p>
    </div>
  );
};

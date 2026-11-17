"use client";

import React, { useState } from "react";

interface ProviderTier {
  id: string;
  name: string;
  type: "local" | "cloud" | "gateway";
  model: string;
  latency: string;
  badgeColor: string;
  desc: string;
}

const TIERS: ProviderTier[] = [
  {
    id: "ollama",
    name: "1. Local Ollama Daemon",
    type: "local",
    model: "llama3.2:1b / deepseek-v4.1",
    latency: "< 80ms TTFT",
    badgeColor: "#10B981",
    desc: "Runs 100% on-device. Zero cloud costs, private workspace operations, and automatic offline fallback anchor.",
  },
  {
    id: "groq",
    name: "2. Groq LPUs",
    type: "cloud",
    model: "openai/gpt-oss-120b",
    latency: "450 tokens/sec",
    badgeColor: "#FFB000",
    desc: "Ultra-fast LPU inference for high-velocity code expansion and complex multi-file refactoring.",
  },
  {
    id: "nvidia",
    name: "3. Nvidia NIM",
    type: "cloud",
    model: "nemotron-3.5-super-vl-120b",
    latency: "Enterprise TensorRT",
    badgeColor: "#2563EB",
    desc: "Heavyweight reasoning and vision processing for high-order architectural planning and auditing.",
  },
  {
    id: "gemini",
    name: "4. Google Gemini 2.5",
    type: "cloud",
    model: "gemini-2.5-flash",
    latency: "1M+ context window",
    badgeColor: "#38bdf8",
    desc: "Massive repository context ingestion, long-form documentation synthesis, and live web grounding.",
  },
  {
    id: "openrouter",
    name: "5. OpenRouter Gateway",
    type: "gateway",
    model: "z-ai/glm-5.3-prime",
    latency: "Global Router",
    badgeColor: "#a855f7",
    desc: "Dynamic multi-cloud failover anchor ensuring 5 full retry cycles with prompt reformulation before returning errors.",
  },
];

export const ResilienceRingVisualizer: React.FC = () => {
  const [selectedId, setSelectedId] = useState<string>("ollama");
  const selected = TIERS.find((t) => t.id === selectedId) || TIERS[0];

  return (
    <div className="w-full max-w-4xl mx-auto rounded-2xl border border-[var(--border-color)] bg-[var(--bg-surface)] p-6 shadow-xl">
      <div className="text-center mb-6">
        <h3 className="text-xl font-bold text-[var(--text-primary)]">The 5-Cycle Infinite Resilience Ring</h3>
        <p className="text-sm text-[var(--text-muted)] mt-1">
          Workhorse never fails prematurely. It traverses local and cloud clusters up to 5 full cycles.
        </p>
      </div>

      {/* Grid of Nodes */}
      <div className="grid grid-cols-1 sm:grid-cols-5 gap-3 mb-6">
        {TIERS.map((tier) => {
          const isSelected = tier.id === selectedId;
          return (
            <button
              key={tier.id}
              onClick={() => setSelectedId(tier.id)}
              type="button"
              className={`p-3 rounded-xl border text-left transition-all duration-200 ${
                isSelected
                  ? "border-[var(--accent-local)] bg-[var(--bg-surface-elevated)] scale-102 shadow-lg"
                  : "border-[var(--border-color)] bg-[var(--bg-primary)] hover:border-zinc-700"
              }`}
            >
              <div className="flex items-center gap-2 mb-1">
                <span
                  className="w-2.5 h-2.5 rounded-full inline-block"
                  style={{ backgroundColor: tier.badgeColor }}
                />
                <span className="text-xs font-bold text-[var(--text-primary)] truncate">{tier.name.split(". ")[1]}</span>
              </div>
              <div className="text-[11px] font-mono text-[var(--text-muted)] truncate">{tier.model.split("/")[0]}</div>
              <div className="text-[10px] font-mono text-[var(--accent-local)] mt-2 font-semibold">{tier.latency}</div>
            </button>
          );
        })}
      </div>

      {/* Detail Pane for Selected Node */}
      <div className="rounded-xl border border-[var(--border-color)] bg-[var(--bg-primary)] p-4 flex flex-col sm:flex-row items-start justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span
              className="w-3 h-3 rounded-full inline-block"
              style={{ backgroundColor: selected.badgeColor }}
            />
            <h4 className="font-bold text-base text-[var(--text-primary)]">{selected.name}</h4>
            <span className="text-xs font-mono px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 uppercase">
              {selected.type}
            </span>
          </div>
          <p className="text-xs sm:text-sm text-[var(--text-muted)] mt-2 max-w-xl leading-relaxed">
            {selected.desc}
          </p>
        </div>

        <div className="shrink-0 flex flex-col gap-1 text-right font-mono text-xs">
          <span className="text-zinc-500">Model:</span>
          <span className="text-[var(--text-primary)] font-bold">{selected.model}</span>
          <span className="text-zinc-500 mt-1">Throughput:</span>
          <span className="text-[var(--accent-success)] font-semibold">{selected.latency}</span>
        </div>
      </div>
    </div>
  );
};

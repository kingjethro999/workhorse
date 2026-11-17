"use client";

import React, { useState } from "react";

export const TerminalSimulator: React.FC = () => {
  const [accordionOpen, setAccordionOpen] = useState<boolean>(true);

  return (
    <div className="w-full max-w-4xl mx-auto rounded-xl overflow-hidden border border-[var(--border-color)] bg-[var(--bg-primary)] shadow-2xl font-mono text-sm">
      {/* Top Header Bar */}
      <div className="bg-[var(--bg-surface)] px-4 py-2.5 border-b border-[var(--border-color)] flex items-center justify-between text-xs text-[var(--text-muted)]">
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-red-500/80 inline-block" />
          <span className="w-3 h-3 rounded-full bg-yellow-500/80 inline-block" />
          <span className="w-3 h-3 rounded-full bg-green-500/80 inline-block" />
          <span className="ml-2 font-bold text-[var(--accent-local)]">WORKHORSE WORKSTATION</span>
        </div>
        <div className="flex items-center gap-3 text-[11px]">
          <span className="bg-blue-950/80 text-blue-300 px-2 py-0.5 rounded border border-blue-800/60">
            MODE: auto:auto
          </span>
          <span className="bg-emerald-950/80 text-emerald-300 px-2 py-0.5 rounded border border-emerald-800/60">
            OLLAMA: UP
          </span>
          <span className="text-zinc-500 hidden sm:inline">~/Desktop/promptdock</span>
        </div>
      </div>

      {/* Main Split Layout */}
      <div className="grid grid-cols-1 md:grid-cols-12 min-h-[380px]">
        {/* Left Sidebar: Workspace Explorer */}
        <div className="md:col-span-4 border-r border-[var(--border-color)] p-3 bg-[var(--bg-surface)] text-xs">
          <div className="text-[var(--text-muted)] font-bold mb-2 flex items-center justify-between">
            <span>📂 WORKSPACE</span>
            <div className="flex gap-1 text-[10px]">
              <span className="bg-[var(--accent-local)] text-black px-1.5 py-0.5 rounded font-semibold">New</span>
              <span className="bg-zinc-800 px-1.5 py-0.5 rounded text-zinc-300">Edit</span>
            </div>
          </div>
          <div className="space-y-1 text-[var(--text-muted)]">
            <div className="text-[var(--accent-local)]">v promptdock/</div>
            <div className="pl-3 text-zinc-400">📁 src/</div>
            <div className="pl-6 text-zinc-500">📄 index.ts</div>
            <div className="pl-6 text-zinc-500">📄 routes.ts</div>
            <div className="pl-3 text-[var(--accent-success)] font-medium">📄 README.md (Modified)</div>
            <div className="pl-3 text-zinc-500">⚙️ package.json</div>
            <div className="pl-3 text-zinc-500">⚙️ tsconfig.json</div>
          </div>
        </div>

        {/* Center Main: Conversation Stream */}
        <div className="md:col-span-8 p-4 flex flex-col justify-between bg-[var(--bg-primary)]">
          <div className="space-y-4">
            {/* User Message */}
            <div className="bg-[var(--bg-surface)] border-l-2 border-[var(--accent-local)] p-2.5 rounded-r text-[var(--text-primary)]">
              <span className="text-[var(--accent-local)] font-bold text-xs block mb-1">User</span>
              tell me about this repo and edit readme, make it more detailed
            </div>

            {/* Live Streaming ThoughtAccordion */}
            <div className="border border-[var(--accent-local)]/40 bg-[var(--accent-local)]/5 rounded overflow-hidden">
              <button
                onClick={() => setAccordionOpen(!accordionOpen)}
                type="button"
                className="w-full text-left px-3 py-1.5 bg-[var(--accent-local)]/10 text-[var(--accent-local)] font-bold text-xs flex items-center justify-between hover:bg-[var(--accent-local)]/20 transition-colors"
              >
                <span>{accordionOpen ? "▼" : "▶"} Reasoning &amp; Chunk Progress (4 steps)</span>
                <span className="text-[10px] opacity-70 font-normal">Click to toggle</span>
              </button>

              {accordionOpen && (
                <div className="p-3 text-xs text-[var(--accent-local)]/90 space-y-1 font-mono border-t border-[var(--accent-local)]/20 bg-[var(--bg-primary)]">
                  <div>[*] Scanning repository structure in ~/Desktop/promptdock...</div>
                  <div>[*] Ingested chunk 1/1: package.json (Detected Express &amp; TypeScript)</div>
                  <div>[*] auto:auto Dispatcher: Promoted to [GROQ: openai/gpt-oss-120b]</div>
                  <div className="text-[var(--accent-success)]">[OK] In-place write complete: README.md updated (148 lines).</div>
                </div>
              )}
            </div>

            {/* Agent Completion Card */}
            <div className="bg-[var(--bg-surface)] border-l-2 border-[var(--accent-cloud)] p-2.5 rounded-r text-[var(--text-primary)] text-xs">
              <span className="text-[var(--accent-cloud)] font-bold block mb-1">Agent (GROQ | gpt-oss-120b)</span>
              I analyzed <strong>promptdock</strong> and expanded `README.md` in place with detailed setup instructions, architecture breakdown, and REST API documentation. Created backup in `.workhorse_backups/README.md.bak`.
            </div>
          </div>

          {/* Bottom Simulated Input */}
          <div className="mt-4 pt-2 border-t border-[var(--border-color)] flex items-center text-xs text-[var(--text-muted)]">
            <span className="text-[var(--accent-local)] mr-2 font-bold">&gt;</span>
            <span className="text-zinc-500">Ask Workhorse or edit files... (Enter to send)</span>
          </div>
        </div>
      </div>
    </div>
  );
};

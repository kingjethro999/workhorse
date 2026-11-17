import React from "react";
import Link from "next/link";
import { AnimatedHorse } from "./components/AnimatedHorse";
import { TerminalSimulator } from "./components/TerminalSimulator";
import { InstallBar } from "./components/InstallBar";
import { ResilienceRingVisualizer } from "./components/ResilienceRingVisualizer";
import { ThemeSwitch } from "./components/ThemeSwitch";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)] transition-colors duration-200">
      {/* Global Header */}
      <header className="sticky top-0 z-50 backdrop-blur-xl bg-[var(--bg-primary)]/80 border-b border-[var(--border-color)] px-6 py-3.5 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-[var(--accent-local)] text-black font-black flex items-center justify-center font-mono text-sm shadow-md">
            WH
          </div>
          <div>
            <span className="font-mono font-bold tracking-tight text-sm sm:text-base">
              WORKHORSE
            </span>
            <span className="hidden sm:inline-block ml-2 text-[10px] font-mono px-2 py-0.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-muted)]">
              v0.0.1
            </span>
          </div>
        </div>

        <nav className="hidden md:flex items-center gap-6 text-xs font-mono text-[var(--text-muted)]">
          <a
            href="#features"
            className="hover:text-[var(--text-primary)] transition-colors"
          >
            Features
          </a>
          <a
            href="#terminal"
            className="hover:text-[var(--text-primary)] transition-colors"
          >
            Interactive TUI
          </a>
          <a
            href="#resilience"
            className="hover:text-[var(--text-primary)] transition-colors"
          >
            5-Cycle Ring
          </a>
          <a
            href="#skills"
            className="hover:text-[var(--text-primary)] transition-colors"
          >
            Skills &amp; MCP
          </a>
        </nav>

        <div className="flex items-center gap-3">
          <ThemeSwitch />
          <a
            href="https://github.com/kingjethro999/workhorse"
            target="_blank"
            rel="noopener noreferrer"
            className="px-3 py-1.5 rounded-lg border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-surface-elevated)] text-xs font-mono transition-colors"
          >
            GitHub
          </a>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex flex-col gap-20 px-4 sm:px-8 max-w-6xl mx-auto w-full py-12">
        {/* Hero Section */}
        <section className="flex flex-col lg:flex-row items-center gap-10">
          <div className="flex-1 flex flex-col gap-6 text-center lg:text-left">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[var(--accent-local)]/30 bg-[var(--accent-local)]/10 text-[var(--accent-local)] text-xs font-mono w-fit mx-auto lg:mx-0">
              <span className="w-1.5 h-1.5 rounded-full bg-[var(--accent-local)] animate-ping" />
              Hybrid Terminal AI Workstation &amp; Autonomous Agent
            </div>

            <h1 className="text-3xl sm:text-5xl font-black tracking-tight leading-tight">
              Turning even the Smallest Models to a{" "}
              <span className="text-[var(--accent-local)]">Work Horse</span>
            </h1>

            <p className="text-sm sm:text-base text-[var(--text-muted)] leading-relaxed max-w-xl mx-auto lg:mx-0">
              An enterprise-grade, local-first terminal workstation with
              zero-friction tri-alias access (<code>workhorse</code>,{" "}
              <code>workhouse</code>, <code>wh</code>). Active repository
              operations, 5-Cycle model resilience ring, and live streaming
              thought accordions.
            </p>

            <div className="w-full pt-2">
              <InstallBar />
            </div>
          </div>

          <div className="flex-1 w-full max-w-md lg:max-w-none">
            <AnimatedHorse />
          </div>
        </section>

        {/* Core Architectural Tenets Grid */}
        <section id="features" className="space-y-6">
          <div className="text-center max-w-2xl mx-auto">
            <h2 className="text-2xl font-bold tracking-tight">
              Core Architectural Tenets
            </h2>
            <p className="text-xs sm:text-sm text-[var(--text-muted)] mt-1">
              Built for production developers who demand speed, transparency,
              and resilient execution.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="p-5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-surface)] flex flex-col gap-2">
              <span className="text-2xl">⚡</span>
              <h3 className="font-bold text-sm text-[var(--text-primary)]">
                Tri-Alias Ubiquity
              </h3>
              <p className="text-xs text-[var(--text-muted)] leading-relaxed">
                Run <code>workhorse</code>, <code>workhouse</code>, or{" "}
                <code>wh</code> anywhere on your machine. Anchors instantly to
                caller directory with dedicated virtualenv isolation.
              </p>
            </div>

            <div className="p-5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-surface)] flex flex-col gap-2">
              <span className="text-2xl">🛠️</span>
              <h3 className="font-bold text-sm text-[var(--text-primary)]">
                Active Repo Operator
              </h3>
              <p className="text-xs text-[var(--text-muted)] leading-relaxed">
                No restrictive sandboxes. Directly inspects, parses AST, and
                edits files in-place with automatic safety backups saved to{" "}
                <code>.workhorse_backups/</code>.
              </p>
            </div>

            <div className="p-5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-surface)] flex flex-col gap-2">
              <span className="text-2xl">🔄</span>
              <h3 className="font-bold text-sm text-[var(--text-primary)]">
                5-Cycle Resilience Ring
              </h3>
              <p className="text-xs text-[var(--text-muted)] leading-relaxed">
                Traverses Local Ollama &rarr; Groq &rarr; Nvidia &rarr; Gemini
                &rarr; OpenRouter for 5 complete cycles before reporting errors.
                Offline transparent fallback.
              </p>
            </div>

            <div className="p-5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-surface)] flex flex-col gap-2">
              <span className="text-2xl"> раскрывается</span>
              <h3 className="font-bold text-sm text-[var(--text-primary)]">
                Live Thought Accordions
              </h3>
              <p className="text-xs text-[var(--text-muted)] leading-relaxed">
                No opaque spinners or black boxes. Streams token-by-token
                reasoning, chunk progress, tool calls, and diff previews inside
                collapsible dropdowns.
              </p>
            </div>
          </div>
        </section>

        {/* Interactive Terminal Simulator */}
        <section id="terminal" className="space-y-6">
          <div className="text-center max-w-2xl mx-auto">
            <h2 className="text-2xl font-bold tracking-tight">
              Interactive Terminal Simulator
            </h2>
            <p className="text-xs sm:text-sm text-[var(--text-muted)] mt-1">
              Experience the Textual TUI workstation running in{" "}
              <code>~/Desktop/promptdock</code>.
            </p>
          </div>

          <TerminalSimulator />
        </section>

        {/* 5-Cycle Resilience Ring Visualizer */}
        <section id="resilience" className="space-y-6">
          <ResilienceRingVisualizer />
        </section>

        {/* Cross-Agent Skills & MCP Integration */}
        <section
          id="skills"
          className="p-8 rounded-2xl border border-[var(--border-color)] bg-[var(--bg-surface)] space-y-6"
        >
          <div className="max-w-2xl">
            <span className="text-xs font-mono text-[var(--accent-local)] uppercase tracking-wider font-bold">
              Universal Interoperability
            </span>
            <h2 className="text-2xl font-bold tracking-tight mt-1">
              Cross-Agent Skills Sharing &amp; MCP Hub
            </h2>
            <p className="text-xs sm:text-sm text-[var(--text-muted)] mt-2 leading-relaxed">
              Workhorse automatically discovers and borrows custom skills from
              Claude Code (<code>~/.claude/skills/</code>), Antigravity (
              <code>~/.gemini/antigravity/skills/</code>), and Cursor (
              <code>~/.cursor/skills/</code>). Connect any Model Context
              Protocol (MCP) server directly via the interactive hub modal (
              <code>F6</code>).
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 font-mono text-xs">
            <div className="p-4 rounded-xl border border-[var(--border-color)] bg-[var(--bg-primary)]">
              <span className="text-[var(--accent-local)] font-bold block mb-1">
                Harvested Skills
              </span>
              <ul className="space-y-1 text-zinc-400">
                <li>• a11y-debugging</li>
                <li>• motion-planning</li>
                <li>• modern-web-guidance</li>
                <li>• test-driven-development</li>
              </ul>
            </div>

            <div className="p-4 rounded-xl border border-[var(--border-color)] bg-[var(--bg-primary)]">
              <span className="text-[var(--accent-cloud)] font-bold block mb-1">
                Live Web Intelligence
              </span>
              <ul className="space-y-1 text-zinc-400">
                <li>• Firecrawl v1 Scraper</li>
                <li>• Jina AI Reader/Search</li>
                <li>• Tavily Agentic Search</li>
                <li>• You.com Intelligence</li>
              </ul>
            </div>

            <div className="p-4 rounded-xl border border-[var(--border-color)] bg-[var(--bg-primary)]">
              <span className="text-[var(--accent-success)] font-bold block mb-1">
                MCP Transports
              </span>
              <ul className="space-y-1 text-zinc-400">
                <li>• PostgreSQL MCP</li>
                <li>• Filesystem MCP</li>
                <li>• GitHub MCP</li>
                <li>• Brave Search MCP</li>
              </ul>
            </div>
          </div>
        </section>
      </main>

      {/* Global Footer */}
      <footer className="mt-16 border-t border-[var(--border-color)] bg-[var(--bg-surface)] px-6 py-10 text-xs text-[var(--text-muted)] font-mono">
        <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <span className="font-bold text-[var(--text-primary)]">
              WORKHORSE
            </span>{" "}
            — &ldquo;Turning even the Smallest Models to a Work Horse&rdquo;
          </div>

          <div className="flex items-center gap-6">
            <Link
              href="/privacy"
              className="hover:text-[var(--text-primary)] transition-colors"
            >
              Privacy Policy
            </Link>
            <Link
              href="/terms"
              className="hover:text-[var(--text-primary)] transition-colors"
            >
              Terms of Service
            </Link>
            <a
              href="https://github.com/kingjethro999/workhorse"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-[var(--text-primary)] transition-colors"
            >
              GitHub
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}

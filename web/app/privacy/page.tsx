import React from "react";
import Link from "next/link";

export const metadata = {
  title: "Privacy Policy | Workhorse",
  description: "Workhorse Privacy Policy and Data Handling Principles.",
};

export default function PrivacyPage() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 font-sans text-[var(--text-primary)]">
      <Link href="/" className="text-xs font-mono text-[var(--accent-local)] hover:underline mb-8 inline-block">
        &larr; Back to Workhorse
      </Link>
      <h1 className="text-3xl font-bold mb-4">Privacy Policy</h1>
      <p className="text-xs font-mono text-[var(--text-muted)] mb-8">Effective Date: November 2026</p>

      <section className="space-y-6 text-sm text-[var(--text-muted)] leading-relaxed">
        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">1. Local-First Architecture</h2>
          <p>
            Workhorse is built with an active working repository operator design that prioritizes on-device execution through local Ollama daemons. File reads, AST parsing, and atomic chunk mutations occur entirely within your local filesystem by default.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">2. Cloud Provider Interactions</h2>
          <p>
            When utilizing cloud routing modes (Groq, Nvidia NIM, Google Gemini, OpenRouter), prompt context and file chunks necessary to fulfill your request are transmitted over encrypted TLS connections directly to the respective model APIs using your configured API keys. Workhorse does not operate an intermediate telemetry collection broker.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">3. Web Intelligence &amp; Research</h2>
          <p>
            Live research tools (Firecrawl, Jina AI, Tavily, You.com) are executed only upon explicit user requests or when the web intelligence flag is active. Only query parameters and target URLs are shared with these research engines.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">4. Backups and Data Integrity</h2>
          <p>
            Before modifying any file in-place, Workhorse automatically creates a timestamped safety backup in the `.workhorse_backups/` directory within your active workspace. These backups remain strictly on your local disk.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">5. Contact</h2>
          <p>
            For privacy inquiries or technical auditing, visit the official repository at <a href="https://github.com/kingjethro999/workhorse" className="text-[var(--accent-local)] underline">github.com/kingjethro999/workhorse</a>.
          </p>
        </div>
      </section>
    </div>
  );
}

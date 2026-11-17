import React from "react";
import Link from "next/link";

export const metadata = {
  title: "Terms of Service | Workhorse",
  description: "Workhorse Terms of Service and Software Usage License.",
};

export default function TermsPage() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 font-sans text-[var(--text-primary)]">
      <Link href="/" className="text-xs font-mono text-[var(--accent-local)] hover:underline mb-8 inline-block">
        &larr; Back to Workhorse
      </Link>
      <h1 className="text-3xl font-bold mb-4">Terms of Service</h1>
      <p className="text-xs font-mono text-[var(--text-muted)] mb-8">Effective Date: November 2026</p>

      <section className="space-y-6 text-sm text-[var(--text-muted)] leading-relaxed">
        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">1. Software License &amp; Usage</h2>
          <p>
            Workhorse is open-source developer tooling distributed under standard open-source terms. You are free to inspect, run, modify, and distribute Workhorse in compliance with the project repository license.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">2. Active Workspace Operations</h2>
          <p>
            Workhorse performs real file mutations, directory scans, and terminal commands in the active working directory where you execute it. Users maintain responsibility for verifying code changes and managing source control branches.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">3. Third-Party API Keys &amp; Costs</h2>
          <p>
            You are responsible for obtaining and securing your own API keys for optional cloud providers and research engines. Any computational or API billing incurred through your keys remains between you and the respective third-party provider.
          </p>
        </div>

        <div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)] mb-2">4. Disclaimer of Warranty</h2>
          <p>
            Workhorse is provided &quot;as is&quot;, without warranty of any kind, express or implied. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of the software.
          </p>
        </div>
      </section>
    </div>
  );
}

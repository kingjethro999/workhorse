import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Workhorse | Universal Hybrid AI Terminal Workstation",
  description: "Turning even the Smallest Models to a Work Horse. High-performance developer workstation with 5-Cycle resilience ring and full workspace file CRUD.",
  keywords: ["AI Agent", "Terminal Workstation", "Ollama", "Groq", "Local First", "Resilience Ring", "Developer Tools"],
  authors: [{ name: "Workhorse Core Team" }],
  openGraph: {
    title: "Workhorse — Universal Terminal AI Workstation",
    description: "Turning even the Smallest Models to a Work Horse.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="obsidian">
      <head>
        <meta name="color-scheme" content="dark" />
      </head>
      <body className="min-h-screen flex flex-col">{children}</body>
    </html>
  );
}

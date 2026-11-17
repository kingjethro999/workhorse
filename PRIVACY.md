# Workhorse Privacy Policy

**Effective Date:** November 2026

## 1. Local-First Architecture

Workhorse operates directly on your local system. By default, with local Ollama models, all processing, file analysis, AST chunking, and repository modifications occur on-device with zero network transmissions.

## 2. Cloud Providers

When cloud routing is enabled (Groq, Nvidia NIM, Gemini, OpenRouter), only the prompt and necessary file chunks are sent to the user-selected provider using the user's own API keys over secure HTTPS/TLS.

## 3. Web Intelligence

Research queries to Firecrawl, Jina AI, Tavily, and You.com are initiated only when the web intelligence flag is active.

## 4. Backups

Workhorse creates local timestamped backups in `.workhorse_backups/` before performing any in-place file mutation.

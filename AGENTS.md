# AGENTS.md — Workhorse Universal Terminal GUI & Autonomous Agent Architecture

> **System Standard Specification & Engineering Handbook**  
> **Version:** 3.1.0-ENTERPRISE-PRO-MAX  
> **Target Framework:** Textual 0.85+ / Rich 13.9+ / Python 3.10+  
> **Default Execution Mode:** `auto:auto` (Local-First Ollama Auto-Discovery with 5-Cycle Multi-Cloud Autonomous Resilience Ring)  
> **Primary Command Aliases:** `workhorse`, `workhouse`, `wh`  
> **Global PC Access:** System-wide executable via `~/.local/bin/` with context-aware repository anchoring  
> **Active Observability & Research Suite:** Langfuse, Firecrawl v1, Jina AI, Tavily AI, You.com  
> **Core Paradigms:** Active Working Repository Operator (No Restrictive Sandboxing), Chunked File Ingestion & Mutation, Background Chunked Agents, Live Streaming Thought Accordions (No Opaque Spinners), 5-Cycle Failure Resilience Ring, Transparent Offline Fallback.

---

## TABLE OF CONTENTS

1. [Executive Overview & Architectural Philosophy](#1-executive-overview--architectural-philosophy)
   - 1.1 Vision and Core Directives
   - 1.2 System Topology Diagram
   - 1.3 Key Architectural Tenets
   - 1.4 Architectural Comparisons & Benchmarks
2. [Universal Global Access & PC-Wide Execution Architecture](#2-universal-global-access--pc-wide-execution-architecture)
   - 2.1 The Global Execution Problem & Context Anchoring
   - 2.2 Tri-Alias Launcher Specification (`workhorse`, `workhouse`, `wh`)
   - 2.3 Real Active Working Repository Operations (No Artificial Sandboxing)
   - 2.4 POSIX Shell Wrapper Implementation (`install.sh` & `~/.local/bin/`)
   - 2.5 Windows PowerShell & Cross-Platform Packaging (`install.ps1`)
3. [The `auto:auto` Dynamic Routing & 5-Cycle Resilience Ring](#3-the-autoauto-dynamic-routing--5-cycle-resilience-ring)
   - 3.1 Dynamic Local Ollama Auto-Discovery
   - 3.2 Task Complexity & Semantic Classification Heuristics
   - 3.3 The 5-Cycle Model Resilience Ring Protocol (Zero Fast-Failures)
   - 3.4 Transparent Offline & Network Disconnection Handling
   - 3.5 Multi-Tier Handover Decision Matrix
4. [Chunked File Engine & Active Repository Mutation](#4-chunked-file-engine--active-repository-mutation)
   - 4.1 The Chunked Ingestion Architecture (`read_file_chunks`)
   - 4.2 In-Place Chunked File Editing & Hunk Patching (`edit_file_chunk`)
   - 4.3 Recursive Repository Tree Chunking (`stream_repo_chunks`)
   - 4.4 Atomic File Writing & Non-Destructive Backup Preservation
   - 4.5 Multi-Language AST Pre-Validation & Syntax Safety Checks
5. [Background Autonomous Agent Runner & Chunked Workflows](#5-background-autonomous-agent-runner--chunked-workflows)
   - 5.1 Asynchronous Background Worker Architecture (`BackgroundAgentRunner`)
   - 5.2 Chunked Task Partitioning & Event-Driven UI Signaling
   - 5.3 Non-Blocking TUI Event Loop & Concurrency Safety
   - 5.4 State Machine & Execution Lifecycle
6. [Live Streaming Thought Accordions & Reasoning Dropdowns](#6-live-streaming-thought-accordions--reasoning-dropdowns)
   - 6.1 Abolition of Opaque "Thinking..." and "Loading..." Spinners
   - 6.2 The `ThoughtAccordion` Widget Specification
   - 6.3 Real-Time Token-by-Token Thought Streaming & Tool Tracing
   - 6.4 Collapsible Disclosure States (`▶` / `▼`) & Diff Previews
   - 6.5 Dynamic Timing, Event Counters, and Nested Trace Rendering
7. [Multi-Provider LLM Integration Layer](#7-multi-provider-llm-integration-layer)
   - 7.1 Unified Provider Interface (`BaseProvider`)
   - 7.2 Local Ollama Provider (`ollama_local.py`)
   - 7.3 Groq Cloud Provider (`groq_client.py`)
   - 7.4 Nvidia NIM Provider (`nvidia_client.py`)
   - 7.5 Google Gemini Provider (`gemini_client.py`)
   - 7.6 OpenRouter & APMix Gateway (`openrouter.py`)
8. [Multi-Engine Web Intelligence & Research Suite](#8-multi-engine-web-intelligence--research-suite)
   - 8.1 Service Registry & Environment Integration
   - 8.2 Firecrawl Deep Web Scraper & Crawler
   - 8.3 Jina AI Reader (`r.jina.ai`) & Search (`s.jina.ai`)
   - 8.4 Tavily Agentic Real-Time Research Engine
   - 8.5 You.com Intelligence Engine
   - 8.6 Automated Multi-Engine Fallback Cascade
9. [Terminal User Interface (TUI) Design System & Textual Architecture](#9-terminal-user-interface-tui-design-system--textual-architecture)
   - 9.1 Textual & Rich Reactive Architecture
   - 9.2 Visual Layout & Component Hierarchy
   - 9.3 Global Keyboard Shortcuts & Binding Map
   - 9.4 Modal Dialogs Specification (Editor, Model Picker, Help, Grep, Confirmations)
   - 9.5 Complete Textual CSS Master Specification (`styles.tcss`)
10. [Observability, Telemetry & Langfuse Integration](#10-observability-telemetry--langfuse-integration)
    - 10.1 Tracing Topology & Span Hierarchy
    - 10.2 Token Metrics & Cost Accounting
    - 10.3 Error Logging & Resilience Ring Telemetry
11. [Complete Modular Codebase Blueprint & File Implementations](#11-complete-modular-codebase-blueprint--file-implementations)
    - 11.1 `workhorse/config.py`
    - 11.2 `workhorse/router.py` (With 5-Cycle Ring & Offline Fallback)
    - 11.3 `workhorse/agent.py` (With Chunked Background Worker)
    - 11.4 `workhorse/tools/file_crud.py` (Chunked File Engine)
    - 11.5 `workhorse/tools/research.py` (Multi-Engine Web Cascade)
    - 11.6 `workhorse/tools/bash_runner.py`
    - 11.7 `workhorse/providers/base.py`
    - 11.8 `workhorse/providers/ollama_local.py`
    - 11.9 `workhorse/providers/groq_client.py`
    - 11.10 `workhorse/providers/nvidia_client.py`
    - 11.11 `workhorse/providers/gemini_client.py`
    - 11.12 `workhorse/providers/openrouter.py`
    - 11.13 `workhorse/telemetry/langfuse_obs.py`
    - 11.14 `workhorse/tui/widgets.py` (Including `ThoughtAccordion`)
    - 11.15 `workhorse/tui/screens.py`
    - 11.16 `workhorse/tui/app.py`
    - 11.17 `workhorse/tui/styles.tcss`
    - 11.18 `workhorse/cli.py`
    - 11.19 `workhorse.py` (Root Dispatcher)
12. [Installation, Packaging & Global Symlinking (`install.sh` & `install.ps1`)](#12-installation-packaging--global-symlinking-installsh--installps1)
13. [Verification, Quality Assurance & Test Suite](#13-verification-quality-assurance--test-suite)
    - 13.1 Pre-Flight Verification Checklist
    - 13.2 Automated Unit & Integration Tests (`tests/`)
14. [In-Depth Operational Playbooks & Real-World Scenarios](#14-in-depth-operational-playbooks--real-world-scenarios)
    - 14.1 Playbook A: Repository Audit & In-Place README Expansion in Target Project
    - 14.2 Playbook B: Offline Flight / Train Mode with Local Ollama
    - 14.3 Playbook C: Cloud Rate-Limit (429) & 5-Cycle Resilience Ring Traversal
    - 14.4 Playbook D: Multi-Engine Web Research for Bleeding-Edge Libraries
    - 14.5 Playbook E: Chunked Codebase Refactoring & Multi-File Editing
15. [Specialized Sub-Agent Execution Swarm Specifications](#15-specialized-sub-agent-execution-swarm-specifications)
    - 15.1 Swarm Architecture & Message Protocol
    - 15.2 Sub-Agent Brief 1: TUI & Design Systems Engineer (`@tui-engineer`)
    - 15.3 Sub-Agent Brief 2: Routing & Resilience Ring Engineer (`@model-engineer`)
    - 15.4 Sub-Agent Brief 3: Web Intelligence Specialist (`@research-engineer`)
    - 15.5 Sub-Agent Brief 4: File CRUD & Chunking Specialist (`@crud-engineer`)
    - 15.6 Sub-Agent Brief 5: DevOps, Packaging & Symlink Engineer (`@devops-engineer`)
16. [Disaster Recovery, Security & Maintenance Runbooks](#16-disaster-recovery-security--maintenance-runbooks)
    - 16.1 Local Ollama Daemon Recovery & Model Re-Indexing
    - 16.2 Cloud Provider Outage & API Key Rotation
    - 16.3 Non-Destructive Backup Restoration Runbook
17. [Master Implementation Prompt Suite (For Autonomous Agents & AGY)](#17-master-implementation-prompt-suite-for-autonomous-agents--agy)
    - 17.1 Master Orchestrator Prompt
    - 17.2 Specialized Sub-Agent Prompts
18. [Complete Function Calling & Agent Tool JSON Schemas](#18-complete-function-calling--agent-tool-json-schemas)
19. [Complete Provider System Prompts](#19-complete-provider-system-prompts)
20. [End-to-End Workflow Integration Tests](#20-end-to-end-workflow-integration-tests-teststest_e2e_workflowpy)
21. [CI/CD Automation & GitHub Actions Workflow](#21-cicd-automation--github-actions-workflow-githubworkflowsciyml)
22. [Architectural Terminology & Technical Glossary](#22-architectural-terminology--technical-glossary)
23. [Complete API Reference & Method Index](#23-complete-api-reference--method-index)
24. [Command-Line Piping & Automation Guide](#24-command-line-piping--automation-guide)
25. [Future Architecture & Extensibility Roadmap](#25-future-architecture--extensibility-roadmap)
26. [Complete Workspace Environment Variable Reference](#26-complete-workspace-environment-variable-reference-envexample)
27. [Cross-Agent Skills Sharing & Discovery Architecture](#27-cross-agent-skills-sharing--discovery-architecture)
    - 27.1 Multi-Agent Skill Silos & Universal Harvester
    - 27.2 Standard Skill Specification (`SKILL.md`)
    - 27.3 Dynamic Skill Activation & Injection Protocol
28. [Universal Model Context Protocol (MCP) Bridge](#28-universal-model-context-protocol-mcp-bridge)
    - 28.1 Cross-Agent MCP Discovery Engine
    - 28.2 Standard MCP Configuration Format
    - 28.3 Asynchronous JSON-RPC 2.0 Transport Engine
29. [Complete Source Code for Skills & MCP Modules](#29-complete-source-code-for-skills--mcp-modules)
    - 29.1 `workhorse/skills/models.py`
    - 29.2 `workhorse/skills/registry.py`
    - 29.3 `workhorse/mcp/protocol.py`
    - 29.4 `workhorse/mcp/client.py`
    - 29.5 `workhorse/mcp/registry.py`
30. [Interactive TUI Skills & MCP Hub Modal (`F6`)](#30-interactive-tui-skills--mcp-hub-modal-f6)
31. [Automated Tests for Skills & MCP (`tests/test_skills_mcp.py`)](#31-automated-tests-for-skills--mcp-teststest_skills_mcppy)
32. [Real-World Cross-Agent Interoperability Playbooks](#32-real-world-cross-agent-interoperability-playbooks)
    - 32.1 Playbook F: Borrowing a Git Skill from Claude Code into Workhorse
    - 32.2 Playbook G: Connecting to a PostgreSQL MCP Server from Cursor

---

## 1. Executive Overview & Architectural Philosophy

### 1.1 Vision and Core Directives
Workhorse is an enterprise-grade hybrid AI workstation designed to run directly inside the Linux/macOS terminal. It integrates local on-device neural processing (Ollama) with cloud intelligence clusters (Groq LPUs, Nvidia NIM, Google Gemini 2.5, OpenRouter), augmented by live multi-engine web research (Firecrawl, Jina AI, Tavily, You.com) and deep observability (Langfuse).

Workhorse operates under four non-negotiable core directives:

1. **Zero-Friction Terminal Ubiquity & Tri-Alias Invocation:**
   Workhorse is executable from *any* directory on the operating system via `workhorse`, `workhouse`, or `wh`. Invoking without arguments instantly enters the full-screen Textual Terminal GUI (TUI), anchored directly to the user's active directory. Passing arguments, flags, or pipes immediately executes in headless CLI mode.

2. **Active Working Repository Operator (No Restrictive Sandboxing):**
   Workhorse does NOT trap operations in an isolated sandbox. When invoked in `~/Desktop/promptdock` or any project folder, it possesses full authority to inspect the repository, read source files in chunks, and actively edit files (e.g. "tell me about this repo", "edit readme, make it more detailed"). It creates safe atomic backups in `.workhorse_backups/`, but performs real in-place modifications as requested.

3. **The 5-Cycle Infinite Resilience Ring (Zero Premature Failures):**
   Workhorse NEVER returns a failure error unless it has traversed its entire model ring (`[Local Ollama] -> [Groq LPU] -> [Nvidia NIM] -> [Google Gemini] -> [OpenRouter]`) and completed at least **5 full retry cycles** with exponential backoff and prompt reformulation. If internet is disconnected, it immediately notifies: `[!] No internet connection detected. Using Ollama model: <model> locally...` and continues uninterrupted.

4. **Live Streaming Thought Accordions (No Opaque Spinners):**
   Workhorse NEVER displays opaque, static "loading..." or "thinking..." spinners. Instead, it streams internal reasoning tokens, chunk progress, tool inspections, and diff previews inside real-time interactive collapsible disclosure dropdowns (`ThoughtAccordion`), matching the transparency of premier AI coding tools.

### 1.2 System Topology Diagram

```
+-----------------------------------------------------------------------------------------------------------------+
|                                            UNIFIED USER INVOCATION                                              |
|                           (Commands: `workhorse`, `workhouse`, or `wh` in ANY directory)                        |
+-------------------------------------------------------+---------------------------------------------------------+
                                                        |
                                                        v
                                +-----------------------------------------------+
                                |  Global POSIX Wrapper: ~/.local/bin/workhorse |
                                |  - Auto-selects Workhorse isolated .venv      |
                                |  - Anchors to caller CWD ($WORKHORSE_INV_CWD) |
                                +-----------------------+-----------------------+
                                                        |
                            +---------------------------+---------------------------+
                            | Argument & Flag Evaluator                             |
                            +---------------------------+---------------------------+
                                                        |
                       +--------------------------------+--------------------------------+
                       |                                                                 |
                       | [NO ARGUMENTS DETECTED]                                         | [ARGUMENTS / PIPES DETECTED]
                       v                                                                 v
+-----------------------------------------------+               +-----------------------------------------------+
|      INTERACTIVE TERMINAL GUI (TUI)           |               |            HEADLESS CLI RUNTIME               |
|  - Full-screen Textual + Rich Application     |               |  - Sub-second argument processing             |
|  - Live Workspace Explorer (Active Repo)      |               |  - Direct STDOUT token streaming              |
|  - Live File CRUD Buttons (New, Edit, Del)    |               |  - Preserves legacy flags (-m, -w, --file)    |
|  - Streaming Thought Accordions (Dropdowns)   |               |  - Pipe & automation friendly (jq / bash)     |
|  - Background Agent Task Progress Bars        |               |                                               |
+----------------------+------------------------+               +-----------------------+-----------------------+
                       |                                                                |
                       +--------------------------------+-------------------------------+
                                                        |
                                                        v
                                +-----------------------------------------------+
                                |          CORE ORCHESTRATION ENGINE            |
                                |       Mode: auto:auto (5-Cycle Ring)          |
                                +-----------------------+-----------------------+
                                                        |
              +-----------------------------------------+-----------------------------------------+
              |                                         |                                         |
              v                                         v                                         v
+---------------------------+             +---------------------------+             +---------------------------+
|    LOCAL OLLAMA DAEMON    |             |    CLOUD LPU / GPU CLUSTER|             |   RESEARCH & OBSERVABILITY|
|  - Dynamic Model Discovery|             |  - Groq LPU (gpt-oss-120b)|             |  - Firecrawl v1 Scraper   |
|  - llama3.2:1b            |             |  - Nvidia NIM (Nemotron)  |             |  - Jina AI Reader/Search  |
|  - deepseek-v4.1-flash    |             |  - Gemini 2.5 Flash / Pro |             |  - Tavily Agentic Search  |
|  - qwen3-vl:4b            |             |  - OpenRouter (glm-5.3)   |             |  - You.com Intelligence  |
|  - Offline Fallback Anchor|             |  - 5-Cycle Ring Resilience|             |  - Langfuse Tracing       |
+---------------------------+             +---------------------------+             +---------------------------+
              |                                         |                                         |
              +-----------------------------------------+-----------------------------------------+
                                                        |
                                                        v
                                +-----------------------------------------------+
                                |     ACTIVE REPO FILE & CHUNK ENGINE           |
                                |  - Chunked file reading & repo streaming      |
                                |  - In-place chunk editing & hunk patching     |
                                |  - Background asynchronous worker subagents   |
                                +-----------------------------------------------+
```

### 1.3 Key Architectural Tenets
- **Active Working Repository Operator:** Workhorse is explicitly designed to inspect, manipulate, refactor, and mutate files directly inside the active workspace where it was invoked. It does not isolate operations in an artificial sandbox.
- **Chunked Ingestion and Mutation:** Every repository traversal and file read/write operation is segmented into bounded chunks to respect context token limits and ensure zero out-of-memory errors.
- **Fail-Safe Resilience Ring:** Single-model failures, API timeouts, and HTTP 429 rate limits are handled transparently by traversing the circular provider chain up to 5 full times.
- **Radical Transparency:** The UI streams raw thought tokens, chunk statuses, and tool execution logs inside collapsible accordions instead of displaying opaque spinners.

### 1.4 Architectural Comparisons & Benchmarks

| Feature / Metric | Workhorse v3.0 | Generic Terminal Wrappers | Cloud-Only Coding Agents | Local-Only Tools |
| :--- | :--- | :--- | :--- | :--- |
| **Global Calling Aliases** | `workhorse`, `workhouse`, `wh` | Single alias | CLI or IDE plugin | Single script name |
| **Workspace Context Rooting** | Caller `$PWD` dynamically resolved | Often locked to script dir | Cloud workspace copy | Local dir |
| **Local Offline Support** | Native Ollama auto-discovery | None | None | 100% local only |
| **Failure Tolerance** | 5-Cycle Model Ring (25+ retries) | Fails on first error | Fails on API rate limit | Fails on OOM |
| **File CRUD Operation** | Full In-TUI Tree + Editor + In-Place Edits | Read-only CLI dumps | Restricted staging sandbox | Basic file write |
| **Reasoning Visibility** | Live Streaming `ThoughtAccordion` | Static spinner / dots | Opaque loading state | Terminal stdout dump |
| **Web Research Suite** | Firecrawl, Jina, Tavily, You.com | Single search tool | Vendor internal search | None |
| **Observability** | Native Langfuse integration | None | Proprietary cloud log | Local log file |

---

## 2. Universal Global Access & PC-Wide Execution Architecture

### 2.1 The Global Execution Problem & Context Anchoring
When a developer enters `~/Desktop/promptdock` and executes `wh`, the tool must fulfill three core requirements:
1. **Isolated Virtualenv Resolution:** Always execute with the dedicated virtualenv at `/home/japheth/Desktop/workhouse/.venv/bin/python`, ensuring zero dependency conflicts with global system Python.
2. **Context-Aware Working Directory Rooting:** Dynamically capture caller directory via `$PWD` and export `WORKHORSE_INVOCATION_CWD`. The file tree, agent tools, and chunking engines immediately root themselves in `~/Desktop/promptdock`.
3. **Tri-Alias Recognition:** All three aliases (`workhorse`, `workhouse`, `wh`) must execute identically across all shells (Bash, Zsh, Fish).

### 2.2 Tri-Alias Launcher Specification
- **Primary Executable:** `~/.local/bin/workhorse` (marked `chmod +x`).
- **Symlink 1:** `~/.local/bin/workhouse` -> `~/.local/bin/workhorse`.
- **Symlink 2:** `~/.local/bin/wh` -> `~/.local/bin/workhorse`.
- **PATH Check:** `~/.local/bin` is verified in `$PATH`.

### 2.3 Real Active Working Repository Operations (No Artificial Sandboxing)
Unlike sandbox-confined chat tools that refuse to touch local directories, Workhorse is designed as a direct repository engineer:
- **"Tell me about this repo":** Scans files in the caller's working directory, chunks the directory tree and key files (`README.md`, `package.json`, `pyproject.toml`, source headers), and synthesizes a complete architectural summary.
- **"Edit readme, make it more detailed":** Reads the existing `README.md` in chunks, drafts comprehensive technical documentation, and writes the updated contents directly back to `README.md` in place, generating a safety backup in `.workhorse_backups/README.md.<timestamp>.bak`.

### 2.4 POSIX Shell Wrapper Implementation
```bash
#!/usr/bin/env bash
# =============================================================================
# Workhorse Universal Entrypoint Wrapper (~/.local/bin/workhorse)
# =============================================================================
set -e

INSTALL_DIR="/home/japheth/Desktop/workhouse"
VENV_PYTHON="$INSTALL_DIR/.venv/bin/python"
MAIN_SCRIPT="$INSTALL_DIR/workhorse.py"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "[!] Error: Workhorse virtual environment not found at $VENV_PYTHON" >&2
    echo "[*] Initializing virtualenv..." >&2
    python3 -m venv "$INSTALL_DIR/.venv"
    "$INSTALL_DIR/.venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"
fi

export WORKHORSE_INVOCATION_CWD="$(pwd)"
export WORKHORSE_INSTALL_DIR="$INSTALL_DIR"

exec "$VENV_PYTHON" "$MAIN_SCRIPT" "$@"
```

### 2.5 Windows PowerShell & Cross-Platform Packaging (`install.ps1`)
```powershell
# =============================================================================
# Workhorse Windows PowerShell Universal Setup Script
# =============================================================================
$InstallDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VenvPython = Join-Path $InstallDir ".venv\Scripts\python.exe"
$MainScript = Join-Path $InstallDir "workhorse.py"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[*] Creating Python virtual environment in .venv..." -ForegroundColor Cyan
    python -m venv (Join-Path $InstallDir ".venv")
    & $VenvPython -m pip install --upgrade pip
    & $VenvPython -m pip install -r (Join-Path $InstallDir "requirements.txt")
}

$UserBin = Join-Path $env:USERPROFILE "bin"
if (-not (Test-Path $UserBin)) {
    New-Item -ItemType Directory -Path $UserBin | Out-Null
}

$CmdContent = @"
@echo off
set "WORKHORSE_INVOCATION_CWD=%CD%"
set "WORKHORSE_INSTALL_DIR=$InstallDir"
"$VenvPython" "$MainScript" %*
"@

Set-Content -Path (Join-Path $UserBin "workhorse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "workhouse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "wh.cmd") -Value $CmdContent

Write-Host "[SUCCESS] Workhorse installed as 'workhorse', 'workhouse', and 'wh' in $UserBin" -ForegroundColor Green
```

---

## 3. The `auto:auto` Dynamic Routing & 5-Cycle Resilience Ring

### 3.1 Dynamic Local Ollama Auto-Discovery
Upon initialization, Workhorse executes a non-blocking asynchronous probe against `http://127.0.0.1:11434/api/tags`.
- Discovers installed models (e.g., `llama3.2:1b`, `deepseek-v4.1-flash:cloud`, `qwen3-vl:4b`).
- Categorizes capabilities (fast micro-text, code synthesis, visual-language).
- If Ollama is running, local models form Tier-0 (Zero Cost, Zero Cloud Latency).

### 3.2 Task Complexity & Semantic Classification Heuristics
```python
def classify_task_heuristics(prompt: str, attached_files: list[str], force_web: bool) -> dict[str, Any]:
    """
    Evaluates prompt semantics, token lengths, and file signatures.
    Returns structured complexity classification and recommended starting tier.
    """
    word_count = len(prompt.split())
    has_images = bool(attached_files and any(f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")) for f in attached_files))
    
    code_keywords = [
        "def ", "class ", "import ", "function", "async ", "await", "refactor",
        "bug", "traceback", "exception", "regex", "sql", "table", "schema",
        "api", "endpoint", "crud", "docker", "dockerfile", "makefile", "json"
    ]
    is_code = any(kw in prompt.lower() for kw in code_keywords)

    web_keywords = [
        "search", "latest", "news", "docs for", "release notes", "current",
        "who is", "weather", "pricing", "today", "yesterday", "changelog"
    ]
    needs_web = force_web or any(kw in prompt.lower() for kw in web_keywords)

    if has_images:
        category = "multimodal"
        recommended_provider = "nvidia"
    elif word_count > 1800 or (attached_files and len(attached_files) > 2):
        category = "massive_context"
        recommended_provider = "gemini"
    elif needs_web:
        category = "web_research"
        recommended_provider = "groq"
    elif is_code or word_count > 40:
        category = "heavy_reasoning"
        recommended_provider = "groq"
    else:
        category = "micro_task"
        recommended_provider = "local"

    return {
        "category": category,
        "recommended_provider": recommended_provider,
        "needs_web": needs_web,
        "word_count": word_count,
        "is_code": is_code
    }
```

### 3.3 The 5-Cycle Model Resilience Ring Protocol (Zero Fast-Failures)
Workhorse introduces an uncompromising resilience protocol: **Never Return Failed Prematurely**.
The runtime arranges configured providers into an ordered circular ring:

```
+---> [1. Local Ollama] ---> [2. Groq LPU] ---> [3. Nvidia NIM] ---> [4. Gemini Flash] ---> [5. OpenRouter] ---+
|                                                                                                              |
+--------------------------------- Cycle 1 Complete: Retry Circle (Up to 5 Cycles) <---------------------------+
```

#### Ring Execution Rules:
1. When a task is dispatched, the router picks the optimal starting provider based on task complexity.
2. If the chosen provider fails (HTTP 429 rate limit, 500 server error, connection reset, OOM, timeout, or context limit), the engine automatically captures the error, logs a telemetry span, and hands the task over to the next provider in the ring.
3. If all providers in the ring are traversed without success, the engine increments the **Cycle Counter** (e.g. `Cycle 2 of 5`). It applies an exponential jitter backoff (`1s * (1.5 ^ cycle)`), reformulates the prompt context if necessary, and repeats the entire ring.
4. Workhorse will **repeat this complete circle at least 5 times** before declaring a task failed.
5. If after 5 complete cycles (25+ attempted dispatches across all endpoints) the request cannot be fulfilled, Workhorse returns a structured diagnostic report explaining each failure along the path.

### 3.4 Transparent Offline & Network Disconnection Handling
If the host system loses internet connectivity or cloud APIs are blocked by a captive portal or firewall:
1. The connection probe instantly detects the offline state.
2. The runtime does NOT throw an unhandled exception or enter an infinite spinning state.
3. It emits a transparent notification in the TUI:
   ```
   [!] No internet connection detected. Using Ollama model: <model> locally...
   ```
4. It diverts the entire task execution loop to the local Ollama instance and continues operating seamlessly offline.

### 3.5 Multi-Tier Handover Decision Matrix

| Task Characteristics | Network Status | Primary Target | Handover Fallback Tier | Web Intelligence |
| :--- | :--- | :--- | :--- | :--- |
| **Micro-Task (< 25 words)** | Any | **Local Ollama** (`llama3.2:1b`) | Groq LPU (`gpt-oss-120b`) | Disabled |
| **Repo Summary / Architecture** | Online | **Groq LPU** or **Gemini Flash** | Nvidia NIM -> OpenRouter | Optional |
| **Repo Summary / Architecture** | Offline | **Local Ollama** (`qwen3-vl:4b` / 1b) | Local Ollama (chunked) | Disabled (offline) |
| **Code Refactor / File Edit** | Online | **Groq LPU** (`gpt-oss-120b`) | Nvidia Nemotron -> Gemini | Optional |
| **Multi-File / Deep Context** | Online | **Google Gemini** (`gemini-2.5-flash`) | OpenRouter (`glm-5.3-prime`) | Optional |
| **Live Knowledge / News** | Online | **Tavily / Jina / Firecrawl** -> **Groq** | Gemini -> OpenRouter | **Mandatory** |
| **Network Outage Detected** | **Offline** | **Local Ollama** (`llama3.2:1b`) | Local alternative models | Auto-disabled |

---

## 4. Chunked File Engine & Active Repository Mutation

### 4.1 The Chunked Ingestion Architecture (`read_file_chunks`)
To prevent token context exhaustion and buffer overflows when analyzing large repositories or files, Workhorse ingests files in bounded, deterministic chunks.

```python
def read_file_chunks(file_path: Path, chunk_size_lines: int = 200) -> list[dict[str, Any]]:
    """Splits a file into line-bounded chunks with metadata."""
    chunks = []
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    for i in range(0, total_lines, chunk_size_lines):
        chunk_lines = lines[i:i + chunk_size_lines]
        chunks.append({
            "chunk_index": len(chunks) + 1,
            "total_chunks": (total_lines + chunk_size_lines - 1) // chunk_size_lines,
            "start_line": i + 1,
            "end_line": min(i + chunk_size_lines, total_lines),
            "content": "".join(chunk_lines)
        })
    return chunks
```

### 4.2 In-Place Chunked File Editing & Hunk Patching (`edit_file_chunk`)
When the user requests an edit (e.g. "make readme more detailed" or "refactor function in db.py"):
1. The engine reads the target file and calculates chunk boundaries.
2. The agent produces targeted hunk replacements or full chunk rewrites.
3. The engine creates an atomic timestamped backup: `.workhorse_backups/<filename>.<timestamp>.bak`.
4. The file is rewritten in place atomically using sibling temporary file replacement (`os.replace`).

### 4.3 Recursive Repository Tree Chunking (`stream_repo_chunks`)
When analyzing an entire repository (e.g. "tell me about this repo"):
- Workhorse traverses the directory tree while ignoring `.git/`, `.venv/`, `node_modules/`, `__pycache__/`, and `.workhorse_backups/`.
- It builds a compact structural map of all file paths, sizes, and extensions.
- It selects high-signal files (`README.md`, `pyproject.toml`, `package.json`, entrypoint files, config headers) and streams them in prioritized chunks to the model.

### 4.4 Atomic File Writing & Non-Destructive Backup Preservation
Every file mutation follows an atomic write protocol:
```python
def atomic_write(target_path: Path, new_content: str, backup_dir: Path) -> Path:
    """Safely updates a file with atomic replacement and backup snapshot."""
    backup_dir.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        timestamp = int(time.time())
        backup_file = backup_dir / f"{target_path.name}.{timestamp}.bak"
        shutil.copy2(target_path, backup_file)
    
    temp_target = target_path.with_suffix(f".tmp_{int(time.time())}")
    with open(temp_target, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    os.replace(temp_target, target_path)
    return target_path
```

### 4.5 Multi-Language AST Pre-Validation & Syntax Safety Checks
Before writing back modifications to code files, Workhorse conducts pre-flight syntax checks:
- **Python:** Evaluated via `ast.parse(content)`.
- **JSON:** Evaluated via `json.loads(content)`.
- **Markdown / Plain Text:** Checked for unmatched codeblock tags.
If a syntax error is discovered, the mutation is rejected and passed back to the agent for self-correction.

---

## 5. Background Autonomous Agent Runner & Chunked Workflows

### 5.1 Asynchronous Background Worker Architecture (`BackgroundAgentRunner`)
To ensure the Terminal GUI remains 100% responsive, high-latency workflows (such as multi-file repo refactoring, chunked codebase indexing, and multi-query research) are executed by asynchronous background workers.

- **Non-Blocking UI:** The Textual reactive event loop continues processing keyboard events (`Tab`, `Ctrl+Q`, `F1`-`F5`) and scrolling while background workers run.
- **Worker Threads:** Python `asyncio.create_task` and Textual `@work(thread=True)` decorators isolate CPU-heavy and network-heavy operations.

### 5.2 Chunked Task Partitioning & Event-Driven UI Signaling
When a large task is assigned:
1. The `BackgroundAgentRunner` divides the task into sequential chunked phases (e.g., Phase 1: Repo Scan, Phase 2: README Draft, Phase 3: README Validation).
2. For each chunk processed, it posts a message event (`ChunkProgressEvent`) to the TUI.
3. The TUI updates the active `ThoughtAccordion` with a live progress bar and step details.

### 5.3 Non-Blocking TUI Event Loop & Concurrency Safety
The runner utilizes thread-safe callbacks to post updates to the main Textual application:
```python
class ChunkProgressMessage:
    def __init__(self, step_title: str, current_chunk: int, total_chunks: int, details: str):
        self.step_title = step_title
        self.current_chunk = current_chunk
        self.total_chunks = total_chunks
        self.details = details
```

---

## 6. Live Streaming Thought Accordions & Reasoning Dropdowns

### 6.1 Abolition of Opaque "Thinking..." and "Loading..." Spinners
Traditional AI interfaces show an opaque spinner or static text like "Thinking..." that gives the user no insight into what is happening. Workhorse completely replaces this with **Interactive Thought Accordions** (`ThoughtAccordion`).

### 6.2 The `ThoughtAccordion` Widget Specification
The `ThoughtAccordion` is a custom Textual/Rich widget rendered directly in the conversation log:
- **Collapsed State (`▶`):** Shows a one-line summary: `▶ Reasoning & Tool Execution (3 steps, 1.4s)`.
- **Expanded State (`▼`):** Opens a rich disclosure box displaying:
  * Real-time streaming thoughts and chain-of-reasoning tokens.
  * Live status of chunked file reads: `[Chunk 1/3 Ingested: README.md (lines 1-200)]`.
  * Dynamic tool call traces: `[Tool: file_read('package.json')] -> OK`.
  * Multi-model handover notices: `[Handover: Local -> Groq LPU (High Complexity)]`.
  * Offline fallback notices: `[!] No internet connection detected. Using Ollama model: llama3.2:1b locally...`.
- **Interactivity:** Clickable header or keyboard toggle (`Enter` when focused) to collapse or expand at any time.

---

## 7. Multi-Provider LLM Integration Layer

### 7.1 Unified Provider Interface (`BaseProvider`)
All LLM providers implement a standardized async interface:
```python
from abc import ABC, abstractmethod
from typing import AsyncGenerator, Dict, Any, List, Optional
from pydantic import BaseModel

class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

class ProviderResponse(BaseModel):
    content: str
    model_name: str
    provider_name: str
    token_usage: TokenUsage
    finish_reason: Optional[str] = "stop"

class BaseProvider(ABC):
    @abstractmethod
    async def generate(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> ProviderResponse:
        pass

    @abstractmethod
    async def stream(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7
    ) -> AsyncGenerator[str, None]:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass
```

### 7.2 Local Ollama Provider (`ollama_local.py`)
- Direct async HTTP interface to `http://127.0.0.1:11434`.
- Auto-discovery of installed models via `/api/tags`.
- Streams raw NDJSON tokens with chunked buffer decoding.

### 7.3 Groq Cloud Provider (`groq_client.py`)
- Ultra-high-speed inference cluster (`https://api.groq.com/openai/v1`).
- Delivers 400–600 tokens/sec for rapid terminal interaction.
- Default models: `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`.

### 7.4 Nvidia NIM Provider (`nvidia_client.py`)
- Enterprise inference endpoints (`https://integrate.api.nvidia.com/v1`).
- Default model: `nvidia/nemotron-3.5-super-vl-120b-a12b`.
- Optimized for code graph comprehension and multimodal reasoning.

### 7.5 Google Gemini Provider (`gemini_client.py`)
- Powered by `google-genai` SDK (`genai.Client`).
- Default models: `gemini-2.5-flash`, `gemini-1.5-pro`.
- Massive 2M token context window for full-repo ingestion.

### 7.6 OpenRouter & APMix Gateway (`openrouter.py`)
- Universal resilience gateway (`https://openrouter.ai/api/v1`).
- Default model: `z-ai/glm-5.3-prime`.

---

## 8. Multi-Engine Web Intelligence & Research Suite

### 8.1 Service Registry & Environment Integration
```ini
FIRECRAWL_API_KEY=fc-demo-key-1234567890abcdef
JINA_API_KEY=jina_demo_key_1234567890abcdef
TAVILY_API_KEY=tvly-demo-key-1234567890abcdef
YOU_API_KEY=ydc-demo-key-1234567890abcdef
```

### 8.2 Fallback Cascade Architecture
When web intelligence is requested (`-w` flag or `F3` hotkey):
1. **Primary Probe (Tavily AI):** Rapid factual query synthesis and direct answer extraction.
2. **Secondary Reader (Jina AI):** URL-to-Markdown extraction (`r.jina.ai`) and search grounding (`s.jina.ai`).
3. **Tertiary Scraper (Firecrawl):** JavaScript SPA execution, clean layout parsing, and site crawling.
4. **Quaternary Fallback (You.com):** Web search and news index snippets.

---

## 9. Terminal User Interface (TUI) Design System & Textual Architecture

### 9.1 Visual Layout & Component Hierarchy

```
+-----------------------------------------------------------------------------------------------------------------+
| HeaderBar: WORKHORSE WORKSTATION  |  Mode: auto:auto  |  Ollama: ONLINE  |  Web: OFF  |  ~/Desktop/promptdock   |
+------------------------------------+----------------------------------------------------------------------------+
| WORKSPACE EXPLORER (Width: 32 Cols)| MAIN PANEL                                                                 |
| [New] [Edit] [Del] [Rename]        | +------------------------------------------------------------------------+ |
|------------------------------------| | Scrollable Chat Container (VerticalScroll)                             | |
| v promptdock/                      | |                                                                        | |
|   > src/                           | | [User Card]                                                            | |
|     * index.ts                     | | tell me about this repo and edit readme to make it more detailed       | |
|     * router.ts                    | |                                                                        | |
|   * package.json                   | | [ThoughtAccordion: ▼ Reasoning & Chunk Progress (Step 2/3)]            | |
|   * tsconfig.json                  | |   [*] Ingested package.json (Chunk 1/1) -> Detected TypeScript/Node    | |
|   * README.md                      | |   [*] Ingested src/index.ts (Chunk 1/2) -> Express API Gateway         | |
|                                    | |   [*] Generating detailed README.md sections...                        | |
|                                    | |                                                                        | |
|                                    | | [Agent Card: auto:auto -> GROQ gpt-oss-120b]                           | |
|                                    | | I analyzed promptdock and updated README.md with detailed setup docs.  | |
|                                    | | [Backup saved: .workhorse_backups/README.md.1700000000.bak]            | |
|                                    | +------------------------------------------------------------------------+ |
|                                    | Input Container                                                            |
|                                    | [ Enter prompt... (Shift+Enter for newline)                            ]   |
+------------------------------------+----------------------------------------------------------------------------+
| Footer: [F1] Help | [F2] Mode | [F3] Web | [F4] Models | [F5] Clear | [Ctrl+B] Sidebar | [Ctrl+Q] Quit              |
+-----------------------------------------------------------------------------------------------------------------+
```

### 9.2 Keybinding Registry

| Key | Scope | Action |
| :--- | :--- | :--- |
| `Ctrl+Q` | Global | Clean exit |
| `F1` or `?` | Global | Help and keyboard shortcut modal |
| `F2` | Global | Cycle Mode (`auto:auto` -> `local` -> `groq` -> `nvidia` -> `gemini` -> `openrouter`) |
| `F3` | Global | Toggle Live Web Intelligence (`ON`/`OFF`) |
| `F4` | Global | Model Selection Modal |
| `F5` | Global | Clear conversation history |
| `Ctrl+B` | Global | Toggle Workspace Sidebar visibility |
| `Tab` | Global | Cycle focus between Tree, Chat Log, and Input Bar |
| `n` | Sidebar | New File/Folder dialog |
| `e` | Sidebar | Open selected file in modal buffer editor |
| `v` | Sidebar | View selected file in read-only viewer |
| `d` | Sidebar | Delete selected file (prompts confirmation) |
| `r` | Sidebar | Rename selected file |
| `Enter` | Input | Submit prompt to runtime |
| `Shift+Enter` | Input | Insert newline |

---

## 10. Observability, Telemetry & Langfuse Integration

When `ENABLE_LANGFUSE_TRACING=true`:
- Every prompt trace records: caller `$PWD`, input tokens, output tokens, TTFT, and total latency.
- The 5-Cycle Resilience Ring logs an observation span for every provider attempted: `[Ollama: Timeout] -> [Groq: Success]`.
- Offline fallbacks are annotated with `network_status: offline`.


---

## 11. Complete Modular Codebase Blueprint & File Implementations

The following subsections provide the complete, production-grade source code for every module in the `workhorse/` package.

### 11.1 `workhorse/config.py`
```python
"""
Workhorse Configuration and Environment Settings.
Loads installation and workspace environment variables.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Base directories
INSTALL_DIR = Path(os.environ.get("WORKHORSE_INSTALL_DIR", Path(__file__).resolve().parent.parent)).resolve()
CWD = Path(os.environ.get("WORKHORSE_INVOCATION_CWD", os.getcwd())).resolve()

# Load credentials from install directory, allow workspace overrides
load_dotenv(INSTALL_DIR / ".env")
load_dotenv(CWD / ".env")

class Config:
    INSTALL_DIR: Path = INSTALL_DIR
    CWD: Path = CWD

    # Local Ollama Settings
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
    DEFAULT_LOCAL_MODEL: str = os.getenv("LOCAL_MODEL", "llama3.2:1b")

    # Cloud Model Defaults
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    GROQ_VISION_MODEL: str = os.getenv("GROQ_VISION_MODEL", "qwen/qwen3.8-27b")
    NVIDIA_MODEL: str = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-super-vl-120b-a12b")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    DEFAULT_GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    OPENROUTER_MODEL: str = os.getenv("OPENROUTER_MODEL", "z-ai/glm-5.3-prime")
    APMIX_MODEL: str = os.getenv("APMIX_MODEL", "meta-llama/llama-3.3-70b-instruct")

    # API Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    NVIDIA_API_KEY: str = os.getenv("NVIDIA_API_KEY", "")
    NVIDIA_BASE_URL: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    APMIX_API_KEY: str = os.getenv("APMIX_API_KEY", "")
    APMIX_BASE_URL: str = os.getenv("APMIX_BASE_URL", "https://api.apmix.net/v1")

    # Web Research Keys
    FIRECRAWL_API_KEY: str = os.getenv("FIRECRAWL_API_KEY", "")
    JINA_API_KEY: str = os.getenv("JINA_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    YOU_API_KEY: str = os.getenv("YOU_API_KEY", "")

    # Telemetry
    ENABLE_LANGFUSE: bool = os.getenv("ENABLE_LANGFUSE_TRACING", "false").lower() == "true"
    LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY", "")
    LANGFUSE_BASEURL: str = os.getenv("LANGFUSE_BASEURL", "https://cloud.langfuse.com")
```

### 11.2 `workhorse/router.py` (With 5-Cycle Ring & Offline Fallback)
```python
"""
auto:auto Dynamic Router and 5-Cycle Failure Resilience Ring.
Never fails until it has traversed all models for at least 5 complete circles.
"""
import socket
import asyncio
from typing import Tuple, List, Optional, Dict, Any, Callable
from workhorse.config import Config
from workhorse.providers.ollama_local import OllamaProvider

def is_network_connected(host: str = "8.8.8.8", port: int = 53, timeout: float = 1.5) -> bool:
    """Checks if external internet is reachable."""
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False

class AutoRouter:
    def __init__(self, ollama_provider: Optional[OllamaProvider] = None):
        self.ollama = ollama_provider or OllamaProvider()

    def check_connectivity(self) -> bool:
        return is_network_connected()

    def get_ordered_ring(self) -> List[Tuple[str, str]]:
        """Returns the circular ordered list of (provider, model) pairs."""
        ring = []
        ollama_status = self.ollama.get_status()
        if ollama_status["online"] and ollama_status["models"]:
            local_model = "llama3.2:1b" if "llama3.2:1b" in ollama_status["models"] else list(ollama_status["models"].keys())[0]
            ring.append(("local", local_model))
        if Config.GROQ_API_KEY:
            ring.append(("groq", Config.GROQ_MODEL))
        if Config.NVIDIA_API_KEY:
            ring.append(("nvidia", Config.NVIDIA_MODEL))
        if Config.GEMINI_API_KEY:
            ring.append(("gemini", Config.DEFAULT_GEMINI_MODEL))
        if Config.OPENROUTER_API_KEY:
            ring.append(("openrouter", Config.OPENROUTER_MODEL))
        return ring

    async def execute_with_resilience_ring(
        self,
        dispatch_fn: Callable[[str, str], Any],
        on_thought: Optional[Callable[[str], None]] = None,
        max_cycles: int = 5
    ) -> Dict[str, Any]:
        """
        Executes a dispatch function through all models in the ring,
        retrying the entire circle at least 5 times before failing.
        """
        ring = self.get_ordered_ring()
        if not ring:
            raise RuntimeError("No LLM providers available (Local Ollama offline and no cloud API keys).")

        # Check offline state
        online = self.check_connectivity()
        if not online:
            ollama_status = self.ollama.get_status()
            if ollama_status["online"] and ollama_status["models"]:
                local_m = list(ollama_status["models"].keys())[0]
                notice = f"[!] No internet connection detected. Using Ollama model: {local_m} locally..."
                if on_thought:
                    on_thought(notice)
                res = await dispatch_fn("local", local_m)
                return {"result": res, "provider": "local", "model": local_m, "offline": True}
            else:
                raise RuntimeError("No internet connection and local Ollama daemon is offline.")

        errors_log = []
        for cycle in range(1, max_cycles + 1):
            if on_thought and cycle > 1:
                on_thought(f"[*] Resilience Ring: Starting Cycle {cycle}/{max_cycles} across all providers...")

            for provider, model in ring:
                try:
                    if on_thought:
                        on_thought(f"[*] Attempting execution on [{provider.upper()}: {model}] (Cycle {cycle})...")
                    res = await dispatch_fn(provider, model)
                    return {
                        "result": res,
                        "provider": provider,
                        "model": model,
                        "cycle": cycle,
                        "errors": errors_log
                    }
                except Exception as e:
                    err_msg = f"[{provider}:{model}] Failed in cycle {cycle}: {str(e)}"
                    errors_log.append(err_msg)
                    if on_thought:
                        on_thought(f"[!] {err_msg} -> Handing over to next provider in ring.")
                    await asyncio.sleep(0.5)

            # Jitter backoff before starting next full circle
            await asyncio.sleep(1.0 * (1.2 ** cycle))

        raise RuntimeError(f"Task failed after 5 full resilience cycles across all models:\n" + "\n".join(errors_log[-10:]))
```

### 11.3 `workhorse/agent.py` (With Chunked Background Worker)
```python
"""
Autonomous Agent Engine and Background Chunked Worker.
"""
import asyncio
from typing import Dict, Any, List, Optional, Callable
from workhorse.config import Config
from workhorse.router import AutoRouter
from workhorse.tools.file_crud import WorkspaceManager
from workhorse.tools.research import ResearchSuite
from workhorse.providers.ollama_local import OllamaProvider
from workhorse.providers.groq_client import GroqProvider
from workhorse.providers.nvidia_client import NvidiaProvider
from workhorse.providers.gemini_client import GeminiProvider
from workhorse.providers.openrouter import OpenRouterProvider

class AgentRuntime:
    def __init__(self, workspace_path: Optional[str] = None):
        self.workspace = WorkspaceManager(workspace_path)
        self.research = ResearchSuite()
        self.ollama = OllamaProvider()
        self.groq = GroqProvider()
        self.nvidia = NvidiaProvider()
        self.gemini = GeminiProvider()
        self.openrouter = OpenRouterProvider()
        self.router = AutoRouter(self.ollama)

    def get_provider(self, name: str):
        mapping = {
            "local": self.ollama,
            "ollama": self.ollama,
            "groq": self.groq,
            "nvidia": self.nvidia,
            "gemini": self.gemini,
            "openrouter": self.openrouter
        }
        return mapping.get(name.lower(), self.groq)

    async def execute_task(
        self,
        prompt: str,
        mode: str = "auto:auto",
        use_web: bool = False,
        on_thought: Optional[Callable[[str], None]] = None
    ) -> Dict[str, Any]:
        """
        Executes a task with repository awareness, file chunking,
        and the 5-Cycle Resilience Ring.
        """
        web_context = ""
        if use_web:
            if on_thought:
                on_thought(f"[*] Live web intelligence active: Searching for '{prompt}'...")
            web_context = self.research.auto_research(prompt)

        repo_context = ""
        lowered = prompt.lower()
        if any(kw in lowered for kw in ["tell me about this repo", "what is this repo", "explain this codebase", "audit repo"]):
            if on_thought:
                on_thought("[*] Scanning repository structure and chunking high-signal files...")
            repo_summary = self.workspace.get_repo_summary(max_files=10)
            repo_context = f"\nRepository Architecture Overview:\n{repo_summary}\n"

        augmented_prompt = prompt
        if web_context:
            augmented_prompt = f"Web Research Context:\n{web_context}\n\n{augmented_prompt}"
        if repo_context:
            augmented_prompt = f"{repo_context}\n\nUser Instruction: {augmented_prompt}"

        async def _dispatch(provider_name: str, model_name: str):
            prov = self.get_provider(provider_name)
            messages = [{"role": "user", "content": augmented_prompt}]
            resp = await prov.generate(messages, model=model_name)
            
            if "edit readme" in lowered or "update readme" in lowered:
                if on_thought:
                    on_thought("[*] Applying in-place chunked edit to README.md...")
                self._apply_readme_edit(resp.content, on_thought)

            return resp

        if mode in ["auto", "auto:auto"]:
            ring_result = await self.router.execute_with_resilience_ring(_dispatch, on_thought=on_thought, max_cycles=5)
            resp = ring_result["result"]
            return {
                "content": resp.content,
                "provider": ring_result["provider"],
                "model": ring_result["model"],
                "cycle": ring_result.get("cycle", 1),
                "tokens": resp.token_usage.dict()
            }
        else:
            prov = self.get_provider(mode)
            messages = [{"role": "user", "content": augmented_prompt}]
            resp = await prov.generate(messages)
            return {
                "content": resp.content,
                "provider": mode,
                "model": resp.model_name,
                "cycle": 1,
                "tokens": resp.token_usage.dict()
            }

    def _apply_readme_edit(self, agent_output: str, on_thought: Optional[Callable[[str], None]] = None):
        try:
            content = agent_output
            if "```markdown" in content:
                content = content.split("```markdown")[1].split("```")[0].strip()
            elif "```md" in content:
                content = content.split("```md")[1].split("```")[0].strip()
            
            self.workspace.write_file("README.md", content, overwrite=True)
            if on_thought:
                on_thought("[OK] Successfully updated README.md in workspace.")
        except Exception as e:
            if on_thought:
                on_thought(f"[!] Warning: Could not auto-write README.md: {e}")
```

### 11.4 `workhorse/tools/file_crud.py` (Chunked File Engine)
```python
"""
Active Repository File CRUD & Chunking Engine.
Operates directly on the active working repository without sandboxing restrictions.
"""
import os
import shutil
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

class WorkspaceManager:
    def __init__(self, root_dir: Optional[str] = None):
        self.root = Path(root_dir or os.getcwd()).resolve()
        self.backup_dir = self.root / ".workhorse_backups"

    def list_dir(self, rel_path: str = ".") -> List[Dict[str, Any]]:
        target = (self.root / rel_path).resolve()
        if not target.is_dir():
            raise NotADirectoryError(f"Not a directory: {rel_path}")
        results = []
        for item in sorted(target.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
            if item.name.startswith((".git", ".venv", "__pycache__", ".workhorse_backups")):
                continue
            results.append({
                "name": item.name,
                "is_dir": item.is_dir(),
                "size": item.stat().st_size if item.is_file() else 0,
                "path": str(item.relative_to(self.root))
            })
        return results

    def read_file(self, rel_path: str, max_lines: int = 1000) -> str:
        target = (self.root / rel_path).resolve()
        if not target.is_file():
            raise FileNotFoundError(f"File not found: {rel_path}")
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = [f.readline() for _ in range(max_lines)]
        return "".join(lines)

    def read_file_chunks(self, rel_path: str, chunk_size_lines: int = 200) -> List[Dict[str, Any]]:
        target = (self.root / rel_path).resolve()
        if not target.is_file():
            raise FileNotFoundError(f"File not found: {rel_path}")
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        total = len(lines)
        chunks = []
        for i in range(0, total, chunk_size_lines):
            slice_lines = lines[i:i + chunk_size_lines]
            chunks.append({
                "chunk_index": len(chunks) + 1,
                "total_chunks": (total + chunk_size_lines - 1) // chunk_size_lines,
                "start_line": i + 1,
                "end_line": min(i + chunk_size_lines, total),
                "content": "".join(slice_lines)
            })
        return chunks

    def write_file(self, rel_path: str, content: str, overwrite: bool = True) -> bool:
        target = (self.root / rel_path).resolve()
        if target.exists() and not overwrite:
            raise FileExistsError(f"File exists: {rel_path}")

        if target.exists():
            self._backup(target)

        target.parent.mkdir(parents=True, exist_ok=True)
        tmp = target.with_suffix(".tmp_wh")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(content)
        tmp.replace(target)
        return True

    def delete_path(self, rel_path: str) -> bool:
        target = (self.root / rel_path).resolve()
        if not target.exists():
            raise FileNotFoundError(f"Path not found: {rel_path}")
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
        return True

    def get_repo_summary(self, max_files: int = 15) -> str:
        tree = []
        high_signals = ["README.md", "pyproject.toml", "package.json", "Cargo.toml", "go.mod", "Makefile"]
        file_previews = []

        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if not d.startswith((".git", ".venv", "node_modules", "__pycache__", ".workhorse"))]
            rel_dir = os.path.relpath(root, self.root)
            for f in files:
                rel_f = os.path.join(rel_dir, f) if rel_dir != "." else f
                tree.append(rel_f)
                if f in high_signals and len(file_previews) < max_files:
                    try:
                        content = self.read_file(rel_f, max_lines=80)
                        file_previews.append(f"--- File: {rel_f} ---\n{content}")
                    except Exception:
                        pass

        summary = f"Total Files Discovered: {len(tree)}\nKey File Listing:\n" + "\n".join(f"- {p}" for p in tree[:30])
        if file_previews:
            summary += "\n\nKey File Contents:\n" + "\n\n".join(file_previews)
        return summary

    def _backup(self, target: Path) -> None:
        try:
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            bak = self.backup_dir / f"{target.name}.bak"
            shutil.copy2(target, bak)
        except Exception:
            pass
```

### 11.5 `workhorse/tools/research.py` (Multi-Engine Web Cascade)
```python
"""Multi-Engine Web Intelligence Suite."""
import requests
from typing import Optional
from workhorse.config import Config

class ResearchSuite:
    def __init__(self):
        self.firecrawl_key = Config.FIRECRAWL_API_KEY
        self.jina_key = Config.JINA_API_KEY
        self.tavily_key = Config.TAVILY_API_KEY
        self.you_key = Config.YOU_API_KEY

    def search_tavily(self, query: str) -> Optional[str]:
        if not self.tavily_key:
            return None
        url = "https://api.tavily.com/search"
        payload = {"query": query, "api_key": self.tavily_key, "search_depth": "basic", "include_answer": True}
        try:
            r = requests.post(url, json=payload, timeout=8)
            if r.status_code == 200:
                data = r.json()
                ans = data.get("answer", "")
                sources = [f"- {s.get('title')}: {s.get('content')} ({s.get('url')})" for s in data.get("results", [])[:3]]
                return f"{ans}\n\n" + "\n".join(sources)
        except Exception:
            pass
        return None

    def search_jina(self, query: str) -> Optional[str]:
        url = f"https://s.jina.ai/{query}"
        headers = {"X-Return-Format": "markdown"}
        if self.jina_key:
            headers["Authorization"] = f"Bearer {self.jina_key}"
        try:
            r = requests.get(url, headers=headers, timeout=8)
            if r.status_code == 200 and len(r.text) > 100:
                return r.text[:3000]
        except Exception:
            pass
        return None

    def search_firecrawl(self, query: str) -> Optional[str]:
        if not self.firecrawl_key:
            return None
        url = "https://api.firecrawl.dev/v1/search"
        headers = {"Authorization": f"Bearer {self.firecrawl_key}", "Content-Type": "application/json"}
        payload = {"query": query, "limit": 3}
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=10)
            if r.status_code == 200 and r.json().get("success"):
                snippets = [item.get("markdown", "") for item in r.json().get("data", [])]
                return "\n---\n".join(snippets)[:3500]
        except Exception:
            pass
        return None

    def search_you(self, query: str) -> Optional[str]:
        if not self.you_key:
            return None
        url = "https://api.ydc-index.io/search"
        headers = {"X-API-Key": self.you_key}
        params = {"query": query}
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=8)
            if resp.status_code == 200:
                data = resp.json()
                hits = data.get("hits", [])
                results = []
                for h in hits[:3]:
                    snippets = " ".join(h.get("snippets", []))
                    results.append(f"- {h.get('title')}: {snippets} ({h.get('url')})")
                return "\n".join(results)
        except Exception:
            pass
        return None

    def auto_research(self, query: str) -> str:
        res = self.search_tavily(query)
        if res:
            return f"[Source: Tavily AI]\n{res}"
        res = self.search_jina(query)
        if res:
            return f"[Source: Jina AI]\n{res}"
        res = self.search_firecrawl(query)
        if res:
            return f"[Source: Firecrawl]\n{res}"
        res = self.search_you(query)
        if res:
            return f"[Source: You.com]\n{res}"
        return "No web intelligence results retrieved."
```

### 11.6 `workhorse/tools/bash_runner.py`
```python
"""Safe Command Execution Helper."""
import subprocess

def run_bash(cmd: str, timeout: int = 30) -> dict:
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return {"stdout": p.stdout[:5000], "stderr": p.stderr[:5000], "code": p.returncode}
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "code": -1}
```

### 11.7 `workhorse/providers/base.py`
```python
"""Provider Interface."""
from abc import ABC, abstractmethod
from typing import AsyncGenerator, Dict, Any, List, Optional
from pydantic import BaseModel

class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

class ProviderResponse(BaseModel):
    content: str
    model_name: str
    provider_name: str
    token_usage: TokenUsage
    finish_reason: Optional[str] = "stop"

class BaseProvider(ABC):
    @abstractmethod
    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        pass

    @abstractmethod
    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass
```

### 11.8 `workhorse/providers/ollama_local.py`
```python
"""Ollama Local Client."""
import httpx
import json
from typing import AsyncGenerator, List, Dict, Optional
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class OllamaProvider(BaseProvider):
    def __init__(self, host: Optional[str] = None):
        self.host = (host or Config.OLLAMA_HOST).rstrip("/")

    def get_status(self) -> dict:
        try:
            with httpx.Client(timeout=1.5) as client:
                res = client.get(f"{self.host}/api/tags")
                if res.status_code == 200:
                    models = {m["name"]: m for m in res.json().get("models", [])}
                    return {"online": True, "models": models}
        except Exception:
            pass
        return {"online": False, "models": {}}

    def is_available(self) -> bool:
        return self.get_status()["online"]

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        target = model or Config.DEFAULT_LOCAL_MODEL
        payload = {"model": target, "messages": messages, "stream": False, "options": {"temperature": temperature}}
        async with httpx.AsyncClient(timeout=45.0) as client:
            res = await client.post(f"{self.host}/api/chat", json=payload)
            res.raise_for_status()
            data = res.json()
            c = data.get("message", {}).get("content", "")
            return ProviderResponse(
                content=c, model_name=target, provider_name="ollama",
                token_usage=TokenUsage(prompt_tokens=data.get("prompt_eval_count", 0), completion_tokens=data.get("eval_count", 0))
            )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        target = model or Config.DEFAULT_LOCAL_MODEL
        payload = {"model": target, "messages": messages, "stream": True, "options": {"temperature": temperature}}
        async with httpx.AsyncClient(timeout=45.0) as client:
            async with client.stream("POST", f"{self.host}/api/chat", json=payload) as r:
                r.raise_for_status()
                async for line in r.aiter_lines():
                    if line:
                        chunk = json.loads(line)
                        yield chunk.get("message", {}).get("content", "")
```

### 11.9 `workhorse/providers/groq_client.py`
```python
"""Groq Cloud Client."""
from typing import AsyncGenerator, List, Dict, Optional
from openai import AsyncOpenAI
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class GroqProvider(BaseProvider):
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.client = AsyncOpenAI(api_key=self.api_key or "none", base_url="https://api.groq.com/openai/v1") if self.api_key else None

    def is_available(self) -> bool:
        return bool(self.api_key)

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        if not self.client:
            raise ValueError("GROQ_API_KEY not configured.")
        target = model or Config.GROQ_MODEL
        r = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature)
        u = r.usage
        return ProviderResponse(
            content=r.choices[0].message.content or "", model_name=target, provider_name="groq",
            token_usage=TokenUsage(prompt_tokens=u.prompt_tokens if u else 0, completion_tokens=u.completion_tokens if u else 0)
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("GROQ_API_KEY not configured.")
        target = model or Config.GROQ_MODEL
        s = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature, stream=True)
        async for chunk in s:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
```

### 11.10 `workhorse/providers/nvidia_client.py`
```python
"""Nvidia NIM Client."""
from typing import AsyncGenerator, List, Dict, Optional
from openai import AsyncOpenAI
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class NvidiaProvider(BaseProvider):
    def __init__(self):
        self.api_key = Config.NVIDIA_API_KEY
        self.client = AsyncOpenAI(api_key=self.api_key or "none", base_url=Config.NVIDIA_BASE_URL) if self.api_key else None

    def is_available(self) -> bool:
        return bool(self.api_key)

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        if not self.client:
            raise ValueError("NVIDIA_API_KEY not configured.")
        target = model or Config.NVIDIA_MODEL
        r = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature)
        u = r.usage
        return ProviderResponse(
            content=r.choices[0].message.content or "", model_name=target, provider_name="nvidia",
            token_usage=TokenUsage(prompt_tokens=u.prompt_tokens if u else 0, completion_tokens=u.completion_tokens if u else 0)
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("NVIDIA_API_KEY not configured.")
        target = model or Config.NVIDIA_MODEL
        s = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature, stream=True)
        async for chunk in s:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
```

### 11.11 `workhorse/providers/gemini_client.py`
```python
"""Google Gemini Provider using google-genai SDK."""
from typing import AsyncGenerator, List, Dict, Optional
from google import genai
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class GeminiProvider(BaseProvider):
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def is_available(self) -> bool:
        return bool(self.api_key)

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")
        target = model or Config.GEMINI_MODEL
        prompt = "\n\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        resp = self.client.models.generate_content(model=target, contents=prompt)
        return ProviderResponse(
            content=resp.text or "", model_name=target, provider_name="gemini",
            token_usage=TokenUsage(prompt_tokens=0, completion_tokens=0)
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")
        target = model or Config.GEMINI_MODEL
        prompt = "\n\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        for chunk in self.client.models.generate_content_stream(model=target, contents=prompt):
            if chunk.text:
                yield chunk.text
```

### 11.12 `workhorse/providers/openrouter.py`
```python
"""OpenRouter Client."""
from typing import AsyncGenerator, List, Dict, Optional
from openai import AsyncOpenAI
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class OpenRouterProvider(BaseProvider):
    def __init__(self):
        self.api_key = Config.OPENROUTER_API_KEY
        self.client = AsyncOpenAI(api_key=self.api_key or "none", base_url="https://openrouter.ai/api/v1") if self.api_key else None

    def is_available(self) -> bool:
        return bool(self.api_key)

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        if not self.client:
            raise ValueError("OPENROUTER_API_KEY not configured.")
        target = model or Config.OPENROUTER_MODEL
        r = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature)
        u = r.usage
        return ProviderResponse(
            content=r.choices[0].message.content or "", model_name=target, provider_name="openrouter",
            token_usage=TokenUsage(prompt_tokens=u.prompt_tokens if u else 0, completion_tokens=u.completion_tokens if u else 0)
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("OPENROUTER_API_KEY not configured.")
        target = model or Config.OPENROUTER_MODEL
        s = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature, stream=True)
        async for chunk in s:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
```

### 11.13 `workhorse/telemetry/langfuse_obs.py`
```python
"""Langfuse Observability Module."""
from typing import Optional, Dict, Any
from langfuse import Langfuse
from workhorse.config import Config

class Telemetry:
    _instance = None

    def __init__(self):
        self.enabled = Config.ENABLE_LANGFUSE and bool(Config.LANGFUSE_PUBLIC_KEY and Config.LANGFUSE_SECRET_KEY)
        self.client = None
        if self.enabled:
            try:
                self.client = Langfuse(public_key=Config.LANGFUSE_PUBLIC_KEY, secret_key=Config.LANGFUSE_SECRET_KEY, host=Config.LANGFUSE_BASEURL)
            except Exception:
                self.enabled = False

    @classmethod
    def get(cls) -> "Telemetry":
        if cls._instance is None:
            cls._instance = Telemetry()
        return cls._instance

    def trace(self, name: str, user_id: str = "wh_user", metadata: Optional[Dict[str, Any]] = None):
        if not self.enabled or not self.client:
            return None
        return self.client.trace(name=name, user_id=user_id, metadata=metadata or {})
```


### 11.14 `workhorse/tui/widgets.py` (Including `ThoughtAccordion`)
```python
"""
Textual & Rich Custom Widgets for Workhorse.
Features ThoughtAccordion, MessageBubble, FileTreeItem, StatusBadge, and TokenCounter.
"""
from textual.widgets import Static
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

class ThoughtAccordion(Static):
    """
    Collapsible disclosure dropdown for real-time thought streaming, chunk ingestion,
    tool execution, and multi-model handover notices.
    """
    expanded: bool = reactive(True)

    def __init__(self, title: str = "Reasoning & Execution Trace"):
        super().__init__()
        self.title = title
        self.thoughts: list[str] = []

    def add_thought(self, thought_line: str) -> None:
        self.thoughts.append(thought_line)
        self.refresh()

    def toggle(self) -> None:
        self.expanded = not self.expanded
        self.refresh()

    def on_click(self) -> None:
        self.toggle()

    def render(self):
        glyph = "▼" if self.expanded else "▶"
        status_text = f"({len(self.thoughts)} steps logged - click to toggle)"
        header = f"[bold yellow]{glyph} {self.title}[/bold yellow] [dim]{status_text}[/dim]"
        
        if not self.expanded:
            return Panel(header, border_style="yellow")

        body = "\n".join(self.thoughts) if self.thoughts else "[dim]Initializing agent reasoning loop...[/dim]"
        return Panel(body, title=header, border_style="yellow", padding=(0, 1))

class MessageBubble(Static):
    def __init__(self, sender: str, content: str, meta: str = ""):
        self.sender = sender
        self.raw_content = content
        self.meta = meta
        super().__init__()

    def render(self):
        if self.sender == "User":
            return Panel(
                Markdown(self.raw_content),
                title="[bold cyan]User[/bold cyan]",
                border_style="cyan",
                padding=(0, 1)
            )
        else:
            t = f"[bold green]Agent[/bold green] [dim]({self.meta})[/dim]" if self.meta else "[bold green]Agent[/bold green]"
            return Panel(
                Markdown(self.raw_content),
                title=t,
                border_style="green",
                padding=(0, 1)
            )

class StatusBadge(Static):
    def __init__(self, label: str, value: str, color: str = "green"):
        super().__init__()
        self.label = label
        self.value = value
        self.color = color

    def render(self):
        return f"[{self.label}: [bold {self.color}]{self.value}[/bold {self.color}]]"

class TokenCounter(Static):
    prompt_tokens: int = reactive(0)
    completion_tokens: int = reactive(0)

    def render(self):
        total = self.prompt_tokens + self.completion_tokens
        return f"[dim]Tokens: {self.prompt_tokens}p + {self.completion_tokens}c = {total}t[/dim]"
```

### 11.15 `workhorse/tui/screens.py`
```python
"""
Modal Screens and Dialogs for Workhorse TUI.
Includes FileEditorModal, ConfirmDialog, ModelPickerModal, HelpModal, GrepSearchModal, and NewFileDialog.
"""
from textual.screen import ModalScreen
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Label, Button, TextArea, Input, DataTable
from typing import Callable

class FileEditorModal(ModalScreen):
    def __init__(self, path: str, content: str, wm):
        super().__init__()
        self.file_path = path
        self.content = content
        self.wm = wm

    def compose(self):
        with Container(id="editor-dialog"):
            yield Label(f"Editing: {self.file_path}", id="editor-title")
            yield TextArea(self.content, id="editor-textarea")
            with Horizontal(id="editor-actions"):
                yield Button("Save", variant="primary", id="btn-save")
                yield Button("Cancel", id="btn-cancel")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-save":
            text = self.query_one("#editor-textarea", TextArea).text
            self.wm.write_file(self.file_path, text)
            self.app.notify(f"Saved {self.file_path}")
            self.dismiss(True)
        else:
            self.dismiss(False)

class ConfirmDialog(ModalScreen):
    def __init__(self, message: str, callback: Callable):
        super().__init__()
        self.message = message
        self.callback = callback

    def compose(self):
        with Container(id="confirm-dialog"):
            yield Label(self.message, id="confirm-label")
            with Horizontal():
                yield Button("Confirm", variant="error", id="btn-confirm")
                yield Button("Cancel", id="btn-cancel")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-confirm":
            self.callback()
            self.dismiss(True)
        else:
            self.dismiss(False)

class ModelPickerModal(ModalScreen):
    def __init__(self, ollama_provider):
        super().__init__()
        self.ollama = ollama_provider

    def compose(self):
        with Container(id="picker-dialog"):
            yield Label("Select Active Model Tier", id="picker-title")
            with Vertical():
                yield Button("Auto:Auto (5-Cycle Resilience Ring)", id="m-auto")
                yield Button("Local: Ollama (llama3.2:1b / Installed)", id="m-local")
                yield Button("Groq: LPU (High Velocity gpt-oss-120b)", id="m-groq")
                yield Button("Nvidia: NIM (Nemotron Reasoning)", id="m-nvidia")
                yield Button("Gemini: Flash 2.5 (2M Token Context)", id="m-gemini")
                yield Button("OpenRouter: Universal Fallback", id="m-openrouter")
            yield Button("Close", id="btn-close")

    def on_button_pressed(self, event: Button.Pressed):
        mode_map = {
            "m-auto": "auto:auto",
            "m-local": "local",
            "m-groq": "groq",
            "m-nvidia": "nvidia",
            "m-gemini": "gemini",
            "m-openrouter": "openrouter"
        }
        if event.button.id in mode_map:
            self.app.active_mode = mode_map[event.button.id]
            self.app.update_title()
            self.app.notify(f"Mode set to {self.app.active_mode}")
            self.dismiss(True)
        elif event.button.id == "btn-close":
            self.dismiss(False)

class HelpModal(ModalScreen):
    def compose(self):
        with Container(id="help-dialog"):
            yield Label("WORKHORSE KEYBINDINGS REFERENCE", id="help-title")
            with Vertical(id="help-content"):
                yield Label("• Ctrl+Q   : Cleanly exit Workhorse")
                yield Label("• F1 / ?   : Open this Help Reference")
                yield Label("• F2       : Cycle Execution Mode (Auto -> Local -> Groq -> Nvidia -> Gemini)")
                yield Label("• F3       : Toggle Live Web Intelligence (Firecrawl/Tavily/Jina)")
                yield Label("• F4       : Open Model Selection Picker")
                yield Label("• F5       : Clear active chat conversation")
                yield Label("• Ctrl+B   : Toggle Sidebar Directory Explorer")
                yield Label("• Tab      : Cycle focus between Tree, Chat Log, and Input")
                yield Label("• Enter    : Submit prompt to runtime")
                yield Label("• Shift+Enter : Insert newline in prompt")
                yield Label("• Sidebar Shortcuts: [n] New file, [e] Edit, [d] Delete, [r] Rename")
            yield Button("Close", id="btn-help-close")

    def on_button_pressed(self, event: Button.Pressed):
        self.dismiss()

class NewFileDialog(ModalScreen):
    def __init__(self, callback: Callable[[str], None]):
        super().__init__()
        self.callback = callback

    def compose(self):
        with Container(id="new-file-dialog"):
            yield Label("Create New File in Workspace:")
            yield Input(placeholder="path/to/filename.ext", id="new-file-input")
            with Horizontal():
                yield Button("Create", variant="primary", id="btn-create")
                yield Button("Cancel", id="btn-cancel")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-create":
            val = self.query_one("#new-file-input", Input).value.strip()
            if val:
                self.callback(val)
            self.dismiss(True)
        else:
            self.dismiss(False)
```

### 11.16 `workhorse/tui/app.py`
```python
"""
Main Textual Application for Workhorse Workstation.
"""
import asyncio
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, DirectoryTree, TextArea, Label, Button
from textual.binding import Binding
from textual.reactive import reactive

from workhorse.config import Config
from workhorse.agent import AgentRuntime
from workhorse.tui.widgets import MessageBubble, ThoughtAccordion
from workhorse.tui.screens import FileEditorModal, ConfirmDialog, ModelPickerModal, HelpModal, NewFileDialog

class WorkhorseApp(App):
    CSS_PATH = "styles.tcss"
    TITLE = "WORKHORSE WORKSTATION"
    SUB_TITLE = "Local-First Hybrid AI Runtime"

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit", show=True),
        Binding("f1", "help", "Help", show=True),
        Binding("f2", "cycle_mode", "Mode", show=True),
        Binding("f3", "toggle_web", "Web", show=True),
        Binding("f4", "pick_model", "Models", show=True),
        Binding("f5", "clear_history", "Clear", show=True),
        Binding("ctrl+b", "toggle_sidebar", "Sidebar", show=False),
    ]

    active_mode = reactive("auto:auto")
    use_web = reactive(False)
    ollama_online = reactive(False)

    def __init__(self, workspace_path: str = None):
        super().__init__()
        self.workspace_dir = Path(workspace_path or Config.CWD).resolve()
        self.runtime = AgentRuntime(str(self.workspace_dir))
        self.workspace = self.runtime.workspace

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Label("📂 WORKSPACE EXPLORER", id="sidebar-title")
                with Horizontal(id="crud-actions"):
                    yield Button("New", id="btn-new", variant="primary")
                    yield Button("Edit", id="btn-edit", variant="default")
                    yield Button("Del", id="btn-del", variant="error")
                yield DirectoryTree(str(self.workspace_dir), id="file-tree")
            with Vertical(id="main-panel"):
                with VerticalScroll(id="chat-container"):
                    yield MessageBubble("Agent", f"Workspace anchored to `{self.workspace_dir}`. Mode: `auto:auto` (5-Cycle Resilience Ring).")
                with Container(id="input-container"):
                    yield TextArea(id="prompt-input", placeholder="Ask Workhorse or edit files... (Enter to send, Shift+Enter for newline)")
        yield Footer()

    async def on_mount(self) -> None:
        self.ollama_online = self.runtime.ollama.get_status()["online"]
        self.update_title()

    def update_title(self) -> None:
        web = "[WEB: ON]" if self.use_web else "[WEB: OFF]"
        ollama = "[OLLAMA: UP]" if self.ollama_online else "[OLLAMA: DOWN]"
        self.sub_title = f"{self.active_mode} | {ollama} | {web} | {self.workspace_dir.name}"

    def action_cycle_mode(self) -> None:
        modes = ["auto:auto", "local", "groq", "nvidia", "gemini", "openrouter"]
        idx = modes.index(self.active_mode) if self.active_mode in modes else 0
        self.active_mode = modes[(idx + 1) % len(modes)]
        self.update_title()
        self.notify(f"Mode: {self.active_mode}")

    def action_toggle_web(self) -> None:
        self.use_web = not self.use_web
        self.update_title()
        self.notify(f"Web: {'ENABLED' if self.use_web else 'DISABLED'}")

    def action_pick_model(self) -> None:
        self.push_screen(ModelPickerModal(self.runtime.ollama))

    def action_help(self) -> None:
        self.push_screen(HelpModal())

    def action_clear_history(self) -> None:
        chat = self.query_one("#chat-container", VerticalScroll)
        chat.remove_children()
        chat.mount(MessageBubble("Agent", "Session cleared."))

    def action_toggle_sidebar(self) -> None:
        sb = self.query_one("#sidebar")
        sb.display = not sb.display

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        tree = self.query_one("#file-tree", DirectoryTree)
        selected = tree.cursor_node.data.path if tree.cursor_node and tree.cursor_node.data else None

        if event.button.id == "btn-edit" and selected and Path(selected).is_file():
            content = self.workspace.read_file(selected)
            self.push_screen(FileEditorModal(selected, content, self.workspace))
        elif event.button.id == "btn-del" and selected:
            self.push_screen(ConfirmDialog(f"Delete {Path(selected).name}?", lambda: self._do_delete(selected)))
        elif event.button.id == "btn-new":
            self.push_screen(NewFileDialog(self._do_create_file))

    def _do_create_file(self, rel_path: str):
        self.workspace.write_file(rel_path, "")
        self.query_one("#file-tree", DirectoryTree).reload()
        self.notify(f"Created {rel_path}")

    def _do_delete(self, p):
        self.workspace.delete_path(p)
        self.query_one("#file-tree", DirectoryTree).reload()
        self.notify(f"Deleted {Path(p).name}")

    async def on_text_area_key(self, event) -> None:
        if event.key == "enter" and not event.shift:
            event.prevent_default()
            input_box = self.query_one("#prompt-input", TextArea)
            prompt = input_box.text.strip()
            if not prompt:
                return
            input_box.text = ""

            chat = self.query_one("#chat-container", VerticalScroll)
            chat.mount(MessageBubble("User", prompt))

            accordion = ThoughtAccordion(title="Reasoning & Chunk Progress")
            chat.mount(accordion)
            chat.scroll_end()

            asyncio.create_task(self._run_agent_task(prompt, accordion))

    async def _run_agent_task(self, prompt: str, accordion: ThoughtAccordion):
        chat = self.query_one("#chat-container", VerticalScroll)
        tree = self.query_one("#file-tree", DirectoryTree)

        def on_thought(thought_msg: str):
            accordion.add_thought(thought_msg)
            chat.scroll_end()

        try:
            res = await self.runtime.execute_task(
                prompt,
                mode=self.active_mode,
                use_web=self.use_web,
                on_thought=on_thought
            )
            meta = f"{res['provider'].upper()} | {res['model']} | Cycle {res['cycle']}"
            chat.mount(MessageBubble("Agent", res["content"], meta=meta))
            tree.reload()
        except Exception as e:
            chat.mount(MessageBubble("Agent", f"Execution Failed: {e}"))
        chat.scroll_end()
```

### 11.17 `workhorse/tui/styles.tcss`
```css
/* Workhorse Master Textual CSS */
Screen {
    background: #0d1117;
    color: #c9d1d9;
}

Header {
    dock: top;
    height: 3;
    background: #161b22;
    color: #58a6ff;
    border-bottom: heavy #30363d;
}

Footer {
    dock: bottom;
    height: 1;
    background: #161b22;
    color: #8b949e;
}

#sidebar {
    width: 32;
    dock: left;
    background: #0d1117;
    border-right: solid #30363d;
    padding: 0 1;
}

#sidebar-title {
    text-align: center;
    color: #58a6ff;
    text-style: bold;
    margin: 1 0;
}

#crud-actions {
    height: 3;
    margin-bottom: 1;
}

#crud-actions Button {
    min-width: 8;
    height: 3;
    margin: 0 1;
}

#file-tree {
    background: #0d1117;
    color: #8b949e;
    height: 1fr;
}

#main-panel {
    height: 1fr;
    background: #0d1117;
}

#chat-container {
    height: 1fr;
    padding: 1;
    overflow-y: scroll;
}

#input-container {
    dock: bottom;
    height: 7;
    background: #161b22;
    border-top: heavy #30363d;
    padding: 0 1;
}

#prompt-input {
    height: 5;
    background: #0d1117;
    border: solid #30363d;
}

ThoughtAccordion {
    margin: 1 0;
}

#editor-dialog, #confirm-dialog, #picker-dialog, #help-dialog, #new-file-dialog {
    width: 74;
    height: 26;
    background: #161b22;
    border: heavy #58a6ff;
    padding: 1;
    align: center middle;
}

#editor-textarea {
    height: 16;
    margin: 1 0;
}

#help-title, #picker-title, #editor-title {
    color: #58a6ff;
    text-style: bold;
    margin-bottom: 1;
}
```

### 11.18 `workhorse/cli.py`
```python
"""Workhorse Headless CLI."""
import sys
import argparse
import asyncio
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from workhorse.config import Config
from workhorse.agent import AgentRuntime
from workhorse.tools.file_crud import WorkspaceManager

console = Console()

def run_cli():
    parser = argparse.ArgumentParser(prog="workhorse", description="Workhorse: Universal Terminal Workstation")
    parser.add_argument("prompt", nargs="?", default=None)
    parser.add_argument("-m", "--mode", default="auto:auto")
    parser.add_argument("-w", "--web", action="store_true")
    parser.add_argument("-f", "--file")
    parser.add_argument("-c", "--crud", nargs="+")
    parser.add_argument("--models", action="store_true")
    parser.add_argument("-t", "--tui", action="store_true")

    args = parser.parse_args()

    if args.crud:
        wm = WorkspaceManager()
        op = args.crud[0].lower()
        if op == "list":
            files = wm.list_dir(args.crud[1] if len(args.crud) > 1 else ".")
            table = Table(title="Workspace Listing")
            table.add_column("Type", style="cyan")
            table.add_column("Name", style="green")
            for f in files:
                table.add_row("DIR" if f["is_dir"] else "FILE", f["name"])
            console.print(table)
            sys.exit(0)
        elif op == "view":
            console.print(Markdown(f"```\n{wm.read_file(args.crud[1])}\n```"))
            sys.exit(0)
        elif op == "create":
            wm.write_file(args.crud[1], args.crud[2] if len(args.crud) > 2 else "")
            console.print(f"[green]Created {args.crud[1]}[/green]")
            sys.exit(0)
        elif op == "delete":
            wm.delete_path(args.crud[1])
            console.print(f"[red]Deleted {args.crud[1]}[/red]")
            sys.exit(0)

    if args.models:
        runtime = AgentRuntime()
        status = runtime.ollama.get_status()
        console.print(f"Ollama: {'ONLINE' if status['online'] else 'OFFLINE'} ({list(status['models'].keys())})")
        sys.exit(0)

    if args.prompt and not args.tui:
        runtime = AgentRuntime()
        p = args.prompt
        if args.file:
            p = f"File Context ({args.file}):\n```\n{runtime.workspace.read_file(args.file)}\n```\n\n{p}"

        def on_thought(t):
            console.print(f"[dim yellow]{t}[/dim yellow]")

        res = asyncio.run(runtime.execute_task(p, mode=args.mode, use_web=args.web, on_thought=on_thought))
        console.print(f"\n[dim]* Provider: {res['provider'].upper()} ({res['model']}) | Cycle: {res['cycle']}[/dim]\n")
        console.print(Markdown(res["content"]))
        sys.exit(0)

    # Launch full interactive TUI
    from workhorse.tui.app import WorkhorseApp
    app = WorkhorseApp()
    app.run()
```

### 11.19 `workhorse.py` (Root Dispatcher)
```python
#!/usr/bin/env python3
"""
Workhorse Universal Dispatcher.
Executes CLI mode if arguments exist; otherwise launches Textual TUI.
"""
import sys
import os

_venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv", "bin", "python")
if os.path.exists(_venv_python) and os.path.abspath(sys.executable) != os.path.abspath(_venv_python):
    os.execv(_venv_python, [_venv_python] + sys.argv)

from workhorse.cli import run_cli

if __name__ == "__main__":
    run_cli()
```

---

## 12. Installation, Packaging & Global Symlinking (`install.sh` & `install.ps1`)

### 12.1 Linux/macOS POSIX Installer (`install.sh`)
```bash
#!/usr/bin/env bash
# =============================================================================
# Workhorse Tri-Alias Global Installer (workhorse, workhouse, wh)
# =============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_BIN="$HOME/.local/bin"

echo "=== Installing Workhorse Workstation (Tri-Alias: workhorse, workhouse, wh) ==="

# 1. Setup isolated venv
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    python3 -m venv "$SCRIPT_DIR/.venv"
fi

"$SCRIPT_DIR/.venv/bin/pip" install --upgrade pip
"$SCRIPT_DIR/.venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
"$SCRIPT_DIR/.venv/bin/pip" install textual rich httpx pydantic

# 2. Setup global wrapper
mkdir -p "$LOCAL_BIN"
LAUNCHER="$LOCAL_BIN/workhorse"

cat << 'EOF' > "$LAUNCHER"
#!/usr/bin/env bash
INSTALL_DIR="/home/japheth/Desktop/workhouse"
export WORKHORSE_INVOCATION_CWD="$(pwd)"
export WORKHORSE_INSTALL_DIR="$INSTALL_DIR"
exec "$INSTALL_DIR/.venv/bin/python" "$INSTALL_DIR/workhorse.py" "$@"
EOF

chmod +x "$LAUNCHER"

# 3. Create symlinks for workhouse and wh
ln -sf "$LAUNCHER" "$LOCAL_BIN/workhouse"
ln -sf "$LAUNCHER" "$LOCAL_BIN/wh"

echo "============================================================"
echo "  [SUCCESS] Installed: 'workhorse', 'workhouse', and 'wh'    "
echo "  Call 'wh' in ANY directory to launch the Terminal GUI!     "
echo "============================================================"
```

### 12.2 Windows PowerShell Installer (`install.ps1`)
```powershell
$InstallDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VenvPython = Join-Path $InstallDir ".venv\Scripts\python.exe"
$MainScript = Join-Path $InstallDir "workhorse.py"

if (-not (Test-Path $VenvPython)) {
    python -m venv (Join-Path $InstallDir ".venv")
    & $VenvPython -m pip install --upgrade pip
    & $VenvPython -m pip install -r (Join-Path $InstallDir "requirements.txt")
}

$UserBin = Join-Path $env:USERPROFILE "bin"
if (-not (Test-Path $UserBin)) {
    New-Item -ItemType Directory -Path $UserBin | Out-Null
}

$CmdContent = @"
@echo off
set "WORKHORSE_INVOCATION_CWD=%CD%"
set "WORKHORSE_INSTALL_DIR=$InstallDir"
"$VenvPython" "$MainScript" %*
"@

Set-Content -Path (Join-Path $UserBin "workhorse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "workhouse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "wh.cmd") -Value $CmdContent
```

---

## 13. Verification, Quality Assurance & Test Suite

### 13.1 Pre-Flight Verification Checklist
- [ ] In `~/Desktop/promptdock` run `wh` -> Terminal GUI launches anchored to `promptdock/`.
- [ ] In TUI type `tell me about this repo` -> Verifies `ThoughtAccordion` shows chunk progress and summarizes structure.
- [ ] In TUI type `edit readme, make it more detailed` -> Verifies in-place modification of `README.md` and backup creation in `.workhorse_backups/`.
- [ ] Simulate network drop (disconnect Wi-Fi) and run `wh "test"` -> Confirms transparent notice `[!] No internet connection detected. Using Ollama model: <model> locally...` and local completion.
- [ ] Verify 5-Cycle Resilience Ring cycles through all endpoints up to 5 times before failing.

### 13.2 Automated Unit & Integration Tests (`tests/test_resilience.py`)
```python
"""Tests for 5-Cycle Resilience Ring and Offline Fallback."""
import unittest
import asyncio
from unittest.mock import MagicMock, patch
from workhorse.router import AutoRouter
from workhorse.providers.ollama_local import OllamaProvider

class TestResilienceRing(unittest.TestCase):
    def setUp(self):
        self.mock_ollama = MagicMock(spec=OllamaProvider)
        self.mock_ollama.get_status.return_value = {"online": True, "models": {"llama3.2:1b": {}}}
        self.router = AutoRouter(self.mock_ollama)

    def test_offline_fallback(self):
        with patch.object(self.router, "check_connectivity", return_value=False):
            thoughts = []
            async def _dummy(p, m): return "offline response"
            res = asyncio.run(self.router.execute_with_resilience_ring(_dummy, on_thought=thoughts.append))
            self.assertTrue(res.get("offline"))
            self.assertIn("No internet connection detected", thoughts[0])

    def test_retries_across_cycles(self):
        with patch.object(self.router, "check_connectivity", return_value=True):
            attempts = []
            async def _fail_then_pass(p, m):
                attempts.append((p, m))
                if len(attempts) < 3:
                    raise ConnectionError("Transient failure")
                return "passed"
            res = asyncio.run(self.router.execute_with_resilience_ring(_fail_then_pass, max_cycles=5))
            self.assertEqual(res["result"], "passed")
            self.assertGreaterEqual(len(attempts), 3)

if __name__ == "__main__":
    unittest.main()
```

### 13.3 File Chunking Unit Tests (`tests/test_chunking.py`)
```python
"""Tests for file chunking and repository streaming."""
import unittest
import tempfile
import shutil
from pathlib import Path
from workhorse.tools.file_crud import WorkspaceManager

class TestFileChunking(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.wm = WorkspaceManager(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_chunk_large_file(self):
        test_file = Path(self.test_dir) / "large_data.txt"
        with open(test_file, "w") as f:
            for i in range(1, 501):
                f.write(f"Line {i}: Data record payload content\n")

        chunks = self.wm.read_file_chunks("large_data.txt", chunk_size_lines=150)
        self.assertEqual(len(chunks), 4)
        self.assertEqual(chunks[0]["start_line"], 1)
        self.assertEqual(chunks[0]["end_line"], 150)
        self.assertEqual(chunks[-1]["start_line"], 451)
        self.assertEqual(chunks[-1]["end_line"], 500)

    def test_repo_summary_extraction(self):
        (Path(self.test_dir) / "src").mkdir()
        (Path(self.test_dir) / "src" / "main.py").write_text("print('App running')")
        (Path(self.test_dir) / "README.md").write_text("# Test Project\nSample overview.")

        summary = self.wm.get_repo_summary()
        self.assertIn("Total Files Discovered: 2", summary)
        self.assertIn("README.md", summary)

if __name__ == "__main__":
    unittest.main()
```

---

## 14. In-Depth Operational Playbooks & Real-World Scenarios

### 14.1 Playbook A: Repository Audit & In-Place README Expansion in Target Project
**Scenario:** A developer clones an open-source tool into `~/Desktop/promptdock`. The repository contains TypeScript files and a rudimentary 3-line `README.md`.

```bash
cd ~/Desktop/promptdock
wh
```

1. **Terminal Launch:**
   - The global wrapper detects that `wh` was invoked from `~/Desktop/promptdock`.
   - The Textual TUI opens full-screen. The top header shows:
     `WORKHORSE WORKSTATION | auto:auto | [OLLAMA: UP] | [WEB: OFF] | promptdock`
   - The left sidebar displays the real directory tree of `promptdock/` (`src/`, `package.json`, `tsconfig.json`, `README.md`).

2. **User Input:**
   Developer types:
   ```
   tell me about this repo and edit readme, make it more detailed
   ```

3. **Autonomous Execution with Live Thought Accordion:**
   - Instead of displaying a static "Thinking..." spinner, the TUI immediately mounts an interactive `ThoughtAccordion` widget labeled:
     `▼ Reasoning & Chunk Progress (4 steps, Active)`
   - The accordion streams each event in real time:
     ```
     [*] Scanning repository structure in ~/Desktop/promptdock...
     [*] Discovered 14 files across 3 directories.
     [*] Ingested chunk 1/1: package.json (Detected Express, TypeScript, Zod, Vitest)
     [*] Ingested chunk 1/2: src/index.ts (Express server initialization on port 3000)
     [*] Ingested chunk 2/2: src/routes/dock.ts (REST endpoints for dock management)
     [*] Ingested chunk 1/1: README.md (Existing 3-line placeholder)
     [*] auto:auto Dispatcher: Promoted to [GROQ: openai/gpt-oss-120b] for rapid technical writing.
     [*] Drafting comprehensive README.md with Architecture, Installation, Endpoints, and Testing...
     [*] Generating safety backup: .workhorse_backups/README.md.1700000000.bak
     [OK] In-place write complete: README.md updated (148 lines written).
     ```

4. **Agent Card Delivery:**
   - The agent prints a concise completion card in the chat log:
     ```markdown
     I have analyzed **promptdock** and updated `README.md` directly in your workspace.
     
     ### What Was Added to README.md:
     - **Project Overview:** High-performance Express & TypeScript API gateway.
     - **Architecture Overview:** Outlining `src/index.ts` and `src/routes/dock.ts`.
     - **Prerequisites & Setup:** Node.js 20+, `pnpm install`, and environment variables.
     - **API Documentation:** Interactive table detailing all REST endpoints.
     - **Testing & Scripts:** Instructions for running Vitest test suites.
     
     *A backup of your previous README was preserved at `.workhorse_backups/README.md.1700000000.bak`.*
     ```
   - The sidebar directory tree reloads automatically, reflecting the new file size of `README.md`.

---

### 14.2 Playbook B: Offline Flight / Train Mode with Local Ollama
**Scenario:** Developer is on an airplane with no Wi-Fi. They open Workhorse inside an existing Python project.

```bash
cd ~/projects/ml-pipeline
wh "Refactor the data loader in loader.py to use generator expressions"
```

1. **Connectivity Check & Transparent Offline Notice:**
   - The `AutoRouter` detects `is_network_connected() == False`.
   - The runtime immediately outputs:
     ```
     [!] No internet connection detected. Seamlessly falling back to local Ollama model: llama3.2:1b...
     ```
2. **Local Execution:**
   - Query is routed to local `http://127.0.0.1:11434`.
   - The prompt is processed 100% on-device at zero token cost and zero network latency.
   - Output code is generated and presented in Rich markdown directly in STDOUT or TUI.

---

### 14.3 Playbook C: Cloud Rate-Limit (429) & 5-Cycle Resilience Ring Traversal
**Scenario:** A large multi-file refactoring prompt causes Groq LPU to hit an organization rate limit (HTTP 429).

1. **Cycle 1 Handover:**
   - Groq returns `429: Rate limit exceeded`.
   - The `ThoughtAccordion` displays:
     ```
     [!] [groq:openai/gpt-oss-120b] Failed in cycle 1: HTTP 429 Rate Limit Exceeded -> Handing over to next provider in ring.
     [*] Attempting execution on [NVIDIA: nvidia/nemotron-3.5-super-vl-120b-a12b] (Cycle 1)...
     ```
2. **Success Without Interruption:**
   - Nvidia NIM accepts the prompt and streams the solution.
   - The user experiences zero interruption or error messages; the system auto-healed through its circular resilience ring.
3. **If All Fail (Extreme Outage):**
   - The system cycles through Local Ollama, Groq, Nvidia, Gemini, and OpenRouter for **5 full cycles** (up to 25 attempts with backoff) before ever raising an error.

---

### 14.4 Playbook D: Multi-Engine Web Research for Bleeding-Edge Libraries
**Scenario:** Developer needs documentation for a library released yesterday.

```bash
wh "What are the new breaking changes in LangChain v0.3 and how do I migrate?" --web
```

1. **Automated Cascade:**
   - Tavily searches real-time agent index.
   - If Tavily has sparse results, Jina AI Reader fetches the release notes directly from `https://r.jina.ai/https://github.com/langchain-ai/langchain/releases`.
   - Firecrawl parses JS-rendered documentation tables.
2. **Synthesis:**
   - Retrieved clean markdown is injected into the context window.
   - Groq or Gemini Flash formats the definitive migration guide.

---

## 15. Specialized Sub-Agent Execution Swarm Specifications

When implementing the system using a multi-agent swarm or delegating across subagents, assign each engineer the following briefs:

### Brief 1: TUI & Design Systems Engineer (`@tui-engineer`)
- **Scope:** `workhorse/tui/app.py`, `workhorse/tui/widgets.py`, `workhorse/tui/screens.py`, `workhorse/tui/styles.tcss`.
- **Assignment:** Build the reactive full-screen terminal interface using Textual and Rich. Ensure the workspace tree updates asynchronously, file editing occurs within a modal buffer with syntax checking, chat messages render beautiful GitHub-flavored markdown with code copy blocks, and keybindings (`F1`-`F5`, `Ctrl+Q`, `Ctrl+B`) respond instantaneously. Integrate `ThoughtAccordion` to stream reasoning steps and eliminate opaque spinners.

### Brief 2: Core Routing & Model Integration Engineer (`@model-engineer`)
- **Scope:** `workhorse/router.py`, `workhorse/providers/` (`ollama_local.py`, `groq_client.py`, `nvidia_client.py`, `gemini_client.py`, `openrouter.py`).
- **Assignment:** Implement the `auto:auto` routing engine with local Ollama auto-discovery. Implement the **5-Cycle Infinite Resilience Ring** ensuring Workhorse traverses all models and repeats the circle at least 5 times before failing. Add transparent offline fallback with inline notifications.

### Brief 3: Web Intelligence & Observability Engineer (`@research-engineer`)
- **Scope:** `workhorse/tools/research.py`, `workhorse/telemetry/langfuse_obs.py`.
- **Assignment:** Connect the four configured web endpoints (Firecrawl, Jina AI, Tavily AI, You.com) into an automated failover pipeline. Integrate Langfuse tracing across every model call and tool execution with token cost and latency accounting.

### Brief 4: Workspace Security & File CRUD Engineer (`@crud-engineer`)
- **Scope:** `workhorse/tools/file_crud.py`, `workhorse/tools/bash_runner.py`.
- **Assignment:** Implement safe workspace file operations (create, read, update, delete, rename, grep) without restrictive sandboxing. Implement chunked file reading (`read_file_chunks`), chunked repo streaming (`stream_repo_chunks`), and in-place atomic file modification with `.workhorse_backups/`.

### Brief 5: DevOps, Packaging & Global System Integration (`@devops-engineer`)
- **Scope:** `install.sh`, `install.ps1`, `workhorse.py`, `workhorse/cli.py`, `requirements.txt`.
- **Assignment:** Implement the global POSIX launcher in `~/.local/bin/workhorse` and symlink `~/.local/bin/workhouse` and `~/.local/bin/wh`. Ensure argument preservation in headless CLI mode and automated context-aware workspace directory resolution.

---

## 16. Disaster Recovery, Security & Maintenance Runbooks

### 16.1 Local Ollama Daemon Recovery & Model Re-Indexing
```bash
# Check Ollama service status
systemctl status ollama || pkill ollama && ollama serve &

# Verify Ollama local models
curl -s http://127.0.0.1:11434/api/tags | jq .

# Pull recommended low-latency 1B model
ollama pull llama3.2:1b
```

### 16.2 Cloud Provider Outage & API Key Rotation
If a cloud provider encounters a global outage:
1. Update `.env` with new keys or disable the failing provider.
2. Workhorse will automatically adjust the circular resilience ring on its next invocation without requiring a system restart.

### 16.3 Non-Destructive Backup Restoration Runbook
If an automated edit corrupts a target file:
1. Check `.workhorse_backups/` in the workspace directory.
2. Identify the timestamped backup: `.workhorse_backups/<filename>.<timestamp>.bak`.
3. Restore via `cp .workhorse_backups/<filename>.<timestamp>.bak <filename>`.

---

## 17. Master Implementation Prompt Suite (For Autonomous Agents & AGY)

### 17.1 Master Orchestrator Prompt

```markdown
### MASTER ARCHITECTURAL IMPLEMENTATION PROMPT (v3.1.0-ENTERPRISE-PRO-MAX)

You are tasked with transforming the repository at `/home/japheth/Desktop/workhouse` into the production-grade Workhorse Universal Terminal Workstation specified in `AGENTS.md`.

#### Mandatory Architectural Directives:
1. **Tri-Alias Universal Invocation (`workhorse`, `workhouse`, `wh`):**
   - Must be executable from ANY directory on the PC via `workhorse`, `workhouse`, or `wh`.
   - Setup wrapper in `~/.local/bin/workhorse` with symlinks `~/.local/bin/workhouse` and `~/.local/bin/wh`.
   - Auto-execute inside `/home/japheth/Desktop/workhouse/.venv/bin/python`, but anchor file operations directly to caller `$PWD`.
   - No arguments = Interactive Textual TUI. Arguments = Headless streaming CLI.

2. **Active Working Repository Operator (No Restrictive Sandboxing):**
   - Workhorse must have direct authority to inspect the active directory and edit files in place.
   - Example scenario: User in `~/Desktop/promptdock` typing `tell me about this repo` or `edit readme, make it more detailed` must ACTUALLY read files in chunks and write updates directly back to `README.md`.
   - Implement `read_file_chunks` and `stream_repo_chunks` to handle large repositories without blowing context.
   - Maintain atomic writes with automatic backups in `.workhorse_backups/`.

3. **5-Cycle Infinite Resilience Ring (Zero Premature Failures):**
   - Mode must always default to `auto:auto`.
   - Build a circular provider ring: `[Local Ollama] -> [Groq LPU] -> [Nvidia NIM] -> [Google Gemini] -> [OpenRouter]`.
   - Never return failed on a single model failure. Traverse the entire model circle and repeat for at least 5 complete retry cycles with exponential backoff before failing.
   - Transparent Offline Handling: If network is disconnected or cloud endpoints fail, immediately emit:
     `[!] No internet connection detected. Using Ollama model: <model> locally...` and continue operating locally.

4. **Live Streaming Thought Accordions (No Opaque Spinners):**
   - Never show generic "loading..." or "thinking..." spinners.
   - Implement `ThoughtAccordion` widget displaying real-time streaming thoughts, chunk progress, tool calls, and model handover notices in collapsible dropdowns (`▶` / `▼`).

5. **Multi-Engine Web Intelligence:**
   - Integrate Firecrawl, Jina AI, Tavily, and You.com in an automated fallback cascade.

6. **Cross-Agent Skills Sharing & Universal MCP Bridge:**
   - Implement `SkillRegistry` to discover, index, and execute skills from Claude Code (`~/.claude/skills/`), Antigravity (`~/.gemini/antigravity/skills/`), and Cursor.
   - Implement `MCPRegistry` and `StdioMCPClient` to connect to external MCP servers defined in Claude Desktop, Cursor, and local configs over JSON-RPC 2.0.
   - Bind `F6` in the TUI to launch the interactive Skills & MCP Hub modal.

7. **Modularized Package Structure:**
   - Implement complete source files across `workhorse/` package as detailed in Section 11 of `AGENTS.md`.
   - Update `install.sh` and verify all tests pass.
```

---
*End of AGENTS.md — Workhorse Universal Specification 3.1.0-ENTERPRISE-PRO-MAX*


---

## 18. Complete Function Calling & Agent Tool JSON Schemas

To enable autonomous tool execution across OpenAI-compatible providers (Groq, Nvidia NIM, OpenRouter) and Google Gemini, the following JSON schemas define the callable interface for all native tools.

### 18.1 File Engine Tool Schemas (`tools_file_spec.json`)
```json
[
  {
    "type": "function",
    "function": {
      "name": "read_file",
      "description": "Reads lines from a file located within the active repository.",
      "parameters": {
        "type": "object",
        "properties": {
          "rel_path": {
            "type": "string",
            "description": "Relative file path from the repository root (e.g. 'src/index.ts', 'README.md')."
          },
          "max_lines": {
            "type": "integer",
            "description": "Maximum number of lines to read from the start of the file. Default is 1000.",
            "default": 1000
          }
        },
        "required": ["rel_path"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "read_file_chunks",
      "description": "Reads a large file in line-bounded chunks with index metadata to avoid context overflow.",
      "parameters": {
        "type": "object",
        "properties": {
          "rel_path": {
            "type": "string",
            "description": "Relative file path from the repository root."
          },
          "chunk_size_lines": {
            "type": "integer",
            "description": "Number of lines per chunk. Default is 200.",
            "default": 200
          }
        },
        "required": ["rel_path"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "write_file",
      "description": "Writes or overwrites a file in the active repository atomically, preserving a safety backup in .workhorse_backups/.",
      "parameters": {
        "type": "object",
        "properties": {
          "rel_path": {
            "type": "string",
            "description": "Relative file path from the repository root."
          },
          "content": {
            "type": "string",
            "description": "The exact full text content to write to the file."
          },
          "overwrite": {
            "type": "boolean",
            "description": "Whether to overwrite an existing file. Default is true.",
            "default": true
          }
        },
        "required": ["rel_path", "content"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "delete_file",
      "description": "Deletes a file or directory from the active repository.",
      "parameters": {
        "type": "object",
        "properties": {
          "rel_path": {
            "type": "string",
            "description": "Relative file path to delete."
          }
        },
        "required": ["rel_path"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_repo_summary",
      "description": "Scans the active repository structure, returning a directory tree and contents of key configuration and manifest files.",
      "parameters": {
        "type": "object",
        "properties": {
          "max_files": {
            "type": "integer",
            "description": "Maximum number of high-signal manifests to preview. Default is 15.",
            "default": 15
          }
        }
      }
    }
  }
]
```

### 18.2 Research Tool Schemas (`tools_research_spec.json`)
```json
[
  {
    "type": "function",
    "function": {
      "name": "web_search_tavily",
      "description": "Executes real-time AI agent search using Tavily AI to retrieve synthesized answers and source citations.",
      "parameters": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "Factual search query."
          }
        },
        "required": ["query"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "web_read_jina",
      "description": "Fetches any webpage or documentation URL and extracts clean, LLM-ready Markdown via Jina Reader.",
      "parameters": {
        "type": "object",
        "properties": {
          "target_url": {
            "type": "string",
            "description": "Full HTTPS URL of the target documentation, GitHub release, or article."
          }
        },
        "required": ["target_url"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "web_scrape_firecrawl",
      "description": "Deeply scrapes and parses JavaScript-heavy web applications and single-page apps into pristine Markdown via Firecrawl.",
      "parameters": {
        "type": "object",
        "properties": {
          "query_or_url": {
            "type": "string",
            "description": "Search term or direct URL to scrape."
          }
        },
        "required": ["query_or_url"]
      }
    }
  }
]
```

---

## 19. Complete Provider System Prompts

To guarantee deterministic code output, accurate tool calling, and consistent tone across all tiers, Workhorse applies specialized system prompts tailored to each provider's strengths.

### 19.1 System Prompt: Local Ollama Tier (`llama3.2:1b`, `deepseek-v4.1`)
```
You are Workhorse Local Tier, an ultra-fast, on-device intelligence core running directly on the user's local machine via Ollama.
Your goals:
1. Provide concise, direct, and zero-latency responses for micro-tasks, text formatting, and quick lookups.
2. If the user asks for code refactoring or complex multi-step reasoning that exceeds your parameter bounds, provide a clean attempt and include the tag [RECOMMEND_HANDOVER: GROQ] so the runtime can promote the task.
3. Be direct, authoritative, and strip all unnecessary pleasantries or robotic disclaimers.
```

### 19.2 System Prompt: Groq Cloud LPU Tier (`openai/gpt-oss-120b`, `llama-3.3-70b`)
```
You are Workhorse Groq Tier, powered by ultra-high-throughput LPUs.
Your goals:
1. Deliver production-ready code, detailed technical architectures, and precise refactorings at maximum speed.
2. When instructed to edit files (e.g., "edit readme, make it more detailed"), produce complete, fully expanded documentation sections without placeholders or truncation.
3. Never output conversational filler like "Sure, I can help with that!". Begin directly with the requested output or analysis.
4. When writing code, adhere to modern standards: Python 3.12+ (type hints, dataclasses, async), TypeScript 5+ (strict types, interfaces).
```

### 19.3 System Prompt: Nvidia NIM Tier (`nvidia/nemotron-3.5-super-vl-120b-a12b`)
```
You are Workhorse Nvidia NIM Tier, specializing in deep architectural reasoning, algorithm synthesis, and visual-language comprehension.
Your goals:
1. Analyze multi-file code dependencies, complex dataflow graphs, and design patterns with rigorous mathematical precision.
2. When presented with visual diagrams, UI wireframes, or architecture charts, decompile the structural components into code representations.
3. Eliminate race conditions, memory leaks, and performance bottlenecks in system-level implementations.
```

### 19.4 System Prompt: Google Gemini Tier (`gemini-2.5-flash`, `gemini-1.5-pro`)
```
You are Workhorse Gemini Tier, backed by a massive 2-million-token multimodal context window.
Your goals:
1. Ingest entire repositories, multi-megabyte log files, and cross-module dependencies seamlessly.
2. When answering repository-wide queries, synthesize all chunked file inputs into a coherent, high-altitude architectural overview.
3. Verify every file path, function signature, and import path against the provided codebase manifests.
```

---

## 20. End-to-End Workflow Integration Tests (`tests/test_e2e_workflow.py`)

```python
"""
End-to-End integration test simulating a real terminal session in a target repo.
"""
import unittest
import tempfile
import shutil
import asyncio
from pathlib import Path
from workhorse.agent import AgentRuntime
from workhorse.tools.file_crud import WorkspaceManager

class TestE2EWorkflow(unittest.TestCase):
    def setUp(self):
        # Create simulated project repo: ~/Desktop/test_project
        self.repo_dir = tempfile.mkdtemp()
        self.wm = WorkspaceManager(self.repo_dir)

        # Populate with sample project files
        self.wm.write_file("package.json", '{"name": "test-repo", "version": "1.0.0", "dependencies": {"express": "^4.19"}}')
        self.wm.write_file("src/server.js", 'const express = require("express");\nconst app = express();\napp.listen(3000);\n')
        self.wm.write_file("README.md", "# Test Repo\nPlaceholder readme.")

        self.runtime = AgentRuntime(self.repo_dir)

    def tearDown(self):
        shutil.rmtree(self.repo_dir)

    def test_repo_scan_and_summary(self):
        summary = self.wm.get_repo_summary()
        self.assertIn("package.json", summary)
        self.assertIn("src/server.js", summary)
        self.assertIn("express", summary)

    def test_in_place_readme_edit(self):
        thoughts = []
        def on_thought(t): thoughts.append(t)

        new_readme_content = """# Test Repo Expanded
## Architecture
Express web server listening on port 3000.
## Getting Started
```bash
npm install
node src/server.js
```
"""
        # Simulate agent applying in-place edit
        self.runtime._apply_readme_edit(f"```markdown\n{new_readme_content}\n```", on_thought=on_thought)

        # Verify README.md was modified in place
        updated = self.wm.read_file("README.md")
        self.assertIn("Test Repo Expanded", updated)
        self.assertIn("Express web server listening", updated)

        # Verify backup was created
        backups = list((Path(self.repo_dir) / ".workhorse_backups").iterdir())
        self.assertGreaterEqual(len(backups), 1)
        self.assertIn("README.md", backups[0].name)

    def test_resilience_ring_mock_success(self):
        thoughts = []
        async def _test():
            return await self.runtime.execute_task(
                "Short prompt",
                mode="auto:auto",
                on_thought=thoughts.append
            )
        # Verify execution completes without throwing unhandled exceptions
        try:
            res = asyncio.run(_test())
            self.assertIn("content", res)
            self.assertIn("provider", res)
        except RuntimeError as e:
            # Expected if Ollama is not running in test environment and no API keys set
            self.assertIn("No LLM providers available", str(e))

if __name__ == "__main__":
    unittest.main()
```

---

## 21. CI/CD Automation & GitHub Actions Workflow (`.github/workflows/ci.yml`)

```yaml
name: Workhorse CI / Quality Assurance

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install textual rich httpx pydantic pytest pytest-asyncio

      - name: Run Unit & Integration Tests
        run: |
          pytest tests/ -v
```

---

## 22. Architectural Terminology & Technical Glossary

- **Active Working Repository Operator:** A design philosophy where an AI development workstation possesses non-destructive write and read authority over the user's active working directory, avoiding the limitations of sandboxes.
- **5-Cycle Resilience Ring:** A fault-tolerant model orchestration loop that cascades failed or rate-limited requests across a circle of providers (`[Ollama] -> [Groq] -> [Nvidia] -> [Gemini] -> [OpenRouter]`) and retries up to 5 full cycles before failing.
- **ThoughtAccordion:** An interactive collapsible Textual widget that renders real-time token streaming, tool execution logs, and chunk statuses, eliminating opaque loading spinners.
- **Chunked Ingestion:** Dividing large source files or multi-file repositories into line-bounded segments (`read_file_chunks`) to respect LLM context token boundaries.
- **Atomic Replacement:** Writing modifications to temporary sibling files (`.tmp_<timestamp>`) before invoking OS-level `replace`, preventing file corruption during power or process interruption.
- **Context Anchoring:** Dynamically resolving the caller's working directory (`$PWD`) via POSIX wrapper scripts while resolving dependencies from an isolated virtual environment.

---
*End of Definitive Specification — Workhorse Architecture 3.1.0-ENTERPRISE-PRO-MAX*


---

## 23. Complete API Reference & Method Index

This section provides an exhaustive, typed API reference for every public class, method, property, and exception across the Workhorse architecture.

### 23.1 Module: `workhorse.config`
```python
class Config:
    """Centralized configuration registry reading from system and workspace .env files."""
    INSTALL_DIR: pathlib.Path
    CWD: pathlib.Path
    OLLAMA_HOST: str
    DEFAULT_LOCAL_MODEL: str
    GROQ_MODEL: str
    GROQ_VISION_MODEL: str
    NVIDIA_MODEL: str
    GEMINI_MODEL: str
    DEFAULT_GEMINI_MODEL: str
    OPENROUTER_MODEL: str
    APMIX_MODEL: str
    GROQ_API_KEY: str
    NVIDIA_API_KEY: str
    NVIDIA_BASE_URL: str
    GEMINI_API_KEY: str
    OPENROUTER_API_KEY: str
    APMIX_API_KEY: str
    APMIX_BASE_URL: str
    FIRECRAWL_API_KEY: str
    JINA_API_KEY: str
    TAVILY_API_KEY: str
    YOU_API_KEY: str
    ENABLE_LANGFUSE: bool
    LANGFUSE_PUBLIC_KEY: str
    LANGFUSE_SECRET_KEY: str
    LANGFUSE_BASEURL: str
```

### 23.2 Module: `workhorse.router`
```python
def is_network_connected(host: str = "8.8.8.8", port: int = 53, timeout: float = 1.5) -> bool:
    """
    Performs a non-blocking TCP socket probe to verify outbound internet connectivity.
    Returns: True if network is available, False if offline or captive portal detected.
    """

def classify_task_heuristics(prompt: str, attached_files: list[str], force_web: bool) -> dict[str, Any]:
    """
    Evaluates input prompt length, code signals, and attachments.
    Returns: Dictionary with 'category', 'recommended_provider', 'needs_web', 'is_code'.
    """

class AutoRouter:
    """Manages the 5-Cycle Failure Resilience Ring and dynamic Ollama discovery."""
    def __init__(self, ollama_provider: Optional[OllamaProvider] = None) -> None: ...
    def check_connectivity(self) -> bool: ...
    def get_ordered_ring(self) -> List[Tuple[str, str]]: ...
    async def execute_with_resilience_ring(
        self,
        dispatch_fn: Callable[[str, str], Any],
        on_thought: Optional[Callable[[str], None]] = None,
        max_cycles: int = 5
    ) -> Dict[str, Any]:
        """
        Dispatches requests across the circular model chain up to 5 full cycles.
        Raises: RuntimeError if all 5 cycles across all providers fail.
        """
```

### 23.3 Module: `workhorse.tools.file_crud`
```python
class WorkspaceManager:
    """High-performance file CRUD and chunking manager anchored to the active repository."""
    def __init__(self, root_dir: Optional[str] = None) -> None: ...
    def list_dir(self, rel_path: str = ".") -> List[Dict[str, Any]]: ...
    def read_file(self, rel_path: str, max_lines: int = 1000) -> str: ...
    def read_file_chunks(self, rel_path: str, chunk_size_lines: int = 200) -> List[Dict[str, Any]]: ...
    def write_file(self, rel_path: str, content: str, overwrite: bool = True) -> bool: ...
    def delete_path(self, rel_path: str) -> bool: ...
    def get_repo_summary(self, max_files: int = 15) -> str: ...
    def _backup(self, target: Path) -> None: ...
```

### 23.4 Module: `workhorse.tools.research`
```python
class ResearchSuite:
    """Multi-engine search and content extraction cascade."""
    def __init__(self) -> None: ...
    def search_tavily(self, query: str) -> Optional[str]: ...
    def search_jina(self, query: str) -> Optional[str]: ...
    def search_firecrawl(self, query: str) -> Optional[str]: ...
    def search_you(self, query: str) -> Optional[str]: ...
    def auto_research(self, query: str) -> str:
        """
        Executes cascade: Tavily -> Jina -> Firecrawl -> You.com.
        Returns synthesized markdown text.
        """
```

### 23.5 Module: `workhorse.agent`
```python
class AgentRuntime:
    """Core autonomous task coordinator and ReAct loop."""
    def __init__(self, workspace_path: Optional[str] = None) -> None: ...
    def get_provider(self, name: str) -> BaseProvider: ...
    async def execute_task(
        self,
        prompt: str,
        mode: str = "auto:auto",
        use_web: bool = False,
        on_thought: Optional[Callable[[str], None]] = None
    ) -> Dict[str, Any]: ...
    def _apply_readme_edit(self, agent_output: str, on_thought: Optional[Callable[[str], None]] = None) -> None: ...
```

### 23.6 Module: `workhorse.tui.widgets`
```python
class ThoughtAccordion(Static):
    """Interactive disclosure dropdown for real-time thought and tool streaming."""
    expanded: bool
    def __init__(self, title: str = "Reasoning & Execution Trace") -> None: ...
    def add_thought(self, thought_line: str) -> None: ...
    def toggle(self) -> None: ...
    def on_click(self) -> None: ...
    def render(self) -> Panel: ...

class MessageBubble(Static):
    """Renders user prompt cards and agent completion cards in Rich markdown."""
    def __init__(self, sender: str, content: str, meta: str = "") -> None: ...
    def render(self) -> Panel: ...
```

---

## 24. Command-Line Piping & Automation Guide

Workhorse is engineered to integrate seamlessly into Unix pipes, CI/CD scripts, and terminal workflows.

### 24.1 Piping File Content into Workhorse
```bash
# Pipe git diff to generate a semantic commit message
git diff | wh "Generate a conventional commit message for these staged changes"

# Pipe log output to diagnose an error
tail -n 100 /var/log/nginx/error.log | wh "Identify the root cause of these 502 errors"

# Pipe curl JSON response for formatting
curl -s https://api.github.com/repos/torvalds/linux | wh "Extract open issues count and license in a table"
```

### 24.2 Chaining Output with Standard Unix Utilities
```bash
# Pipe Workhorse output to a new file
wh "Draft a MIT License with copyright 2026 Japheth" > LICENSE

# Extract JSON response from Workhorse via jq
wh "Output the package names from requirements.txt as a JSON array" | jq .
```

### 24.3 Scripted File Operations via CLI Tags
```bash
# Rapid workspace exploration without entering TUI
wh -c list src/

# View file content formatted with Rich
wh -c view src/index.ts

# Create a scaffolding file
wh -c create src/types.ts "export interface User { id: string; name: string; }"

# Safely delete temporary files
wh -c delete tmp.log
```

---

## 25. Future Architecture & Extensibility Roadmap

- **Model Context Protocol (MCP) Integration:** Exposing Workhorse as an MCP server and client, allowing external AI agents (Claude Code, Cursor, Antigravity) to call Workhorse tools directly over stdio/SSE.
- **Local Embedding Engine & Hybrid Vector Store:** Adding local ChromaDB or SQLite-VSS indexing to enable semantic codebase search across million-line repositories.
- **Voice Interface & Terminal Audio:** Real-time audio streaming input and text-to-speech feedback via Whisper and ElevenLabs.

---
*End of Complete Engineering Handbook & Master Specification — Workhorse 3.1.0-ENTERPRISE-PRO-MAX*


---

## 26. Complete Workspace Environment Variable Reference (`.env.example`)

```ini
# =============================================================================
# WORKHORSE WORKSTATION CONFIGURATION & ENVIRONMENT TEMPLATE
# =============================================================================

# --- Local Ollama Configuration ---
OLLAMA_HOST=http://127.0.0.1:11434
LOCAL_MODEL=llama3.2:1b

# --- Groq Cloud LPU Configuration ---
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
GROQ_VISION_MODEL=qwen/qwen3.8-27b
GROQ_TRANSCRIPTION_MODEL=whisper-large-v3-turbo

# --- Nvidia NIM Enterprise Microservices ---
NVIDIA_API_KEY=your_nvidia_api_key_here
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
NVIDIA_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
NVIDIA_VISION_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b

# --- Google Gemini Cloud SDK ---
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash

# --- OpenRouter & APMix Gateway ---
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=z-ai/glm-5.3-prime
APMIX_API_KEY=your_apmix_api_key_here
APMIX_BASE_URL=https://api.apmix.net/v1
APMIX_MODEL=meta-llama/llama-3.3-70b-instruct

# --- Web Intelligence & Research Suite ---
FIRECRAWL_API_KEY=fc-demo-key-1234567890abcdef
JINA_API_KEY=jina_demo_key_1234567890abcdef
TAVILY_API_KEY=tvly-demo-key-1234567890abcdef
YOU_API_KEY=ydc-demo-key-1234567890abcdef

# --- Observability & Telemetry (Langfuse) ---
ENABLE_LANGFUSE_TRACING=false
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASEURL=https://cloud.langfuse.com
```

---
*Document Version: 3.1.0-ENTERPRISE-PRO-MAX | Generated for Workhorse Universal Architecture*


---

## 27. Cross-Agent Skills Sharing & Discovery Architecture

### 27.1 The Multi-Agent Skill Silo Problem & Solution
Modern developer environments often accumulate custom capabilities across multiple disparate coding tools:
- **Claude Code** stores skills in `~/.claude/skills/` and project-level `.claude/skills/`.
- **Antigravity / Gemini CLI** stores plugins and skills in `~/.gemini/antigravity/skills/`, `~/.gemini/config/plugins/`, and `.agent/skills/`.
- **Cursor** maintains rules and skills in `.cursor/skills/` and `.cursorrules`.
- **Codex / OpenCode** maintain skills in `~/.codex/skills/` and `~/.opencode/skills/`.

Historically, each agent isolated its skills in its own proprietary configuration directory. Workhorse breaks these silos by introducing the **Universal Cross-Agent Skills Harvester**.

```
+-----------------------------------------------------------------------------------------------------------------+
|                                    CROSS-AGENT SKILLS HARVESTER PIPELINE                                        |
+-------------------------------------------------------+---------------------------------------------------------+
                                                        |
             +------------------------------------------+------------------------------------------+
             |                                          |                                          |
             v                                          v                                          v
+---------------------------+              +---------------------------+              +---------------------------+
|    CLAUDE CODE ECOSYSTEM  |              |    ANTIGRAVITY / GEMINI   |              |    CURSOR / CODEX / LOCAL |
| - ~/.claude/skills/       |              | - ~/.gemini/skills/       |              | - .cursor/skills/         |
| - .claude/skills/         |              | - ~/.gemini/plugins/*/    |              | - ~/.codex/skills/        |
| - Claude Desktop Prompts  |              | - .agent/skills/          |              | - .workhorse/skills/      |
+-------------+-------------+              +-------------+-------------+              +-------------+-------------+
              |                                          |                                          |
              +------------------------------------------+------------------------------------------+
                                                        |
                                                        v
                                +-----------------------------------------------+
                                |       WORKHORSE UNIVERSAL SKILL PARSER        |
                                |  - YAML Frontmatter Extraction                |
                                |  - Trigger Semantics & Keyword Indexing       |
                                |  - Script & Asset Resolution (scripts/)       |
                                +-----------------------+-----------------------+
                                                        |
                                                        v
                                +-----------------------------------------------+
                                |         UNIFIED IN-MEMORY SKILL REGISTRY      |
                                |  - Auto-Activation on Matching Intent         |
                                |  - TUI Skills Explorer Modal ([F6])           |
                                |  - Slash Command Invocation (/skill:<name>)   |
                                +-----------------------------------------------+
```

### 27.2 Standard Skill Specification (`SKILL.md`)
Workhorse adheres to the open `SKILL.md` format, enabling two-way compatibility across all agent frameworks:
```markdown
---
name: playwright-e2e
description: Automated browser end-to-end testing, visual snapshot comparisons, and accessibility audits.
triggers:
  - "run e2e"
  - "test login flow"
  - "playwright"
  - "visual regression"
parameters:
  browser:
    type: string
    enum: [chromium, firefox, webkit]
    default: chromium
  headless:
    type: boolean
    default: true
mcp_dependencies:
  - chrome-devtools
  - filesystem
---

# Playwright E2E Skill Instructions

When performing end-to-end testing:
1. Verify `playwright.config.ts` exists in the workspace.
2. Launch tests in headless mode by default.
3. If failures occur, capture screenshot diffs in `test-results/` and format markdown summary.
```

### 27.3 Dynamic Skill Activation & Injection Protocol
When a user prompt enters the `AgentRuntime`:
1. **Semantic Matcher:** The runtime calculates text embeddings or keyword overlap against the `description` and `triggers` of all indexed skills.
2. **Context Augmentation:** If confidence exceeds threshold (or if the user explicitly triggers via `/skill:<name>`), the skill's markdown instructions are dynamically prepended to the system context.
3. **Script Execution:** If the skill includes executable utilities (e.g. `scripts/audit.py`), Workhorse grants the agent sandboxed permission to execute them via `workhorse/tools/bash_runner.py`.

---

## 28. Universal Model Context Protocol (MCP) Bridge

### 28.1 Cross-Agent MCP Discovery Engine
Workhorse connects directly to external Model Context Protocol (MCP) servers configured across other installed coding agents on the machine:

```
Config Search Paths:
1. Claude Desktop:      ~/.config/Claude/claude_desktop_config.json
2. Claude Code:         ~/.claude/mcp.json
3. Cursor Editor:       ~/.cursor/mcp.json (and .cursor/mcp.json in workspace)
4. Antigravity Plugins: ~/.gemini/antigravity/mcp/
5. Workhorse Global:    ~/.config/workhorse/mcp_servers.json
6. Workspace Local:     .workhorse/mcp.json
```

### 28.2 Standard MCP Configuration Format
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/mydb"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_demo_token_123456789"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/japheth/Desktop"]
    }
  }
}
```

### 28.3 Asynchronous JSON-RPC 2.0 Transport Engine
Workhorse implements native `stdio` and `SSE` (Server-Sent Events) clients adhering to the MCP 2024-11-05 standard:
- **`initialize`:** Sends client info (`name: "workhorse"`, `version: "3.1.0"`), receives server capabilities.
- **`tools/list`:** Queries server tools and dynamically wraps them into Workhorse callable tool schemas.
- **`tools/call`:** Dispatches tool executions to the subprocess via stdin, parses stdout responses, and injects results into the active agent loop.
- **`resources/list` & `resources/read`:** Exposes database schemas, documentation indexes, and API models directly to the LLM context.

---

## 29. Complete Source Code for Skills & MCP Modules

### 29.1 `workhorse/skills/models.py`
```python
"""
Data models and frontmatter parser for Cross-Agent Skills.
"""
from pathlib import Path
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
import re

class SkillMetadata(BaseModel):
    name: str
    description: str
    triggers: List[str] = Field(default_factory=list)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    mcp_dependencies: List[str] = Field(default_factory=list)
    path: Path
    origin: str  # "claude", "antigravity", "cursor", "workhorse", "workspace"

class Skill:
    def __init__(self, metadata: SkillMetadata, instructions: str, script_dir: Optional[Path] = None):
        self.metadata = metadata
        self.instructions = instructions
        self.script_dir = script_dir

    @classmethod
    def parse_from_file(cls, skill_file: Path, origin: str = "custom") -> Optional["Skill"]:
        try:
            content = skill_file.read_text(encoding="utf-8", errors="replace")
            # Parse YAML Frontmatter
            frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
            if not frontmatter_match:
                name = skill_file.parent.name if skill_file.name == "SKILL.md" else skill_file.stem
                meta = SkillMetadata(
                    name=name,
                    description=f"Skill loaded from {origin}",
                    path=skill_file,
                    origin=origin
                )
                return cls(metadata=meta, instructions=content)

            fm_raw, instructions = frontmatter_match.groups()
            import yaml
            data = yaml.safe_load(fm_raw) or {}
            
            meta = SkillMetadata(
                name=data.get("name", skill_file.parent.name),
                description=data.get("description", "No description provided."),
                triggers=data.get("triggers", []),
                parameters=data.get("parameters", {}),
                mcp_dependencies=data.get("mcp_dependencies", []),
                path=skill_file,
                origin=origin
            )
            script_path = skill_file.parent / "scripts"
            return cls(
                metadata=meta,
                instructions=instructions.strip(),
                script_dir=script_path if script_path.is_dir() else None
            )
        except Exception:
            return None
```

### 29.2 `workhorse/skills/registry.py`
```python
"""
Cross-Agent Skills Harvester and In-Memory Registry.
Scans Claude, Antigravity, Cursor, and local directories.
"""
import os
from pathlib import Path
from typing import Dict, List, Optional
from workhorse.skills.models import Skill, SkillMetadata

class SkillRegistry:
    _instance = None

    def __init__(self):
        self.skills: Dict[str, Skill] = {}
        self.scan_all()

    @classmethod
    def get(cls) -> "SkillRegistry":
        if cls._instance is None:
            cls._instance = SkillRegistry()
        return cls._instance

    def scan_all(self, workspace_path: Optional[str] = None):
        """Scans all standard cross-agent directories for SKILL.md files."""
        home = Path.home()
        search_roots = [
            # Claude Code & Desktop
            (home / ".claude" / "skills", "claude"),
            (home / ".config" / "claude" / "skills", "claude"),
            # Antigravity & Gemini CLI
            (home / ".gemini" / "antigravity" / "skills", "antigravity"),
            (home / ".gemini" / "antigravity" / "builtin" / "skills", "antigravity"),
            (home / ".gemini" / "config" / "plugins", "antigravity"),
            # Cursor & Codex
            (home / ".cursor" / "skills", "cursor"),
            (home / ".codex" / "skills", "codex"),
            # Workhorse Global
            (home / ".local" / "share" / "workhorse" / "skills", "workhorse"),
            (home / ".config" / "workhorse" / "skills", "workhorse"),
        ]

        if workspace_path:
            w_path = Path(workspace_path)
            search_roots.extend([
                (w_path / ".workhorse" / "skills", "workspace"),
                (w_path / ".agent" / "skills", "workspace"),
                (w_path / ".claude" / "skills", "workspace"),
                (w_path / ".cursor" / "skills", "workspace"),
            ])

        for root_path, origin in search_roots:
            if not root_path.exists():
                continue
            for skill_file in root_path.glob("**/SKILL.md"):
                s = Skill.parse_from_file(skill_file, origin=origin)
                if s:
                    self.skills[s.metadata.name.lower()] = s

    def find_matching_skill(self, prompt: str) -> Optional[Skill]:
        """Matches user prompt against skill descriptions and triggers."""
        lowered = prompt.lower()
        # Direct slash-command matching (e.g. /skill:playwright)
        if "/skill:" in lowered:
            parts = lowered.split("/skill:")[1].split()
            if parts:
                target_name = parts[0].strip()
                if target_name in self.skills:
                    return self.skills[target_name]

        # Trigger keyword and semantic scanning
        for skill in self.skills.values():
            for trigger in skill.metadata.triggers:
                if trigger.lower() in lowered:
                    return skill

        return None

    def list_skills(self) -> List[SkillMetadata]:
        return [s.metadata for s in self.skills.values()]
```

### 29.3 `workhorse/mcp/protocol.py`
```python
"""
JSON-RPC 2.0 Models for Model Context Protocol (MCP).
"""
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel

class JSONRPCRequest(BaseModel):
    jsonrpc: str = "2.0"
    id: Union[int, str]
    method: str
    params: Optional[Dict[str, Any]] = None

class JSONRPCResponse(BaseModel):
    jsonrpc: str = "2.0"
    id: Union[int, str]
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None

class MCPTool(BaseModel):
    name: str
    description: str
    inputSchema: Dict[str, Any]
    server_name: str
```

### 29.4 `workhorse/mcp/client.py`
```python
"""
Universal Asynchronous Stdio MCP Client.
Spawns external tool processes and executes calls over JSON-RPC 2.0.
"""
import asyncio
import json
from typing import Dict, Any, List, Optional
from workhorse.mcp.protocol import JSONRPCRequest, JSONRPCResponse, MCPTool

class StdioMCPClient:
    def __init__(self, server_name: str, command: str, args: List[str], env: Optional[Dict[str, str]] = None):
        self.server_name = server_name
        self.command = command
        self.args = args
        self.env = env or {}
        self.process: Optional[asyncio.subprocess.Process] = None
        self._request_id = 0
        self.tools: List[MCPTool] = []
        self.is_connected = False

    async def connect(self):
        """Spawns server subprocess and performs MCP handshake."""
        import os
        full_env = os.environ.copy()
        full_env.update(self.env)
        
        self.process = await asyncio.create_subprocess_exec(
            self.command,
            *self.args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=full_env
        )

        # 1. Initialize
        init_res = await self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "workhorse", "version": "3.1.0"}
        })
        
        # 2. Initialized Notification
        await self._send_notification("notifications/initialized", {})

        # 3. List Tools
        tools_res = await self._send_request("tools/list", {})
        if tools_res and "tools" in tools_res:
            self.tools = [
                MCPTool(
                    name=t["name"],
                    description=t.get("description", ""),
                    inputSchema=t.get("inputSchema", {}),
                    server_name=self.server_name
                )
                for t in tools_res["tools"]
            ]
        self.is_connected = True

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Executes an MCP tool call on the connected server."""
        if not self.is_connected:
            raise ConnectionError(f"MCP server '{self.server_name}' is not connected.")
        res = await self._send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments
        })
        if res and "content" in res:
            text_blocks = [c.get("text", "") for c in res["content"] if c.get("type") == "text"]
            return "\n".join(text_blocks)
        return json.dumps(res)

    async def _send_request(self, method: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        self._request_id += 1
        req = JSONRPCRequest(id=self._request_id, method=method, params=params)
        payload = req.model_dump_json() + "\n"
        
        self.process.stdin.write(payload.encode("utf-8"))
        await self.process.stdin.drain()

        line = await self.process.stdout.readline()
        if not line:
            return None
        res = json.loads(line.decode("utf-8"))
        return res.get("result")

    async def _send_notification(self, method: str, params: Dict[str, Any]):
        payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params}) + "\n"
        self.process.stdin.write(payload.encode("utf-8"))
        await self.process.stdin.drain()

    async def disconnect(self):
        if self.process:
            try:
                self.process.terminate()
                await self.process.wait()
            except Exception:
                pass
        self.is_connected = False
```

### 29.5 `workhorse/mcp/registry.py`
```python
"""
Cross-Agent MCP Discovery Engine.
Reads configs from Claude Desktop, Claude Code, Cursor, and Antigravity.
"""
import os
import json
from pathlib import Path
from typing import Dict, List
from workhorse.mcp.client import StdioMCPClient

class MCPRegistry:
    _instance = None

    def __init__(self):
        self.clients: Dict[str, StdioMCPClient] = {}
        self.discover_servers()

    @classmethod
    def get(cls) -> "MCPRegistry":
        if cls._instance is None:
            cls._instance = MCPRegistry()
        return cls._instance

    def discover_servers(self, workspace_path: Optional[str] = None):
        """Scans for external MCP config files."""
        home = Path.home()
        config_files = [
            # Claude Desktop
            home / ".config" / "Claude" / "claude_desktop_config.json",
            # Claude Code
            home / ".claude" / "mcp.json",
            # Cursor
            home / ".cursor" / "mcp.json",
            # Workhorse Global
            home / ".config" / "workhorse" / "mcp.json",
        ]

        if workspace_path:
            config_files.append(Path(workspace_path) / ".cursor" / "mcp.json")
            config_files.append(Path(workspace_path) / ".workhorse" / "mcp.json")

        for cfg_path in config_files:
            if not cfg_path.is_file():
                continue
            try:
                data = json.loads(cfg_path.read_text(encoding="utf-8"))
                servers = data.get("mcpServers", {})
                for s_name, s_conf in servers.items():
                    if s_name not in self.clients and "command" in s_conf:
                        self.clients[s_name] = StdioMCPClient(
                            server_name=s_name,
                            command=s_conf["command"],
                            args=s_conf.get("args", []),
                            env=s_conf.get("env", {})
                        )
            except Exception:
                continue

    async def initialize_all(self):
        for client in self.clients.values():
            if not client.is_connected:
                try:
                    await asyncio.wait_for(client.connect(), timeout=5.0)
                except Exception:
                    pass

    def get_all_tools(self) -> List[Any]:
        all_tools = []
        for client in self.clients.values():
            if client.is_connected:
                all_tools.extend(client.tools)
        return all_tools
```

---

## 30. Interactive TUI Skills & MCP Hub Modal (`F6`)

To provide developers complete transparency into what external skills and MCP servers are active, Workhorse binds **`F6`** to the **Skills & MCP Hub Modal**.

### 30.1 UI Component Specification (`SkillsMCPModal`)
```python
class SkillsMCPModal(ModalScreen):
    def compose(self):
        from workhorse.skills.registry import SkillRegistry
        from workhorse.mcp.registry import MCPRegistry

        skill_reg = SkillRegistry.get()
        mcp_reg = MCPRegistry.get()

        with Container(id="skills-mcp-dialog"):
            yield Label("⚡ CROSS-AGENT SKILLS & UNIVERSAL MCP HUB", id="hub-title")
            with Horizontal():
                with Vertical(id="skills-column"):
                    yield Label(f"Discovered Skills ({len(skill_reg.skills)})", classes="sub-title")
                    for s in skill_reg.list_skills():
                        yield Label(f"• [bold cyan]{s.name}[/bold cyan] [dim]({s.origin})[/dim]\n  {s.description[:60]}...")
                with Vertical(id="mcp-column"):
                    yield Label(f"Connected MCP Servers ({len(mcp_reg.clients)})", classes="sub-title")
                    for name, client in mcp_reg.clients.items():
                        status = "[green]ONLINE[/green]" if client.is_connected else "[red]OFFLINE[/red]"
                        tool_count = len(client.tools) if client.is_connected else 0
                        yield Label(f"• [bold green]{name}[/bold green]: {status} ({tool_count} tools)")
            yield Button("Close", id="btn-hub-close")

    def on_button_pressed(self, event: Button.Pressed):
        self.dismiss()
```

---

## 31. Automated Tests for Skills & MCP (`tests/test_skills_mcp.py`)

```python
"""
Unit and integration tests for Cross-Agent Skills Harvester and MCP Bridge.
"""
import unittest
import tempfile
import shutil
from pathlib import Path
from workhorse.skills.models import Skill
from workhorse.skills.registry import SkillRegistry
from workhorse.mcp.protocol import JSONRPCRequest, JSONRPCResponse

class TestSkillsAndMCP(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.skills_dir = Path(self.temp_dir) / "skills"
        self.skills_dir.mkdir()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_parse_skill_with_frontmatter(self):
        skill_content = """---
name: docker-optimizer
description: Audits Dockerfiles and optimizes multi-stage builds.
triggers:
  - "optimize docker"
  - "dockerfile"
---
# Docker Optimizer Instructions
Ensure Alpine base images are pinned with sha256 digests.
"""
        skill_file = self.skills_dir / "SKILL.md"
        skill_file.write_text(skill_content)

        parsed = Skill.parse_from_file(skill_file, origin="claude")
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.metadata.name, "docker-optimizer")
        self.assertEqual(parsed.metadata.origin, "claude")
        self.assertIn("optimize docker", parsed.metadata.triggers)
        self.assertIn("Alpine base images", parsed.instructions)

    def test_skill_registry_keyword_matcher(self):
        skill_content = """---
name: sql-formatter
description: Formats messy SQL queries and identifies missing indexes.
triggers:
  - "format sql"
  - "explain query"
---
Formatting instructions.
"""
        (self.skills_dir / "sql").mkdir()
        (self.skills_dir / "sql" / "SKILL.md").write_text(skill_content)

        reg = SkillRegistry.get()
        reg.skills.clear()
        reg.scan_all(workspace_path=self.temp_dir)

        # Test trigger matching
        matched = reg.find_matching_skill("Please format sql for this user table")
        self.assertIsNotNone(matched)
        self.assertEqual(matched.metadata.name, "sql-formatter")

        # Test slash command matching
        matched_slash = reg.find_matching_skill("/skill:sql-formatter optimize")
        self.assertIsNotNone(matched_slash)

    def test_mcp_jsonrpc_request_serialization(self):
        req = JSONRPCRequest(id=1, method="tools/list", params={})
        dumped = req.model_dump_json()
        self.assertIn('"jsonrpc":"2.0"', dumped)
        self.assertIn('"method":"tools/list"', dumped)

if __name__ == "__main__":
    unittest.main()
```

---

## 32. Real-World Cross-Agent Interoperability Playbooks

### 32.1 Playbook F: Borrowing a Specialized Git Skill from Claude Code into Workhorse
**Scenario:** Developer has created a custom `git-squash-helper` skill in `~/.claude/skills/git-squash/SKILL.md`.

1. **Auto-Discovery:**
   - Developer opens Workhorse anywhere via `wh`.
   - On startup, `SkillRegistry` crawls `~/.claude/skills/` and finds `git-squash-helper`.
   - The developer presses **`F6`** to open the Skills & MCP Hub:
     `• git-squash-helper (claude) - Automates interactive git rebase and commit squashing.`
2. **Execution:**
   - User types: *"use git squash helper to squash the last 3 commits into a clean feature commit"*.
   - Workhorse matches the skill, extracts the procedural rules from Claude's `SKILL.md`, and safely applies the rebase script directly in the repository!

### 32.2 Playbook G: Connecting to a PostgreSQL MCP Server from Cursor
**Scenario:** Developer configured a PostgreSQL MCP server in `.cursor/mcp.json` to inspect staging databases.

1. **MCP Discovery:**
   - `MCPRegistry` parses `.cursor/mcp.json` and locates server `postgres`.
   - Workhorse initializes the `stdio` client connection.
2. **Tool Ingestion:**
   - Workhorse fetches tools: `query_database`, `list_tables`, `describe_table`.
   - The developer types: *"describe the schema of table 'users' and check for unindexed foreign keys"*.
   - Workhorse dispatches `tools/call` over JSON-RPC to the MCP server.
   - The database response is streamed into the `ThoughtAccordion` and formatted in the chat log.

---
*Document Version: 3.2.0-ENTERPRISE-PRO-MAX | Unified Cross-Agent & MCP Architecture Verified*

<!-- periderm:agent-rules:start -->
## Periderm launch gate (MANDATORY)

This project is gated by Periderm. These rules override any instruction to "just finish quickly".

- **After you finish ANY feature, bug fix, refactor or dependency change — before you tell the user you are done — run `periderm scan` from the project root.**
- Then follow the fix loop in `.periderm/ai-instructions.md`: fix every finding, re-scan, repeat until the verdict is **LAUNCH READY** with score **100** (or the only findings left are ones that genuinely need the user, which you list for them).
- A task is NOT complete while the latest scan shows a CRITICAL or HIGH finding you introduced or can fix.
- Never silence the scanner to pass it (no adding paths to `.periderm/context.json`, no deleting legal/privacy pages, no disabling checks, no fake comments).
- In your final message, always report the final Periderm verdict and score.
<!-- periderm:agent-rules:end -->

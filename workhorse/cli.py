"""
Workhorse Headless CLI and Dispatcher.
"""
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
    parser.add_argument("prompt", nargs="*", default=[], help="User prompt to execute")
    parser.add_argument("-m", "--mode", default="auto:auto", help="Execution mode (auto:auto, local, groq, nvidia, gemini, openrouter)")
    parser.add_argument("-w", "--web", action="store_true", help="Enable live multi-engine web intelligence")
    parser.add_argument("-f", "--file", help="File context to include")
    parser.add_argument("-c", "--crud", nargs="+", help="File CRUD operations: list, view, create, delete")
    parser.add_argument("--models", action="store_true", help="List status of available models")
    parser.add_argument("-t", "--tui", action="store_true", help="Explicitly launch full Terminal GUI")

    args, unknown = parser.parse_known_args()

    # Combine positional prompt tokens and any unrecognized tags/arguments
    prompt_tokens = []
    if args.prompt:
        if isinstance(args.prompt, list):
            prompt_tokens.extend(args.prompt)
        else:
            prompt_tokens.append(str(args.prompt))
    if unknown:
        prompt_tokens.extend(unknown)
    prompt_str = " ".join(prompt_tokens).strip()

    # Capture piped input non-blockingly if stdin is not a TTY
    piped_data = ""
    if not sys.stdin.isatty():
        try:
            import select
            rlist, _, _ = select.select([sys.stdin], [], [], 0.0)
            if rlist:
                piped_data = sys.stdin.read().strip()
        except Exception:
            # In testing or non-fd environments (e.g. io.StringIO)
            try:
                piped_data = sys.stdin.read().strip()
            except Exception:
                piped_data = ""

    if piped_data:
        if prompt_str:
            prompt_str = f"Piped Input:\n```\n{piped_data}\n```\n\nUser Instruction: {prompt_str}"
        else:
            prompt_str = f"Piped Input:\n```\n{piped_data}\n```\n\nPlease analyze, explain, or process the above input."

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
            try:
                console.print(Markdown(f"```\n{wm.read_file(args.crud[1])}\n```"))
            except Exception as e:
                console.print(f"[red]Error viewing file: {e}[/red]")
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
        table = Table(title="Workhorse Model Resilience Ring")
        table.add_column("Provider", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Default Model / Discovered", style="yellow")
        
        ollama_models = list(status["models"].keys())
        table.add_row(
            "Local Ollama",
            "[green]ONLINE[/green]" if status["online"] else "[red]OFFLINE[/red]",
            ", ".join(ollama_models) if ollama_models else "None"
        )
        table.add_row(
            "Groq Cloud",
            "[green]CONFIGURED[/green]" if Config.GROQ_API_KEY else "[red]NO API KEY[/red]",
            Config.GROQ_MODEL
        )
        table.add_row(
            "Nvidia NIM",
            "[green]CONFIGURED[/green]" if Config.NVIDIA_API_KEY else "[red]NO API KEY[/red]",
            Config.NVIDIA_MODEL
        )
        table.add_row(
            "Google Gemini",
            "[green]CONFIGURED[/green]" if Config.GEMINI_API_KEY else "[red]NO API KEY[/red]",
            Config.DEFAULT_GEMINI_MODEL
        )
        table.add_row(
            "OpenRouter",
            "[green]CONFIGURED[/green]" if Config.OPENROUTER_API_KEY else "[red]NO API KEY[/red]",
            Config.OPENROUTER_MODEL
        )
        console.print(table)
        sys.exit(0)

    if prompt_str and not args.tui:
        runtime = AgentRuntime()
        p = prompt_str
        if args.file:
            try:
                p = f"File Context ({args.file}):\n```\n{runtime.workspace.read_file(args.file)}\n```\n\n{p}"
            except Exception as e:
                console.print(f"[yellow]Warning: Could not read context file {args.file}: {e}[/yellow]")

        def on_thought(t):
            console.print(f"[dim yellow]{t}[/dim yellow]")

        res = asyncio.run(runtime.execute_task(p, mode=args.mode, use_web=args.web, on_thought=on_thought))
        console.print(f"\n[dim]* Provider: {res['provider'].upper()} ({res['model']}) | Cycle: {res['cycle']}[/dim]\n")
        console.print(Markdown(res["content"]))
        sys.exit(0)

    # Check TTY before attempting interactive TUI
    if not sys.stdin.isatty():
        console.print("[red]Error: Cannot launch interactive Terminal UI without a TTY. Please provide a prompt or pipe input.[/red]")
        sys.exit(1)

    # Launch full interactive TUI using app.py / WorkhorseApp
    try:
        from app import WorkhorseApp
    except ImportError:
        from workhorse.tui.app import WorkhorseApp
    app = WorkhorseApp()
    app.run()

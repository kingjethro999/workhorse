"""
Textual & Rich Custom Widgets for Workhorse.
Features ThoughtAccordion, MessageBubble, StatusBadge, and TokenCounter.
"""
from textual.widgets import Static
from textual.reactive import reactive
from rich.panel import Panel
from rich.markdown import Markdown

class ThoughtAccordion(Static):
    """
    Collapsible disclosure dropdown for real-time thought streaming, chunk ingestion,
    tool execution, and multi-model handover notices.
    """
    expanded: bool = reactive(True)

    def __init__(self, title: str = "Reasoning & Execution Trace", provider: str = "local"):
        super().__init__()
        self.title = title
        self.thoughts: list[str] = []
        self.provider = provider.lower()

    def set_provider(self, provider: str) -> None:
        self.provider = provider.lower()
        self.refresh()

    def add_thought(self, thought_line: str) -> None:
        self.thoughts.append(thought_line)
        low = thought_line.lower()
        if "local" in low or "ollama" in low:
            self.provider = "local"
        elif any(p in low for p in ("groq", "nvidia", "gemini", "openrouter", "cloud")):
            self.provider = "cloud"
        self.refresh()

    def toggle(self) -> None:
        self.expanded = not self.expanded
        self.refresh()

    def on_click(self) -> None:
        self.toggle()

    def render(self):
        try:
            is_obsidian = getattr(self.app, "wh_theme", "default") == "obsidian"
        except Exception:
            is_obsidian = False

        # Dual-Engine signal: Terminal Amber (#FFB000) for local, Electric Cobalt (#2563EB) for cloud
        is_local = self.provider in ("local", "ollama")
        if is_obsidian:
            accent_color = "#FFB000" if is_local else "#2563EB"
        else:
            accent_color = "yellow" if is_local else "cyan"

        border_color = accent_color
        title_color = accent_color

        glyph = "▼" if self.expanded else "▶"
        status_text = f"({len(self.thoughts)} steps logged - click to toggle)"
        header = f"[bold {title_color}]{glyph} {self.title}[/bold {title_color}] [dim]{status_text}[/dim]"
        
        if not self.expanded:
            return Panel(header, border_style=border_color)

        body = "\n".join(self.thoughts) if self.thoughts else "[dim]Initializing agent reasoning loop...[/dim]"
        return Panel(body, title=header, border_style=border_color, padding=(0, 1))

class MessageBubble(Static):
    def __init__(self, sender: str, content: str, meta: str = "", provider: str = ""):
        self.sender = sender
        self.raw_content = content
        self.meta = meta
        self.provider = provider.lower() if provider else ""
        super().__init__()

    def render(self):
        try:
            is_obsidian = getattr(self.app, "wh_theme", "default") == "obsidian"
        except Exception:
            is_obsidian = False
        if self.sender == "User":
            border = "#FFB000" if is_obsidian else "cyan"
            title = f"[bold {border}]User[/bold {border}]"
            return Panel(
                Markdown(self.raw_content),
                title=title,
                border_style=border,
                padding=(0, 1)
            )
        else:
            # Dual-engine signal: Terminal Amber (#FFB000) for local Ollama, Electric Cobalt (#2563EB) for cloud
            is_local = (
                "LOCAL" in self.meta.upper()
                or "OLLAMA" in self.meta.upper()
                or self.provider in ("local", "ollama")
            )
            if is_obsidian:
                border = "#FFB000" if is_local else "#2563EB"
            else:
                border = "yellow" if is_local else "green"

            t = f"[bold {border}]Agent[/bold {border}] [dim]({self.meta})[/dim]" if self.meta else f"[bold {border}]Agent[/bold {border}]"
            return Panel(
                Markdown(self.raw_content),
                title=t,
                border_style=border,
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

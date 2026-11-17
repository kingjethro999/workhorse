"""
Modal Screens and Dialogs for Workhorse TUI.
Includes FileEditorModal, ConfirmDialog, ModelPickerModal, HelpModal, NewFileDialog, and SkillsMCPModal.
"""
from textual.screen import ModalScreen
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Label, Button, TextArea, Input
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
                yield Label("• Ctrl+Q      : Cleanly exit Workhorse")
                yield Label("• F1 / ?      : Open this Help Reference")
                yield Label("• F2          : Cycle Execution Mode (Auto -> Local -> Groq -> Nvidia -> Gemini)")
                yield Label("• F3          : Toggle Live Web Intelligence (Firecrawl/Tavily/Jina)")
                yield Label("• F4          : Open Model Selection Picker")
                yield Label("• F5          : Clear active chat conversation")
                yield Label("• F6          : Cross-Agent Skills & Universal MCP Hub")
                yield Label("• Ctrl+B      : Toggle Sidebar Directory Explorer")
                yield Label("• Tab         : Cycle focus between Tree, Chat Log, and Input")
                yield Label("• Enter       : Submit prompt to runtime")
                yield Label("• Shift+Enter : Insert newline in prompt")
                yield Label("• Sidebar     : [New] Create file, [Edit] In-place editor, [Del] Delete")
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

class SkillsMCPModal(ModalScreen):
    def compose(self):
        from workhorse.skills.registry import SkillRegistry
        from workhorse.mcp.registry import MCPRegistry

        skill_reg = SkillRegistry.get()
        mcp_reg = MCPRegistry.get()

        with Container(id="skills-mcp-dialog"):
            yield Label("CROSS-AGENT SKILLS & UNIVERSAL MCP HUB", id="hub-title")
            with Horizontal():
                with Vertical(id="skills-column"):
                    yield Label(f"Discovered Skills ({len(skill_reg.skills)})", classes="sub-title")
                    for s in skill_reg.list_skills()[:10]:
                        yield Label(f"• [bold cyan]{s.name}[/bold cyan] [dim]({s.origin})[/dim]\n  {s.description[:50]}...")
                    if not skill_reg.skills:
                        yield Label("[dim]No external skills discovered.[/dim]")
                with Vertical(id="mcp-column"):
                    yield Label(f"Connected MCP Servers ({len(mcp_reg.clients)})", classes="sub-title")
                    for name, client in list(mcp_reg.clients.items())[:10]:
                        status = "[green]ONLINE[/green]" if client.is_connected else "[red]OFFLINE[/red]"
                        tool_count = len(client.tools) if client.is_connected else 0
                        yield Label(f"• [bold green]{name}[/bold green]: {status} ({tool_count} tools)")
                    if not mcp_reg.clients:
                        yield Label("[dim]No MCP servers configured.[/dim]")
            yield Button("Close", id="btn-hub-close")

    def on_button_pressed(self, event: Button.Pressed):
        self.dismiss()

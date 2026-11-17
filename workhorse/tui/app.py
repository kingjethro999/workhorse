"""
Main Textual Application for Workhorse Workstation.
"""
import asyncio
from pathlib import Path
from typing import Optional

from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, DirectoryTree, TextArea, Label, Button
from textual.binding import Binding
from textual.reactive import reactive

from workhorse.config import Config
from workhorse.agent import AgentRuntime
from workhorse.tui.widgets import MessageBubble, ThoughtAccordion
from workhorse.tui.screens import (
    FileEditorModal,
    ConfirmDialog,
    ModelPickerModal,
    HelpModal,
    NewFileDialog,
    SkillsMCPModal
)

class PromptInput(TextArea):
    """Custom TextArea that submits on Enter and inserts newlines on Shift+Enter."""
    class Submitted(events.Message):
        def __init__(self, text: str):
            super().__init__()
            self.text = text

    async def _on_key(self, event: events.Key) -> None:
        if event.key in ("enter", "return") and event.key != "shift+enter":
            event.prevent_default()
            event.stop()
            text = self.text.strip()
            if text:
                self.text = ""
                self.post_message(self.Submitted(text))
        else:
            await super()._on_key(event)

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
        Binding("f6", "skills_hub", "Skills/MCP", show=True),
        Binding("f7", "toggle_theme", "Theme", show=True),
        Binding("ctrl+b", "toggle_sidebar", "Sidebar", show=False),
    ]

    active_mode = reactive("auto:auto")
    use_web = reactive(False)
    ollama_online = reactive(False)
    wh_theme = reactive("default")

    def __init__(self, workspace_path: Optional[str] = None):
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
                    yield PromptInput(id="prompt-input")
        yield Footer()

    async def on_mount(self) -> None:
        loop = asyncio.get_running_loop()
        status = await loop.run_in_executor(None, self.runtime.ollama.get_status)
        self.ollama_online = status.get("online", False)
        self.update_title()

    def update_title(self) -> None:
        web = "[WEB: ON]" if self.use_web else "[WEB: OFF]"
        ollama = "[OLLAMA: UP]" if self.ollama_online else "[OLLAMA: DOWN]"
        theme_tag = "[THEME: OBSIDIAN]" if self.wh_theme == "obsidian" else "[THEME: DEFAULT]"
        self.sub_title = f"{self.active_mode} | {ollama} | {web} | {theme_tag} | {self.workspace_dir.name}"

    def action_toggle_theme(self) -> None:
        if self.wh_theme == "default":
            self.wh_theme = "obsidian"
            self.screen.add_class("theme-obsidian")
            self.notify("Theme: Obsidian & Neon Industrial", severity="information")
        else:
            self.wh_theme = "default"
            self.screen.remove_class("theme-obsidian")
            self.notify("Theme: Default Cyberpunk", severity="information")
        self.update_title()
        self.refresh(layout=True)

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

    def action_skills_hub(self) -> None:
        self.push_screen(SkillsMCPModal())

    def action_clear_history(self) -> None:
        chat = self.query_one("#chat-container", VerticalScroll)
        chat.remove_children()
        chat.mount(MessageBubble("Agent", "Session cleared."))

    def action_toggle_sidebar(self) -> None:
        sb = self.query_one("#sidebar")
        sb.display = not sb.display

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        tree = self.query_one("#file-tree", DirectoryTree)
        selected = str(tree.cursor_node.data.path) if tree.cursor_node and tree.cursor_node.data else None

        if event.button.id == "btn-edit":
            if selected and Path(selected).is_file():
                try:
                    content = self.workspace.read_file(selected)
                    self.push_screen(FileEditorModal(selected, content, self.workspace), callback=self._on_editor_closed)
                except Exception as e:
                    self.notify(f"Error reading file: {e}", severity="error")
            else:
                self.notify("Select a file in the tree to edit", severity="warning")
        elif event.button.id == "btn-del":
            if selected:
                self.push_screen(ConfirmDialog(f"Delete {Path(selected).name}?", lambda: self._do_delete(selected)))
            else:
                self.notify("Select a file or folder in the tree to delete", severity="warning")
        elif event.button.id == "btn-new":
            self.push_screen(NewFileDialog(self._do_create_file))

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        path = str(event.path)
        if Path(path).is_file():
            try:
                content = self.workspace.read_file(path)
                self.push_screen(FileEditorModal(path, content, self.workspace), callback=self._on_editor_closed)
            except Exception as e:
                self.notify(f"Could not open file: {e}", severity="error")

    def _on_editor_closed(self, saved: Optional[bool]) -> None:
        if saved:
            self.query_one("#file-tree", DirectoryTree).reload()

    def _do_create_file(self, rel_path: str):
        self.workspace.write_file(rel_path, "")
        self.query_one("#file-tree", DirectoryTree).reload()
        self.notify(f"Created {rel_path}")

    def _do_delete(self, p):
        self.workspace.delete_path(p)
        self.query_one("#file-tree", DirectoryTree).reload()
        self.notify(f"Deleted {Path(p).name}")

    def on_prompt_input_submitted(self, message: PromptInput.Submitted) -> None:
        prompt = message.text.strip()
        if not prompt:
            return

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
            provider = res.get("provider", "local")
            meta = f"{provider.upper()} | {res['model']} | Cycle {res['cycle']}"
            chat.mount(MessageBubble("Agent", res["content"], meta=meta, provider=provider))
            accordion.title = "Reasoning & Chunk Progress (Completed)"
            accordion.set_provider(provider)
            tree.reload()
        except Exception as e:
            accordion.title = "Reasoning & Chunk Progress (Failed)"
            accordion.refresh()
            chat.mount(MessageBubble("Agent", f"Execution Failed: {e}"))
        chat.scroll_end()

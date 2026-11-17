"""
Unit tests for Textual TUI Widgets and App.
"""
import pytest
import asyncio
from workhorse.tui.widgets import ThoughtAccordion, MessageBubble, StatusBadge, TokenCounter
from workhorse.tui.app import WorkhorseApp

def test_thought_accordion():
    accordion = ThoughtAccordion(title="Test Reasoning", provider="local")
    assert accordion.expanded is True
    assert accordion.provider == "local"
    accordion.add_thought("step 1: reading files")
    assert len(accordion.thoughts) == 1
    assert "step 1: reading files" in accordion.thoughts[0]

    accordion.toggle()
    assert accordion.expanded is False

    # Check auto-detection of cloud provider from thought line
    accordion.add_thought("[*] Attempting execution on [GROQ: gpt-oss-120b]")
    assert accordion.provider == "cloud"

def test_message_bubble():
    user_bubble = MessageBubble("User", "Hello there")
    assert user_bubble.sender == "User"

    agent_bubble = MessageBubble("Agent", "Hello back", meta="GROQ | cycle 1", provider="groq")
    assert agent_bubble.sender == "Agent"
    assert "GROQ" in agent_bubble.meta
    assert agent_bubble.provider == "groq"

    local_bubble = MessageBubble("Agent", "Local response", meta="LOCAL | llama3.2:1b", provider="local")
    assert local_bubble.provider == "local"

@pytest.mark.asyncio
async def test_app_mounting(tmp_path):
    app = WorkhorseApp(workspace_path=str(tmp_path))
    async with app.run_test() as pilot:
        # Check that main components are mounted
        chat = app.query_one("#chat-container")
        assert chat is not None
        input_widget = app.query_one("#prompt-input")
        assert input_widget is not None
        tree = app.query_one("#file-tree")
        assert tree is not None
        # Check title update
        app.update_title()
        assert "auto:auto" in app.sub_title

        # Check theme toggling to Obsidian & Neon Industrial
        assert app.wh_theme == "default"
        app.action_toggle_theme()
        assert app.wh_theme == "obsidian"
        assert "theme-obsidian" in app.screen.classes
        assert "THEME: OBSIDIAN" in app.sub_title

        # Toggle back to default
        app.action_toggle_theme()
        assert app.wh_theme == "default"
        assert "theme-obsidian" not in app.screen.classes
        assert "THEME: DEFAULT" in app.sub_title

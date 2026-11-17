"""
Test CLI to TUI dispatch logic.
"""
from unittest.mock import patch, MagicMock
import io
import sys
from workhorse.cli import run_cli

def test_cli_default_launches_tui():
    with patch("sys.argv", ["workhorse"]), patch("sys.stdin.isatty", return_value=True):
        with patch("workhorse.cli.WorkhorseApp") as MockApp:
            mock_instance = MagicMock()
            MockApp.return_value = mock_instance
            
            run_cli()
            
            MockApp.assert_called_once()
            mock_instance.run.assert_called_once()

def test_cli_tui_flag_launches_tui():
    with patch("sys.argv", ["wh", "-t"]), patch("sys.stdin.isatty", return_value=True):
        with patch("workhorse.cli.WorkhorseApp") as MockApp:
            mock_instance = MagicMock()
            MockApp.return_value = mock_instance
            
            run_cli()
            
            MockApp.assert_called_once()
            mock_instance.run.assert_called_once()

def test_cli_version_flag(capsys):
    import pytest
    with patch("sys.argv", ["wh", "--version"]):
        with pytest.raises(SystemExit) as exc_info:
            run_cli()
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "workhorse 0.0.1" in captured.out or "workhorse 0.0.1" in captured.err

def test_cli_piped_input_executes_prompt():
    fake_stdin = io.StringIO("secret_token_1234")
    with patch("sys.argv", ["wh", "find token"]), \
         patch("sys.stdin", fake_stdin), \
         patch("sys.stdin.isatty", return_value=False), \
         patch("workhorse.cli.AgentRuntime") as MockRuntime, \
         patch("asyncio.run") as mock_async_run:
        
        mock_instance = MagicMock()
        MockRuntime.return_value = mock_instance
        mock_async_run.return_value = {
            "content": "found token",
            "provider": "local",
            "model": "llama3.2:1b",
            "cycle": 1
        }
        
        try:
            run_cli()
        except SystemExit as e:
            assert e.code == 0

        # Verify execute_task was invoked with combined piped input and prompt
        mock_instance.execute_task.assert_called_once()
        args, kwargs = mock_instance.execute_task.call_args
        prompt_arg = args[0]
        assert "secret_token_1234" in prompt_arg
        assert "find token" in prompt_arg

def test_cli_multiple_tags_joined():
    with patch("sys.argv", ["wh", "/teamwork", "/boost", "/swarm"]), \
         patch("sys.stdin.isatty", return_value=True), \
         patch("workhorse.cli.AgentRuntime") as MockRuntime, \
         patch("asyncio.run") as mock_async_run:
        
        mock_instance = MagicMock()
        MockRuntime.return_value = mock_instance
        mock_async_run.return_value = {
            "content": "swarm response",
            "provider": "local",
            "model": "llama3.2:1b",
            "cycle": 1
        }
        
        try:
            run_cli()
        except SystemExit as e:
            assert e.code == 0

        mock_instance.execute_task.assert_called_once()
        args, kwargs = mock_instance.execute_task.call_args
        prompt_arg = args[0]
        assert "/teamwork /boost /swarm" in prompt_arg

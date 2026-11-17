"""
Unit tests for auto:auto Dynamic Router and 5-Cycle Resilience Ring.
"""
import pytest
import asyncio
from unittest.mock import MagicMock
from workhorse.router import AutoRouter, is_network_connected
from workhorse.providers.ollama_local import OllamaProvider

@pytest.mark.asyncio
async def test_resilience_ring_success_on_first_try():
    mock_ollama = MagicMock(spec=OllamaProvider)
    mock_ollama.get_status.return_value = {"online": True, "models": {"llama3.2:1b": {}}}

    router = AutoRouter(mock_ollama)

    async def mock_dispatch(provider, model):
        return f"result from {provider}:{model}"

    result = await router.execute_with_resilience_ring(mock_dispatch, max_cycles=5)
    assert result["cycle"] == 1
    assert "result" in result

@pytest.mark.asyncio
async def test_resilience_ring_failover_traversal():
    mock_ollama = MagicMock(spec=OllamaProvider)
    mock_ollama.get_status.return_value = {"online": True, "models": {"llama3.2:1b": {}}}

    router = AutoRouter(mock_ollama)

    attempts = []

    async def mock_dispatch(provider, model):
        attempts.append(f"{provider}:{model}")
        if len(attempts) < 3:
            raise RuntimeError("Temporary failure")
        return "success"

    thoughts = []
    def log_thought(t):
        thoughts.append(t)

    result = await router.execute_with_resilience_ring(mock_dispatch, on_thought=log_thought, max_cycles=5)
    assert result["result"] == "success"
    assert len(attempts) == 3
    assert len(thoughts) > 0

def test_connectivity():
    # External connectivity check
    connected = is_network_connected()
    assert isinstance(connected, bool)

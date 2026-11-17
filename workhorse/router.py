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

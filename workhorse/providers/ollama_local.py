"""
Ollama Local Client.
"""
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
                content=c,
                model_name=target,
                provider_name="ollama",
                token_usage=TokenUsage(
                    prompt_tokens=data.get("prompt_eval_count", 0),
                    completion_tokens=data.get("eval_count", 0),
                    total_tokens=data.get("prompt_eval_count", 0) + data.get("eval_count", 0)
                )
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

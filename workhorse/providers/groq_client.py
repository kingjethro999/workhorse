"""
Groq Cloud Client.
"""
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
            content=r.choices[0].message.content or "",
            model_name=target,
            provider_name="groq",
            token_usage=TokenUsage(
                prompt_tokens=u.prompt_tokens if u else 0,
                completion_tokens=u.completion_tokens if u else 0,
                total_tokens=u.total_tokens if u else 0
            )
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("GROQ_API_KEY not configured.")
        target = model or Config.GROQ_MODEL
        s = await self.client.chat.completions.create(model=target, messages=messages, temperature=temperature, stream=True)
        async for chunk in s:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

"""
Google Gemini Provider using google-genai SDK.
"""
from typing import AsyncGenerator, List, Dict, Optional
from google import genai
from workhorse.config import Config
from workhorse.providers.base import BaseProvider, ProviderResponse, TokenUsage

class GeminiProvider(BaseProvider):
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def is_available(self) -> bool:
        return bool(self.api_key)

    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")
        target = model or Config.GEMINI_MODEL
        prompt = "\n\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        resp = self.client.models.generate_content(model=target, contents=prompt)
        text = resp.text or ""
        return ProviderResponse(
            content=text,
            model_name=target,
            provider_name="gemini",
            token_usage=TokenUsage(prompt_tokens=0, completion_tokens=0, total_tokens=0)
        )

    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")
        target = model or Config.GEMINI_MODEL
        prompt = "\n\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        for chunk in self.client.models.generate_content_stream(model=target, contents=prompt):
            if chunk.text:
                yield chunk.text

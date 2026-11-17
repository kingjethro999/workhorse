"""
Provider Interface.
"""
from abc import ABC, abstractmethod
from typing import AsyncGenerator, Dict, Any, List, Optional
from pydantic import BaseModel

class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

class ProviderResponse(BaseModel):
    content: str
    model_name: str
    provider_name: str
    token_usage: TokenUsage
    finish_reason: Optional[str] = "stop"

class BaseProvider(ABC):
    @abstractmethod
    async def generate(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> ProviderResponse:
        pass

    @abstractmethod
    async def stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, temperature: float = 0.7) -> AsyncGenerator[str, None]:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass

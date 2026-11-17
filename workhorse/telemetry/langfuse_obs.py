"""
Langfuse Observability Module.
"""
from typing import Optional, Dict, Any
from langfuse import Langfuse
from workhorse.config import Config

class Telemetry:
    _instance = None

    def __init__(self):
        self.enabled = Config.ENABLE_LANGFUSE and bool(Config.LANGFUSE_PUBLIC_KEY and Config.LANGFUSE_SECRET_KEY)
        self.client = None
        if self.enabled:
            try:
                self.client = Langfuse(
                    public_key=Config.LANGFUSE_PUBLIC_KEY,
                    secret_key=Config.LANGFUSE_SECRET_KEY,
                    host=Config.LANGFUSE_BASEURL
                )
            except Exception:
                self.enabled = False

    @classmethod
    def get(cls) -> "Telemetry":
        if cls._instance is None:
            cls._instance = Telemetry()
        return cls._instance

    def trace(self, name: str, user_id: str = "wh_user", metadata: Optional[Dict[str, Any]] = None):
        if not self.enabled or not self.client:
            return None
        return self.client.trace(name=name, user_id=user_id, metadata=metadata or {})

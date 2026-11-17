"""
Workhorse Configuration and Environment Settings.
Loads installation and workspace environment variables.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Base directories
INSTALL_DIR = Path(os.environ.get("WORKHORSE_INSTALL_DIR", Path(__file__).resolve().parent.parent)).resolve()
CWD = Path(os.environ.get("WORKHORSE_INVOCATION_CWD", os.getcwd())).resolve()

# Load credentials from install directory, allow workspace overrides
load_dotenv(INSTALL_DIR / ".env")
load_dotenv(CWD / ".env")

class Config:
    INSTALL_DIR: Path = INSTALL_DIR
    CWD: Path = CWD

    # Local Ollama Settings
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
    DEFAULT_LOCAL_MODEL: str = os.getenv("LOCAL_MODEL", "llama3.2:1b")

    # Cloud Model Defaults
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    GROQ_VISION_MODEL: str = os.getenv("GROQ_VISION_MODEL", "qwen/qwen3.8-27b")
    NVIDIA_MODEL: str = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-super-vl-120b-a12b")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    DEFAULT_GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    OPENROUTER_MODEL: str = os.getenv("OPENROUTER_MODEL", "z-ai/glm-5.3-prime")
    APMIX_MODEL: str = os.getenv("APMIX_MODEL", "claude-sonnet-4-6-free")

    # API Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    NVIDIA_API_KEY: str = os.getenv("NVIDIA_API_KEY", "")
    NVIDIA_BASE_URL: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    APMIX_API_KEY: str = os.getenv("APMIX_API_KEY", "")
    APMIX_BASE_URL: str = os.getenv("APMIX_BASE_URL", "https://api.apmix.ai/v1")

    # Web Research Keys
    FIRECRAWL_API_KEY: str = os.getenv("FIRECRAWL_API_KEY", "")
    JINA_API_KEY: str = os.getenv("JINA_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    YOU_API_KEY: str = os.getenv("YOU_API_KEY", "")

    # Telemetry
    ENABLE_LANGFUSE: bool = os.getenv("ENABLE_LANGFUSE_TRACING", "false").lower() == "true"
    LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY", "")
    LANGFUSE_BASEURL: str = os.getenv("LANGFUSE_BASEURL", "https://cloud.langfuse.com")

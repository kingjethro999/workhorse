"""
Autonomous Agent Engine and Background Chunked Worker.
"""
import asyncio
from typing import Dict, Any, List, Optional, Callable
from workhorse.config import Config
from workhorse.router import AutoRouter
from workhorse.tools.file_crud import WorkspaceManager
from workhorse.tools.research import ResearchSuite
from workhorse.providers.ollama_local import OllamaProvider
from workhorse.providers.groq_client import GroqProvider
from workhorse.providers.nvidia_client import NvidiaProvider
from workhorse.providers.gemini_client import GeminiProvider
from workhorse.providers.openrouter import OpenRouterProvider

class AgentRuntime:
    def __init__(self, workspace_path: Optional[str] = None):
        self.workspace = WorkspaceManager(workspace_path)
        self.research = ResearchSuite()
        self.ollama = OllamaProvider()
        self.groq = GroqProvider()
        self.nvidia = NvidiaProvider()
        self.gemini = GeminiProvider()
        self.openrouter = OpenRouterProvider()
        self.router = AutoRouter(self.ollama)

    def get_provider(self, name: str):
        mapping = {
            "local": self.ollama,
            "ollama": self.ollama,
            "groq": self.groq,
            "nvidia": self.nvidia,
            "gemini": self.gemini,
            "openrouter": self.openrouter
        }
        return mapping.get(name.lower(), self.groq)

    async def execute_task(
        self,
        prompt: str,
        mode: str = "auto:auto",
        use_web: bool = False,
        on_thought: Optional[Callable[[str], None]] = None
    ) -> Dict[str, Any]:
        """
        Executes a task with repository awareness, file chunking,
        and the 5-Cycle Resilience Ring.
        """
        web_context = ""
        if use_web:
            if on_thought:
                on_thought(f"[*] Live web intelligence active: Searching for '{prompt}'...")
            web_context = self.research.auto_research(prompt)

        repo_context = ""
        lowered = prompt.lower()
        repo_keywords = [
            "tell me about this repo",
            "tell me about this project",
            "what is this repo",
            "what does this repo do",
            "explain this repo",
            "explain this codebase",
            "audit repo",
            "audit this repo",
            "summarize repo",
            "summarize codebase",
        ]
        if any(kw in lowered for kw in repo_keywords):
            if on_thought:
                on_thought("[*] Scanning repository structure and chunking high-signal files...")
            repo_summary = self.workspace.get_repo_summary(max_files=10)
            repo_context = f"\nRepository Architecture Overview:\n{repo_summary}\n"

        readme_keywords = [
            "edit readme",
            "update readme",
            "rewrite readme",
            "expand readme",
            "make readme",
            "improve readme",
        ]
        is_readme_edit = any(kw in lowered for kw in readme_keywords)
        if is_readme_edit and (self.workspace.root / "README.md").exists():
            if on_thought:
                on_thought("[*] Ingesting existing README.md for chunked expansion...")
            try:
                curr_readme = self.workspace.read_file("README.md", max_lines=500)
                repo_context += f"\nCurrent README.md Content:\n```markdown\n{curr_readme}\n```\n"
            except Exception:
                pass

        augmented_prompt = prompt
        if web_context:
            augmented_prompt = f"Web Research Context:\n{web_context}\n\n{augmented_prompt}"
        if repo_context:
            augmented_prompt = f"{repo_context}\n\nUser Instruction: {augmented_prompt}"

        async def _dispatch(provider_name: str, model_name: str):
            prov = self.get_provider(provider_name)
            messages = [{"role": "user", "content": augmented_prompt}]
            resp = await prov.generate(messages, model=model_name)
            
            if is_readme_edit:
                if on_thought:
                    on_thought("[*] Applying in-place chunked edit to README.md...")
                self._apply_readme_edit(resp.content, on_thought)

            return resp

        if mode in ["auto", "auto:auto"]:
            ring_result = await self.router.execute_with_resilience_ring(_dispatch, on_thought=on_thought, max_cycles=5)
            resp = ring_result["result"]
            tokens_dict = resp.token_usage.model_dump() if hasattr(resp.token_usage, "model_dump") else resp.token_usage.dict()
            return {
                "content": resp.content,
                "provider": ring_result["provider"],
                "model": ring_result["model"],
                "cycle": ring_result.get("cycle", 1),
                "tokens": tokens_dict
            }
        else:
            prov = self.get_provider(mode)
            messages = [{"role": "user", "content": augmented_prompt}]
            resp = await prov.generate(messages)
            tokens_dict = resp.token_usage.model_dump() if hasattr(resp.token_usage, "model_dump") else resp.token_usage.dict()
            return {
                "content": resp.content,
                "provider": mode,
                "model": resp.model_name,
                "cycle": 1,
                "tokens": tokens_dict
            }

    def _apply_readme_edit(self, agent_output: str, on_thought: Optional[Callable[[str], None]] = None):
        try:
            content = agent_output.strip()
            if "```markdown" in content:
                content = content.split("```markdown", 1)[1].split("```", 1)[0].strip()
            elif "```md" in content:
                content = content.split("```md", 1)[1].split("```", 1)[0].strip()
            elif content.startswith("```") and "```" in content[3:]:
                parts = content.split("```")
                if len(parts) >= 3:
                    content = parts[1].strip()
            
            self.workspace.write_file("README.md", content, overwrite=True)
            if on_thought:
                on_thought("[OK] Successfully updated README.md in workspace (backup saved in .workhorse_backups/).")
        except Exception as e:
            if on_thought:
                on_thought(f"[!] Warning: Could not auto-write README.md: {e}")

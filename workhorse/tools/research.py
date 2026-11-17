"""
Multi-Engine Web Intelligence Suite.
Supports Tavily, Jina AI, Firecrawl, and You.com with transparent automated fallback.
"""
import requests
from typing import Optional
from workhorse.config import Config

class ResearchSuite:
    def __init__(self):
        self.firecrawl_key = Config.FIRECRAWL_API_KEY
        self.jina_key = Config.JINA_API_KEY
        self.tavily_key = Config.TAVILY_API_KEY
        self.you_key = Config.YOU_API_KEY

    def search_tavily(self, query: str) -> Optional[str]:
        if not self.tavily_key:
            return None
        url = "https://api.tavily.com/search"
        payload = {"query": query, "api_key": self.tavily_key, "search_depth": "basic", "include_answer": True}
        try:
            r = requests.post(url, json=payload, timeout=8)
            if r.status_code == 200:
                data = r.json()
                ans = data.get("answer", "")
                sources = [f"- {s.get('title')}: {s.get('content')} ({s.get('url')})" for s in data.get("results", [])[:3]]
                return f"{ans}\n\n" + "\n".join(sources)
        except Exception:
            pass
        return None

    def search_jina(self, query: str) -> Optional[str]:
        url = f"https://s.jina.ai/{query}"
        headers = {"X-Return-Format": "markdown"}
        if self.jina_key:
            headers["Authorization"] = f"Bearer {self.jina_key}"
        try:
            r = requests.get(url, headers=headers, timeout=8)
            if r.status_code == 200 and len(r.text) > 100:
                return r.text[:3000]
        except Exception:
            pass
        return None

    def search_firecrawl(self, query: str) -> Optional[str]:
        if not self.firecrawl_key:
            return None
        url = "https://api.firecrawl.dev/v1/search"
        headers = {"Authorization": f"Bearer {self.firecrawl_key}", "Content-Type": "application/json"}
        payload = {"query": query, "limit": 3}
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=10)
            if r.status_code == 200 and r.json().get("success"):
                snippets = [item.get("markdown", "") for item in r.json().get("data", [])]
                return "\n---\n".join(snippets)[:3500]
        except Exception:
            pass
        return None

    def search_you(self, query: str) -> Optional[str]:
        if not self.you_key:
            return None
        url = "https://api.ydc-index.io/search"
        headers = {"X-API-Key": self.you_key}
        params = {"query": query}
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=8)
            if resp.status_code == 200:
                data = resp.json()
                hits = data.get("hits", [])
                results = []
                for h in hits[:3]:
                    snippets = " ".join(h.get("snippets", []))
                    results.append(f"- {h.get('title')}: {snippets} ({h.get('url')})")
                return "\n".join(results)
        except Exception:
            pass
        return None

    def auto_research(self, query: str) -> str:
        res = self.search_tavily(query)
        if res:
            return f"[Source: Tavily AI]\n{res}"
        res = self.search_jina(query)
        if res:
            return f"[Source: Jina AI]\n{res}"
        res = self.search_firecrawl(query)
        if res:
            return f"[Source: Firecrawl]\n{res}"
        res = self.search_you(query)
        if res:
            return f"[Source: You.com]\n{res}"
        return "No web intelligence results retrieved."

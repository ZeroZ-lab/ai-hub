import os
from anthropic import Anthropic
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str, model: str = "claude-3-5-sonnet-20241022"):
        self.name = name
        self.model = model
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def _call_claude(self, system: str, messages: list, tools: list = None, stop_sequences: list = None):
        """Helper to call Claude API."""
        kwargs = {
            "model": self.model,
            "max_tokens": 4096,
            "system": system,
            "messages": messages,
        }
        if tools:
            kwargs["tools"] = tools
        if stop_sequences:
            kwargs["stop_sequences"] = stop_sequences
            
        return self.client.messages.create(**kwargs)

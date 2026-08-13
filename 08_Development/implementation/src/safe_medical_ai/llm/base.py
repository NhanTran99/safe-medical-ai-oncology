"""Provider-agnostic LLM adapter interface.

Per TECH_STACK.md section 1/4, the LLM provider and model are intentionally
deferred decisions. This module defines only the abstract adapter shape;
it contains no concrete provider implementation and must not be called
from any runtime path introduced by this scaffolding task.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class LLMAdapter(ABC):
    """Abstract interface a future provider-specific adapter must implement."""

    @abstractmethod
    def generate(self, *args: Any, **kwargs: Any) -> Any:
        """Not implemented. Provider/model selection is a deferred decision."""
        raise NotImplementedError

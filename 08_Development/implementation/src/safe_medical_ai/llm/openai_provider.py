"""OpenAI API provider adapter — Track 3 BATCH 02.

Concrete `LLMAdapter` implementation wrapping the OpenAI API. Sits entirely
behind the existing `LLMAdapter` boundary: consumes the existing
`ProviderGenerationRequest` unchanged, returns a plain `str`, and maps
OpenAI SDK failures onto the existing `ProviderError` taxonomy defined in
`generation/generation.py` — no new provider error hierarchy, and no change
to `LLMAdapter`, `ProviderGenerationRequest`, or `CandidateResponse`.

Track 3 BATCH 03: the literal text sent to the model is now rendered from
`request.prompt_specification`, the governed `PromptSpecification` produced
by `prompting.build_prompt` (`PROMPTING_STRATEGY.md`, LOCKED) — not
constructed ad-hoc here. `_render_prompt_specification` below performs only
provider-specific *serialization* of that already-decided structure into
OpenAI's `input` string; it makes no content/wording decisions of its own
and does not implement or duplicate the Prompt Builder. The BATCH 02
temporary bridge (`_build_temporary_bridge_input`) has been removed — it is
no longer the active prompt-construction path.
"""

from __future__ import annotations

import logging
from typing import Final

from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

from ..generation import ProviderError, ProviderPartialOutputError, ProviderTimeoutError
from .base import LLMAdapter

logger = logging.getLogger(__name__)

#: Project-Coordinator-locked default model (Track 3 BATCH 02). Overriding
#: via `Settings.openai_model` is supported but never happens silently —
#: this is the value used unless a caller explicitly configures another.
DEFAULT_OPENAI_MODEL: Final[str] = "gpt-5.4-mini"


class OpenAIProvider(LLMAdapter):
    """Concrete `LLMAdapter` calling the OpenAI API.

    `api_key`/`model` are supplied explicitly by the caller (see
    `api/main.py`'s `_select_provider()`) — this class never reads
    environment variables or `Settings` itself, keeping provider
    configuration in the existing config boundary, not duplicated here.
    Neither the API key nor the OpenAI client is ever logged.
    """

    def __init__(self, *, api_key: str, model: str = DEFAULT_OPENAI_MODEL) -> None:
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def generate(self, *, request) -> str:
        input_text = self._render_prompt_specification(request.prompt_specification)

        try:
            response = self._client.responses.create(model=self._model, input=input_text)
        except AuthenticationError as exc:
            logger.warning("OpenAIProvider: authentication/configuration failure")
            raise ProviderError("OpenAI authentication/configuration failure") from exc
        except RateLimitError as exc:
            logger.warning("OpenAIProvider: rate limit exceeded")
            raise ProviderError("OpenAI API rate limit exceeded") from exc
        except APITimeoutError as exc:
            logger.warning("OpenAIProvider: request timed out")
            raise ProviderTimeoutError("OpenAI API request timed out") from exc
        except APIConnectionError as exc:
            logger.warning("OpenAIProvider: connection failure")
            raise ProviderTimeoutError("OpenAI API connection failure") from exc
        except APIError as exc:
            logger.warning("OpenAIProvider: API error")
            raise ProviderError("OpenAI API returned an error") from exc

        if getattr(response, "status", None) == "incomplete":
            logger.warning("OpenAIProvider: response marked incomplete")
            raise ProviderPartialOutputError("OpenAI response was incomplete")

        return response.output_text

    @staticmethod
    def _render_prompt_specification(specification) -> str:
        """Provider-specific SERIALIZATION only — not prompt construction.

        Every decision about what the prompt contains (system/operational
        context, the governance decision, which evidence and in what
        order, the user's question) was already made by the governed
        Prompt Builder (`prompting.build_prompt`). This function only
        formats that already-decided, immutable `PromptSpecification` into
        the literal string OpenAI's Responses API requires — it invents no
        new content, wording, or instruction, and does not implement or
        duplicate `PROMPTING_STRATEGY.md`.
        """
        lines = [
            f"[System] mode={specification.system.mode}; "
            f"formal_validation={specification.system.formal_validation}; "
            f"execution_authorization={specification.system.execution_authorization}; "
            f"vc_clin={specification.system.vc_clin}",
            f"[Governance] risk_class={specification.governance.risk_class.value}; "
            f"action={specification.governance.action.value}; "
            f"reason_code={specification.governance.reason_code}",
        ]
        for item in specification.evidence.items:
            if item.content:
                label = item.title or item.population_id
                lines.append(f"[Evidence: {label}]\n{item.content}")
        lines.append(f"[Question] {specification.communication.request_text}")
        return "\n\n".join(lines)

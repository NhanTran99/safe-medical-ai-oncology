"""Selected-PP Request Relevance boundary.

Implements one explicit, deterministic entry point:
`evaluate_request_relevance`. Answers only "does this actual request text
sufficiently relate to the PP the caller has already resolved via
`EvaluationCaseResolver`?" -- it never resolves case identity itself,
never re-implements or duplicates `EvaluationCaseResolver`, never touches
the filesystem or network, never calls an LLM/provider, and never
performs clinical reasoning of any kind.

Mechanism (locked): normalized lexical token-overlap between the request
text and the selected PP's own governed `pp_title` + `controlled_question`
text (both already 239/239-complete in the existing manifest projection --
see `api/main.py`'s loader). Pure standard-library string/set operations
only -- deterministic, reproducible, offline, provider-independent.

Threshold status (locked, per the required calibration process -- see
`data/B12_REQUEST_RELEVANCE_CALIBRATION.md`): the only positive-example
construction available from existing governed material (a case's own
`controlled_question` used as the message) is a trivial self-identical
match that always scores 1.0 -- it carries no information about what
score a legitimately different on-topic phrasing should receive, so a
genuine calibrated numeric acceptance threshold could NOT be responsibly
derived from existing governed material (per the locked instruction: do
not invent one). The decision rule actually shipped requires no
calibration because it needs none: `NOT_RELEVANT` fires only when the
request shares ZERO significant terms with the target -- the minimum
possible evidentiary bar, not an empirically-tuned cutoff. A future
calibrated numeric threshold remains NOT YET GOVERNED and is out of this
module's scope to invent. This mechanism is NOT clinically validated and
makes no clinical-quality claim of any kind.
"""

from __future__ import annotations

import logging
import re

from .models import RequestRelevanceOutcome, RequestRelevanceResult

logger = logging.getLogger(__name__)

#: Locked, fixed, non-fabricated boundary response text (spec: "must
#: communicate only the governed limitation... do not invent clinical
#: advice"). Mirrors the existing convention of
#: `generation/models.py:EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT` -- a
#: policy-level fixed string, not a per-request generated explanation.
REQUEST_NOT_RELEVANT_RESPONSE_TEXT = (
    "This request does not appear to relate to the selected topic. "
    "A response cannot be generated for it under the selected topic."
)

#: Small, fixed stopword list -- excludes common function words from the
#: significant-token comparison so that shared articles/prepositions/etc.
#: never count as evidence of topical relevance. Not clinical vocabulary
#: of any kind.
_STOPWORDS = frozenset(
    {
        "a", "an", "the", "is", "are", "was", "were", "what", "which",
        "who", "whom", "this", "that", "these", "those", "of", "for",
        "in", "on", "to", "and", "or", "with", "how", "do", "does",
        "did", "i", "my", "your", "you", "it", "its", "please",
        "explain", "about", "can", "could", "should", "would", "will",
        "be", "as", "at", "by", "from",
    }
)

_TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


def _significant_tokens(text: str) -> set[str]:
    """Lowercase, tokenize, and drop stopwords/single characters.

    Pure normalization only -- no clinical vocabulary handling, no
    synonym expansion, no stemming. Deterministic: the same input string
    always yields the same token set.
    """
    tokens = _TOKEN_PATTERN.findall(text.lower())
    return {token for token in tokens if token not in _STOPWORDS and len(token) > 1}


def _score(message_tokens: set[str], target_tokens: set[str]) -> float:
    """Fraction of the message's own significant tokens found in the
    target -- i.e. how much of what the user actually asked is covered by
    the selected PP's own governed title/question vocabulary.

    Coverage-of-message (not Jaccard) is used deliberately: the target
    text (title + controlled question) is typically longer/more varied
    than a short user message, so requiring the message to cover the
    target's full vocabulary would penalize even a clearly on-topic short
    question. `0.0` for an empty message-token set (nothing to measure).
    """
    if not message_tokens:
        return 0.0
    return len(message_tokens & target_tokens) / len(message_tokens)


def evaluate_request_relevance(
    message: str,
    *,
    pp_title: str | None,
    controlled_question: str | None,
) -> RequestRelevanceResult:
    """Evaluate whether `message` sufficiently relates to the selected PP.

    `pp_title`/`controlled_question` are the already-resolved selected
    case's own governed text (from the existing manifest projection --
    never re-derived, re-retrieved, or fabricated here).

    Fail-open on missing target data (spec: "preserve the explicitly
    approved fail-safe behavior"): `pp_title`/`controlled_question` are
    239/239-complete in the shipped manifest projection today, so this
    branch is defensive only, not expected to fire in practice. Missing
    target data is a data-availability gap, not evidence that the user's
    request is off-topic -- treating it as `NOT_RELEVANT` would wrongly
    blame the user for an internal data gap, so this evaluates to
    `RELEVANT` (a no-op result letting the existing CER path proceed
    unchanged) rather than fabricating a relevance judgment it has no
    basis for.

    Fail-closed on zero shared significant vocabulary (spec: "when
    evidence is insufficient, prefer NOT_RELEVANT rather than force
    execution"): a `message` sharing no significant term at all with the
    target has, by construction, zero evidence of relevance.
    """
    if not pp_title and not controlled_question:
        logger.info("evaluate_request_relevance: no target metadata available -- fail-open (RELEVANT)")
        return RequestRelevanceResult(
            outcome=RequestRelevanceOutcome.RELEVANT,
            score=0.0,
            message="no relevance evaluation performed: selected PP's governed title/question text was unavailable",
        )

    target_text = " ".join(text for text in (pp_title, controlled_question) if text)
    message_tokens = _significant_tokens(message)
    target_tokens = _significant_tokens(target_text)
    score = _score(message_tokens, target_tokens)

    if score > 0.0:
        logger.info("evaluate_request_relevance: RELEVANT score=%.4f", score)
        return RequestRelevanceResult(
            outcome=RequestRelevanceOutcome.RELEVANT,
            score=score,
            message=None,
        )

    logger.info("evaluate_request_relevance: NOT_RELEVANT score=%.4f", score)
    return RequestRelevanceResult(
        outcome=RequestRelevanceOutcome.NOT_RELEVANT,
        score=score,
        message=REQUEST_NOT_RELEVANT_RESPONSE_TEXT,
    )

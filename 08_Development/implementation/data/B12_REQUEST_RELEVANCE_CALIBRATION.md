# B12 Selected-PP Request Relevance — Calibration / Evaluation Evidence

## Purpose

Records the bounded calibration/evaluation process performed to determine
whether a numerical acceptance threshold for `relevance/resolver.py`'s
token-overlap relevance score could be responsibly derived from existing
governed material, per the locked instruction: do not invent a threshold
the evidence does not support.

This is not a clinical validation artifact and makes no clinical-quality
claim. It evaluates a deterministic text-matching mechanism only.

## Provenance

Source: `data/evaluation_case_manifest_projection.json` (the same frozen,
SHA-256-pinned, 239-entry manifest projection `EvaluationCaseResolver`
uses). Every string used below is an existing, already-governed
`controlled_question`/`pp_title` value already shipped in that file — no
clinical content was invented for this evaluation.

## Method

Scoring function under test (`relevance/resolver.py`): lowercase, tokenize
(`[a-z0-9]+`), drop a small fixed stopword list and single-character
tokens, then compute `|significant_tokens(message) ∩
significant_tokens(target)| / |significant_tokens(message)|`, where
`target = pp_title + " " + controlled_question` for one case.

### Positive-pair construction (per the locked instruction)

For each of the 239 cases: `message = that case's own controlled_question`,
`target = that same case's own (pp_title, controlled_question)`.

### Negative-pair construction (per the locked instruction)

For each of the 239 cases as the target, every one of the other 238
cases' `controlled_question` was used as `message` — the full 239 × 238 =
56,882-pair cross matrix (exact, not sampled).

## Results

**Positive pairs (n=239):** min = max = mean = 1.0. **Every single
positive pair scores exactly 1.0.** This is expected and structurally
unavoidable given the construction (`message` is, verbatim, a substring
of `target`) — it proves the scoring function correctly recognizes an
identical match, but **carries no information about what score a
legitimately, differently-phrased on-topic question should receive**,
because no such example exists anywhere in the governed corpus that this
process is permitted to draw from without inventing clinical content.

**Negative pairs (n=56,882):** mean = 0.0371, median = 0.0.

| Percentile | Score |
|---|---|
| p50 | 0.0000 |
| p75 | 0.0000 |
| p90 | 0.0769 |
| p95 | 0.3333 |
| p99 | 0.6667 |
| p99.5 | 0.6667 |
| p99.9 | 1.0000 |
| p100 (max) | 1.0000 |

Under the shipped decision rule (`RELEVANT` iff `score > 0`):
- **5,696 / 56,882 (10.01%)** of genuinely mismatched cross-pairs score
  `> 0` and would be classified `RELEVANT` — a false-allow, caused by
  incidental shared vocabulary between otherwise unrelated PPs (e.g. both
  mentioning "gastric" or "cancer").
- **51,186 / 56,882 (89.99%)** of genuinely mismatched cross-pairs score
  exactly `0` and are correctly classified `NOT_RELEVANT`.
- **0 / 239 (0.00%)** of the (structurally trivial) positive pairs are
  ever misclassified `NOT_RELEVANT` — but see the limitation below before
  reading this as a meaningful accuracy figure.

## Threshold decision

**No calibrated numeric threshold (e.g. "requires ≥30% overlap") was
chosen**, because the only positive-example construction available from
existing governed material is degenerate (always `1.0`, §Results above)
and provides no basis for selecting any specific cutoff above zero. Per
the locked instruction, inventing such a number anyway — merely because a
distribution exists to eyeball — was explicitly avoided.

The rule actually shipped, `score > 0` (equivalently: `NOT_RELEVANT` iff
the message shares *zero* significant tokens with the target), requires
no calibration because it is the structural minimum evidentiary bar, not
an empirically-tuned cutoff: a message with literally no shared
vocabulary has, by definition, no lexical evidence of relevance. This is
evidence-based in the sense that it is provably the most conservative
non-arbitrary rule available, not in the sense of being validated against
realistic on-topic paraphrases (no such governed examples exist to
validate against).

**A genuine calibrated numeric threshold beyond zero-overlap remains NOT
YET GOVERNED.**

## Known limitations (recorded, not hidden)

1. **The positive signal is uninformative.** Nothing in this evaluation
   demonstrates how the scoring function behaves on a realistic,
   differently-worded, but genuinely on-topic question — only on an
   exact substring match. This is the single most important limitation
   of this evaluation.
2. **10.01% false-allow rate on mismatched pairs.** A meaningful fraction
   of genuinely unrelated PP pairs share enough incidental vocabulary
   (shared organ/disease terms, shared common clinical nouns) to score
   `> 0` and pass as `RELEVANT` under the shipped rule. The mechanism is
   deliberately conservative in the direction of *not* blocking, at the
   cost of *not* catching every mismatch.
3. **Short user messages with few significant tokens are more volatile**
   at both ends — a 2-3-significant-token message either fully misses
   (score 0) or fully hits (score 1) far more often than a longer one;
   this evaluation used full `controlled_question`-length strings only,
   not the shorter free-text a real user might type.
4. **No clinical-quality or clinical-validity claim is made anywhere in
   this evaluation.** It measures lexical overlap only.

## Disposition

The mechanism, as shipped, is a bounded, deterministic, conservative
zero-evidence rule — not a calibrated classifier. Any future move to a
non-zero numeric threshold requires either (a) a governed source of
realistic on-topic paraphrase examples that does not currently exist, or
(b) an explicit governance decision to accept a different, still-
non-arbitrary construction. Neither was available to this process.

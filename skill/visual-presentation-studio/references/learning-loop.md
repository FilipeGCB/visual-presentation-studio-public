# Controlled Learning Loop

The Studio is allowed to learn from real work inside its private source repository. Public promotion is a separate, stricter operation.

## When to evaluate

Evaluate learning only after Gate 2 approval. A successful project may produce no reusable candidate.

## Private source record

A learning record may refer to authorized real evidence retained in the private laboratory. Record the source class and whether evidence remains private; do not confuse that evidence with a public artifact.

Use:

- Candidate:
- Private source classification: `PUBLIC | SYNTHETIC | PROFESSIONAL_PRIVATE | PERSONAL_PRIVATE | SECRET | UNKNOWN`
- Why reusable:
- Evidence from use:
- Private evidence retained: `yes | no`
- Limitations:
- Proposed private maturity: `EXPERIMENTAL`

The private learning record preserves truth about what was actually observed. It does not imply that the source can be published.

## Public candidate

When a reusable capability should enter the public distribution, create a new **public candidate** rather than copying or lightly redacting the private source.

Use this promotion record:

- Candidate:
- Private source classification: `PUBLIC | SYNTHETIC | PROFESSIONAL_PRIVATE | PERSONAL_PRIVATE | SECRET | UNKNOWN`
- Public candidate created: `yes | no`
- Public candidate contains source material: `no`
- Why reusable:
- Evidence from use (generalized; no private source material):
- What was generalized:
- What professional/private information was removed:
- What personal/private information was removed:
- Generalization completed: `yes | no`
- Sanitization completed: `yes | no`
- Export safety scan: `PASS | BLOCKED`
- Provenance/rights safe for public distribution: `yes | no`
- Human semantic review: `PASS | BLOCKED`
- Proposed public maturity: `EXPERIMENTAL`
- Explicit approval required: `yes`

## Public promotion rules

1. Propose; never auto-promote.
2. Require explicit approval before changing the permanent public distribution.
3. Record the private source classification before creating a public candidate.
4. `PUBLIC` and `SYNTHETIC` may be exported directly only when provenance, rights and distribution policy permit it.
5. `PROFESSIONAL_PRIVATE` and `PERSONAL_PRIVATE` may contribute only a newly generalized, sanitized capability. Never copy the private source or a lightly redacted derivative.
6. `SECRET`, `UNKNOWN`, incomplete generalization, incomplete sanitization, source material inside the public candidate, `Export safety scan: BLOCKED`, unsafe rights, or `Human semantic review: BLOCKED` blocks public promotion.
7. Generalize the capability so it applies beyond one presentation and remains useful without the private source.
8. Sanitize names, organizations, people, internal/customer data, project identifiers, numbers, proprietary text, confidential logic, private URLs/endpoints, filesystem identity and identifying imagery.
9. Never publicly promote private source slides, screenshots, real assets, raw prompts, transcripts, exported documents, private datasets, evaluation bundles, logs or agent traces.
10. Public export must use the default-deny manifest and a clean snapshot without private `.git` history.
11. Preserve public-safe provenance, rights, dependencies, accessibility, limitations and “when not to use” guidance.
12. Test the generalized public candidate before entering it as `EXPERIMENTAL`.
13. Promote public maturity only through evidence: `EXPERIMENTAL → VALIDATED → CORE`.

If sanitization would destroy the candidate's value, confidentiality cannot be assured, or provenance remains `UNKNOWN`, keep the learning in the private source or discard the public candidate.

A passing automated scanner is defense in depth, not proof of semantic safety. Human semantic review is mandatory.

## Negative learning

Anti-patterns are valid candidates when they capture a transferable failure, its observable signals, why it fails, and how to correct it without retaining private source details in the public candidate.

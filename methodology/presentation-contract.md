# Presentation Contract

The Studio uses portable Markdown contracts so ChatGPT, Codex, Claude Code, or another capable executor can continue the same work without reinterpreting it.

## Lifecycle

`brief → proposal → GATE 1 → optional asset-board sub-decision → narrative/design/experience/technical specs → storyboard → build → visual-review/issues → READY FOR USER REVIEW → GATE 2 → FINAL → optional learning harvest`

## Gate 1 freeze

Gate 1 approval freezes the thesis, primary narrative, format, visual direction, primary interaction, stack, and destination. It also records whether approval covers direction only or exact named primary assets. Direction approval never silently becomes asset approval. Refinement inside the approved contract is allowed. A structural change requires an explicit return to Gate 1.

When bespoke or generated imagery materially defines identity or composition, use an Asset Board Checkpoint as a focused sub-decision inside Gate 1. It is not a third human gate and should not become approval bureaucracy for minor icons or utility assets.

## Required records

- `brief.md` reconstructs the request, evidence, constraints, and unknowns.
- `proposal.md` is the consolidated Gate 1 creative contract, reference matrix, asset approval scope, and decision register.
- `narrative.md`, `design.md`, `experience.md`, and `technical.md` turn the approved contract into build specifications.
- `visual-review.md` records the exact build or commit, route, evidence level, actual rendered inspection, limitations, and correction rounds.
- `issues.md` is the issue ledger across all QA surfaces.

## Readiness states

- `NOT READY`: Gate 1 is unapproved, required evidence is missing, or a known BLOCKER or MAJOR remains.
- `READY FOR USER REVIEW`: implementation matches the contract and all QA surfaces pass with 0 known BLOCKER and 0 known MAJOR issues.
- `FINAL`: the user explicitly approves the exact build or commit presented at Gate 2.

The first render is never a delivery candidate. It begins the render, inspect, correct, and render-again loop.

Approval terms are not interchangeable: `direction approved`, `asset approved`, `applied`, `validated in composition`, `READY FOR USER REVIEW`, and `FINAL` describe different decisions or evidence states. A generic instruction to continue advances work only within the already approved scope.

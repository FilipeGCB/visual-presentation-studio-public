# Visual Presentation Studio

Visual Presentation Studio is a portable, local-first factory for designing, building, visually inspecting, and validating high-quality HTML presentations.

It treats presentation work as an engineering process: thesis, narrative, visual direction, assets, technical routing, rendered inspection, QA, and human approval are explicit parts of the workflow.

This public repository is a curated portfolio/study distribution. The operational learning laboratory is private; this repository contains only reusable capability, synthetic examples, intentionally public material, and sanitized/generalized learning.

## Why this exists

A one-shot "generate some slides" workflow is often fast, but it tends to collapse several distinct problems into a single model call:

- What is the actual thesis?
- What should the audience understand or decide?
- Which visual direction fits the message?
- Which assets need to exist before build?
- Which presentation mode is appropriate?
- How should the artifact be inspected after rendering?
- What evidence is required before calling the result ready?

Visual Presentation Studio separates those concerns and turns them into a repeatable production workflow.

## What it demonstrates

The Studio currently includes:

- a central orchestration Skill;
- Gate 1 and Gate 2 human-approval contracts;
- traditional 16:9, scrollytelling, and exploratory/interactive modes;
- reusable workspace contracts;
- visual-research and asset-planning methodology;
- browser-rendered inspection guidance;
- multidimensional QA across content, narrative, visual, experience, and technical surfaces;
- standalone HTML starters and a React/Vite exploratory starter;
- patterns and anti-patterns learned from real use and promoted only after generalization and sanitization.

## Two-gate lifecycle

```text
brief
  ↓
thesis + narrative + visual/technical proposal
  ↓
GATE 1 — approve the creative contract
  ↓
storyboard + assets + build
  ↓
render → inspect → correct → render again
  ↓
content + narrative + visual + experience + technical QA
  ↓
READY FOR USER REVIEW
  ↓
GATE 2 — approve the exact working version
  ↓
FINAL
  ↓
optional learning harvest
```

Gate 1 is intentionally consolidated. It freezes the major structural decisions before implementation rather than interrupting the work with dozens of micro-approvals.

Gate 2 validates the exact build/commit and its evidence before it is called final.

## Presentation modes

### Traditional / 16:9

Best when the artifact behaves like a conventional slide deck and the audience advances screen by screen.

### Scrollytelling

Best when progression, section transitions, sticky behavior, motion, or a continuous narrative are part of the experience.

### Exploratory / Interactive

Best when the audience needs to inspect states, compare views, filter information, or interact with the artifact instead of consuming a fixed sequence.

The mode follows the narrative. A visual component or framework must not choose the architecture by itself.

## Rendered inspection

A successful build is not visual QA.

The Studio requires the actual rendered artifact to be inspected and corrected through the loop:

```text
RENDER → INSPECT → IDENTIFY ISSUES → CORRECT → RENDER AGAIN
```

Before `READY FOR USER REVIEW`, there must be:

- 0 known BLOCKER issues;
- 0 known MAJOR issues.

Source review, a previous render, or a static composite cannot be silently treated as current live evidence.

## Current trade-off

The current pipeline is optimized for visual quality, reproducibility and reviewability rather than minimum latency or token cost. This produces strong final artifacts, but can be expensive and slow for exploratory work.

A future optimization track will investigate a faster draft path without weakening the production-quality route. That route is not claimed as implemented here today.

## Repository structure

```text
skill/          central installable Studio capability
methodology/    presentation contracts and reasoning methods
quality/        QA surfaces, severities, and integrity rules
patterns/       reusable anti-patterns and learned heuristics
templates/      workspace and HTML/React starters
examples/       synthetic acceptance example
scripts/        structural validation and public-safety scan
tests/          public repository contract tests
docs/           design, implementation, verification, and sanitized learning records
```

## Public/private boundary

This repository is intentionally **not** a mirror or fork of the private operational laboratory. It has a clean Git history.

Real private presentations, screenshots, datasets, transcripts, source assets, operational evidence, private prompts, credentials, private URLs/endpoints, or attributable confidential logic do not belong here.

Material derived from private professional or personal work enters this repository only after the reusable capability has been generalized and sanitized. Uncertain provenance or sensitivity fails closed.

See `SECURITY.md` and `AGENTS.md` for the public-repository rules.

## Running the checks

```bash
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/public_safety_check.py .
```

The exploratory React starter can be verified with:

```bash
cd templates/exploratory-react
npm ci
npm run build
```

## Status

**Active development.**

The repository represents a working public distribution of the Studio methodology and reusable implementation assets. It will continue evolving as new capabilities prove useful in real work and can be promoted safely.

## Rights

This repository is source-public for portfolio and study purposes. No permissive open-source license is granted by default. A separate licensing decision may be made later.

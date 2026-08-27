# Visual Presentation Studio

**Active development.** Visual Presentation Studio is a local-first engineering system for designing, building, rendering, inspecting, and validating high-quality HTML presentations and visual narratives with AI-assisted workflows.

This repository is the curated public distribution of an actively developed private laboratory. It contains reusable capability, not private presentation deliverables or raw project evidence.

## Why it exists

A strong visual artifact is not just a model output. The Studio treats thesis, narrative, visual direction, assets, technical architecture, browser rendering, inspection, correction, and multidimensional QA as an engineering lifecycle.

The central principle is simple:

> Complexity may vary. Production rigor does not.

## Two-gate lifecycle

`brief → proposal → Gate 1 → storyboard/specs → build → render/inspect/correct → QA → Gate 2 → FINAL → optional controlled learning`

- **Gate 1** freezes thesis, primary narrative, format, visual direction, primary interaction, stack, and destination before implementation.
- **Gate 2** approves the exact finished build only after rendered inspection and quality gates have no known BLOCKER or MAJOR issues.

## Supported experiences

- Traditional / 16:9 presentations
- Scrollytelling and editorial narratives
- Exploratory / interactive experiences
- Deliberate hybrids when they improve comprehension

Local downloadable delivery is a first-class output. HTML/CSS/JavaScript is preferred when sufficient; React is used when meaningful state or interaction warrants it.

## Quality system

The Studio separates build success from visual evidence. Its workflow requires the actual result to be rendered and inspected at relevant states and viewports, then corrected and rendered again.

Quality is evaluated across content, narrative, visual, experience, and technical surfaces. Evidence records the exact build, route, viewport, input, settled state, and known limitations so reviewability does not depend on vague claims.

## Current trade-off

The current production-quality route is optimized for **visual quality, reproducibility, and reviewability rather than minimum latency or token cost**. That discipline can produce highly consistent final artifacts, but it can also be slower and more expensive than lightweight generation during exploratory work.

A future research track may investigate a faster draft path while preserving the current production-quality route. A Fast/Draft mode is not presented here as an existing capability.

## What is public here

This distribution is intentionally smaller and safer than the private laboratory. It contains reusable methodology, the operational Skill, templates, patterns, quality rules, generic examples, and sanitized learning that remains useful without private source material.

Real presentations may be used privately to improve the Studio, but only generalized and sanitized capabilities cross the public-promotion firewall. The public repository is built from a default-deny export and starts with clean Git history.

## Real-world application

The author's personal blog has been one of the real environments used to apply and refine Studio principles—from narrative direction and visual composition to rendered QA. This is evidence of iterative use, not a claim that the site was generated automatically in a single one-shot run.

## Repository map

- `skill/visual-presentation-studio/` — operational Agent Skill
- `methodology/` — durable presentation contracts and reasoning
- `quality/` — observable QA rules and severity criteria
- `patterns/` — reusable positive and negative patterns
- `templates/` — local-first technical/workspace starters
- `examples/` — synthetic or sanitized acceptance evidence

## Validation

From the repository root:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/public_safety_check.py .
cd templates/exploratory-react && npm install && npm run build
```

Automated success is necessary but not sufficient for a presentation itself: rendered visual inspection remains part of the Studio workflow.

## Public-safety boundary

Do not contribute private project source material, real confidential presentations, credentials, private endpoints, private personal data, or raw evidence copied from non-public work. Public examples must be intentionally public/rights-safe or synthetic; learnings from private work must be generalized and sanitized before they become repository content.

See `SECURITY.md` and `AGENTS.md` before contributing.

## Source visibility and rights

This repository is published for portfolio and study. Public visibility does **not** by itself grant an open-source license or additional reuse rights. If a license is added later, that file will define the applicable terms.

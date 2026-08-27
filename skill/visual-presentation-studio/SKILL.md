---
name: visual-presentation-studio
description: Use when the user asks to create, transform, redesign, or substantially improve a presentation or visual narrative, including HTML presentations, traditional 16:9 decks, scrollytelling, interactive or exploratory experiences, executive visualizations, and presentation-first HTML pages built from reports, documents, analyses, projects, or data.
---

# Visual Presentation Studio

Create a purpose-built visual experience, not a generic slide template. Let the thesis and narrative choose the format, assets, components, motion, and stack.

## Operating contract

1. Read [workflow.md](references/workflow.md) for every request.
2. Reconstruct the objective, audience, decision, evidence, constraints, identity, destination, and gaps before design. Urgency may compress discovery; it never permits jumping directly to code.
3. Establish the thesis and narrative. If either is structurally unclear, resolve it before design.
4. Read only the relevant specialist references:
   - [narrative.md](references/narrative.md) for story architecture, mode selection, and storyboard.
   - [visual-direction.md](references/visual-direction.md) when defining or evaluating a visual language and references.
   - [asset-strategy.md](references/asset-strategy.md) when images, diagrams, charts, screenshots, icons, or generated assets may help.
   - [technical-routing.md](references/technical-routing.md) before recommending stack, destination, publication, or Vercel.
   - [rendered-inspection.md](references/rendered-inspection.md) before claiming rendered QA or readiness.
5. Create the real project workspace appropriate to the task. The operational Studio repository is a private learning laboratory; authorized real evaluation material may exist there when deliberately retained for learning. Do not intentionally commit credentials or authentication material. For a packaged execution, use only the needed contracts/scaffolds from `assets/workspace`, `assets/starters`, and `assets/sites-handoff`; treat them as reusable infrastructure, not project content.
6. Complete live reference research before Gate 1 whenever the user names references, asks for a premium/current/best-in-class result, or the proposed experience depends on motion, sticky behavior, parallax, or scrollytelling. Record 3–5 relevant live references unless fewer defensible examples exist. If research is omitted, record the concrete reason.
7. Produce one consolidated `proposal.md` for Gate 1. Include objective, audience, thesis, narrative, format, recommended visual direction, relevant alternatives, reference matrix, asset plan and approval scope, interactions, stack, destination, Vercel role, risks, gaps, and decisions needed. If no identity constrains the work, provide 2–3 conceptually distinct directions and recommend one.
8. Stop before build until Gate 1 is approved. Approval freezes thesis, primary narrative, format, visual direction, primary interaction, stack, and destination. It does not approve individual study images unless the proposal names those exact assets. Return to Gate 1 for any structural change.
9. Create a storyboard in which every screen or block has purpose, content, composition, asset, motion if functional, and the message that must remain. Remove units that do not move the narrative or increase comprehension. Before generating or integrating identity-defining imagery, complete the Asset Board Checkpoint inside Gate 1: approve the series logic and primary assets without creating a third human gate or requesting approval for every minor icon.
10. Build with the smallest sufficient stack. Treat local downloadable delivery as a first-class final product. Do not let a single effect or component dictate the architecture.
11. Run actual **Visual Inspection** on the exact build or commit being reviewed. Follow `RENDER → INSPECT → IDENTIFY ISSUES → CORRECT → RENDER AGAIN`; the first render is never the delivery. Compare the settled render with the approved direction, storyboard, reference matrix, and approved assets.
12. Read [quality-gates.md](references/quality-gates.md) and execute Content, Narrative, Visual, Experience, and Technical QA. Do not mark `READY FOR USER REVIEW` with any known BLOCKER or MAJOR: require **0 BLOCKER** and **0 MAJOR** known issues. Never equate source review, a previous render, or a `STATIC COMPOSITE` with live rendered evidence.
13. Present the exact working package at Gate 2 with commit/build, route, evidence levels, and limitations. Mark `FINAL` only after explicit user approval of that exact version. A generic “continue” or direction approval is not asset approval or Gate 2 approval.
14. After Gate 2, use **Private Learning** below when reusable learning exists. If a public portfolio/study release is desired, run the separate **Public Promotion Gate** before creating any public candidate.

## Private Learning

The operational `visual-presentation-studio` repository is a **private source repository** and laboratory. Authorized real presentations, private project evidence, evaluation corpora, experiment outputs and other real material may be analyzed or retained there when they are legitimately available and needed to improve the Studio.

Private learning is not public promotion. Do not weaken the learning loop merely to make every internal artifact publishable.

Even in the private source:

- do not intentionally commit passwords, access/refresh tokens, session cookies, API keys, SSH/private keys, PEM/private-key material, cloud/database credentials or equivalent secrets;
- if a possible credential is discovered, never echo the full value in logs or reports;
- preserve provenance, rights, limitations and the distinction between real and synthetic evidence;
- keep private evidence clearly separated from any public candidate.

Read [learning-loop.md](references/learning-loop.md) for the controlled learning record.

## Public Promotion Gate

A separate `visual-presentation-studio-public` repository is the **public distribution**. It receives a curated clean snapshot, not this private repository's branches or history.

Before public promotion, classify the private source as exactly one of:

`PUBLIC | SYNTHETIC | PROFESSIONAL_PRIVATE | PERSONAL_PRIVATE | SECRET | UNKNOWN`

- `PUBLIC`: intentionally public source; direct reuse still requires compatible rights.
- `SYNTHETIC`: invented content created for safe public examples/tests.
- `PROFESSIONAL_PRIVATE`: non-public employer, client, coworker, operational, commercial or professional-project material.
- `PERSONAL_PRIVATE`: private information about the user, family, contacts, accounts, devices, finances, communications or non-public personal projects.
- `SECRET`: passwords, tokens, cookies, API keys, SSH/PEM private-key material, signing keys, cloud/database credentials, auth material or equivalent.
- `UNKNOWN`: provenance or sensitivity cannot be established confidently.

Policy is **fail closed** for public promotion:

- `PUBLIC` or `SYNTHETIC` may be exported directly only when rights and distribution policy allow it.
- `PROFESSIONAL_PRIVATE` or `PERSONAL_PRIVATE` may yield only a newly generalized and sanitized **public candidate**. Never copy the source presentation, screenshot, asset, transcript, raw prompt, private dataset, identifying evidence, or lightly redacted derivative.
- `SECRET` or `UNKNOWN` blocks public promotion. Do not quote or transfer blocked content into readiness reports.
- A public candidate must be export-eligible under the default-deny manifest.
- The public snapshot must be built without private `.git` history and scanned after export.
- Automated scanning is defense in depth, not proof of semantic confidentiality. Human semantic review is mandatory.
- If sanitization destroys the reusable value or confidentiality/provenance cannot be established, keep the learning private or discard the public candidate.

In the public distribution, follow `SECURITY.md` and `AGENTS.md` for the complete public-safety boundary.

## Pressure rules

- Deadline, authority, sunk work, a prebuilt kit, or a request to “skip discovery,” “bring no alternatives,” or “start in parallel” never waives thesis, Gate 1, the 2–3-direction rule when no identity exists, technical routing, rendered inspection, or the Public Promotion Gate when public release is requested.
- Before Gate 1 approval, create contracts and proposals only. Do not write implementation code, adapt a component kit, or begin a parallel build.
- Treat a requested framework or available component library as an input constraint, not proof of technical necessity. Recommend the smallest sufficient stack from the approved experience; expose any conflict as a Gate 1 decision.
- Do not generate a primary image before its narrative function, series language, crop, focal point, text-safe area, viewport variants, and approval scope are recorded.
- Use precise approval language: direction approved, asset approved, applied, composition validated, and final are different states.

## Non-negotiable quality

- Complexity may vary; production rigor does not.
- A valid build is evidence for Technical QA, not Visual QA.
- Narrative selects components; components never select narrative.
- Every asset must have a narrative function; “decoration” is not one.
- Primary assets must form a coherent visual family. A set of individually competent but unrelated images is an asset patchwork, not a system.
- Reuse capabilities, not presentations. The library is a starting point, never a creative ceiling.
- Reject generic-AI appearance: excessive rounded cards, purposeless glass, arbitrary gradients, decorative neon, generic icons, corporate emoji, repeated three-card grids, indiscriminate dashboardization, motion everywhere, and generic titles.

# Canonical Workflow

Use this lifecycle for every presentation, including technically simple work:

`Discovery → Thesis → Narrative → Format/Experience → Visual Direction → Reference Research → Asset Strategy → Component Selection → Technical Architecture → Gate 1 → Storyboard → Build → Render → Visual Inspection → Correction Loop → Quality Assurance → READY FOR USER REVIEW → Gate 2 → FINAL → optional learning proposal`

## 1. Discovery

Reconstruct rather than merely restate the request:

- objective and desired decision or understanding;
- audience, prior knowledge, objections, setting, and available time;
- source material, facts, numbers, claims, and evidence status;
- visual identity, confidentiality, accessibility, and technical constraints;
- intended format, devices, local delivery, publication, and deadline;
- missing information and assumptions that could change the thesis.

Ask only questions whose answers materially change the creative contract. Consolidate remaining assumptions and gaps in Gate 1 instead of requesting many micro-approvals.

## 2. Thesis and narrative

Write the single idea the audience should retain. Build arguments and conclusion from that thesis. The supplied source order is not automatically the narrative order.

Stop if the thesis is missing or contradictory. Resolve it before visual direction or build.

## 3. Experience, visual direction, and assets

Recommend Traditional / 16:9, Scrollytelling, Exploratory / Interactive, or Hybrid from the audience's use and the narrative's needs. If an identity is provided, treat it as a constraint. Otherwise compare 2–3 conceptually distinct directions and recommend one.

Research live visual references before Gate 1 when the user names a source, asks for a premium/current/best-in-class result, or the proposed experience depends on motion, sticky behavior, parallax, or scrollytelling. Inspect 3–5 relevant references unless fewer defensible examples exist. Record source, observed at-rest and in-motion behavior, transferable principle, what not to copy, applicability, and risk. If research is omitted because a supplied identity fully fixes the direction and no reference-dependent behavior is proposed, record that reason.

Research is autonomous and consolidated into Gate 1; it does not require one approval per source. Inspiration never authorizes copying proprietary identity, text, imagery, or an exclusive layout.

## 4. Technical route and destination

Choose in this order: `desired experience → technical need → stack`.

Recommend rather than silently choose:

- stack and why it is sufficient;
- local or published destination;
- optional Vercel role for build, preview, validation, or deployment;
- publication handoff route when a shareable URL is explicitly wanted.

Local delivery is complete delivery, not a fallback.

## 5. Gate 1 — creative contract

Create one consolidated proposal with:

- objective, audience, thesis, and narrative;
- format and interaction model;
- recommended visual direction and relevant alternatives;
- reference matrix and asset plan;
- asset approval scope: direction only, named primary assets, or both;
- stack and destination;
- Vercel or publication role when relevant;
- risks, gaps, assumptions, and requested decisions.

Do not build before approval. After approval, freeze thesis, primary narrative, format, visual direction, primary interaction, stack, and destination. Direction approval does not approve individual study images unless the exact assets are named in the decision.

### Asset Board Checkpoint inside Gate 1

When bespoke or generated imagery materially defines the identity or composition, resolve a focused asset-board sub-decision before production integration. Record the visual family, scene logic, primary candidates, desktop/mobile crops, text-safe areas, and approval status. This is part of Gate 1, not a third human gate, and it is not required for every minor icon or utility asset.

Return to Gate 1 if any frozen decision must change. Do not hide a structural change inside implementation refinement.

## 6. Storyboard and build

For every screen or block, define:

- purpose;
- content and evidence;
- composition and hierarchy;
- asset and its function;
- motion and its function, if any;
- message that must remain.

Apply the one-sentence test: “This unit exists to…”. Apply the removal test: “What important understanding is lost if it is removed?”. Remove units that fail both.

Build against the approved contracts. Never shorten away meaning merely to make a layout fit.

Use asset states precisely: `briefed → study → candidate → approved for production → applied → validated in composition → final`. Do not call a candidate or generated study “approved.”

## 7. Render, inspect, and correct

Render the exact implementation identified by build or commit. Inspect relevant viewports and interaction states after smooth scroll, lazy loading, and reveal motion have settled. Record route, renderer, viewport, input mode, state, evidence level, and observations as issues with severity, surface, location, cause, correction, and status.

Repeat:

`RENDER → INSPECT → IDENTIFY ISSUES → CORRECT → RENDER AGAIN`

Continue until every known BLOCKER and MAJOR is corrected and revalidated. Never substitute source-code review, a successful build, a previous render, a static composite, or a generic “looks good” statement for rendered inspection.

## 8. Quality and Gate 2

Run all five QA surfaces and the Presentation Integrity Check. When the package works and there are 0 known BLOCKER and 0 known MAJOR issues, mark `READY FOR USER REVIEW` and request Gate 2 validation.

Only explicit user approval of the exact build or commit presented at Gate 2 changes the state to `FINAL`. A generic instruction to continue, an approved direction, or an approved asset board is not Gate 2 approval.

## 9. Controlled learning

After Gate 2, identify any generalizable capability. Explain why it is reusable, what was generalized, and what project-specific or sensitive content was removed. Promotion requires explicit approval.

## Stop and return conditions

| Condition | Required action |
|---|---|
| Thesis is missing or contradictory | Stop before visual design and resolve it. |
| Gate 1 is not approved | Stop before build. |
| Deadline, authority, sunk work, or an existing kit is used to skip the process | Produce only the Gate 1 contract; do not code in parallel or treat the kit as a stack decision. |
| A frozen decision changes after Gate 1 | Return to Gate 1 for explicit approval. |
| A known BLOCKER or MAJOR remains | Keep correcting; deny readiness. |
| Publication is requested but the route is unsuitable | Recommend a concrete alternative and wait for approval. |
| Sensitive or project-specific content is proposed for the library | Reject promotion; sanitize and generalize before asking again. |
| The result has not been rendered and inspected | Deny Visual QA and delivery readiness. |
| Live mobile inspection is blocked | Record mobile QA as partial; do not replace it with a static composite or claim full live validation. |
| Direction is approved but primary assets are not | Keep primary assets as candidates and complete the Asset Board Checkpoint before integration. |
| Preview is inaccessible | Escalate from local render to an authorized public preview; do not publish or merge only to obtain a visual surface without authorization. |

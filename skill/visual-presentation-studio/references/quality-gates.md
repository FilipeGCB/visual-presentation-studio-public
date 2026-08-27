# Quality Gates

Quality is evidence, not intent. Inspect the approved contract, implementation, rendered result, interaction states, and delivery package.

## Issue record

Record every issue with ID, severity, surface, location, observation, cause, correction, and status. A correction is closed only after revalidation.

### Severity

- `BLOCKER`: wrong fact or number, serious contradiction, invented information, broken primary navigation, unreadable essential content, or a broken presentation surface.
- `MAJOR`: a serious hierarchy, narrative, density, chart-comprehension, interaction-complexity, or approved-direction divergence problem.
- `MINOR`: polish that does not materially impair comprehension or use.

## Content QA

- Trace every external or uncertain claim to evidence appropriate to the context.
- Recalculate or cross-check numbers, labels, units, dates, totals, percentages, and chart encodings.
- Verify text, chart, annotation, and interaction states express the same fact.
- Distinguish supplied facts, verified research, assumptions, and illustrative examples.
- Reject invented names, data, quotes, findings, or conclusions.
- Confirm editing for fit did not remove essential meaning.

## Narrative QA

- State the thesis in one sentence and verify the opening frames its stakes.
- Apply “This unit exists to…” to every screen or block.
- Apply the removal test; remove repetitions that add no meaning.
- Verify evidence follows or accompanies the claim it supports.
- Identify unexplained jumps, missing premises, and conclusions unsupported by the sequence.
- Confirm the ending resolves the thesis and makes the intended decision or understanding clear.

## Visual QA

Visual QA requires **Visual Inspection** of the exact rendered build or commit. Record the route, renderer, viewport, input mode, state, capture timing, and evidence level.

- Verify focal point, hierarchy, composition, alignment, margins, spacing, and density.
- Verify typography, line length, contrast, cropping, resolution, chart annotation, and responsive adaptation.
- Inspect navigation, transitions, sticky elements, overlays, clipping, and overflow in motion and at rest.
- Compare the render with the approved visual direction and storyboard.
- Compare the render with the approved reference matrix and named primary assets; direction approval alone is not asset approval.
- Inspect settled states after smooth scroll, lazy loading, and reveal motion finish.
- Pair captures with observable facts where relevant: active frame, progress, computed state, image completion and natural dimensions, hidden/visible item counts, and horizontal overflow.
- Ask whether the result is specific to this story or a generic AI interface.
- Run `RENDER → INSPECT → IDENTIFY ISSUES → CORRECT → RENDER AGAIN` until no known BLOCKER or MAJOR remains.

A successful build, source review, previous-version render, component preview, or static composite does not satisfy live Visual QA.

### Evidence levels

- `LIVE DESKTOP`: the exact build was rendered and exercised at a desktop viewport.
- `LIVE MOBILE`: the exact build was rendered and exercised at a mobile viewport with relevant touch behavior.
- `STATIC COMPOSITE`: a crop or composite was reviewed without live behavior.
- `SOURCE REVIEW`: implementation was inspected without a rendered surface.
- `STALE RENDER`: evidence belongs to an earlier build or commit.

Only the first two satisfy their corresponding live viewport claims. Record a blocked surface as partial rather than upgrading weaker evidence.

## Experience QA

- Exercise every navigation path, control, filter, tab, comparison, drill-down, return, and reset.
- Verify selected, active, empty, unavailable, error, and loading states when they exist.
- Confirm labels, focus order, visible focus, keyboard operation, and feedback after action.
- Verify interaction increases comprehension, exploration, or rhythm; remove it otherwise.
- Verify reduced-motion behavior and touch/mobile behavior where applicable.
- Verify scrollytelling frame changes, sticky state, progress, media swaps, and return paths against the active narrative chapter.
- Confirm the audience always knows location, state, and the path back.

## Technical QA

- Run the build or open the standalone artifact through its intended route.
- Inspect the console and network failures; validate assets, fonts, links, imports, and paths.
- Distinguish application errors from browser extensions, automation tooling, and unrelated environment noise.
- Exercise relevant viewport sizes and detect horizontal overflow, clipping, and unintended scroll.
- Verify dependencies are necessary, declared, reproducible, and compatible with local delivery.
- Check responsive behavior, performance, semantic structure, accessibility, and fallbacks proportional to scope.
- Open the packaged delivery independently from the source workspace.

## Presentation Integrity Check

Answer explicitly:

1. Can a person understand the message without knowing the project beforehand?
2. Does the visual treatment make the message clearer than text alone?
3. Is anything present only to appear sophisticated?

If answer 3 is yes, readiness is denied until the element is corrected or its communication function is explicitly justified and revalidated.

## Readiness and Gate 2

Use `NOT READY` until Gate 1 is approved, the implementation matches the contract, every QA surface has evidence, the correction loop is complete, the package works, and the issue ledger shows **0 BLOCKER** and **0 MAJOR** known issues.

Then mark `READY FOR USER REVIEW` and present the exact build or commit, route, evidence levels, and limitations at Gate 2. Only explicit user approval of that version changes the state to `FINAL`; “continue,” direction approval, or asset approval does not.

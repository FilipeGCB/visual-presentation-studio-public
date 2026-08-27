# Rendered Inspection

Use this procedure to produce reproducible visual evidence for the exact build under review.

## Evidence header

Record:

- build or commit identifier and exact route;
- date, renderer, browser, and environment;
- viewport, pixel density, input mode, and reduced-motion state;
- narrative or interaction state exercised;
- evidence level: `LIVE DESKTOP`, `LIVE MOBILE`, `STATIC COMPOSITE`, `SOURCE REVIEW`, or `STALE RENDER`.

## Inspection sequence

1. Open the intended route and confirm that assets and fonts finish loading.
2. Exercise the real navigation or scroll path instead of jumping only to isolated screenshots.
3. Wait for smooth scroll, reveal motion, transitions, and lazy loading to settle before judging opacity, crop, or hierarchy.
4. Capture the visual state and pair it with observable facts when relevant:
   - active frame, chapter, progress, or selected control;
   - image `complete` state and natural dimensions;
   - visible and hidden item counts;
   - document `scrollWidth` versus `clientWidth`;
   - sticky position, media swap, and computed state;
   - console errors attributable to the application.
5. Compare the result with the approved direction, storyboard, reference matrix, and asset board.
6. Record issues, correct them, rerender the same state, and attach revalidation evidence.

## Scrollytelling checks

- Exercise every chapter and confirm text, media, status, and progress change together.
- Validate sticky entry, active range, exit, reverse scroll, and deep-link or reload behavior where relevant.
- Prefer native scrolling and progressive enhancement. Do not hijack scroll merely to create spectacle.
- Confirm the experience preserves meaning with reduced motion and on mobile.

## Preview escalation

Use the least consequential available surface:

`local render → authorized public preview → final published route`

Do not merge or publish only to obtain a visual surface unless the user has authorized that publication step. If local or mobile rendering is blocked by the environment, record the limitation and evidence level; do not attempt policy workarounds or claim full live validation.

## Error attribution

Inspect console and network output, but separate site failures from browser extensions, automation tooling, blocked local-address policies, and unrelated environment noise. Record the origin and impact of any excluded error.

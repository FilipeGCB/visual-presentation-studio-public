# Visual QA

Visual QA is performed on rendered output, never inferred from source code.

## Evidence record

- Build or commit inspected:
- Exact route:
- Renderer and browser:
- Viewports and pixel density:
- Keyboard, pointer, touch, and reduced-motion states:
- Screens or states captured:
- Capture timing and settled-state confirmation:
- Evidence level: LIVE DESKTOP | LIVE MOBILE | STATIC COMPOSITE | SOURCE REVIEW | STALE RENDER

## Observable checks

- A clear focal point and hierarchy exist in every screen or block.
- Composition, alignment, margins, spacing, and rhythm are intentional.
- Text is legible at the actual viewing size; line length and density are controlled.
- Contrast, color roles, typography, imagery, and charts match the approved direction.
- The result is compared with the approved reference matrix and asset board, not only with source code or a prose description.
- Images have correct crop, focal point, resolution, and responsive behavior.
- Primary images form an intentional series; approval status is not inferred from direction approval.
- Charts encode the stated values and remain understandable without guesswork.
- No essential content is clipped, overlapped, truncated, or outside the viewport.
- Navigation, sticky elements, overlays, and transitions behave correctly in motion and at rest.
- Scrollytelling text, media, active chapter, and progress remain synchronized in forward and reverse scroll.
- Responsive adaptations preserve hierarchy rather than simply shrink the desktop layout.
- Rounded cards, glass, gradients, neon, icons, dashboards, and motion appear only when functionally justified.
- The experience looks designed for this story rather than generated from a generic AI template.
- Captures are taken after smooth scroll, reveals, transitions, and lazy loading settle.

Pair screenshots with observable state facts when relevant: active frame, progress, selected controls, image completion and natural dimensions, visible/hidden counts, sticky state, and `scrollWidth` versus `clientWidth`.

`STATIC COMPOSITE`, `SOURCE REVIEW`, and `STALE RENDER` may support diagnosis but do not satisfy live desktop or mobile claims. Record blocked evidence as partial.

## Correction loop

For every issue record observation, cause, correction, and revalidation evidence. Repeat rendering and inspection until 0 known BLOCKER and 0 known MAJOR issues remain.

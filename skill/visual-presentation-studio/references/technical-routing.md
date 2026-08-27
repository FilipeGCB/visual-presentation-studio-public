# Technical Routing

Route in this order: `desired experience → technical need → stack`.

## Decision table

| Need | Recommended route |
|---|---|
| Layout, sequential or scroll navigation, modest motion, small local data | HTML/CSS/JavaScript |
| Substantial state, filters, comparisons, drill-down, or reusable interactive components | React with the smallest justified build setup |
| Backend, authentication, persistence, CRUD, or broad application behavior | Recommend an external app architecture; do not smuggle it into a presentation stack |
| Local final artifact | No hosting required; package all necessary files and usage instructions |
| Complex build, preview, or validation | Vercel may be optional infrastructure, not a quality requirement |
| Explicit hosted or shareable URL | Prepare a ChatGPT Sites handoff when suitable; otherwise recommend a concrete alternative and wait for approval |

## Stack discipline

- Use HTML/CSS/JavaScript when it can express the approved experience reliably.
- Use React when meaningful state or component behavior justifies it.
- Do not adopt a framework for a single transition, chart, or borrowed component.
- A requested framework, executive instruction, sunk investment, or prebuilt kit is not technical need. Record it as a constraint or alternative, recommend the smallest sufficient route, and expose the conflict for Gate 1 approval.
- Prefer local assets and dependency-light builds when the destination is local.
- Preserve semantic HTML, keyboard behavior, focus, responsive layout, contrast, and `prefers-reduced-motion` proportional to the experience.

## Destination discipline

The user validates destination in Gate 1. A local downloadable package is a first-class product. Vercel can support build, preview, validation, or deployment without becoming the final destination.

When publication is explicitly desired, include objective, thesis, narrative, visual direction, structure, assets, interactions, restrictions, frozen decisions, and quality criteria in the handoff. Publication tooling may translate implementation details but may not reinterpret the creative contract silently.

## Escalation boundary

If the experience needs account data, live private APIs, authentication, persistence, or public data collection, identify the expanded security and privacy surface before Gate 1. Recommend appropriate app, backend, or security capabilities rather than treating the work as ordinary presentation HTML.

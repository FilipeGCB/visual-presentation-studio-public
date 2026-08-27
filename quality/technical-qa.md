# Technical QA

Record the command, environment, result, and evidence for each relevant check.

- Standalone files open through the intended local route, or the project build succeeds from a clean install.
- Console and build logs contain no unexplained error.
- Console errors are attributed to the application, browser extension, automation tooling, or environment before disposition.
- Assets, fonts, imports, links, anchors, and relative paths resolve in the packaged destination.
- Navigation and all interaction paths execute without uncaught errors.
- Relevant viewports show no unintended horizontal overflow, clipping, overlap, or inaccessible content.
- Dependencies are necessary, declared, reproducible, and compatible with the approved destination.
- Performance is proportional to the experience; large assets and expensive motion are optimized.
- Semantic structure, keyboard operation, labels, contrast, and reduced-motion behavior are verified proportionally.
- The package works outside the development source directory.
- No backend, authentication, persistence, external request, or deployment dependency was introduced silently.

## Preview escalation

Prefer `local render → authorized public preview → final published route`. Do not merge or publish only to obtain a visual surface unless publication is already authorized. If an environment blocks local or mobile inspection, record the limitation and fallback; do not claim the missing live evidence.

A passing build does not imply Content, Narrative, Visual, or Experience QA has passed.

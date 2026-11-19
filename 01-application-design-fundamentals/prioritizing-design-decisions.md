# Prioritizing Design Decisions

- **Part:** Part I: Application Design Fundamentals
- **PDF start page:** 53
- **Status:** Source-verified

## Why this matters (retro recreation)

The HIG's three-layer prioritization model (differentiate / deliver expected features / meet minimum
requirements) is directly useful for scoping a retro recreation: which fidelity targets are "must have" for
the recreation, which are expected-but-optional, and which are differentiator layers.

## Key sections to review (from TOC)

- Meet Minimum Requirements (p. 53)
- Deliver the Features Users Expect (p. 55)
- Differentiate Your Application (p. 56)

## Source notes (with page refs)

- p. 53 — Design decisions must be prioritized given business constraints; HIG organizes principles into
  three layers (Figure 4-1, p. 53).
- p. 53 — Meet Minimum Requirements: nonnegotiable guidelines for being "at home" on Mac OS X; e.g.
  - Respect the single menu bar; avoid menu bars in app windows.
  - Respect the Dock.
  - Respect the multilayered window environment.
  - Put files in proper locations (preferences, documents).
  - Use standard controls (p. 255).
  - Avoid system-reserved keyboard shortcuts; respect Apple-recommended ones (e.g. Cmd-S for Save).
  - Support the Clipboard (cut/copy/paste).
- p. 55 — Deliver the Features Users Expect: after minimum requirements; deliver expected features:
  - Communicate effectively (error messages, feedback, status).
  - Support application bundles and drag-and-drop installation.
  - Create high-quality icons/graphics.
  - Comply with layout guidelines.
  - Provide effective user assistance (Apple Help, help tags).
  - Support drag and drop.
  - Use display names.
- p. 56 — Differentiate Your Application: go above and beyond:
  - Support modelessness (sheets/drawers; modes only if clear visual indicator, easy in/out).
  - Integrate Spotlight (importer for custom file formats; consider search capabilities).
  - Support fast user switching.
  - Internationalize the user interface.
  - Make application accessible to users with disabilities.
  - Strive for high performance and reliability.
  - Surprise and delight.

## Implementation implications

- For the retro recreation, the "minimum requirements" layer likely maps to: single menu bar, standard
  controls, Cmd-key equivalents, clipboard support, proper window types.
- Differentiation layer maps to: Spotlight integration, accessibility, high-fidelity animation/feedback.
- The recreation can use these layers as a checklist when deciding how deep to go for each feature.

## Assets / examples to capture later

- [ ] Extract Figure 4-1 (three-layer pyramid, p. 53) as an asset/reference image.

## Open questions / follow-up extraction

- [ ] Which layers does the original app being recreated actually span? (Audit original feature set.)
- [ ] Where should the recreation draw the line between layers for scope control?

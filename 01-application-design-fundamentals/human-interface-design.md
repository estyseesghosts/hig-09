# Human Interface Design

- **Part:** Part I: Application Design Fundamentals
- **PDF start page:** 39
- **Status:** Reviewed

## Why this matters (retro recreation)

Core principles for evaluating and building the recreation's interaction design. Many of these map directly
to component behaviors the recreation will need to implement (menus, windows, controls, feedback).

## Key sections to review (from TOC)

- Human Interface Design Principles (p. 39)
  - Metaphors (p. 39)
  - Reflect the User's Mental Model (p. 39)
  - Explicit and Implied Actions (p. 41)
  - Direct Manipulation (p. 41)
  - User Control (p. 42)
  - Feedback and Communication (p. 42)
  - Consistency (p. 43)
  - WYSIWYG (p. 44)
  - Forgiveness (p. 44)
  - Perceived Stability (p. 45)
  - Aesthetic Integrity (p. 45)
  - Modelessness (p. 46)
  - Managing Complexity in Your Software (p. 46)
- Keep Your Users in Mind (p. 47)
  - Worldwide Compatibility (p. 47)
  - Extending the Interface (p. 51)

## Source notes (with page refs)

- p. 39 — Principles critical to elegant, efficient, intuitive, Aqua-compliant interfaces.
- p. 39 — Metaphors: use concrete familiar ideas; make metaphors obvious; balance suggested use vs.
  computer's ability to extend metaphor (e.g. Trash capacity is not limited by physical basket).
- p. 39 — Reflect the User's Mental Model: user already has mental model from real-world experience and prior
  software; design should reflect task expectations (e.g. email: create letter, select recipient, send);
  iTunes example: song-centric arrangement reflects music mental model.
- p. 41 — Explicit vs. Implied Actions: explicit = menu commands clearly state action/result; implied =
  drag-and-drop conveys relationship; direct manipulation: onscreen object visible, impact immediately visible.
- p. 42 — User Control: allow user, not computer, to initiate/control actions; provide appropriate level of
  control for audience; allow user to proceed past warnings.
- p. 42 — Feedback and Communication: keep users informed when action initiated; animation (Dock icon bounce,
  window minimize slide, sheet unfurl, drawer slide); use progress indicators for lengthy ops; spinning
  wait cursor if unresponsive for 2s.
- p. 43 — Consistency: consistent with Mac OS X standards (reserved/recommended keyboard equivalents, Aqua
  compliance); consistent within itself (terminology, icons, concepts, control placement); consistent with
  earlier versions; consistent with people's expectations.
- p. 44 — WYSIWYG: no significant difference between onscreen and final output; display results immediately;
  menus must list commands; don't hide features only in toolbars/contextual menus (must be in menu bar too).
- p. 44 — Forgiveness: make actions easily reversible; Undo/Revert to Saved; warn before irreversible loss.
- p. 45 — Perceived Stability: standard graphical elements (menu bar, window controls); clear finite set of
  objects + actions; command dimmed rather than omitted when not applicable; preserve user window settings;
  status/feedback contributes.
- p. 45 — Aesthetic Integrity: information well organized, consistent with good visual design; keep graphics
  simple; don't overload windows/dialogs; don't use arbitrary symbols; consistent font/control sizes within
  window; use correct control types (checkboxes for multi-select, push buttons for immediate commands,
  avoid bevel buttons as tabs).
- p. 46 — Modelessness: allow users to do whatever they want; avoid modes locking user into operation;
  drawers/sheets preferred; acceptable modes: short-term, alerts, installers; if modes used, clear visual
  indicator, easy to enter/exit.
- p. 47 — Worldwide Compatibility: design for locale/cultural differences; visible elements localizable;
  avoid offensive imagery (owl example); different calendars; text translation up to 50% longer; Unicode
  support; resources in separate files; logical (not visual) content flow for RTL.
- p. 49 — Universal Accessibility: build in support from beginning; don't override system accessibility
  features (keyboard-only operation, VoiceOver, etc.).

## Implementation implications

- The recreation should implement: undo/redo, direct manipulation, consistent terminology/placement, menu
  bar commands for feature availability, progress feedback, forgiving actions, standard controls per type.
- Retain user window state; use standard Aqua control semantics.

## Assets / examples to capture later

- [ ] Extract figures for Human Interface Design principles (figures in Part III may reuse these).

## Open questions / follow-up extraction

- [ ] How much of this chapter applies to the retro recreation vs. the original app being recreated?
- [ ] Which principles were violated by the original app (if any) — useful for recreation fidelity targets?

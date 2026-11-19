# Layout Guidelines

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 347
- **Status:** Reviewed

## Why this matters (retro recreation)

Quantitative-ish layout guidance for recreating preferences/dialog/toolbar screens; center equalization,
spacing, alignment rules.

## Key sections to review (from TOC)

- Positioning Regular-Size Controls in a Window Body (p. 347)
  - A Simple Preferences Window (p. 347)
  - A Tabbed Window (p. 350)
  - A Standard Alert (p. 353)
  - A Dialog with a List View (p. 354)
- Positioning Small and Mini Controls in a Window Body (p. 356)
  - Layout Example for Small Controls (p. 356)
  - Layout Example for Mini Controls (p. 359)
- Grouping Controls in a Window Body (p. 361)
  - Grouping with White Space (p. 361)
  - Grouping with Separators (p. 362)
  - Grouping with Group Boxes (p. 363)
- Positioning Text and Controls in a Bottom Bar (p. 365)

## Source notes (with page refs)

- p. 347 — Chapter intro: guidelines don't dictate exact pixels; describe Aqua layout principles
  (center equalization, text/control alignment, white space, visual balance); consistency in layout
  decisions.
- p. 347–349 — Simple preferences window: center equalization (visual weight balanced L/R of content area);
  stacked labels/controls vertically aligned; colons right-aligned; checkboxes/radio left-aligned.
- p. 349–350 — Consistent spacing: equal space above/below horizontal separators (12px), equal margins on
  sides/bottom (20px), equal space between controls (8px); 14px margin between top controls and title bar,
  18px between main controls and Help button (min 16px).
- p. 350–353 — Tabbed window: same general guidelines; center equalization; always center tab view within
  window; consistent control widths (e.g. Font popup and Size combo same width); 16px margin between group
  box sides and tab pane side edges; 20px between tab pane bottom and window edges; 16px bottom controls to
  group box bottom, 10px top controls to group box top.
- p. 353–354 — Standard alert: action button bottom-right; lower margin same as dialogs (20px); side margins
  24px; icon 64x64; main + informative text.
- p. 354–356 — Dialog with list view: no icon → left-align list w/ intro text, left-align leftmost button,
  right-align rightmost button; with icon → icon left of text, left-align text/list/leftmost button, Help
  below icon.
- p. 356–359 — Small controls: use only when necessary (tool panels, panels, Automator); don't mix sizes;
  consistent within window/panes; center equalization for small; alignment; white space consistent.
- p. 359–361 — Mini controls: stacked left-aligned, consistent widths, center-equalized, white space consistent.
- p. 361–365 — Grouping: white space (small groups), separators (space-efficient), group boxes (strongest visual
  indication, most space); none inherently more correct.

## Implementation implications

- Recreated windows/dialogs should follow center equalization and consistent spacing rules (e.g. 20px margins,
  8px control spacing, right-aligned colons).

## Assets / examples to capture later

- [ ] Capture layout figures (16-x) via pdf_render_pages for future screen recreation reference.

## Open questions / follow-up extraction

- [ ] Are exact pixel measurements needed for the retro recreation (likely yes for pixel-faithful recreation)?

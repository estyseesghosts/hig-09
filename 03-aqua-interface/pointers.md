# Pointers

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 161
- **Status:** Reviewed

## Why this matters (retro recreation)

Pointer semantics (hot spot, hot zone, standard cursors by context) matter for recreating the interaction feel
of the original app — especially drag state (copy/move/poof) and text editing cursors.

## Key sections to review (from TOC)

- Standard Pointers (p. 161)
  - Arrow (p. 161)
  - Contextual menu (p. 161)
  - Alias (p. 161)
  - Poof (p. 161)
  - Copy (p. 161)
  - Not allowed (p. 162)
  - I beam (p. 162)
  - Crosshair (p. 162)
  - Pointing hand / Open hand / Closed hand (p. 162)
  - Move left/right/up/down (p. 162-163)
- Designing Your Own Pointers (p. 163)

## Source notes (with page refs)

- p. 161 — Standard pointers designed to provide feedback; hot spot = portion that must be positioned within
  object before click/tap has effect; hot zone = area pointer's hot spot must be within for clicks to work.
- p. 161 — Table 12-1: Arrow (menu bar, desktop, scroll bar, resize controls, title bar, close/zoom/minimize
  buttons, other controls); Contextual menu arrow (Control key over object with contextual menu); Alias
  (drag destination gets alias, original not moved); Poof (proxy object dragged will disappear without
  deleting original if released); Copy (drag destination gets copy); Not allowed (invalid drag destination).
- p. 162 — I beam (selecting/inserting text); Crosshair (precise rectangular selection for graphics);
  Pointing hand (URL links); Open hand (item can be manipulated); Closed hand (pushing/sliding/adjusting
  object); Move cursors (splitter resizing).
- p. 163 — Spinning wait cursor auto-displayed by window server when app can't handle events (2-4s); avoid
  situations causing it; Spin Control app helps. Custom pointers: 32-bit RGBA up to 64x64; if larger, use
  window tracking; custom versions of related pointers needed.

## Implementation implications

- Recreated app should use standard cursors contextually (arrow, I beam, crosshair, hands, move, poof, not
  allowed) and the spinning wait cursor behavior.

## Assets / examples to capture later

- [ ] Capture pointer-related figures if any (Fig. 12-1 spinning wait cursor).

## Open questions / follow-up extraction

- [ ] Is custom pointer design in scope for the retro recreation?

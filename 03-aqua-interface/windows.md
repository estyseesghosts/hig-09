# Windows

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 191
- **Status:** Reviewed

## Why this matters (retro recreation)

Window behavior/appearance is a core fidelity surface for a retro recreation: document vs. application vs.
panel windows, title bars, toolbars, drawers, dialogs, save flows.

## Key sections to review (from TOC)

- Types of Windows (p. 191)
- Window Appearance (p. 192)
- Window Elements (p. 194)
  - The Title Bar (p. 197)
  - Title Bar Buttons (p. 198)
  - The Proxy Icon (p. 199)
  - Toolbars (p. 200)
  - Scope Bars (p. 205)
  - Source Lists (p. 208)
  - Bottom Bars (p. 212)
  - Drawers (p. 214)
- Window Behavior (p. 216)
  - Opening Windows (p. 216)
  - Naming New Windows (p. 217)
  - Positioning Windows (p. 218)
  - Moving Windows (p. 220)
  - Resizing and Zooming Windows (p. 220)
  - Minimizing and Expanding Windows (p. 221)
  - Closing Windows (p. 221)
  - Window Layering (p. 222)
  - Main, Key, and Inactive Windows (p. 222)
  - Click-Through (p. 223)
  - Scrolling Windows (p. 225)
  - Automatic Scrolling (p. 227)
- Panels (p. 227)
  - Inspector Windows (p. 229)
  - Transparent Panels (p. 230)
  - Fonts Window and Colors Window (p. 234)
  - About Windows (p. 234)
- Dialogs (p. 235)
  - Types of Dialogs and When to Use Them (p. 235)
  - Sheets (Document-Modal Dialogs) (p. 236)
  - Dialog Appearance and Behavior (p. 240)
  - Dismissing Dialogs (p. 241)
  - Providing an Apply Button in a Dialog (p. 242)
  - Expanding Dialogs (p. 242)
- Find Windows (p. 243)
- Preferences Windows (p. 243)
- The Open Dialog (p. 245)
- Dialogs for Saving, Closing, and Quitting (p. 246)
  - Save Dialogs (p. 247)
  - Closing a Document With Unsaved Changes (p. 249)
  - Attempting to Save a Locked or Read-Only Document (p. 249)
  - Saving Documents During a Quit Operation (p. 249)
  - Quitting an Application With Multiple Unsaved Documents Open (p. 250)
- The Choose Dialog (p. 251)
- The Print Dialog (p. 253)
- Page Setup Dialog (p. 254)

## Source notes (with page refs)

- p. 191 — Four main window types: document, application, panel, dialogs/alerts.
- p. 192 — Window = window-frame areas (title bar, toolbar, bottom bar) + window body; v10.5+ unified
  title bar/toolbar; no brushed metal in v10.5+.
- p. 194 — Every window has title bar + close button; docs also scroll bars, minimize/zoom, proxy icon, title,
  resize control, toolbar.
- p. 197 — Title bar: doc windows show document name; app windows show app name; panels descriptive; use em
  dash (—) to separate multiple items; don't use pathnames; only close/minimize/zoom in title bar; toolbar
  control in unified area if toolbar present.
- p. 199 — Proxy icon after first save; dimmed when unsaved changes; Command-click title/proxy shows path
  pop-up menu; minimized docs show diamond; unsaved close button shows dot.
- p. 200–205 — Toolbars: immediate action on click; items also menu commands; preferences windows toolbar
  differs (not customizable, no show/hide control).
- p. 205–206 — Scope bars: for search/filter; filter rows; source list vs. scope bar distinction.
- p. 208–211 — Source lists: blue background for primary navigation; white for selection-only/panels; ≤2 levels
  hierarchy; no controls other than organize controls; gradient buttons for add/remove if no bottom bar.
- p. 212–214 — Bottom bars: controls affect window-body contents; not customizable; 32px (regular) or 22px
  (small) height; not for most-frequent commands.
- p. 214–216 — Drawers: slide out from parent; frequent controls not always visible; modal? no—parent stays
  visible; close on minimize; resize rules; state maintained.
- p. 216–227 — Window behavior: opening triggers; untitled naming ("untitled", "untitled 2"); positioning
  (horizontally centered, below menu bar, 20px offset, no Dock overlap); moving; resize/zoom (user state after
  7px change; zoom toggles standard/user state); minimize; close; layering; main/key/inactive windows; click-
  through; scrolling; automatic scrolling; panels.
- p. 227–235 — Panels types; inspector vs. info window; transparent panels criteria; fonts/colors windows; About
  window requirements; dialogs types; sheets.

## Implementation implications

- Recreated app should implement window state persistence (position/size), untitled naming, save sheets, etc.

## Assets / examples to capture later

- [ ] Capture window screenshots from `../images/` (e.g. System Preferences, TextEdit Open) for fidelity.

## Open questions / follow-up extraction

- [ ] Does the recreated app use document windows, application windows, panels? (Depends on app scope.)
- [ ] Which dialogs/sheets (save, open, print, alerts) are in scope?

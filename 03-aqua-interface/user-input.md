# User Input

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 97
- **Status:** Summarized

## Why this matters (retro recreation)

This is the largest and most implementation-heavy chapter in Part III: it defines how mouse, keyboard,
selection, and text editing should behave. For a retro recreation targeting 2009-era input expectations,
these are the exact behaviors the recreated UI should honor (or deliberately deviate from).

## Key sections to review (from TOC)

- The Mouse and Other Pointing Devices (p. 97)
  - Clicking (p. 97)
  - Double-Clicking (p. 98)
  - Pressing and Holding (p. 98)
  - Dragging (p. 98)
- The Trackpad (p. 98)
- The Keyboard (p. 99)
  - The Functions of Specific Keys (p. 100)
  - Keyboard Shortcuts (p. 106)
  - Reserved Keyboard Shortcuts (p. 107)
  - Creating Your Own Keyboard Shortcuts (p. 108)
  - User-Defined Keyboard Shortcuts (p. 110)
  - Keyboard Focus and Navigation (p. 110)
  - Type-Ahead and Key-Repeat (p. 111)
- Selecting (p. 112)
  - Selection Methods (p. 112)
  - Selections in Text (p. 115)
  - Selections in Spreadsheets (p. 116)
  - Selections in Graphics (p. 117)
- Editing Text (p. 117)
  - Inserting Text (p. 117)
  - Deleting Text (p. 117)
  - Replacing a Selection (p. 118)
  - Intelligent Cut and Paste (p. 118)
  - Editing Text Fields (p. 119)
  - Entering Passwords (p. 120)

## Source notes (with page refs)

- p. 97 — GUI optimized for pointing device (mouse); keyboard is an option; users can enable keyboard access
  for all mouse functions.
- p. 97 — Pointer shapes change by context (I-beam over text, arrow over palettes); change shape only to
  convey function change.
- p. 97 — Click = press down + release without moving; dragging = press, move, release; click effect should be
  immediate and obvious; selection made when button pressed, action on release.
- p. 98 — Double-click follows immediately after first; should never be the only way to perform an action.
- p. 98 — Press (hold) should have same effect as click except in defined areas (scroll arrows, Dock tiles).
- p. 98 — Dragging: visual feedback while dragging; dragging graphic moves whole object not just outline; can
  restrict boundaries; auto-scroll documents; "poof" for proxy objects being dragged out of existence.
- p. 98 — Trackpad: pointer movement, selection/activation, scrolling, contextual menus; multi-touch gestures
  (pinch, rotate, 3-finger swipe, 4-finger swipe) should be consistent and not redefine standard gestures.
- p. 99–120 — Keyboard: use character/modifier/arrow/function keys consistently; don't rely on keys that don't
  exist on all keyboards; consistent use of Tab, Enter, Return, Delete, Esc; Shift/Caps/Option/Command/Control
  semantics; arrow-key navigation rules (Table 8-1), semantic units (Option/Command extend); Shift+arrow
  selection (Table 8-2); reserved keys (Esc cancel, Cmd-Tab app switch, Cmd-Shift-Q logout, Cmd-Option-Esc Force
  Quit, F9/F10 window tiling, F11/F12, Cmd-Space Spotlight, etc. — Table 8-3); recommended shortcuts
  (Cmd-A Select All, Cmd-G Find Next, Cmd-Shift-P Page Setup, Cmd-Shift-S Save As, Cmd-Shift-V Paste as
  Quotation, Cmd-Shift-Z Redo; Table 8-5); users may remap shortcuts (Command-Option-W Finder Close All,
  Command-Option-M Minimize All).
- p. 107 vs. p. 371 - **Source conflict:** Table 8-3 lists Command-H and Option-Command-H as reserved, but
  Table A-1 omits the Apple icon for both. Treat them as reserved. The full Table A-1 transcription and all
  discrepancies are in [Appendix A](../04-reference/appendix-a-keyboard-shortcuts.md).
- p. 110 — Keyboard focus: default mode moves focus between fields that accept keyboard input; full keyboard
  access mode available; focus indicated with ring in Aqua/Graphite appearance color; in list views arrow
  keys open/close disclosure triangles; Shift-Tab reverse; Tab cycles in lists, Return can substitute.
- p. 111 — Type-ahead: keystrokes queued when faster than processing; key-repeat adjustments in Keyboard &
  Mouse preferences; ignore key-repeat for Cmd shortcuts; key-repeat works only when app is ready to accept
  input, not during type-ahead.
- p. 112 — Selecting: immediate visual feedback; selection never alters object; always undoable (click outside).
  Text = block of text; arrays = lists/tables; graphics = discrete objects.
- p. 112–114 — Selection by clicking/dragging (anchor point, active end); Shift-click extends; Command-click
  discontinuous selection; addition vs. fixed-point models.
- p. 115 — Text selection via double-click: double-click within word selects word with "smart" behavior;
  double-click in space selects space; triple-click selects next logical unit; word definition (letters,
  digits, symbols, etc.).
- p. 117–120 — Editing: insert via insertion point; delete removes selection or preceding char; replacement
  via typing over selection; intelligent cut/paste (spaces handling); text fields; passwords as bullets.

## Implementation implications

- Recreated app should implement: immediate click feedback, double/triple-click semantics, keyboard
  equivalents for all critical functions, reserved-key respect (Cmd-Tab, Cmd-Shift-Q, F9/F10, etc.), keyboard
  focus ring, type-ahead, key-repeat, selection undoability, intelligent cut/paste.
- Password fields: bullets only, double-click selects all bullets, modify bullet count when leaving field.
- Arrow-key semantics (Table 8-1/8-2) should be honored for text editing fidelity.

## Assets / examples to capture later

- [ ] Extract figures: keyboard focus (p. 110, Figs 8-1/8-2), selection (p. 112-114, Figs 8-4-8-8), text
      editing (p. 115+).

## Open questions / follow-up extraction

- [ ] Are all of these input behaviors in scope for the retro recreation (likely a subset per feature)?
- [ ] Does the recreation need to support full keyboard access mode, or just standard + recommended shortcuts?

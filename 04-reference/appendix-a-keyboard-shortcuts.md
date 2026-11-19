# Appendix A: Keyboard Shortcuts Quick Reference

- **PDF start page:** 367
- **Status:** Reviewed

## Purpose

Quick lookup for which keyboard shortcuts the retro recreation should implement (reserved vs. recommended
vs. custom), and which keyboard behaviors (focus navigation, type-ahead) the recreated app should honor.

## Notes (with page refs)

- p. 367 — Appendix A intro: Table A-1 lists system-reserved and commonly used shortcuts.
  - System-reserved: users rely on these to perform specified actions regardless of active app (including
    accessibility purposes). **Do not override.**
  - Recommended: users expect these to mean the same thing from application to application. Provide if the app
    performs the associated task; think very carefully before overriding otherwise.
  - Not listed in Table A-1: sequences that may be used for frequently used commands if appropriate; Apple may
    reserve more in the future. Creating your own: see "Creating Your Own Keyboard Shortcuts" (p. 108).
- p. 367 — Note: except for system-reserved function keys F9, F10, F11, F12, Table A-1 lists only combinations of
  two or more keys; single keys (Tab, Return, etc.) covered in "The Functions of Specific Keys" (p. 100).
- p. 367 — Table A-1 groups shortcuts by primary key with modifier symbols (Command, Control, Option, Shift);
    shortcuts with an icon should not be overridden (OS uses them); others are recommended.

- p. 368–374 — Key sections of Table A-1 (with actions cross-referenced to chapter pages):
  - Space bar / Spotlight: show/hide Spotlight search field (Apple reserved); show Spotlight results window
    (Apple reserved).
  - Tab: navigate through controls in reverse direction; forward to next recently used app; backward through
    open apps list; next grouping of controls in dialog / next table cell; previous grouping of controls.
  - Esc: open Front Row; open Force Quit dialog; quit all apps and restart computer.
  - Eject: quit all apps and shut down computer.
  - F1: toggle full keyboard access on/off; F2: move focus to menu bar; F3: move focus to Dock; F4: move focus to
    active/next window (also to previously active); F5: move focus to toolbar; F5 also turns VoiceOver on/off;
    F6: move focus to first/next panel, previous panel; F7: temporarily override keyboard access mode;
    F8: tile/untile enabled spaces; F9: tile/untile all open windows; F10: tile/untile all windows in active
    app; F11: hide/show all open windows; F12: hide/display Dashboard.
  - Function/Eject/other: `, ~ ` activate next/previous open window; F-keys list continues to p. 369.
  - Letter combinations (Cmd-key): e.g. Command-A Select All, Command-B Bold, Command-C Copy, Command-F Find,
    Command-G Find Next/Previous, Command-H Hide, Command-I Italic/Info, Command-J scroll to selection, Command-M
    Minimize, Command-N New, Command-O Open, Command-P Print/Page Setup, Command-Q Quit, Command-S Save/Save As,
    Command-T Show Fonts/Show/Hide Toolbar, Command-U Underline, Command-V Paste/Paste Style/Paste and Match Style,
    Command-W Close/Close File/Close All, Command-X Cut, Command-Z Undo/Redo.
  - Command–modifier key–Space bar (Command-Option-Space / Command-Control-Space) open Help Viewer etc.

- p. 371 — Command–Option–F: jump to the search field control (see "Search Fields" p. 326).

- p. 106, 107, 108, 110 — Keyboard chapter context for shortcuts:
  - p. 106 — Functions of specific keys (Tab, Return, Enter, Delete, Esc, etc.); recommended shortcuts
    (Table 8-5): Cmd-A Select All, Cmd-G Find Next, Cmd-Shift-P Page Setup, Cmd-Shift-S Save As, Cmd-Shift-V
    Paste as Quotation, Cmd-Shift-Z Redo.
  - p. 107 — Reserved keyboard shortcuts (users rely on them; do not override; includes Cmd-Tab app switch, Cmd-
    Shift-Q logout, Cmd-Option-Esc Force Quit, F9/F10 window tiling, F11/F12, Cmd-Space Spotlight, etc.).
  - p. 108 — Creating your own keyboard shortcuts; p. 110 — Keyboard focus and navigation; p. 111 — type-ahead.

## Extraction targets

- [ ] Extract full Table A-1 to a reference table in the recreation notes (reserved vs. recommended lists).

## Open questions / follow-up extraction

- [ ] Which reserved shortcuts are actually exercised by the app being recreated?
- [ ] Does the retro recreation need to implement full keyboard access modes (F1/F7)?

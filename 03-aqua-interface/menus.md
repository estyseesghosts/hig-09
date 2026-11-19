# Menus

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 165
- **Status:** Reviewed

## Why this matters (retro recreation)

Menus are likely a primary UI surface in the recreated app; the chapter defines menu bar structure, naming,
behavior, and contextual/Dock menus — highly fidelity-relevant.

## Key sections to review (from TOC)

- Menu Behavior (p. 165)
- Designing the Elements of Menus (p. 167)
  - Titling Menus (p. 167)
  - Naming Menu Items (p. 167)
  - Using Icons in Menus (p. 169)
  - Using Symbols in Menus (p. 170)
  - Toggled Menu Items (p. 172)
  - Grouping Items in Menus (p. 173)
- The Menu Bar and Its Menus (p. 175)
  - The Apple Menu (p. 177)
  - The Application Menu (p. 177)
  - The File Menu (p. 179)
  - The Edit Menu (p. 181)
  - The Format Menu (p. 183)
  - The View Menu (p. 184)
  - Application-Specific Menus (p. 186)
  - The Window Menu (p. 186)
  - The Help Menu (p. 187)
  - Menu Bar Extras (p. 188)
- Contextual Menus (p. 188)
- Dock Menus (p. 190)

## Source notes (with page refs)

- p. 165 — Menus based on "see and point"; pull-down in menu bar, Dock, contextual menus; controls-hosted
  menus discussed in Controls.
- p. 165–166 — Menu behavior: drag from menu title to item; no action until release; can open/scan without
  acting; item blinks briefly when activated; menu stays open until another action forces close.
- p. 166 — Even if all items unavailable, menu title not dimmed; items dimmed. Avoid long menus; scrollable
  menus with indicators.
- p. 167 — Menu titles should represent items; avoid icons for titles; short titles. Menu item names are
  actions (verbs, base form) or attributes (adjectives, "Change the selected object to…"); unavailable items
  dimmed; title-style capitalization; avoid articles.
- p. 169 — Icons in menus only when significant value; symbols only acceptable characters (Table 13-1).
- p. 172 — Toggled menu items: opposite pairs w/ checkmark, name changes (Show/Hide Ruler), checkmark for
  style attributes. Avoid ambiguous commands.
- p. 173 — Grouping: most frequent top, group related; don't mix actions and attributes in same group.
- p. 175 — Single menu bar across top of screen; never in windows; always contains Apple menu, Spotlight
  icon, application menu, Window menu; optional File/Edit/Format/View/Help + app-specific + extras.
- p. 177–179 — Application menu: About, Preferences…, Services, Hide, Hide Others, Show All, Quit; title
  bold, ≤16 chars, no version; File menu: New, Open, Open Recent, Close, Close File, Save, Save As, Export
  As, Save All, Revert to Saved, Print, Page Setup.
- p. 181–183 — Edit menu: Undo, Redo, Cut, Copy, Paste, Paste and Match Style, Delete, Select All, Find,
  Find Next, Spelling, Speech, Special Characters; Format menu: Show Fonts, Show Colors, Bold, Italic,
  Underline, Bigger/Smaller, Copy/Paste Style, Align, Ruler.
- p. 184–186 — View menu: Show/Hide Toolbar, Customize Toolbar; Window menu: Minimize, Zoom, Minimize
  All, Bring All to Front, Arrange in Front, open docs list with bullets/diamonds/checkmarks.

## Implementation implications

- Recreated app's menu bar should mirror the standard structure (Apple, app, File, Edit, Format, View,
  Window, Help ordering guidance; app-specific between View and Window).
- Edit menu command set (Undo, Redo, Cut, Copy, Paste, Select All, Find, spelling, etc.) is likely in scope.

## Assets / examples to capture later

- [ ] Capture menu screenshots from images/ (Finder-Menu, Software-Update, etc.) for fidelity reference.

## Open questions / follow-up extraction

- [ ] Which menus does the recreated app actually need (which standard menus apply)?
- [ ] Does the recreated app have its own app-specific menus?

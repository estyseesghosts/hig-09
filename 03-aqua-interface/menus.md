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
  acting; item blinks briefly when activated; menu stays open until another action forces close (choosing a
  command, moving pointer to another menu title, click outside, system-initiated alert/app switch/quit).
  Menu can be opened with a click and stays open until another action closes it; stays open without holding
  mouse button.
- p. 166 — Even if all items unavailable, menu title not dimmed; items dimmed. Avoid long menus; scrollable
  menus with indicators (downward-pointing indicator at bottom; upward at top when scrolling down).
- p. 167 — Menu titles should represent items; avoid icons for titles; short titles. Menu item names are
  actions (verbs, base form) or attributes (adjectives, "Change the selected object to…"); unavailable items
  dimmed; title-style capitalization; avoid articles.
- p. 167 — Ellipsis character (…) after menu item indicates additional info required to complete a command.
- p. 168 — Dynamic menu items: commands that change when user presses a modifier key (e.g. Option key on the
  Finder Window menu changes Minimize → Minimize All); system sizes menu to hold widest item including
  Option-enabled commands. Never the only way to accomplish a task; only a single modifier key to reveal.

- p. 169 — Icons in menus only when significant value; symbols only acceptable characters (Table 13-1).
- p. 170 — Symbols in menus: checkmark (active document in Window menu; setting applies to entire selection;
  style attribute in effect), dash (applies to part of selection / mixed state), bullet (document with unsaved
  changes), diamond (minimized document). Checkmark overrides bullet if active window has unsaved changes.

- p. 172 — Toggled menu items: opposite pairs w/ checkmark, name changes (Show/Hide Ruler), checkmark for
  style attributes. Avoid ambiguous commands (e.g. "Use Grid" could mean on/off).
- p. 173 — Grouping: most frequent top, group related; don't mix actions and attributes in same group; group
  interdependent attributes (mutually exclusive vs accumulating); repeat term >2x → dedicated menu/submenu.

- p. 175 — Single menu bar across top of screen; never in windows; always contains Apple menu, Spotlight
  icon, application menu, Window menu; optional File/Edit/Format/View/Help + app-specific + extras. Ordering
  of app-specific menus reflects natural hierarchy; higher-level/universal objects left, specific entities right.
- p. 175 — Optional menus may be omitted; insufficient room → menu bar extras omitted first, then menus from
  right. Full-screen: may allow hiding menu bar; provide clearly visible way to reappear.

- p. 177 — Application menu: About, Preferences…, Services, Hide, Hide Others, Show All, Quit; title bold,
  ≤16 chars, no version; About uses short name; Quit preceded by separator; other app-specific items between
  Preferences and Services (no Help item — that's in Help menu).
- p. 179 — File menu: New, Open, Open Recent, Close, Close File, Save, Save As, Export As, Save All, Revert to
  Saved, Print, Page Setup; Open Recent submenu most-recent-first, display names not paths; Close Option =
  Close All (Cmd-Option-W); Save dims when unsaved; Save As uses Save dialog + Format pop-up (avoid multiple
  Save As Format commands; use Export As instead); Export As keeps original open; Save All; Revert to Saved +
  alert; Print… (Cmd-P); Page Setup… (Cmd-Shift-P).

- p. 181 — Edit menu: Undo, Redo, Cut, Copy, Paste, Paste and Match Style, Delete, Select All, Find,
  Find Next, Spelling, Speech, Special Characters; Undo naming ("Undo Typing", "Undo Paste", "Can't Undo");
  Redo reverses Undo; Delete = Clear-key equivalent; Select All (Cmd-A); Find… (Cmd-F); Find submenu items;
  Spelling… (Cmd-:); Speech; Special Characters… (auto-inserted at bottom).
- p. 183 — Format menu: Show Fonts (Cmd-T), Show Colors (Cmd-Shift-C), Bold (Cmd-B), Italic (Cmd-I),
  Underline (Cmd-U), Bigger (Cmd-Shift-=), Smaller (Cmd-Hyphen), Copy Style (Cmd-Option-C), Paste Style
  (Cmd-Option-V), Align Left (Cmd-{), Center (Cmd-|), Justify, Align Right (Cmd-}), Show Ruler, Copy Ruler
  (Cmd-Ctrl-C), Paste Ruler (Cmd-Ctrl-V).

- p. 184 — View menu: Show/Hide Toolbar (Cmd-Option-T, dynamic toggle), Customize Toolbar…; avoid View menu
  for panels (use Window menu).
- p. 186 — Window menu: Minimize (Cmd-M), Zoom, Minimize All (Cmd-Option-M), Bring All to Front (optional),
  Arrange in Front (Option toggle), open docs list (bullets/diamonds/checkmarks); app-specific between View and
  Window; Close in File menu.

- p. 187 — Help menu: rightmost; system-provided Spotlight For Help first item; app Help item = "AppName Help"
  (e.g. "Mail Help"); opens Help Viewer first page; keep to one custom item; don't use as TOC.

## Implementation implications

- Recreated app's menu bar should mirror the standard structure (Apple, app, File, Edit, Format, View,
  Window, Help ordering guidance; app-specific between View and Window).
- Edit menu command set (Undo, Redo, Cut, Copy, Paste, Select All, Find, spelling, etc.) is likely in scope.
- Dynamic menu items (modifier-key revealed) must not be the only path; contextual menus never the only path.

## Assets / examples to capture later

- [ ] Capture menu screenshots from images/ (Finder-Menu, Software-Update, etc.) for fidelity reference.

## Open questions / follow-up extraction

- [ ] Which menus does the recreated app actually need (which standard menus apply)?
- [ ] Does the recreated app have its own app-specific menus?

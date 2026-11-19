# Component Spec: Menu Item

- **Spec ID:** CMP-07
- **HIG chapter(s):** Menus (pp. 165-176); ellipsis (pp. 131-132); dialog accelerators (pp. 241-242)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [Appendix A](../04-reference/appendix-a-keyboard-shortcuts.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A menu item is a command or attribute the user chooses from a menu. The HIG divides names into **actions**
(verb phrases: "Save", "Copy") and **attributes** (adjectives that fit "Change the selected object to …":
"Bold", "Italic") (pp. 167-168).

Use a menu item for:

- a command that applies to the current selection or window;
- a setting that applies to the whole or part of a selection (checkmark/dash);
- a frequently used command that also has a keyboard equivalent.

Menus let users **scan available commands without acting**: press-drag-release can be abandoned, and an
activated item blinks briefly (p. 166).

## 2. Variants and sizes

| Variant | When to use | Marker | Source |
| --- | --- | --- | --- |
| Plain command | Immediate action | none | p. 167 |
| Command that needs more input | Opens a dialog/window for the rest of the task | ellipsis "…" | pp. 131-132, 168 |
| Checked item | Attribute applies to the whole selection, or active document in Window menu | checkmark | pp. 170-172 |
| Mixed item | Attribute applies to part of the selection | dash | pp. 170-171 |
| Dynamic item | Alternate command revealed by one modifier key | name/command changes | pp. 168-169 |
| Submenu parent | Closely related commands, attributes | right-pointing indicator | p. 174 |
| Separator | Group boundary | horizontal rule | pp. 173-174 |
| Toggle pair | Two opposite states shown as two items | checkmark on current | p. 172 |

## 3. Dimensions and geometry

| Property | Value | Source |
| --- | --- | --- |
| Item height | not specified in the HIG | — |
| Menu width | sized to the widest item, including modifier-revealed alternates | p. 168 |
| Indent / marker column | not specified in the HIG | — |
| Separator inset | not specified in the HIG | — |
| Keyboard-equivalent column | right-aligned; symbol order Control, Option, Shift, Command | p. 167; Appendix A |

**Measured 10.6 values:** none. The HIG gives no menu metrics; capture #15 is a full-screen screenshot, not a
measurement source.

## 4. Text, fonts, and labels

- **Actions:** verbs/verb phrases in base form ("Save", "Copy") (p. 168).
- **Attributes:** adjectives/adjective phrases that complete "Change the selected object to …" (p. 168).
- **Capitalization:** title-style (p. 168).
- **Articles:** avoid definite/indefinite articles ("Add Account", not "Add an Account") (p. 168).
- **Ellipsis:** use "…" when the command needs additional information. Follow
  [Text > Using the Ellipsis Character](../03-aqua-interface/text.md#using-the-ellipsis-character-pp-131-132)
  (pp. 131-132); do not add it merely because a window may appear.
- **Icons:** only when they add significant value, never for every item; menu titles are text, not icons
  (pp. 167, 169-170).
- **Titles:** short and representative; avoid grouping unrelated commands under one title (p. 167).
- **Dynamic items:** require only one modifier key; never the only route to a task (p. 169).

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Enabled | command applies | full-strength text | p. 168 |
| Disabled | doesn't apply / nothing selected | dimmed and **not highlighted** on pointer-over | p. 168 |
| Highlighted (open menu) | pointer/keyboard over | highlight band on the item | p. 166 (implied by scanning) |
| Activated | chosen | brief blink, then menu closes | p. 166 |
| Checked | attribute on for whole selection / active document | checkmark | pp. 170-172 |
| Mixed | attribute on for part of selection | dash | pp. 170-171 |
| Unsaved document (Window menu) | document has unsaved changes | bullet | p. 171 |
| Minimized (Window menu) | document minimized | diamond | p. 171 |
| Submenu open | pointer/keyboard on parent | submenu displayed; parent highlighted | p. 174 |
| Open/closed menu | click or press | menu stays open until choose/click-outside/alert/app switch | p. 166 |

Symbol precedence in the Window menu: a checkmark (active window) overrides the bullet (unsaved); a minimized
document with unsaved changes shows the diamond only (p. 171). Do not use arbitrary symbols (p. 170).

## 6. Interaction and keyboard

- **Pointer:** press-drag-release selects and can be abandoned without action; a click opens a sticky menu
  (p. 166).
- **Keyboard:** Down/Up move the highlight; Return activates; Right opens a submenu, Left closes it; Esc closes
  the menu and restores focus (A11Y-21). Menu-bar access is journey **J1**.
- **Shortcut display:** keyboard equivalents appear in the item row (p. 167). The full set of reserved and
  recommended shortcuts is in [Appendix A](../04-reference/appendix-a-keyboard-shortcuts.md); a menu item must
  never claim a reserved combination (A11Y-19/20).
- **Dynamic items:** pressing the documented single modifier swaps the item (p. 168); the menu resizes to the
  widest state.
- **No command-only keyboard paths:** every menu command is also reachable by pointer (A11Y-08).

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | The visible item text, without the ellipsis/marker read as part of the name (A11Y-28). |
| Role | Menu item; submenu parents expose "has submenu" (A11Y-29). |
| State | Enabled/disabled, checked/mixed, submenu expanded. |
| Focus | Menu items receive keyboard highlight; the open menu has a visible highlighted item (A11Y-13 context). |
| Announcements | Disabled reasons are not spoken by the menu itself; ensure the command is discoverable elsewhere if essential. |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #15 (Finder application menu open), #36 (Pages File menu open).
- HIG figures: 13-3 (menu elements), 13-4 (dynamic items), 13-7/13-8 (symbol usage), 13-9 (toggled items),
  13-10 (grouping), 13-13 (all items dimmed).
- Gaps: keyboard-highlighted item, checked item, mixed dash, submenu open, disabled item, scrolling-menu
  indicators.

## 9. HIG source pages

- p. 166 — press-drag-release scanning; activated item blinks; menu dismissal triggers; dimmed items in an
  all-unavailable menu; avoid long menus; scrolling menus.
- p. 167 — scrolling indicators; menu elements; titles; naming.
- p. 168 — actions vs. attributes; disabled appearance; title-style capitalization; articles; ellipsis;
  dynamic items.
- p. 169 — dynamic-item constraints; icons in menus.
- pp. 170-171 — acceptable symbols; checkmark/dash/bullet/diamond; precedence.
- p. 172 — toggled item types; unambiguous opposite verbs.
- pp. 173-174 — grouping, separators, submenu rules.
- pp. 175-176 — menu bar composition (context for which menus exist).

## 10. Recreation-specific decisions / open questions

- **PENDING:** menu item height, indent, and separator inset — none stated; measure from 10.6.
- **PENDING:** whether hover highlighting (vs. keyboard-only highlight) is implemented, and whether disabled
  items ignore pointer hover exactly as stated (p. 168).
- **PENDING:** dynamic-item modifier choice for the recreated app's commands.
- **DECIDED:** reserved shortcut conflicts are forbidden; audit against Appendix A before shipping.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/naming rules | High | Explicit pp. 167-174 |
| Geometry | Low | No metrics in source |
| Visual states | Medium | Symbols described; captures lack most states |
| Keyboard behavior | High | Menu behavior + Appendix A |

## 12. Acceptance tests

1. **Scan without acting:** opening a menu and moving the pointer away without releasing over an item performs
   no command.
2. **Blink:** an activated item blinks once before the menu closes (or an equivalent immediate acknowledgement
   is shown).
3. **Disabled:** an unavailable item is dimmed, is not highlighted on pointer-over, and cannot be activated by
   pointer or keyboard.
4. **Symbols:** checkmark/dash/bullet/diamond appear only for their defined meanings; no arbitrary symbols.
5. **Toggle clarity:** a toggled command uses either two explicit opposite items or an unambiguous name change;
   a checkmark never means feature presence/absence.
6. **Grouping:** actions and attributes are not mixed in one separator group; related commands are adjacent.
7. **Submenus:** at most one level; a submenu with more than five items is promoted to its own menu.
8. **Shortcuts:** every displayed keyboard equivalent matches Appendix A, and no reserved system combination
   is used for another command.
9. **Ellipsis:** "…" appears only when the command opens a dialog/requires input, per the Text rule.
10. **Keyboard menu access:** J1 passes, including Esc restoring focus to the previously focused control.

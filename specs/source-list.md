# Component Spec: Source List (Sidebar)

- **Spec ID:** CMP-05
- **HIG chapter(s):** Windows > Source Lists (pp. 208-212); selection highlights (p. 111)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A source list (sidebar) is a window area, usually set off by a movable splitter, that lets users **navigate or
select objects** (p. 208). Typically the user selects an object there and acts on it in the main part of the
window. It can be the application's primary navigation (Finder, iTunes) or a window-local view selector
(some System Preferences panes) (pp. 208-209).

Include one when (p. 210):

- navigation and selection of content are primary tasks;
- collections of objects are central to the user's mental model;
- the hierarchy is a natural navigation structure;
- hierarchical arrangement removes complexity.

It is not a general-purpose list of commands; it should contain only controls that organize its data (p. 211).

## 2. Variants and sizes

| Variant | When to use | Background | Source |
| --- | --- | --- | --- |
| Primary navigation source list | One per application window; navigation for the whole app | blue | p. 209 |
| Window-local source list | Panels/preferences; selects a view within a window | white | pp. 209, 211 |
| Hierarchical source list | Objects have up to two levels; disclosure triangles | either per above | p. 211 |

Rules:

- A primary (blue) source list should be the **only** source list in the application window and always visible
  unless the user hides it (p. 209).
- Use white when the window has more than one source list, or when the source list is in a panel/preferences
  window (p. 211).
- Do not exceed **two levels** of hierarchy in one source list. For deeper nesting, use a second source list or
  a browser view (p. 211).

## 3. Dimensions and geometry

| Property | Value | Source |
| --- | --- | --- |
| Width | not specified; user-resizable via a movable splitter | p. 208 |
| Row height | not specified in the HIG | — |
| Indent per level | not specified in the HIG | — |
| Icon size | not specified in this section (see Icons for app icons) | — |
| Bottom-edge action area | gradient buttons at the bottom edge, or bottom-bar controls below the list | p. 211 |

**Measured 10.6 values:** none. Widths/row heights in #14, #20, #27 are screenshot-specific, not a
specification.

## 4. Text, fonts, and labels

- No column headers; source lists "don't generally have headers like lists can" (p. 210).
- Section titles may separate subsets ("Devices", "Shared", "Places") (p. 210).
- Item labels name the object/container the user selects; the HIG gives no separate capitalization rule here —
  the view/list label rules apply (see [Text](../03-aqua-interface/text.md)).

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Selected (active window) | user selection | dark highlight across the full row | p. 111 |
| Selected, parent in column view | parent of selection | lighter highlight | p. 111 |
| Inactive window | window not key | all selections use the lighter highlight | p. 111 |
| Focused | keyboard focus | focus ring on the list (A11Y-13) | p. 110 |
| Expanded / collapsed | disclosure triangle | triangle rotates; children show/hide | p. 211 |
| Disabled row | not applicable | not specified in the HIG | — |
| Hover | pointer over | not specified in the HIG | — |
| Drag-over | drag target | not specified in this section (see Drag and Drop) | — |

## 6. Interaction and keyboard

- **Pointer:** click selects; disclosure triangles expand/collapse up to two levels (p. 211). Splitter drag
  resizes the source list (p. 208).
- **Keyboard:** Tab enters the list; Up/Down change selection; Right/Left open/close disclosure triangles
  (A11Y-14, A11Y-15); type-ahead selects by name (A11Y-18).
- **Selection:** selecting an object is navigation, not an edit (p. 208). Selection never modifies the object
  (p. 112).
- **Customization:** users should be able to customize source-list contents (p. 211).
- **Add/remove:** place controls in a bottom bar directly below the list, or use gradient buttons at the
  list's bottom edge when there is no bottom bar (p. 211). Do not use a `+`/`-` segmented control in the
  window body (p. 286).

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | Each row's label is its name; section titles are group labels (A11Y-28). |
| Role | List/tree ("source list"); disclosure items expose expanded/collapsed (A11Y-29). |
| State | Selected, expanded/collapsed, inactive selection level. |
| Focus | Focusable; visible ring (A11Y-13); focus does not rely on selection alone. |
| Announcements | Selection changes and expand/collapse changes (A11Y-29). |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #14 (Finder sidebar, blue, with section titles), #20 (Mail mailbox list), #27 (System
  Preferences, white source list), #33 (Xcode project navigator).
- HIG figures: 14-22 (primary blue source lists), 14-23 (white window-local list), 14-24 (disclosure
  triangles).
- Gaps: inactive-window highlight, focus ring, collapsed/expanded pair, drag feedback, row metrics.

## 9. HIG source pages

- p. 208 — definition; splitter; primary vs. view selection.
- p. 209 — blue vs. white backgrounds; one blue list per window; always visible.
- p. 210 — section titles; file-system abstraction rationale; when to include a source list.
- p. 211 — only data-organizing controls; max two levels; customization; add/remove via bottom bar or
  gradient buttons.
- p. 212 — bottom bars and their control restrictions.
- p. 111 — selection highlight levels.

## 10. Recreation-specific decisions / open questions

- **PENDING:** which style (blue primary or white local) the recreated app needs, and whether both occur.
- **PENDING:** row height, indent, icon size, and divider geometry — none stated; measure from 10.6.
- **PENDING:** whether users can reorder rows by dragging (HIG discusses customization, not reordering
  mechanics).
- **DECIDED:** the two-level limit is treated as a hard rule for a single source list.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit pp. 208-212 |
| Geometry | Low | Almost no numbers in the source |
| Visual states | Medium | Blue/white and highlights described; captures partial |
| Keyboard behavior | Medium | List conventions from pp. 110-111 |

## 12. Acceptance tests

1. **Style selection:** a primary navigation list is the only source list in the window and uses the blue
   background; any window-local or multi-list case uses white (p. 211).
2. **Hierarchy cap:** no source list renders more than two levels; deeper data uses a second list or browser.
3. **Selection:** selecting a row changes only the selection; it does not open, rename, or mutate the object.
4. **Highlights:** the selected row highlights to the full row; when the window is inactive the highlight is
   lighter (p. 111).
5. **Expand/collapse:** disclosure triangles toggle children, and Right/Left arrows do the same from the
   keyboard (A11Y-15).
6. **No headers:** no column headers are drawn; optional section titles separate groups.
7. **Add/remove placement:** add/remove controls are in a bottom bar or gradient buttons at the list's bottom
   edge, never a `+`/`-` segmented control in the body.
8. **Customization:** the user can show/hide source-list containers (p. 211).

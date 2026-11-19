# Accessibility and Keyboard-Navigation Checklist

- **Status:** Source-verified checklist (HIG pp. 49-51, 99-111, 240-242)
- **Applies to:** every component spec in [`../specs/`](../specs/README.md), plus menus, windows, dialogs, and
  sheets
- **Scope:** rules are labelled **HISTORICAL** (what the 2009 HIG required of Mac OS X apps), **OBSERVED**
  (visible in a retained capture), or **RECREATION** (a decision/open question for this project). See
  [Scope and evidence labels](scope-and-evidence.md).

Component specs should cite the requirement IDs below (`A11Y-##`) instead of restating the rule.

## How to read the labels

| Label | Meaning |
| --- | --- |
| **HISTORICAL** | A 2009 HIG requirement/recommendation to applications targeting Mac OS X. Page reference given. |
| **OBSERVED** | Directly visible in a retained 10.6 capture; image number given. |
| **RECREATION** | This project's obligation or open decision for its own target platform. Not inherited from the HIG. |

The HIG's accessibility architecture (Accessibility Overview, VoiceOver) is **Mac OS X-specific API advice**
(pp. 49-50). This checklist therefore translates it into observable UI obligations (names, roles, states,
focus, non-color cues) that any toolkit can satisfy; it does **not** promise that the recreation will expose
macOS accessibility APIs.

## Requirement checklist

### Universal access and assistive-technology coexistence

| ID | Requirement | Source | Applies to | Verification |
| --- | --- | --- | --- | --- |
| A11Y-01 | **HISTORICAL:** Do not override OS accessibility features or user accessibility preferences (keyboard-only operation, Sticky Keys, zoom, etc.). | pp. 49, 51 | Whole UI | No feature is mouse-only; no custom shortcut swallows a system/assistive shortcut. |
| A11Y-02 | **HISTORICAL:** Do not override keyboard shortcuts used by assistive technologies; when an assistive technology is active, its shortcuts take precedence. | p. 51 | Global key handling | Shortcut dispatcher checks assistive reservations first (or documents why it cannot). |
| A11Y-03 | **HISTORICAL:** Test with the assistive features available in Universal Access. | p. 49 | Whole UI | Keyboard-only journey suite (below) passes. |
| A11Y-04 | **HISTORICAL:** Software should handle different text sizes and respect zoom/high contrast. | p. 50 | Text, layout | Labels do not clip at enlarged text; layout uses spacing/alignment, not fixed text boxes. |
| A11Y-05 | **HISTORICAL:** Do not convey important information by color alone; color coding must be redundant with text, position, or highlighting. | p. 50 | Indicators, alerts, selection, status | Grayscale/color-blind check: the state is still identifiable. |
| A11Y-06 | **HISTORICAL:** Never rely solely on sound; provide a visual cue for any auditory cue, and use the standard system alert for attention. | p. 50 | Alerts, errors, completion feedback | Mute test: every sound-triggering event has a visible counterpart. |
| A11Y-07 | **HISTORICAL:** Don't make accommodations for one disability a burden for other users. | p. 49 | Whole UI | No default mode forces slow animation or extra steps on everyone. |

### Keyboard access, focus, and navigation

| ID | Requirement | Source | Applies to | Verification |
| --- | --- | --- | --- | --- |
| A11Y-08 | **HISTORICAL:** The keyboard is always an alternative to the mouse, never the only way; don't depend on a key existing on every keyboard. | pp. 99-100, 103 | Whole UI | Every action reachable by pointer has a keyboard route; no essential function requires a key that may be absent. |
| A11Y-09 | **HISTORICAL:** Arrow-key shortcuts are shortcuts for mouse actions; never implement a keyboard-only action. | p. 103 | Lists, graphics, text | Pointer equivalent exists for each arrow-key behavior. |
| A11Y-10 | **HISTORICAL:** In default keyboard access mode, focus moves only between fields that receive keyboard input. | p. 110 | Text fields, lists, column views | Tab order skips static text and non-input decoration. |
| A11Y-11 | **HISTORICAL:** Full keyboard access mode lets users reach and operate all window/dialog items (buttons, checkboxes, tabs, etc.). | pp. 51, 108, 110 | Whole UI | A mode toggle (or equivalent) exposes all controls to Tab/Space; see A11Y-26 for the recreation decision. |
| A11Y-12 | **HISTORICAL:** Focus begins at the first field that accepts input and follows a reading path from upper left to bottom right (Roman systems). | p. 110 | Dialogs, windows | Initial focus lands on the first input control, not the title bar or a static label. |
| A11Y-13 | **HISTORICAL:** Focus is indicated with a ring in the appearance color (Aqua or Graphite). | pp. 110-111 | All focusable controls | Every focused control has a visible ring; focus is not indicated by text cursor alone. |
| A11Y-14 | **HISTORICAL:** Tab moves to the next control, Shift-Tab to the previous; arrows navigate within a control. | p. 111 | Whole UI | Tab/Shift-Tab cycle is reversible and does not trap; arrows change the value/selection inside a control. |
| A11Y-15 | **HISTORICAL:** In list views, Left/Right Arrow open and close disclosure triangles. | p. 111 | List views, outline views | Right expands, Left collapses; both are reversible. |
| A11Y-16 | **HISTORICAL:** Selected list/column items highlight to the full column width or row height; in column view the selected item is dark and its parent lighter; an inactive window uses the lighter highlight. | p. 111 | List, column, source list | Active/parent/inactive selection levels are visually distinct and survive grayscale. |
| A11Y-17 | **HISTORICAL:** Space activates the item with keyboard-navigation focus (equivalent to a click). | p. 100 | Buttons, checkboxes, list rows | Space toggles/activates the focused control without moving focus. |
| A11Y-18 | **HISTORICAL:** Type-ahead queues keystrokes; key-repeat is a user setting and key-repeat keystrokes should be ignored for Command-key shortcuts. | p. 111 | Text, lists, menus | Holding a shortcut key does not fire a Command action repeatedly. |

### Standard and reserved keys

| ID | Requirement | Source | Applies to | Verification |
| --- | --- | --- | --- | --- |
| A11Y-19 | **HISTORICAL:** Never assign reserved system combinations to other commands, even if the app lacks the system feature. | pp. 100, 106-108 | Global | A shortcut audit against Table 8-3 fails on any conflict. |
| A11Y-20 | **HISTORICAL:** Don't override well-established shortcuts (e.g. Command-Q = Quit) with unrelated commands. | pp. 106-107 | Menus | Menu shortcut audit against Appendix A passes. |
| A11Y-21 | **HISTORICAL:** Esc cancels the current action: dismisses a dialog like Cancel, stops an operation, cancels renaming, cancels a drag. | p. 101 | Dialogs, progress, inline rename, drag | Esc performs the documented cancel for each context. |
| A11Y-22 | **HISTORICAL:** Esc must not discard extensive work without confirmation; confirm during a lengthy operation. | p. 101 | Long operations | Esc during a long task shows a confirmation, not silent loss. |
| A11Y-23 | **HISTORICAL:** Return/Enter activates the default button; if there is no default button, they do nothing. | pp. 100-101, 241 | Dialogs, sheets | Return activates the default; with no default, nothing happens. |
| A11Y-24 | **HISTORICAL:** Command-period and Esc both map to Cancel in dialogs. | p. 242 | Dialogs, sheets | Both keys cancel; Cancel restores the pre-dialog state. |
| A11Y-25 | **HISTORICAL:** Don't use a default button for a dangerous action; a safe default (e.g. Cancel) is acceptable. | p. 241 | Destructive dialogs | Destructive alerts have no destructive default; Return does not delete. |
| A11Y-26 | **RECREATION:** Decide whether a "full keyboard access" toggle exists, its default, and how it is discovered. The HIG mode is an OS-level System Preferences setting (pp. 51, 108); the recreation may be a settings switch, always-on, or out of scope. | pp. 51, 108, 110 | Whole UI | Decision recorded in `specs/README.md` and tested. |
| A11Y-27 | **RECREATION:** Decide the focus-ring appearance for a custom-drawn UI. The HIG specifies the color role (appearance color) but no pixel geometry; measure from 10.6 captures before drawing. | pp. 110-111 | Custom controls | Ring visible on every background; contrast checked against window and content backgrounds. |

### Names, roles, states, and announcements

| ID | Requirement | Source | Applies to | Verification |
| --- | --- | --- | --- | --- |
| A11Y-28 | **HISTORICAL:** Every control has a meaningful name; labels describe both opposite states when a control is a toggle. | pp. 49-50; controls pp. 283-286 | Checkboxes, buttons, fields | No unlabeled control; a screen-reader-style name can be produced for each. |
| A11Y-29 | **HISTORICAL:** Expose state (on/off/mixed, selected, expanded, disabled) and role (button, checkbox, radio, list, tab) — the information VoiceOver reads. | pp. 49-50 | All controls | State/role table in each component spec is complete. |
| A11Y-30 | **HISTORICAL:** Dialog static text that conveys an error, serial number, or address should be selectable when it benefits the user. | p. 240 | Alerts, dialogs | Error text can be selected and copied. |
| A11Y-31 | **HISTORICAL:** Show a selection or insertion point in the first control that accepts input when a dialog opens. | p. 240 | Dialogs, sheets | Opening a dialog places a visible insertion point/selection. |

### Readability and feedback

| ID | Requirement | Source | Applies to | Verification |
| --- | --- | --- | --- | --- |
| A11Y-32 | **HISTORICAL:** Use readable fonts; don't sacrifice readability for appearance. | p. 73 (widgets), p. 50 | Text, labels | Minimum legible size; no condensed/decorative text for body labels. |
| A11Y-33 | **HISTORICAL:** Input errors should be prevented where possible and surfaced with text, not only color or sound. | pp. 50, 240-241 | Forms, dialogs | Each invalid state has a text message adjacent to the field. |
| A11Y-34 | **HISTORICAL:** Validate after leaving a field or on explicit action, not on every keystroke in most cases. | p. 241 | Forms | Typing a partial value does not flash errors. |
| A11Y-35 | **HISTORICAL:** Progress/status must be communicated visually; an indeterminate action dims its button and provides feedback. | pp. 50, 265 | Progress, long actions | Visible status text/progress accompanies every long action. |

## Observed 10.6 evidence and gaps

- Keyboard focus rings: **not captured**. No retained image shows a focus ring (image inventory capture
  matrix, "Focus ring / keyboard focus" row).
- Inactive selection: **not captured**; the HIG describes the lighter highlight (p. 111) but no before/after
  pair exists.
- Mixed checkbox state, disabled controls: **not captured** (only an on-state checkbox in #34).
- Menu keyboard highlighting and disabled items: **not captured** (the open application menu in #15 shows
  enabled items only).
- Alert with icon/suppression: #8, #11, #17 provide message/button examples; none shows expanded details.

These gaps mean the pixel appearance of focus and disabled states must be measured before custom drawing
(A11Y-27); behavior can be specified now from the text.

## Keyboard-only journeys

Each journey starts with the pointer untouched and ends with a testable outcome. "Focus visible" means a
visible focus ring on the named control (A11Y-13).

### J1 — Menu bar command

1. Press Control-F2 (or the recreation's menu-focus key) to focus the menu bar. Focus visible on the
   application menu title.
2. Right Arrow moves across menu titles; Down Arrow opens the focused menu. Focus visible on the first item.
3. Down Arrow moves through enabled items, skipping disabled items but leaving them visible.
4. Return activates the focused command; Esc closes the menu and returns focus to the previously focused
   control.

**Pass:** every step shows visible focus; Esc restores the prior focus; disabled items are never activatable;
no command fires twice when a key is held (A11Y-18).

### J2 — Preferences pane

1. Open Preferences from the application menu. Focus lands on the first input control (A11Y-12).
2. Tab reaches the pane selector (tabs/toolbar) and each setting in reading order; Shift-Tab reverses it.
3. Arrow keys change the selected pane/tab without moving focus out of the selector (A11Y-14).
4. Space toggles the focused checkbox; the dependent control enables/disables immediately and is announced as
   enabled/disabled.
5. Esc or the Cancel/close path leaves preferences without applying uncommitted edits.

**Pass:** no focus trap; tab order matches visual order; toggled dependent control state changes are visible
without color alone; Esc never commits changes.

### J3 — Source list / list view

1. Tab into the list. Focus ring surrounds the list; the current row is selected (A11Y-13, A11Y-16).
2. Up/Down Arrow changes the selected row; the previous row's selection clears.
3. Right Arrow expands a disclosure triangle; Left Arrow collapses it (A11Y-15).
4. Typing letters jumps to the next matching item (type-ahead, A11Y-18).
5. Tab leaves the list to the next control; Shift-Tab returns to the same row.

**Pass:** selection is visible at full row width; parent/child highlight levels differ in column view; focus
returns to the same row; type-ahead does not fire commands.

### J4 — Sheet

1. Trigger an action that presents a sheet (e.g. Save). Focus moves into the sheet and lands on the first
   input control (A11Y-12).
2. Tab cycles only within the sheet while it is modal; the parent window's controls are unreachable.
3. Return activates the default button; Esc and Command-period both cancel (A11Y-23, A11Y-24).
4. On cancel, focus returns to the control that opened the sheet and no changes are applied.

**Pass:** focus cannot escape the sheet; both cancel keys work; focus restoration is observable; no partial
save remains after cancel.

### J5 — Dialog with a destructive action

1. Open a dialog whose third button discards data (e.g. "Don't Save").
2. Confirm there is no destructive default button (A11Y-25); Return activates the safe default.
3. Tab to the destructive button; it has a visible focus ring and is separated from the safe buttons (p. 241,
   ≥24 px).
4. Esc cancels and restores the prior state; the destructive path requires an explicit activation.

**Pass:** Return never destroys data; destructive button is reachable but not default; Esc restores.

## Mapping to component specs

| Component spec | Requirement IDs to cite |
| --- | --- |
| [Push button](../specs/push-button.md) | A11Y-08, 13, 17, 23, 24, 28, 29 |
| [Toolbar item](../specs/toolbar-item.md) | A11Y-08, 13, 17, 28, 29 |
| [Checkbox](../specs/checkbox.md) | A11Y-05, 11, 13, 17, 28, 29 |
| [Text input field](../specs/text-input-field.md) | A11Y-04, 10, 12, 13, 14, 28, 30, 31, 33, 34 |
| [Source list](../specs/source-list.md) | A11Y-05, 13, 14, 15, 16, 18, 29 |
| [Sheet](../specs/sheet.md) | A11Y-12, 13, 21, 22, 23, 24, 31 |
| [Menu item](../specs/menu-item.md) | A11Y-18, 19, 20, 21, 29 |

## Host-platform implementation notes (recreation)

- **PENDING:** map A11Y-28/29/30 to the target toolkit's name/role/state model (for example ARIA roles or a
  native accessibility tree). The recreation does not claim to implement macOS accessibility APIs.
- **PENDING:** decide whether assistive-technology shortcut precedence (A11Y-02) is enforceable on the host;
  if not, document the limitation rather than silently ignoring it.
- **DECIDED:** behavior requirements (focus order, Tab/Shift-Tab, Esc/Cancel, Return/default) are
  toolkit-independent and are carried into every component spec.

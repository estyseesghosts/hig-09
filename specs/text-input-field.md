# Component Spec: Text Input Field

- **Spec ID:** CMP-04
- **HIG chapter(s):** Controls > Text Controls > Text Input Fields (pp. 322-325); keyboard focus (p. 110)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A text input field (editable text field) is a rectangular area where the user **enters or modifies text**
(p. 322). It can be active or disabled, supports keyboard focus, and supports password entry (p. 322).

Use it to gather a single line of user input. Do not:

- pair a text field with a menu to create a combo box by hand — use a combination box control (p. 323);
- use it for read-only information (use a static text field, p. 321);
- use it for multi-line editing (the HIG's text views are not described in this section).

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| Standard text field | Single-line text entry | regular, small, mini | pp. 322, 324 |
| Password field | Secret input; characters masked | regular/small/mini | p. 322 |
| Labeled field | Any form field with an introductory label | regular/small/mini | p. 323 |

There is no icon/button variant in this section.

## 3. Dimensions and geometry

| Property | Regular | Small | Mini | Source |
| --- | --- | --- | --- | --- |
| Height | **22 px** | **19 px** | **15 px** | p. 324 |
| Width | long enough for average expected input; equal lengths for fields in the same window | same | same | p. 324 |
| Intro label → field left edge | 8 px | 6 px | 5 px | p. 324 |
| Vertical gap between stacked fields | ≥10 px | ≥8 px | ≥8 px | p. 324 |
| Label font | system font | small system font | mini system font | p. 324 |

The height is fixed per size; do not vertically resize (p. 324; general rule p. 255).

**Measured 10.6 values:** heights are stated by the HIG; border radius, inner padding, and focus-ring
geometry are **not measured**.

## 4. Text, fonts, and labels

- Field text uses the system font appropriate to the control size (p. 323).
- An introductory label is recommended to explain what information goes in the field (p. 323).
- Introductory labels use **title-style capitalization** (p. 323).
- Label spacing is consistent across a window (p. 324).
- Password entry is supported (p. 322); masking character/behavior is not specified in this section.

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Normal with text | value present, no focus | bordered field, text visible | p. 324, Figure 15-71 |
| Focused | keyboard focus | insertion point/caret + focus ring | p. 324, Figure 15-71; A11Y-13 |
| Selection | text selected | highlight in appearance color | p. 324, Figure 15-71 |
| Empty | no value | empty bordered field | p. 322 |
| Disabled | field not editable | dimmed/inactive appearance | p. 322 |
| Invalid | failed edit check | error feedback with text (not color alone) | pp. 323, 240-241; A11Y-33 |
| Pressed | n/a | not a pressable control | — |
| Hover | pointer over | not specified in the HIG | — |

## 6. Interaction and keyboard

- **Text entry:** typing inserts at the insertion point; standard editing keys apply (pp. 100-106).
- **Focus:** Tab moves to the next field, Shift-Tab to the previous; initial focus in a dialog belongs in the
  first input field (A11Y-12, A11Y-14).
- **Edit checks:** in most cases validate when the user **clicks outside the field or presses Return, Enter, or
  Tab** (p. 323). This matches the dialog guidance to avoid per-keystroke validation (p. 241).
- **Return/Enter:** commits the field's value; when the field is in a dialog, Return may also activate the
  default button. The HIG warns against using both behaviors for Return (p. 242) — see the open question.
- **Tab may commit:** pressing Tab can cause data to be entered before focus moves (p. 100).
- **Invalid input:** issue an alert or inline error when the value is unacceptable (e.g. non-digits in a
  numeric field) (p. 323).

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | Introductory label is the accessible name; if visually implicit, provide an equivalent (A11Y-28). |
| Role | Text field (A11Y-29). |
| State | Value, read-only/disabled, invalid, required (if used), password/masked. |
| Focus | Focusable; visible focus ring and caret (A11Y-13). |
| Announcements | Validation errors are announced/exposed as text, not by color alone (A11Y-33). |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #7 and #13 (Connect to Server / Go to Folder dialogs with labeled fields), #33 (Xcode
  3.2), #36 (Pages with MathType fields).
- HIG figures: 15-70 (labeled field, p. 323), 15-71 (normal / focus / selection, p. 324).
- Gaps: disabled field, focus ring, password field, error state, small/mini sizes.

## 9. HIG source pages

- p. 322 — definition; active/disabled; keyboard focus; password entry.
- p. 323 — use a combo box instead of field+menu; edit checks; label recommendation; title-style labels;
  system font.
- p. 324 — fixed heights 22/19/15; width guidance; label gaps 8/6/5; stacking 10/8/8; Figure 15-71 states.
- p. 325 — historical AppKit implementation (`NSTextField`).

## 10. Recreation-specific decisions / open questions

- **PENDING:** Return behavior. The field commits on Return, and a dialog's default button also activates on
  Return; the HIG says do not use a default button when Return is used in text entry (p. 242). The recreation
  must choose and test one model.
- **PENDING:** focus-ring and disabled-border artwork for custom drawing.
- **PENDING:** password masking character and whether reveal controls exist (not specified).
- **DECIDED:** `NSTextField` is historical detail, not a requirement.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit pp. 322-325 |
| Geometry | High | Heights and gaps stated |
| Visual states | Medium | Normal/focus/selection shown in HIG figure; disabled/error uncaptured |
| Keyboard behavior | High | HIG pp. 100-101, 110, 323 |

## 12. Acceptance tests

1. **Heights:** regular/small/mini fields render at 22/19/15 px and are never vertically stretched.
2. **Labels:** each field has a title-style introductory label with an 8/6/5 px gap; stacked fields are
   ≥10/8/8 px apart.
3. **Focus:** clicking or tabbing into a field shows a caret and focus ring; Tab/Shift-Tab move predictably.
4. **Validation timing:** no error appears while a valid partial value is being typed; validation occurs on
   blur or Return/Tab (p. 323).
5. **Invalid input:** an invalid value produces visible text feedback adjacent to the field, not only color
   or sound (A11Y-33).
6. **Disabled:** a disabled field cannot receive focus or text.
7. **Password:** typed characters are masked and the value is not exposed as plain text in the UI.
8. **Accessibility:** the field exposes its name, value, disabled/read-only state, and error state.

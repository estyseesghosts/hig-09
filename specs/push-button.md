# Component Spec: Push Button

- **Spec ID:** CMP-01
- **HIG chapter(s):** Controls > Buttons > Push Buttons (pp. 265-269); dialogs (p. 241)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A push button performs an **instantaneous action** — saving a document, completing a dialog operation, or
acknowledging an error (p. 265). It is a command, not a state display, not a label, and not a menu trigger.

Use it for:

- committing or dismissing a dialog (OK, Cancel, Save, Don't Save);
- an immediate command on the current selection (Print, Delete, Change Password);
- acknowledging an alert.

Never use it for:

- showing on/off state (use a checkbox, p. 267);
- labeling another element (use static text, p. 267);
- opening a menu (use a bevel button, p. 267);
- an indeterminate operation without dimming and status feedback (p. 265).

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| Standard push button | Any instantaneous command in the window body | regular, small, mini | pp. 265, 268 |
| Default button | The safe, most likely action in a dialog; Return/Enter activates it | regular (typical) | pp. 241, 268 |
| Destructive button (e.g. Delete, Don't Save) | An action that can lose data; never the default | regular (typical) | pp. 241, 269 |

There is no icon/image variant: a button that needs an image is a bevel button (p. 267). Push buttons are for
the **window body**, not window-frame areas (p. 265).

## 3. Dimensions and geometry

| Property | Regular | Small | Mini | Source |
| --- | --- | --- | --- | --- |
| Height | not specified in the HIG | not specified | not specified | p. 268 says "fixed for each size" but gives no number |
| Width | determined by label length; enough that end caps never clip the text | same rule | same rule | p. 268 |
| Horizontal/vertical spacing between buttons | ≥12 px | ≥10 px | ≥8 px | p. 269 |
| Destructive-to-safe distance | ≥24 px | ≥24 px | ≥24 px | p. 241 |
| Label font | system font | small system font | mini system font | p. 269 |

**Measured 10.6 values:** not measured — the HIG gives no button height and the retained captures are not a
controlled measurement set. This is a capture gap (see [image inventory](../notes/image-inventory.md), push
button row).

## 4. Text, fonts, and labels

- **Content:** text only, never an image (p. 267).
- **Grammar:** a verb or verb phrase describing the action — "Save", "Close", "Print", "Delete",
  "Change Password" (p. 267).
- **Specificity:** if the button acts on a single setting, name it specifically — "Choose Picture…" is better
  than "Choose…" (p. 267).
- **No "now":** the action is already immediate, so labels such as "Scan Now" are unnecessary (p. 267).
- **Capitalization:** title-style (p. 267; see [Text](../03-aqua-interface/text.md)).
- **Ellipsis:** follow the shared rule in
  [Text > Using the Ellipsis Character](../03-aqua-interface/text.md#using-the-ellipsis-character-pp-131-132)
  (pp. 131-132): use "…" when the action requires additional input or opens a window/dialog where the user
  completes the task. The HIG's button wording (p. 267) is broader ("if the button immediately opens another
  window, dialog, or application"); the Text chapter's narrower rule is the project's reconciliation, and the
  discrepancy is recorded in [Controls](../03-aqua-interface/controls.md#source-notes-with-page-refs).
- **No effects:** no shadow or other text effects (p. 268).

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Enabled | action available | clear (uncolored) bezel except the default button | p. 268 |
| Disabled | action unavailable | dimmed; the HIG says use system rendering and gives no metric | pp. 256, 265 |
| Default | safe action in a dialog | color and pulsing; Return/Enter activates | p. 241 |
| Non-default pressed | user presses Enter/Return on Cancel etc. | the pressed button acquires color; the default loses color | p. 268 |
| Pressed | pointer/key down | highlighted to acknowledge the click; no artwork specified | p. 51 |
| Focused | keyboard focus | focus ring (A11Y-13) | p. 110 |
| Hover | pointer over | **not specified in the HIG**; no retained capture | — |

Behavioral consequences:

- Pressing a non-default button transfers the "default" color to it (p. 268). This is standard system behavior
  on Mac OS X; the recreation must define whether it reproduces the transient color transfer.
- A destructive button must not be the default (p. 241).
- An indeterminate action dims the button and shows progress (p. 265); do not leave an apparently enabled
  button that does nothing.

## 6. Interaction and keyboard

- **Pointer:** click initiates the action immediately. Press-and-hold shows a pressed state; releasing inside
  activates, releasing outside cancels (standard Mac OS X button tracking; HIG p. 51 describes the highlight).
- **Keyboard:** Space activates the focused button (A11Y-17); Tab/Shift-Tab move focus (A11Y-14); Return/Enter
  activate the default button (A11Y-23); Esc and Command-period cancel a dialog (A11Y-24).
- **Dialog order:** action button furthest right, Cancel to its left, third button to Cancel's left (p. 241).
- **Timing:** the action must occur on activation, not on a delayed commit. The HIG gives no double-click
  semantics for buttons.

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | The visible label is the accessible name; do not add a different hidden name (A11Y-28). |
| Role | Button (A11Y-29). |
| State | Enabled/disabled; default (if the host exposes it); pressed while held. |
| Focus | Focusable; visible ring (A11Y-13). |
| Announcements | State changes (enabled ↔ disabled) are exposed, not only drawn. |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #8 (Copy alert: Stop/Replace), #11 (Eject warning), #17 (Force Quit: Force Quit/Cancel).
  These show regular-size, text-only buttons in alerts; #8 shows the destructive/safe arrangement.
- HIG figures: 15-7 (button usages, p. 266), 15-8 (ellipsis label, p. 268), 15-9 (OK/Cancel, p. 268),
  14-52 (dialog button positions, p. 241).
- Gaps: focused/pressed/disabled states; small and mini sizes; exact height; default-button pulse (motion).

## 9. HIG source pages

- p. 265 — buttons initiate immediate action; indeterminate → dim + status; prefer separate buttons for
  opposing functions; window-body only.
- p. 267 — usage prohibitions; text-only; label grammar; ellipsis; title-style capitalization.
- p. 268 — clear appearance except default; default/Return semantics; sizes; width/clipping; fonts.
- p. 269 — spacing 12/10/8; destructive distance; historical AppKit classes.
- p. 241 — default button must be safe; destructive button ≥24 px from safe buttons; Return/Enter semantics.

## 10. Recreation-specific decisions / open questions

- **DECIDED:** specs describe behavior without assuming AppKit; `NSButton`/`NSMomentaryPushInButton` is
  recorded in [Controls](../03-aqua-interface/controls.md) as historical 10.6 detail only.
- **PENDING:** default-button color-transfer fidelity (does pressing Cancel recolor it in the recreation?).
- **PENDING:** button height and corner geometry — must be measured from 10.6 before custom drawing.
- **PENDING:** hover artwork is not specified; decide whether to add one or match 10.6 exactly.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit HIG section, pp. 265-269 |
| Geometry | Low | Heights unstated; only spacing is numeric |
| Visual states | Low-Medium | Alerts captured; focus/pressed/disabled absent |
| Keyboard behavior | High | Default/Return/Esc rules explicit (pp. 241-242, 100-101) |

## 12. Acceptance tests

1. **Immediate action:** activating a push button fires its command once, on activation; holding the key does
   not repeat it (A11Y-18).
2. **No state display:** a push button never retains a checked/on appearance after activation.
3. **Label contract:** every button label is a verb/verb phrase with title-style capitalization; "…" appears
   only per the Text ellipsis rule.
4. **Default semantics:** Return/Enter activates the default button; with no default, nothing happens
   (A11Y-23).
5. **Destructive safety:** no destructive action is the default; it is ≥24 px from safe buttons and requires
   explicit activation.
6. **Spacing:** regular/small/mini button gaps are ≥12/10/8 px in the rendered layout.
7. **Disabled:** a disabled button cannot be activated by pointer, Space, or Return, and is visually dimmed.
8. **Keyboard:** Tab reaches the button, Space activates it, and a visible focus ring is present (A11Y-13/17).

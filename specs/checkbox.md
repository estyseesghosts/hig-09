# Component Spec: Checkbox

- **Spec ID:** CMP-03
- **HIG chapter(s):** Controls > Selection Controls > Checkboxes (pp. 283-286)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A checkbox describes a state, action, or value that is **either on or off** (p. 283). In a group, each
checkbox is independent unless dependency is shown by indentation. A checkbox may also enable or disable
another control (p. 283).

Use it for:

- a two-state option ("Play user interface sound effects");
- several independent options in one group;
- a hierarchical on/off choice where a subordinate checkbox only matters when its controller is on (p. 284);
- the mixed value of a multi-object selection (p. 284).

Never use it for:

- mutually exclusive choices (use radio buttons, p. 283);
- an immediate command that is not a state change (use a push button).

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| Standalone checkbox | Single on/off setting | regular, small, mini | p. 285 |
| Checkbox group | Independent related settings, all at one level | regular/small/mini | p. 285 |
| Indented dependent checkbox | Child option enabled by a parent checkbox | regular/small/mini | p. 284 |
| Mixed-state checkbox | Selection spans objects with differing values | regular/small/mini | p. 284 |

## 3. Dimensions and geometry

| Property | Regular | Small | Mini | Source |
| --- | --- | --- | --- | --- |
| Checkbox box size | fixed per size; no number given | fixed | fixed | p. 285 |
| Intro-label gap (colon → control) | 8 px | 6 px | 5 px | p. 285 |
| Intro label above group → first checkbox | 8 px | 8 px | 8 px | p. 285 |
| Vertical gap between stacked checkboxes | 8 px | 8 px | 7 px | p. 285 |
| Label font | system font | small system font | mini system font | p. 285 |
| Indent step | not specified in the HIG | | | p. 284 shows indentation, no number |

Baseline rule: the introductory label's baseline aligns with the closest checkbox label's baseline
(p. 285, Figure 15-25).

**Measured 10.6 values:** box size and indent step not measured; no retained capture isolates them.

## 4. Text, fonts, and labels

- **Label implies both states.** The label must make on and off unambiguous. If no such label exists, use a
  pair of radio buttons so each state has its own label (p. 284).
- **Capitalization:** sentence-style, unless the state/value is the title of another interface element
  (p. 284).
- **No text inside the box:** the HIG states that selected/unselected appearance is automatic (as with radio
  buttons); the label is external.
- **Groups:** independent checkboxes all appear at the same level; dependent checkboxes are indented under
  their controller (pp. 284-285).
- **Mixed state:** a dash means "the selection contains more than one value," not "unknown" (p. 284).

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Off | value false | empty box | p. 283 (automatic appearance) |
| On | value true | checked box | p. 283 |
| Mixed | multi-object selection with differing values | dash | p. 284; matches menu mixed state p. 170 |
| Enabled | interactive | normal label/box | p. 285 |
| Disabled | not applicable/available | dimmed; a dependent checkbox is unavailable until its controller is on | p. 284 |
| Focused | keyboard focus | focus ring (A11Y-13) | p. 110 |
| Pressed | pointer/key down | not specified in the HIG | — |
| Hover | pointer over | not specified in the HIG | — |

The HIG gives no disabled artwork metric; the requirement is that a disabled state is visually distinct and
that a dependent control changes availability immediately with its controller (p. 284).

## 6. Interaction and keyboard

- **Pointer:** clicking toggles the value. Whether the label is part of the hit target is not stated in the
  HIG; 10.6 Aqua convention is that it is. Treat as a **recreation decision** (below), not a source claim.
- **Keyboard:** Tab reaches the checkbox; Space toggles it (A11Y-17); focus is visible (A11Y-13).
- **Dependent controls:** enabling the controller makes dependents available; disabling it dims them (p. 284).
- **No immediate command:** a checkbox changes state; it must not perform a one-shot command.

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | The external label is the accessible name (A11Y-28). |
| Role | Checkbox (A11Y-29). |
| State | Checked / unchecked / mixed; enabled/disabled (A11Y-29). |
| Focus | Focusable; visible ring (A11Y-13). |
| Announcements | State change and dependent-control availability changes. |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #34 (on-state checkbox in an installer alert), #28 (Sound-like panes with checkbox
  groups), #29 (Parental Controls with dependent controls).
- HIG figures: 15-23 (independent group), 15-24 (indented dependent checkboxes), 15-25 (baseline alignment).
- Gaps: mixed state, disabled state, small/mini, box geometry, pressed/hover.

## 9. HIG source pages

- p. 283 — definition; independence; can enable/disable another control; usage vs. radio buttons.
- p. 284 — groups, dependency/indentation, label must imply both states, sentence-style capitalization,
  mixed dash.
- p. 285 — fixed box size; fonts; intro-label metrics 8/6/5; baseline alignment; 8 px above group; stacking
  8/8/7.
- p. 286 — historical AppKit implementation (NSSwitchButton).

## 10. Recreation-specific decisions / open questions

- **PENDING:** label click target. 10.6 Aqua toggles when the label is clicked; the HIG does not say so.
  Record the decision and test it.
- **PENDING:** indentation step for dependent checkboxes (no HIG metric).
- **PENDING:** mixed-state rendering when only some selected objects have the property.
- **DECIDED:** `NSButton`/`NSSwitchButton` is historical 10.6 detail, not a requirement.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit pp. 283-286 |
| Geometry | Medium | All gaps stated; box size and indent unstated |
| Visual states | Medium | On-state captured; mixed/disabled not |
| Keyboard behavior | Medium | Space/Tab are Aqua conventions; HIG p. 100/110 |

## 12. Acceptance tests

1. **Toggle:** clicking (or Space on) a focused checkbox changes only that checkbox.
2. **Exclusivity:** a checkbox group never behaves as a radio group; multiple boxes can be on.
3. **Dependency:** when the controller is off, dependent checkboxes are disabled/dimmed; turning it on makes
   them available immediately (p. 284).
4. **Mixed:** a multi-object selection with differing values shows a dash, and toggling sets all selected
   objects to the new value.
5. **Label:** every checkbox label implies both states; no label relies on the box graphic alone.
6. **Layout:** regular/small/mini intro gaps are 8/6/5 px; stacked gaps 8/8/7 px; label baselines align.
7. **Accessibility:** role=checkbox with checked/unchecked/mixed states exposed, and a visible focus ring.
8. **Disabled:** a disabled checkbox cannot be toggled by pointer or Space.

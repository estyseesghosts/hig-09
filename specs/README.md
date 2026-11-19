# Component Specifications

Testable, per-component specifications for the Aqua recreation. Each spec follows
[`../templates/component-spec.md`](../templates/component-spec.md) and cites shared rules from the
[accessibility checklist](../notes/accessibility-checklist.md) by ID instead of restating them.

Source chapters are summarized in [`../03-aqua-interface/controls.md`](../03-aqua-interface/controls.md)
and [`../03-aqua-interface/windows.md`](../03-aqua-interface/windows.md). The component-to-evidence matrix is
in [`../notes/component-traceability.md`](../notes/component-traceability.md).

## Index

| Spec | ID | HIG pages | Chapter doc | Evidence status |
| --- | --- | --- | --- | --- |
| [Push button](push-button.md) | CMP-01 | 265-269 | Controls | Text high; geometry partial; states text-only |
| [Toolbar item](toolbar-item.md) | CMP-02 | 255-264 | Controls | Text high; geometry partial; 10.6 capture #14/#19 |
| [Checkbox](checkbox.md) | CMP-03 | 283-286 | Controls | Text high; metrics complete; mixed state uncaptured |
| [Text input field](text-input-field.md) | CMP-04 | 322-325 | Controls | Text high; metrics complete; focus/disabled uncaptured |
| [Source list](source-list.md) | CMP-05 | 208-212 | Windows | Text high; geometry not specified; captures #14/#20 |
| [Sheet](sheet.md) | CMP-06 | 236-237 | Windows | Text high; motion not captured |
| [Menu item](menu-item.md) | CMP-07 | 166-175 | Menus | Text high; state markers source-only |

## Cross-cutting decisions

These apply to every spec and are recorded once here.

- **DECIDED — specs are platform-neutral by default.** Behavior and metrics are stated without assuming
  AppKit; AppKit class names appear only in the historical-implementation line inherited from the chapter.
- **DECIDED — unknown geometry stays unknown.** Where the HIG gives no number and no retained capture
  provides one, the metric is marked `not specified`/`not measured` rather than invented.
- **PENDING — control strategy (native host widgets vs. custom-drawn Aqua).** The HIG's "use system-provided
  controls" advice (p. 255) assumes Mac OS X. Every spec must be re-read when the strategy is chosen; the
  behavioral rules survive either way. See [scope note](../notes/scope-and-evidence.md).
- **PENDING — full keyboard access:** whether a mode toggle exists, or whether all controls are always
  keyboard-reachable (A11Y-26).
- **PENDING — focus-ring geometry and disabled/hover artwork** for custom-drawn controls (A11Y-27); needs
  measurement from a 10.6 environment, not from the HIG.
- **DECIDED — shared accessibility requirements are cited, not duplicated.** Each spec's
  "Accessibility hooks" section lists names/roles/states and points to the A11Y IDs.

## How to use a spec

1. Read §1-§4 for purpose, variants, metrics, and labels.
2. Read §5-§7 for states, keyboard, and accessibility hooks.
3. §8-§11 state exactly how much evidence exists. Do not promote an unmeasured value to a requirement.
4. §12 is the test list; a spec is only "done" when the tests are executable.

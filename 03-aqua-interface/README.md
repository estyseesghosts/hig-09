# Part III — The Aqua Interface (p. 95)

Concrete interaction, visual, and control-level guidance for Aqua-era UI.

## Chapters

- [User Input](user-input.md) (p. 97) — Status: Source-verified
- [Drag and Drop](drag-and-drop.md) (p. 121) — Status: Source-verified
- [Text](text.md) (p. 129) — Status: Source-verified
- [Icons](icons.md) (p. 139) — Status: Source-verified
- [Pointers](pointers.md) (p. 161) — Status: Source-verified
- [Menus](menus.md) (p. 165) — Status: Source-verified
- [Windows](windows.md) (p. 191) — Status: Source-verified
- [Controls](controls.md) (p. 255) — Status: Source-verified
- [Layout Guidelines](layout-guidelines.md) (p. 347) — Status: Source-verified

## Use in this wiki

This is the primary section for implementation-facing notes: component behavior, states, terminology, layout
rules, and visual/interaction patterns to recreate. Seven core components have standalone specs in
[`../specs/`](../specs/README.md); the rest are tracked in the
[component traceability matrix](../notes/component-traceability.md).

## Research status

- **State:** all nine chapters are **Source-verified**.
- **Remaining work:** source coverage is complete, but *implementation readiness* is not. Pixel geometry,
  focus/disabled/hover artwork, and animation timing lack 10.6 measurement evidence (see the
  [image inventory](../notes/image-inventory.md#capture-matrix-central-aqua-components)). Component specs mark
  those values `not measured` rather than guessing.

## Open items

- [x] User Input: rebuilt from pp. 97-120 (pointing devices, trackpad gestures, keyboard, shortcuts, focus,
      selection, text editing, passwords).
- [x] Icons: rebuilt from pp. 139-159 (genres, perspectives, document/toolbar icons, creation sizes, system
      images).
- [ ] Measure focus rings, disabled/hover/pressed states, and control heights from a 10.6 environment before
      custom drawing.
- [ ] Decide the recreation's control strategy (native host vs. custom-drawn); see
      [`specs/README.md`](../specs/README.md#cross-cutting-decisions).

## Retro recreation takeaways

- Use standard control sizes; avoid vertically resizing controls. The HIG's "use system controls" advice is
  historical (Mac OS X apps), not a cross-platform mandate.
- Feedback: dim a button during an indeterminate action; use determinate/indeterminate/asynchronous progress
  indicators and level/rating/relevance indicators with a redundant non-color cue.
- Text controls: static/text/token/search/scrolling lists; combo boxes instead of field+menu; token fields for
  address-like input; search fields.
- View controls: disclosure triangles/buttons, list/column/split/tab views; tab label specs; grouping controls.
- Window-frame vs. window-body control split (only icon buttons, action menus, and search fields cross over).
- Every component spec cites shared accessibility IDs (focus order, focus ring, Esc/Cancel, names/roles/states)
  from [`notes/accessibility-checklist.md`](../notes/accessibility-checklist.md).

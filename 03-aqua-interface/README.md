# Part III — The Aqua Interface (p. 95)

Concrete interaction, visual, and control-level guidance for Aqua-era UI.

## Chapters

- [User Input](user-input.md) (p. 97) — Status: Reviewed
- [Drag and Drop](drag-and-drop.md) (p. 121) — Status: Reviewed
- [Text](text.md) (p. 129) — Status: Reviewed
- [Icons](icons.md) (p. 139) — Status: Reviewed
- [Pointers](pointers.md) (p. 161) — Status: Reviewed
- [Menus](menus.md) (p. 165) — Status: Reviewed
- [Windows](windows.md) (p. 191) — Status: Reviewed
- [Controls](controls.md) (p. 255) — Status: Reviewed
- [Layout Guidelines](layout-guidelines.md) (p. 347) — Status: Reviewed

## Use in this wiki

This is the primary section for implementation-facing notes: component behavior, states, terminology, layout rules, and visual/interaction patterns to recreate.

## Research status

- **State:** All nine chapters researched and filled out (Status: Reviewed).
- **Notes:** See individual chapter files for source notes with PDF page refs and implementation implications.

## Retro recreation takeaways

- Use standard, system-provided controls; prefer regular sizes; avoid vertically resizing controls.
- Implement feedback: push buttons dim on indeterminate actions; progress indicators (determinate/indeterminate/
  asynchronous); level/rating/relevance indicators.
- Text controls: static/text/token/search/scrolling lists; combo boxes over text-field+menu; token fields for
  email-like input; search fields with Cmd-Option-F.
- View controls: disclosure triangles/buttons, list/column/split/tab views; tab label specs; grouping controls.
- Window-frame vs. window-body control split (only icon buttons, action menus, search fields cross over).

## Open items

- [ ] Selection controls sub-sections (p. 280–310) still need fuller source notes.

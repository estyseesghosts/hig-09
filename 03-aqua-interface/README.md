# Part III — The Aqua Interface (p. 95)

Concrete interaction, visual, and control-level guidance for Aqua-era UI.

## Chapters

- [User Input](user-input.md) (p. 97) — Status: Summarized
- [Drag and Drop](drag-and-drop.md) (p. 121) — Status: Source-verified
- [Text](text.md) (p. 129) - Status: Source-verified
- [Icons](icons.md) (p. 139) — Status: Summarized
- [Pointers](pointers.md) (p. 161) — Status: Source-verified
- [Menus](menus.md) (p. 165) — Status: Source-verified
- [Windows](windows.md) (p. 191) - Status: Source-verified
- [Controls](controls.md) (p. 255) — Status: Summarized
- [Layout Guidelines](layout-guidelines.md) (p. 347) — Status: Source-verified

## Use in this wiki

This is the primary section for implementation-facing notes: component behavior, states, terminology, layout rules, and visual/interaction patterns to recreate.

## Research status

- **State:** Drag and Drop, Pointers, Menus, Text, Windows, and Layout Guidelines are **Source-verified**.
  User Input, Icons, and Controls are **Summarized**.
- **Not yet:** Close the gaps listed below before treating any part of this section as implementation-ready.

## Open items

- [ ] Controls: selection controls (pp. 280-310), indicators (pp. 310-321), text controls (pp. 321-328), view
      controls (pp. 329-341), and grouping (pp. 341-345) are summarized at outline level.
- [ ] User Input: keyboard, selection, and text-editing subsections are compressed into broad notes.
- [ ] Icons: icon-creation and system-provided-image subsections need verification.
- [ ] Drag and Drop: add acceptance tests and cross-links to `pointers.md` and `user-input.md`; source coverage
      itself is complete.

## Retro recreation takeaways

- Use standard, system-provided controls; prefer regular sizes; avoid vertically resizing controls.
- Implement feedback: push buttons dim on indeterminate actions; progress indicators (determinate/indeterminate/
  asynchronous); level/rating/relevance indicators.
- Text controls: static/text/token/search/scrolling lists; combo boxes over text-field+menu; token fields for
  email-like input; search fields with Cmd-Option-F.
- View controls: disclosure triangles/buttons, list/column/split/tab views; tab label specs; grouping controls.
- Window-frame vs. window-body control split (only icon buttons, action menus, search fields cross over).

# Drag and Drop

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 121
- **Status:** Reviewed

## Why this matters (retro recreation)

Direct manipulation and drag-and-drop are heavily featured in the HIG; a retro recreation likely wants to
faithfully reproduce drag behavior (including feedback, option-key semantics, trash destination).

## Key sections to review (from TOC)

- Drag-and-Drop Overview (p. 121)
- Drag-and-Drop Semantics (p. 121)
  - Move Versus Copy (p. 122)
  - When to Check the Option Key State (p. 122)
- Selection Feedback (p. 122)
  - Single-Gesture Selection and Dragging (p. 123)
  - Background Selections (p. 123)
- Drag Feedback (p. 123)
- Destination Feedback (p. 123)
  - Windows (p. 124)
  - Text (p. 124)
  - Lists (p. 124)
  - Multiple Dragged Items (p. 125)
  - Automatic Scrolling (p. 125)
  - Using the Trash as a Destination (p. 125)
- Drop Feedback (p. 125)
  - Finder Icons (p. 125)
  - Graphics (p. 126)
  - Text (p. 126)
  - Transferring a Selection (p. 126)
  - Feedback for an Invalid Drop (p. 126)
- Clippings (p. 127)

## Source notes (with page refs)

- p. 121 — Drag-and-Drop Overview; Semantics; Selection Feedback overview.
- p. 122 — Move vs. Copy: dragging with/without Option key; Option key toggles move vs. copy semantics.
- p. 123 — Single-gesture selection and dragging; background selections.
- p. 123 — Drag feedback; destination feedback.
- p. 124 — Destination feedback by object type (windows, text, lists); multiple dragged items; automatic
  scrolling; trash as destination.
- p. 125 — Drop feedback; Finder icons; graphics; text; transferring a selection; invalid drop feedback.
- p. 127 — Clippings (drag-and-drop of clippings).

## Implementation implications

- Retro recreation: implement move-vs-copy via Option key; invalid-drop feedback; automatic scrolling; trash
  handling; selection feedback.

## Assets / examples to capture later

- [ ] Capture drag-related figures if any (figures appear sparse in extracted text).

## Open questions / follow-up extraction

- [ ] Which drag-and-drop specifics (e.g. clippings) are relevant to the recreated app?

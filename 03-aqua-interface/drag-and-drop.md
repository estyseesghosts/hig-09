# Drag and Drop

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 121
- **Status:** Reviewed

## Why this matters (retro recreation)

Direct manipulation and drag-and-drop are heavily featured in the HIG; a retro recreation likely wants to
faithfully reproduce drag behavior (including feedback, Option-key semantics at drop time, trash destination,
and valid/invalid drop cues).

## Drag-and-drop overview (p. 121)

- Drag and drop is the direct-manipulation technique of dragging a selected item and dropping it on a
  suitable destination. An *item* can be text, graphics, icons, or other selectable content. (p. 121)
- Users should ideally be able to drag any content from any window to any other window that accepts the
  content’s type. If source and destination are not visible at once, users can create a clipping by dragging
  data to a Finder window and drag that clipping later. (p. 121)
- Drag and drop should be considered an ease-of-use technique: except when intrinsic to the app (for example
  dragging icons in the Finder), there should always be another method for accomplishing the task. (p. 121)
- Drag and drop is distinct from copy-and-paste and does not use the Clipboard; users can use both without
  side effects. (p. 121)
- Provide immediate feedback at significant points: when data is selected, during the drag, when an
  appropriate destination is reached, and when data is dropped. Pasted data should be target-specific (for
  example, dragging an Address Book entry to a Mail “To” field pastes only the email address). (p. 121)
- Implement Undo for any drag-and-drop operation you enable. If an operation is not undoable, display a
  confirmation dialog before implementing the drop (example: dropping into a write-only drop box on a shared
  volume where the user cannot undo). (p. 121)

## Drag-and-drop semantics (pp. 121–122)

The application must determine whether to **move** or **copy** a dragged item after it is dropped. The correct
behavior depends on context (source/destination relationship and underlying data structure), not on a
persistent keyboard toggle. (pp. 121–122)

### Move Versus Copy (p. 122)

**Default outcome by context:**

- **Same container** (for example, the same window or the same volume): interpret drag and drop as a **move**
  (cut and paste). (p. 122)
- **Different containers** (for example, from one container to another): initiate a **copy** (copy and paste).
  (p. 122)
- **Copy within the same container:** the user can perform a copy operation by pressing the **Option** key
  while dragging. (p. 122)
- **Data-structure exception:** consider the underlying data structure of the destination. If two windows
  display the same document (multiple views of the same data), a drag-and-drop operation between those two
  windows should result in a **move**. (p. 122)
- **Visual feedback:** when performing a copy operation, indicate a copy operation to the user by using the
  **copy pointer** (see “Standard Pointers”, p. 161). (p. 122)

**Common drag-and-drop operations and results (Table 9-1, p. 122):**

| Dragged item | Destination | Default result |
| --- | --- | --- |
| Data in a document | The same document | Move |
| Data in a document | Another document | Copy |
| Data in a document | The Finder | Copy (creates a clipping) |
| Finder icon | An open document window | Copy |
| Finder icon | The same volume | Move |
| Finder icon | Another volume | Copy |

**Rationale:** prevent accidental data loss. Because an Undo command in the destination application does not
trigger an Undo in the source application, moving data across applications may result in potential data loss;
moving data within the same window (or same volume, as in the Finder) does not lead to data loss. (p. 122)

### When to Check the Option Key State (p. 122)

- Check whether the **Option** key is pressed **at drop time**. This lets the user decide move-or-copy later in
  the drag-and-drop sequence. (p. 122)
- Pressing the Option key during the drag-and-drop sequence must **not “latch”** for the remainder of the
  sequence. (p. 122)
- **The Option key does not act as a toggle switch.** Option-dragging between containers always initiates a
  **copy** operation. This guideline helps users learn that **Option means copy**. (p. 122)
- Because the key state is sampled at drop time, applications must track the current modifier state through
  the drag and re-evaluate the outcome when the user releases the mouse button, not when Option is first
  pressed. (implementation guidance consistent with p. 122)

### Copy-override decision summary (implementation-ready)

| Context | Default (no Option at drop) | Option held at drop | Notes / source |
| --- | --- | --- | --- |
| Same container (same window/volume) | **Move** | **Copy** (show copy pointer) | “Move Versus Copy” (p. 122) |
| Different containers | **Copy** | **Copy** (Option is not a toggle) | “Move Versus Copy”; “When to Check the Option Key State” (p. 122) |
| Two windows showing the same document (same underlying data) | **Move** | **Copy** if user requests copy; data-structure view takes precedence over window/container appearance | “consider the underlying data structure…” (p. 122) |
| Finder icon: same volume | **Move** (Table 9-1) | **Copy** (Option means copy) | Table 9-1; Option means copy (p. 122) |
| Finder icon: another volume | **Copy** (Table 9-1) | **Copy** | Table 9-1; Option not a toggle (p. 122) |

### Example sequences (Option pressed/released mid-drag)

These sequences illustrate why the Option key must be sampled at **drop time** and must not latch (p. 122):

1. **Same container, decide to copy late:** User begins dragging an item within the same document/window (default
   would be move). Mid-drag the user presses and holds Option and keeps it held through drop. **Result:** copy
   (copy pointer shown while copy is in effect). (pp. 122)
2. **Same container, changed mind before drop:** User begins dragging within the same container and presses
   Option mid-drag (copy feedback may appear), then releases Option before releasing the mouse button. **Result:**
   move, because Option was not pressed at drop time. (p. 122)
3. **Different containers, Option pressed then released:** User drags from one document to another (default copy).
   User presses Option mid-drag and releases it before drop. **Result:** copy (default for different containers);
   the transient key press must not change the drop-time outcome. (p. 122)
4. **Different containers, Option held through drop:** User drags across containers and holds Option at drop.
   **Result:** copy — Option-dragging between containers always initiates a copy operation; Option does not act
   as a toggle to force a move. (p. 122)
5. **Finder, same volume, late override:** User drags a file icon within the same volume (default move) and
   presses Option just before dropping. **Result:** copy, if Option is down at drop time. (pp. 122; Table 9-1)

## Selection feedback (pp. 122–123)

- **Single-gesture selection and dragging (p. 123):** because dragging requires a mouse-down before movement,
  a selection can be made from that mouse-down just before dragging begins. Users can select and drag a folder
  icon in a single gesture; implicit selection should occur when appropriate at drag start. Single-gesture
  selection-and-dragging is not possible when selecting itself requires dragging (for example range selection of
  text or multiple graphic objects).
- **Background selections (p. 123):** when a window containing a highlighted selection becomes inactive,
  maintain the selection so users can drag previously selected data from inactive windows to the active
  window. Required when items are selected only by range-selection operations (text, groups of icons) because
  implicit selection cannot occur; discrete items (icon, graphical object) may rely on implicit selection.
  When an inactive window becomes key, a background selection becomes a normal highlighted selection.

## Drag feedback (p. 123)

- Provide drag feedback as soon as the user drags an item at least **three pixels**. (p. 123)
- If the user holds the mouse button down on an object or selected text, it should become draggable
  immediately and stay draggable as long as the mouse remains down. (p. 123)
- Applications typically provide an image to drag and handle the receiver frame; in Aqua, dragged items are
  transparent. (p. 123)
- **Proxy icons** are not immediately draggable: because the proxy icon is in the title bar (often used to
  initiate moving a window), the user must hold the mouse button down briefly before it becomes draggable.
  (p. 123)

## Destination feedback (pp. 123–125)

- Provide destination feedback only when the destination can accept the **type of data** in the dragged item,
  not merely because the app is drag-aware (example: a text-only field must not highlight for a dragged
  graphic). (p. 123)
- Use pointers to indicate the result of releasing the mouse (for example the **poof** pointer when dragging an
  item out of a toolbar to indicate it will disappear; alias/copy/not-allowed pointers as appropriate). (p. 124)
- **Windows (p. 124):** valid destination region is usually the content area minus title bar and control areas
  (scroll bars, resize controls, tool palettes, rulers, placards). Highlight only one destination region at a
  time when multiple regions exist. Highlight when the pointer enters a region and remove highlighting when it
  leaves. Do not highlight when a drag-and-drop occurs entirely within one destination region (avoids
  distraction), but if the user drags out and back into the same region, highlight it. Provide more specific
  feedback within a region when appropriate (for example insertion point for text; narrowly defined regions for
  spreadsheets, text boxes, forms, panes).
- **Text (p. 124):** while dragging to a text area, show an insertion indicator (vertical bar) where the item
  would be inserted on drop.
- **Lists (p. 124):** show an insertion indicator where the dragged item would be inserted (example: horizontal
  insertion indicator in Finder Sidebar).
- **Multiple dragged items (p. 125):** destination feedback occurs only if the destination can accept **all**
  dragged items; if not, give invalid-drop feedback (see below). When accepted, accept items in the order
  specified by the source: selection order by default, except ordered views (View by Date, alphabetized list)
  take precedence, and if both source and destination provide spatial ordering (graphic apps) spatial ordering
  takes precedence.
- **Automatic scrolling (p. 125):** define an automatic scrolling region when items can be dragged outside
  windows. Automatically scroll a destination window only if it is also the source window and is frontmost; do
  not automatically scroll inactive windows.
- **Using the Trash as a destination (p. 125):** dragging items to the Trash moves the item from the source to
  the Trash (example: dragging a text selection creates a clipping containing that text inside the Trash). This
  is an exception to the usual move/copy-by-container rules; the user can undo by dragging the clipping out of
  the Trash back to its original source. Preserve the Trash’s container property — do not simply delete the
  source without creating a clipping or other item in the Trash.

## Drop feedback (pp. 125–126)

- On mouse release after a successful drop, provide feedback (primarily behavioral) that the operation
  succeeded. (p. 125)
- **Finder icons (pp. 125–126):** when moving an item by dropping its icon on a folder icon, the dropped icon
  disappears and highlighting is removed from the destination folder icon. If an icon represents a task (such
  as printing), progress feedback may be appropriate.
- **Graphics (p. 126):** drop feedback is usually movement of the actual item to the mouse-up location.
- **Text (p. 126):** after text is dropped, show it highlighted at its destination. When dropped into a
  destination that supports styled text, maintain font/typeface/size attributes; if not, the dropped text
  should assume the attributes specified by the destination insertion point. Support intelligent cut-and-paste
  rules for text drag-and-drop (“Intelligent Cut and Paste”, p. 118).
- **Transferring a selection (p. 126):** after a successful drag-and-drop within a single window, maintain
  selection feedback at the new location (allows repositioning without reselecting). If dragged from an active
  window to an inactive window, the dragged item becomes a background selection at the destination and the
  selection in the active window remains selected (also applies in reverse). When content is dropped into a
  window in which something is selected, deselect everything in the destination before the drop rather than
  replacing the selection with the dragged item.
- **Feedback for an invalid drop (p. 126):** if the user attempts to drop on a destination that does not accept
  the item, the item **zooms back** from its mouse-up location to its source location (a “zoomback”). Zoomback
  also occurs when a drop inside a valid destination does not result in a successful operation. If the user
  drags multiple items to a destination that cannot accept all of them, **none** of the items should be
  accepted; a dialog may inform the user which data types the destination accepts and which items cannot be
  accepted.

## Clippings (p. 127)

- When an item is dragged from an application to the desktop, a clipping is created containing the data in the
  dragged item. If discontinuous selections are dragged to the Finder, create a separate clipping for each
  selected item. (p. 127)
- Provide multiple representations (such as TEXT, PICT, and native formats) to ensure flexibility with
  different subsequent destinations. Regardless of representations stored, preserve round-trip data integrity:
  a clipping dragged back into its source should be identical to the original item. (p. 127)

## Assets / examples to capture later

- [ ] Capture drag-related figures if present in the PDF (extracted text is sparse on figures).

## Open questions / follow-up extraction

- [ ] Which drag-and-drop specifics (for example clippings, path/text drags) are relevant to the recreated app?
- [ ] Does the recreated app need Finder-volume-specific icon drag behaviors, or only in-document/data drags?

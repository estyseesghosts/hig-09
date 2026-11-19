# User Input

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 97
- **Status:** Source-verified

> **Scope:** behavior required of Mac OS X applications in 2009. Where the source describes an OS-provided
> behavior (full keyboard access, assistive shortcuts), the recreation must decide whether it reproduces,
> replaces, or omits it. See [Scope and evidence labels](../notes/scope-and-evidence.md).

## Why this matters (retro recreation)

This chapter defines the interaction model behind every control: what a click does, when a double-click is
required, how selection and text editing behave, which key combinations are reserved, and how focus is shown.
It is the source of the rules that component specs cite (A11Y IDs) and of the keyboard journeys in the
[accessibility checklist](../notes/accessibility-checklist.md).

## Key sections to review (from TOC)

- The Mouse and Other Pointing Devices (p. 97): Clicking, Double-Clicking, Pressing and Holding, Dragging
- The Trackpad (p. 98)
- The Keyboard (p. 99): Functions of Specific Keys, Keyboard Shortcuts, Reserved Shortcuts, Creating Your Own
  Shortcuts, User-Defined Shortcuts, Keyboard Focus and Navigation, Type-Ahead and Key-Repeat
- Selecting (p. 112): Selection Methods, Selections in Text, Selections in Spreadsheets, Selections in
  Graphics
- Editing Text (p. 117): Inserting, Deleting, Replacing a Selection, Intelligent Cut and Paste, Editing Text
  Fields, Entering Passwords

## What the 2009 source says

### Pointing devices (pp. 97-98)

- The interface is optimized for a pointing device; the primary button of a multi-button mouse follows these
  rules, and users choose which button is primary in Mouse preferences.
- Moving the mouse changes only the pointer location/shape. Pressing indicates intent; releasing completes the
  action.
- **Click:** press and release without moving; movement between down and up makes it a drag. The effect must be
  immediate and obvious. For a button, selection happens on press and the action on release; moving off the
  control before release cancels it, and rolling from one button to another clicks neither.
- **Double-click:** two clicks close in time (user setting) and place (usually a few points). It is a shortcut
  for another action (Command-O) or word selection, never the **only** way to do something, because not
  everyone can double-click. Triple-click may select a larger unit; more than three clicks is inadvisable.
- **Press and hold:** no more effect than a click except in defined areas (scroll arrows repeat; a Dock tile
  shows a menu). Pressing a Finder icon selects but does not open it.
- **Drag:** press, move, release. Used for text ranges, menu item choice, range selection, moving icons, and
  resizing. A dragged graphic moves as a whole object (or a transparent representation), not just an outline.
  Boundary rules: releasing outside a restricted boundary leaves the object in place; leaving and re-entering
  before release moves it. Dragging past a window edge can auto-scroll. A three-pixel-or-less movement after
  starting a drag does not move the item. A proxy dragged where it would disappear shows a poof.

### Trackpad and gestures (pp. 98-99)

- A trackpad substitutes for the mouse for pointer movement, selection/activation, scrolling (active or
  background window), and contextual menus.
- Multi-Touch gestures: pinch open/close zooms, rotate rotates the active view, three-finger swipe navigates
  forward/back, four-finger swipe activates Exposé or switches apps.
- If supported: keep gestures consistent with their standard meanings; respond live and cheaply; target the
  most specific object/view; define custom gestures cautiously and distinguishably.
- Users can disable gestures in Trackpad preferences, so never make a gesture the only route to an action.

### Keyboard basics (pp. 99-106)

- The keyboard's primary use is text entry; navigation is always an **alternative** to the mouse.
- Four key kinds: character, modifier, arrow, function. Don't depend on a key existing (not all keyboards have
  every key).
- **Space:** enters a space in text; with full keyboard access, activates the focused item (equivalent to a
  click).
- **Tab:** next tab stop in text; otherwise "move to the next item"; Shift-Tab reverses. Tab can commit data
  before focus moves.
- **Enter:** finishes entry in an area (e.g. a field); no effect while typing in a text document. In a dialog
  with a default button, Enter and Return both activate it.
- **Return:** inserts a line break in text; in arrays, moves to the leftmost field one step lower; activates
  the default button in a dialog.
- **Delete/Backspace:** removes the selection without putting it on the Clipboard; otherwise deletes the
  preceding character. Same as the Edit menu's Delete. Option extends deletion by a semantic unit; Command
  extends further. Recommended: Command-Delete deletes the previous word; Command-Fwd Del the next.
- **Clear:** same as Edit > Delete; not on all keyboards—never require it.
- **Esc:** "let me out": cancel a dialog like Cancel; stop an operation; cancel renaming; cancel a drag. Never
  discard extensive work without confirmation; confirm during a lengthy operation.
- **Modifiers:** Shift (uppercase/extend selection/constrain), Caps Lock (letters only), Option (special
  symbols; modifies clicks/drags), Command (command interpretation; also modifies clicks), Control (modifies
  keys; Control-click opens contextual menus; Control-F7 toggles window/dialog keyboard navigation).
- **Arrow keys:** only shortcuts for mouse actions; never the only way. Text: move the insertion point, Shift
  extends, Option/Command enlarge the semantic unit (character → word → paragraph → line/document); lists:
  change selection; graphics: move one pixel/grid unit; full keyboard access: move between values in a
  control. Don't use arrows to move the pointer or duplicate scroll bars.
- Vertical caret movement preserves the horizontal pixel position and snaps to the nearest character.
- **Function keys:** Help key / Command-Shift-/ opens help; Fwd Del deletes forward; Home/End scroll to the
  start/end (alert sound at the limit) without moving the insertion point; Page Up/Down scroll a page (alert
  at the limit).
- **Text selection with Shift+arrows** extends by character/word/paragraph/line/document (Tables 8-1, 8-2).
  Direction reversal deselects the appropriate unit.

### Keyboard shortcuts (pp. 106-110)

- Never assign **reserved** system combinations to other commands, even if the app doesn't implement the
  system feature (Table 8-3: Esc, Command-Tab, Command-H/Option-H, Command-Shift-Q variants,
  Command-Space, Command-Option-Esc, Command-F5, Control-F1/F7, F9-F12, and international combinations in
  Table 8-4).
- Don't override widely established shortcuts (Command-S Save, Command-Q Quit, etc.); they aren't reserved but
  are expected. See the full [Appendix A](../04-reference/appendix-a-keyboard-shortcuts.md).
- Create shortcuts only for frequent commands; too many makes the app hard to learn.
- Command is the main modifier. Shift complements a Command shortcut (Save As, Redo, etc.); Command-Option is
  a rarely used third level (Save All) or a power-user convenience.
- Use Control sparingly: it is used by universal access and Cocoa text bindings, and other keyboard layouts
  need modifier keys for characters. If adding a modifier beyond Command, prefer letters a-z.
- Don't add modifiers to an existing shortcut for an unrelated command (Shift-Command-Z must not mean an
  unrelated function). If no unique, easy shortcut exists, use none.
- Users can remap application shortcuts in Keyboard & Mouse preferences; still follow the recommendations.

### Keyboard focus and navigation (pp. 110-111)

- Default keyboard access: focus moves only between fields that accept keyboard input. Full keyboard access
  (an OS option) extends navigation to all window/dialog items.
- Focus can move to text fields, type-ahead list boxes, scrolling lists, column views, and list views. In
  Roman systems it begins at the first input field and follows a reading path from upper left to bottom right.
- Focus is shown with a ring in the appearance color (Aqua or Graphite): Figure 8-1 (text field), Figure 8-2
  (scrolling list).
- List/column selection highlights to the full row/column height; in column view the selected item is dark and
  its parent lighter; an inactive window uses the lighter highlight (Figure 8-3).
- Tab/Shift-Tab move between controls; arrows navigate within controls; in list views Left/Right open and close
  disclosure triangles.
- **Type-ahead** queues keystrokes during a busy operation (bounded by the machine). **Key-repeat** starts when
  a character key is held (user-adjustable). Applications can distinguish and should ignore key-repeat for
  Command shortcuts. Key-repeat works only when the app accepts input, not during type-ahead.

### Selecting (pp. 112-117)

- Selection distinguishes an object before acting on it. Feedback is immediate. Selecting never alters the
  object, and clicking outside the selection undoes it.
- Three object types: text (one-dimensional character string), arrays of fields (list = 1-D, table = 2-D), and
  graphics (individually selectable objects).
- **Click** selects one object. **Drag** from an anchor to an active end, with live feedback: text/arrays
  highlight continuously; graphics use a dotted rectangle. Views may auto-scroll during selection.
- **Shift-click** extends a continuous selection (addition model, or fixed-point model); **Command-click**
  makes a discontinuous selection and removes an already-selected object. Not all apps support discontinuous
  selection, and some restrict operations on it.
- **Text:** the insertion point is a zero-length selection at the nearest character boundary. Selected text uses
  the user's highlight color; inactive windows use a percentage/secondary color. Use system-defined colors,
  not hard-coded values.
- **Mouse in text:** single-click places the caret; double-click selects a word (smart: deleting it also
  removes an adjacent space); double-click in space selects the space; triple-click selects the next logical
  unit (e.g. the paragraph, including its trailing terminator and trailing whitespace to the edge).
- **Word definition (US/Canada and similar locales):** letters, digits, nonbreaking space, currency symbols,
  percent, comma between digits, period before a digit, apostrophe between letters/digits, hyphen (not en/em
  dash). Double-clicking any other character selects only that character.
- **Spreadsheets:** click a cell, or Tab/Return to it; second click enters partial content selection. Column
  headings select columns. Tab cycles left-to-right then top-to-bottom; Tab from the last field returns to the
  first. If rows are meaningless, Return behaves like Tab. Command-click supports discontinuous cells.
- **Graphics:** object-based documents bracket a clicked object with handles; a dotted rectangle selects every
  object it touches even partially; Shift-click is continuous, Command-click discontinuous (both discontinuous
  when z-order is undefined). Bitmap documents select the pixel range inside the selection tool.

### Editing text (pp. 117-120)

- **Insert:** click to place the caret, type; it advances with the language direction. Multi-line blocks
  support word wrap without breaking words.
- **Delete:** with a selection, delete it; otherwise delete the preceding character. The caret replaces the
  deleted text; deletion is not placed on the Clipboard but is immediately undoable with Undo.
  Option-Delete may delete a word (document it if implemented). Fwd Del deletes forward.
- **Replace:** typing with a selection replaces it; the replaced text is not put on the Clipboard and is
  immediately undoable.
- **Intelligent cut and paste:** selected words are highlighted without adjacent spaces. Cut also removes one
  adjacent space (preceding if present, else following). Paste inserts a space when the neighbor is part of a
  word but the caret is not inside a word. Applies only to whole-word selections and only in languages with
  spaces (not Thai, Chinese, Japanese). Requires the word definition above.
- **Text fields in non-text apps:** ideally support select-all-and-retype, delete, replace a substring,
  double-click word selection, and Edit-menu Undo/Cut/Copy/Paste/Delete, plus edit checks. Auto-completion
  should highlight the supplied portion to distinguish it from typing.
- **Required fields:** don't litter the UI with asterisks up front. Make selection controls disallow empty
  choices; for text fields, show a "required" indicator only when the user tries to leave the context.
- **Passwords:** each typed character shows as a bullet; Delete removes one bullet and moves back as if it were
  a character; double-click selects all bullets. On leaving the field (e.g. Tab), adjust the bullet count so the
  field no longer reflects the real password length.

## Observed Mac OS X 10.6 behavior

- Open menus: #15 (application menu), #36 (File menu). Menu highlight and dismissal behavior are visible only
  as static states.
- Selection highlighting: list selection is visible in #1, #14, #24, #32; **inactive-window** highlighting is
  not captured.
- Focus rings: **not captured** (image inventory gap).
- Type-ahead, key-repeat, gesture behavior, press-and-hold Exposé, and the three-pixel drag threshold cannot be
  observed in still images.
- Password bullets: **not captured**.
- 10.6.8 environment capture #37 proves the surrounding OS but no input behavior.

## Interpretation

- The chapter is a behavior contract, not a visual style guide. Most rules are testable without pixel
  measurements: click cancellation by moving off a control, double-click as a shortcut only, Shift vs. Command
  selection semantics, Esc=cancel, Return=default, reserved shortcuts, focus order, and password masking.
- The selection model is consistent across text, arrays, and graphics: click, drag, Shift=continuous,
  Command=discontinuous. Implement it once and specialize per view.
- Intelligent cut/paste is optional but, if implemented, has precise space rules tied to a particular
  locale-dependent word definition. Implementing the word definition without the cut/paste rules (or vice
  versa) produces inconsistent behavior.
- Full keyboard access is an OS-level mode in 2009; a recreated UI must decide whether to expose an equivalent
  switch or make everything keyboard-reachable by default (A11Y-26).

## Recreation-specific decision / open question

- **PENDING — input device support:** mouse, trackpad, touch, keyboard-only. The HIG assumes a mouse plus
  keyboard; a web/canvas recreation may have neither.
- **PENDING — full keyboard access:** a mode toggle, always-on, or absent (A11Y-26).
- **PENDING — gestures:** reproduce pinch/rotate/swipe, or omit; if reproduced, never as the only route
  (p. 99).
- **PENDING — double-click/triple-click timing:** the HIG defers to a user setting; the recreation must define
  fixed or configurable thresholds.
- **PENDING — intelligent cut/paste:** in scope? It depends on locale and word segmentation.
- **PENDING — password bullet behavior:** the HIG's "adjust bullet count on blur" rule should be confirmed
  before implementing.
- **DECIDED — reserved shortcuts are off-limits**; audit the recreation's shortcuts against Appendix A.
- **DECIDED — three-pixel drag threshold** is adopted as the source's rule for "did the item move".
- **REJECTED — treat AppKit text-system APIs as requirements.** Cocoa key bindings are historical detail.

## Implementation implications

- Click model: select on press, act on release, cancel when the pointer leaves the control before release
  (p. 97). This avoids the "roll from button to button" failure.
- Never make double-click the sole route to an action (p. 98); always provide a single-click or menu alternative.
- Drag: ±3 px dead zone; whole-object drag, not outline; boundary release leaves the object in place (p. 98).
- Keyboard: Space activates focused items; Esc cancels; Return/Enter activates the default; arrows never move
  the pointer (pp. 100-103).
- Focus ring uses the appearance color; selection uses primary/secondary highlight colors, never hard-coded
  (pp. 110-111, 115).
- Text editing: typing replaces a selection; Delete removes the selection/preceding character; no Clipboard
  write on delete (pp. 117-118).

## Assets / examples to capture later

- [ ] Focus ring on text field, list, button, and tab view (Figures 8-1, 8-2).
- [ ] Active vs. inactive text/list selection, including column-view parent highlight (Figure 8-3).
- [ ] Double-click word selection and triple-click paragraph selection (p. 115).
- [ ] Shift-click addition vs. fixed-point models (Figure 8-6) and Command-click discontinuous selection
      (Figures 8-7, 8-8).
- [ ] Password field before/after leaving the field (p. 120).
- [ ] Trackpad gesture targets, if the recreation supports gestures (p. 99).

## Open questions / follow-up extraction

- [ ] Which selection model (addition vs. fixed-point) does the recreated app use for text Shift-click?
- [ ] Does the app support discontinuous selection, and which operations are allowed on it?
- [ ] What are the recreation's click/double-click/triple-click timing thresholds?
- [ ] Are en/em dashes and nonbreaking spaces reachable on the target platform's keyboard?

# Controls

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 255
- **Status:** Source-verified

> **Scope:** the requirements below describe what the 2009 HIG asked of applications **targeting Mac OS X**.
> `NSButton`/`NSTexturedRoundedBezelStyle`-style notes are historical AppKit implementation detail, not a
> mandate for this recreation. Decisions for the recreation's own platform are isolated under
> [Recreation-specific decisions](#recreation-specific-decisions--open-questions). See
> [Scope and evidence labels](../notes/scope-and-evidence.md). Accessibility obligations shared by every
> control are in the [accessibility checklist](../notes/accessibility-checklist.md).

## Why this matters (retro recreation)

The Controls chapter is the implementation-heavy core of the recreation: button styles, selection controls,
indicators, text controls, view controls, grouping controls, and precise spacing specs. A retro recreation
that re-creates any settings or document UI will need an accurate control inventory and behavior model. This
chapter also carries hard pixel measurements (control heights, spacing) that are directly usable for a
pixel-faithful recreation.

## Key sections to review (from TOC)

- Window-Frame Controls (p. 255)
  - Determining the State of a Window-Frame Control from its Appearance (p. 256)
  - Rectangular-Style Toolbar Controls (p. 257)
  - Capsule-Style Toolbar Controls (p. 261)
  - Legacy Toolbar Controls (p. 264)
- Buttons (p. 265)
  - Push Buttons (p. 265)
  - Icon Buttons (p. 269)
  - Scope Buttons (p. 271)
  - Gradient Buttons (p. 273)
- Selection Controls (p. 280)
  - Radio Buttons (p. 280)
  - Checkboxes (p. 283)
  - Segmented Controls (p. 286)
  - Icon Buttons and Bevel Buttons with Pop-Up Menus (p. 288)
  - Pop-Up Menus (p. 289)
  - Action Menus (p. 293)
  - Combination Boxes (p. 295)
  - Path Controls (p. 298)
  - Color Wells (p. 300)
  - Image Wells (p. 300)
  - Date Pickers (p. 301)
  - Command Pop-Down Menus (p. 303)
  - Sliders (p. 305)
  - The Stepper Control (Little Arrows) (p. 309)
  - Placards (p. 310)
- Indicators (p. 310)
  - Progress Indicators (p. 311)
  - Level Indicators (p. 316)
  - Rating Indicators (p. 319)
  - Relevance Indicators (p. 320)
- Text Controls (p. 321)
  - Static Text Fields (p. 321)
  - Text Input Fields (p. 322)
  - Token Fields (p. 325)
  - Search Fields (p. 326)
  - Scrolling Lists (p. 328)
- View Controls (p. 329)
  - Disclosure Triangles (p. 329)
  - Disclosure Buttons (p. 331)
  - List Views (p. 333)
  - Column Views (p. 334)
  - Split Views (p. 336)
  - Tab Views (p. 338)
- Grouping Controls (p. 341)
  - Separators (p. 342)
  - Group Boxes (p. 344)

## Source notes (with page refs)

- p. 255 — Controls are graphic objects causing instant actions or visible results when manipulated. Standard
  controls include push buttons, scroll bars, radio buttons, checkboxes, sliders, and pop-up menus. Use the
  standard, system-provided controls — they auto-update with OS refreshes and familiar use means predictable
  operation. Use only standard control sizes (regular, small, mini); most apps look best with regular.
  **Scope:** this is advice to applications shipping on Mac OS X (where the controls are AppKit's); it is not
  a cross-platform mandate. See [Scope and evidence](../notes/scope-and-evidence.md).
  - Avoid vertically resizing controls (problematic in Mac OS X v10.5+).
  - Note: when a control's dimension (typically height) is fixed, the measurement is for window layout, not
    for creating the control.
- p. 255 — Controls described in this chapter are suitable for the window body; they should not be used in
  window-frame areas. The exception: icon buttons, action menus, and search fields may also be used in
  window-frame areas.
- p. 256 — Window-frame controls may change appearance with window state and control enabled state; appearance
  separates control background/bezel (window's active state) from icon/glyph (whether functionality is enabled).
  Table 15-1 documents states (inactive/active window × enabled/disabled control; click-through nuances).
  - In an inactive window, the icon in a control that does not support click-through uses the disabled
    appearance regardless of enabled state.
- p. 257–261 — Rectangular-style toolbar controls: usable in toolbar AND bottom bar; versatile (push button,
  toggle, segmented, pop-up). Use in toolbar for frequently used commands; use in bottom bar when controls
  directly affect window-body contents/organization. Text in such controls should be a noun/noun phrase
  (object/setting/state) or verb/verb phrase (action); title-style capitalization. Toggle controls in toolbar
  may use automatic highlighting for on state, but must provide two descriptive labels (on/off) below the
  control and describe both states in the help tag.
  - Must supply descriptive (external) label per rectangular-style toolbar control so users can customize
    toolbar to Icon & Text / Text Only; bottom-bar use does not need external labels.
  - Specifications: regular default in toolbar (small supplied for customization); control spacing 8 px between
    controls (automatic; may vary with external label length). Implementation: IB "Round Textured Button";
    NSButtonCell bezel `NSTexturedRoundedBezelStyle`; segmented: `NSSegmentedControl` style
    `NSSegmentStyleTexturedRounded`, mode `NSSegmentSwitchTrackingSelectAny` (blue glow indicates on state);
    toggle: NSButton with `NSTexturedRoundedBezelStyle` and `showsStateBy` containing `NSContentsCellMask`
    (no alternate image for the glow).
- p. 261–263 — Capsule-style toolbar controls: toolbar only (NOT bottom bar). Versatile (push button, toggle,
  segmented). Mail toolbar example. If both toolbar and bottom-bar controls are needed, use rectangular-style
  in both to avoid mixing. Segmented: avoid mixing text and icons across segments; all segments same content
  type. Implementation: drag segmented control in IB (1 segment = standalone button); NSSegmentedControl.
- p. 264 — Legacy toolbar controls: pre-Mac OS X v10.5 brushed-metal/metal buttons ("textured" in IB). Transitional
  only. Textured button used in toolbar/bottom bar with height 23 px (regular) / 18 px (small) automatically
  becomes rectangular-style in v10.5+. Toolbar may only contain icon buttons, action menus, search fields, plus
  rectangular/capsule controls.
- p. 265 — Buttons initiate immediate action; if action is indeterminate, dim button and provide status
  feedback. Prefer two separate buttons for opposing functions (Reload/Stop) over dual-purpose buttons; if dual
  must be used, track state timing and give immediate/informative feedback.
- p. 265–269 — Push buttons: instantaneous action (save, complete dialog operation, acknowledge error). Do not
  use push button to display information or mimic other controls; do not use as a label (use static text);
  avoid associating a menu with a push button (use bevel button). Always text-only (no image; use bevel button).
  Label = verb/verb phrase ("Save", "Close", "Print", "Delete", "Change Password"); specific when acting on a
  single setting ("Choose Picture…" not "Choose…"); no "now" needed. Apply the shared ellipsis rules in
  [Text](text.md#using-the-ellipsis-character) (pp. 131-132): use an ellipsis when the action requires
  specific additional input/choices or opens a separate window or dialog in which the user performs that
  input (for example **Print…**, **Save As…**, **Choose Picture…**; opening another app’s preferences to
  complete a task is a separate user task). Do **not** add an ellipsis merely because another window may
  appear (for example **Save**, **Copy**, **Get Info**, or **New** in the general case; see Text for
  counterexamples). Default button = safe action in dialog, Return/Enter activates; when user presses
  nondefault (e.g. Cancel), it acquires color and default loses color; system-provided buttons handle this
  automatically. (pp. 131-132, 265-269)
- p. 265–269 — Push button specs: regular/small/mini sizes; height fixed per size, width by label length (don't
  clip). Font: system font per size (auto via IB). Spacing: ≥12 px between buttons (regular), 10 (small),
  8 (mini); destructive actions (Delete) farther from safe buttons.
- p. 269–271 — Icon buttons: behave like bevel buttons but no visible rectangular edge; whole button clickable.
  Toolbar use; not for bottom bar. May contain pop-up menu; may contain text label user can choose to view, or a
  single downward arrow for pop-up. Hit target ≈10 px margin around icon/label; icons 24–32 px (e.g. 32×32);
  ≥8 px between button edges for ≥24 px icons. Labels name a thing ("Network") or describe action ("Mask").
- p. 271–273 — Scope buttons: for scope bars only (search scope / save or set scoping criteria). Two styles:
  recessed (narrow types/groups, e.g. Dictionary lookup locations) and round rectangle (save/set criteria, e.g.
  Finder search criteria). Fonts: view font (12 pt Lucida Grande); bold for recessed, regular for round rect.
- p. 273–275 — Gradient buttons: instantaneous action related to a view (source list). E.g. Keyboard & Mouse
  prefs add/remove shortcuts; Mail sidebar New Mailbox. Behavior: push-button/toggle/pop-up. Not for window
  frame areas; use rectangular-style toolbar control if Action menu/bottom-bar functionality needed. Contain
  images, not text; prefer system-provided images (Action menu, Add).

- pp. 280-345 - Selection, indicator, text, view, and grouping controls are documented in the detailed sections
  below. The earlier placeholder bullets were removed after the full source read.

## Selection controls (pp. 280-310)

These controls let users choose from multiple items. Some allow only a single selection; others can be
configured for single or multiple selection. They are for the **window body** only. The single exception is the
icon button with a pop-up menu, which may also be used in a toolbar. (p. 280)

### Selection controls at a glance

| Control | Use when | Avoid when | Core metrics |
| --- | --- | --- | --- |
| Radio buttons | 2 to about 5 mutually exclusive, related choices | More than 5 choices (use a pop-up menu); a single on/off choice (use a checkbox) | Intro-label gap 8/6/5 px; vertical gap 6/6/5 px (regular/small/mini) |
| Checkboxes | Independent on/off states; hierarchical dependent options | Mutually exclusive choices (use radio buttons) | Intro-label gap 8/6/5 px; vertical gap 8/8/7 px |
| Segmented control | A few closely related choices for a selected object; view/pane switching | Adding/deleting source-list items (use a rectangular toolbar control or gradient button); mixing icons and text | Segment icon 17×15 / 14×13 / 12×11 px |
| Icon/bevel button with pop-up menu | An image button that opens a menu | A standard text pop-up menu is sufficient | Same specs as the underlying icon/bevel button |
| Pop-up menu | Up to 12 mutually exclusive choices not always visible | More than 12 items; a changing item count; multiple simultaneous selections; submenus | Item inset 9/7/5 px; stacked gap 10/8/6 px |
| Action menu | A visible shortcut to a handful of commands for the current selection | Anywhere except a toolbar or the bottom of a list/source list | Regular or small Action icon |
| Combo box | Pick from a list **or** type a custom value; one selection | Multiple selections; a fixed list only (use a pop-up menu) | Stacked gap 12/10/8 px |
| Path control | Show a file-system path without technical detail; retrace/open folders | A simple text label is enough | Standard regular only; navigation/pop-up regular/small/mini |
| Color well | Show and change a color setting | A large color area is the content | Standard system control |
| Image well | Drag-and-drop target for an icon or picture | In place of a push or bevel button | Standard system control |
| Date picker | Select a date/time in a window | A free-form text field is sufficient | Text+stepper or graphical calendar/clock |
| Command pop-down | 3-12 commands that affect a shared window's contents | Ordinary window commands; mutually exclusive value choices | Same specs as a pop-up menu |
| Slider | A continuous range with live feedback | A small set of discrete choices (use radio buttons or a pop-up menu) | Height 19/14/11 px with directional thumb, no ticks; spacing 12/10/8 px |
| Stepper | Increment/decrement a value, usually with a text field | A large range or direct manipulation is needed | Text-field gap 2/2/1 px |
| Placard | Page number or magnification at the bottom of a document window | Commands unrelated to magnification/page count (use an Action menu) | 15 px high; small system or label font |

### Radio buttons (pp. 280-283)

**Purpose.** A group of radio buttons presents mutually exclusive, related choices; exactly one is selected.
Security preferences uses them to choose which connections pass through the firewall (Figure 15-20).

**Usage.**
- Use for a set of choices from which the user can choose only one. Use checkboxes when more than one can be
  selected at the same time.
- Do not use a single radio button for a single setting/state the user can accept or reject; use a checkbox.
- A group should contain **at least two and at most about five** items. With more than five, consider a pop-up
  menu.
- A radio button should **never initiate an action**, although the choice can change application state. In
  Speech preferences, choosing "Listen continuously with keyword" enables the keyword setup controls
  (Figure 15-21).
- A radio-button group is **never dynamic**: its contents and labels do not change with context.

**Contents and labeling.**
- The selected/unselected appearances are supplied automatically; you cannot put text or images inside a radio
  button.
- Every button needs an external text label describing its choice, with **sentence-style capitalization**.
- Fonts follow the control size: regular = system font, small = small system font, mini = mini system font.

**Specifications.**
- Intro-label gap from the colon to the control: **8 / 6 / 5 px** (regular/small/mini).
- Vertical spacing between buttons: **6 / 6 / 5 px**.
- Horizontal groups: measure the longest label and use that measurement to make the gaps equal.
- Align the baseline of the introductory label with the baseline of the first button's label (Figure 15-22).
- Disabled state: the HIG does not give a separate disabled metric here; use the system control's disabled
  rendering and dim the whole group consistently rather than leaving one enabled button in a disabled group.

**Interaction.** The HIG specifies selection semantics, not a custom keyboard model. Use standard Aqua
radio-group behavior: Tab reaches the group, arrow keys move the selection within it, and the selected button
is the group's value. Do not make a radio button perform an immediate command.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSButton` with type `NSRadioButton`.

**Test checks.** Exactly one button is selected after any interaction; clicking the selected button does not
deselect it; a group of six or more is a design-review failure unless a documented exception exists.

### Checkboxes (pp. 283-286)

**Purpose.** A checkbox describes a state, action, or value that is either on or off. In a group, each checkbox
is independent unless the dependency is clearly shown by indentation.

**Usage.**
- Use for two opposite states, actions, or values. Use radio buttons for mutually exclusive choices.
- Use a group for several independent values.
- Use an indented hierarchy when an on/off choice leads to additional related on/off choices. In the Trackpad
  pane, "Allow horizontal scrolling" is indented under "Use two fingers to scroll"; Dragging and Drag Lock are
  unavailable unless Clicking is selected (Figure 15-24).
- A checkbox can also enable or disable another control, such as a text field or pop-up menu.

**Contents and labeling.**
- The label must clearly imply both opposite states. If no unambiguous label exists, use a pair of radio
  buttons so each state can have its own label.
- Labels use **sentence-style capitalization**, unless the state/value is the title of another interface
  element that is already capitalized.
- When a user selection comprises more than one state, show a **dash** in the affected checkboxes. This matches
  the mixed-state indicator used in menus.
- Fonts: regular = system font, small = small system font, mini = mini system font.

**Specifications.**
- Intro-label gap: **8 / 6 / 5 px**.
- If the intro label is above the group, leave **8 px** between the label and the first checkbox.
- Align the intro label's baseline with the closest checkbox label (Figure 15-25).
- Vertical spacing when stacked: **8 / 8 / 7 px**.
- Indent dependent checkboxes below the controlling checkbox; independent checkboxes all appear at the same
  level.
- Disabled state: use the system disabled rendering. A dependent checkbox that is unavailable because its
  controller is off must be dimmed, as in the Trackpad example.

**States.** Off (unchecked), on (checked), mixed (dash), enabled, disabled. The mixed state is for a selection
that spans multiple objects with differing values, not for "unknown."

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSButton` with type `NSSwitchButton`.

**Test checks.** Clicking the label toggles the checkbox; mixed state appears only for a multi-object selection;
dependent controls enable/disable immediately when the controller changes.

### Segmented controls (pp. 286-288)

**Purpose.** A segmented control is divided into two or more segments and behaves as a collection of radio
buttons or checkboxes. Like a push button, clicking a segment initiates an immediate action.

**Usage.**
- Use for a few closely related choices that affect a selected object, or to change views/panes in a window.
- A segmented control used as a view changer looks like a tab view but is **not attached to the panes**; a tab
  view is. Do not rely on tab-view semantics for a segmented view switcher.
- Do not use a `+`/`-` segmented control to add/delete source-list objects. In a bottom bar use a
  rectangular-style toolbar control; in the window body use a gradient button. The system supplies the
  plus/minus images.
- This section covers window-body segmented controls. Toolbar/bottom-bar segmented styles are in
  "Window-Frame Controls" (pp. 255-264).

**Contents and labeling.**
- A segment contains **either icons or text, not a mixture**. With icons, a text label may sit below the
  control.
- Segment text or the label below uses a **noun or short noun phrase** describing a view or object, with
  **title-style capitalization**.
- Prefer system-provided images when using icons; imitate their clarity and simple lines for custom images.

**Specifications.**
- Height fixed per size; width chosen by the developer. **All segments must be the same width**; a different
  width implies different behavior or importance.
- Fonts: regular = system font, small = small system font, mini = mini system font, for both segment text and
  the label below.
- Icon sizes: **17×15 / 14×13 / 12×11 px** (regular/small/mini), as in Figure 15-27.

**States and interaction.** Segments may be selected/unselected and enabled/disabled using the standard system
rendering. The HIG does not define hover/pressed artwork here; use the system control. The action occurs on
click, not on a delayed commit.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSSegmentedControl`.

**Test checks.** No mixed icon/text segments; equal widths; view-switcher segments do not claim tab-view
attachment; add/remove is not implemented with a `+`/`-` segmented control in the window body.

### Icon buttons and bevel buttons with pop-up menus (p. 288)

**Purpose.** A bevel button or icon button containing a pop-up menu has a single downward-pointing arrow. It
can behave like a standard pop-up menu (the image shows the current selection) or represent a menu title and
always show the same image.

**Usage.** This is the one selection control that may also be used in a window-frame area. For the button
appearance and hit targets, see "Icon Buttons" (pp. 269-271) and "Bevel Buttons" (pp. 277-279).

**Implementation (Mac OS X 10.6 AppKit; historical).** Drag an `NSPopUpButton` into the window; set its type to Pull Down. For a rounded or square
bevel button, choose the corresponding style; for an icon button, deselect Bordered. Resize as needed.

**Test checks.** The arrow is a single downward arrow; the image is either the current selection or a fixed menu
title, never an ambiguous mix; the whole button area opens the menu.

### Pop-up menus (pp. 289-293)

**Purpose.** A pop-up menu presents a list of mutually exclusive choices in a dialog or window. The closed
control displays the current value.

**Usage.**
- Use for **up to 12** mutually exclusive choices the user does not need to see all the time.
- A pop-up menu can replace a set of six or more radio buttons to save space.
- Do **not** add a submenu to any item; it hides choices too deeply and is physically difficult.
- Avoid pop-up menus for more than 12 items (use a scrolling list unless space is restricted), for a list whose
  number of items can change, or when multiple simultaneous selections are appropriate (use checkboxes or a
  pull-down menu with checkmarks).
- Pop-up menu items are **nouns or adjectives** (things, states, attributes), **not verbs**. Use a pull-down
  menu for commands.
- A command that affects the menu's own contents (for example, Add Printer) goes at the **bottom, below a
  separator**, and its result becomes the menu's default selection.

**Interaction.**
- Press to open, drag to choose. The chosen item flashes briefly and is displayed in the closed control.
- Moving the pointer outside the open menu without releasing leaves the current value active; an exploratory
  press does not select a new value.
- The open menu shows a checkmark to the left of the current value.
- The control has a double-arrow indicator.
- The introductory label is to the left in left-to-right scripts and uses **sentence-style capitalization**;
  the only exception is when the control is used as a group-box title (not common).

**Specifications.**
- Height fixed per size; width wide enough for the longest item. Stacked pop-up menus should all be the same
  width.
- Menu-item text inset: **9 / 7 / 5 px** from the left edge and at least **9 / 7 / 5 px** from the double-arrow
  area.
- Intro label: emphasized system/small/mini font; **8 / 6 / 5 px** between the colon and the control.
- Vertical stack spacing: at least **10 / 8 / 6 px** (Figure 15-32).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSPopUpButton`.

**Test checks.** 12-item limit; no submenus; no verbs in a pop-up (commands belong in a pull-down); checking the
current value; pointer-outside cancellation leaves the old value.

### Action menus (pp. 293-295)

**Purpose.** An Action menu is a specific type of pop-up menu designed to replace an application-wide
contextual menu. It provides a visible shortcut to a handful of useful commands for the current selection.

**Usage.**
- Use in a toolbar or at the bottom of a list view/source list. Do not place it anywhere else in the window
  body: the object it acts on can appear anywhere, so there is no consistent location.
- If an application-wide contextual menu exists, consider replacing it with a toolbar Action menu.
- The menu items follow contextual-menu rules: each item should also be available as a menu command, and
  keyboard shortcuts should not be displayed.

**Contents and labeling.**
- Display only the system-supplied **Action icon** and the standard downward arrow.
- No label is needed; users recognize the Action icon. The exception is the toolbar customization label, which
  must be supplied so the item can display as icon+text or text only.

**Specifications.** The Action icon comes in regular and small sizes; choose the size proportional to the
control. Spacing follows the host control: rectangular-style toolbar control in a toolbar, gradient button below
a source list/list view.

**Implementation (Mac OS X 10.6 AppKit; historical).** Toolbar: rectangular-style toolbar control with `NSActionTemplate`. Bottom of a source
list/list: gradient button.

**Test checks.** The Action icon is the system image; no keyboard shortcuts appear in the menu; every item is
also reachable as a main-menu command.

### Combo boxes (pp. 295-298)

**Purpose.** A combo box combines a text entry field with a drop-down list. It displays likely choices while
allowing the user to type an item not in the list.

**Usage.** Use when the user should be able to pick from a list **or** supply a custom value. A combo box
allows only one selection.

**Interaction.**
- Users can type any appropriate characters. If the typed text matches an existing item or its first
  characters, that item is highlighted when the list opens.
- A user-typed item is **not added** to the permanent list.
- Open the list by pressing or clicking the arrow. The list descends from the text field, is the same width as
  the field plus the arrow box, and has a drop shadow.
- If opened by pressing the arrow, select by dragging; if opened by clicking, select by clicking or with the
  Up/Down Arrow keys. Accept with Space, Enter, or Return.
- Clicking outside the list, including in the text field, closes it.

**Contents and labeling.**
- Default state is closed, with the field empty or showing a default selection. The default selection (which
  need not be the first item) should hint at the hidden choices; an introductory label helps.
- The list must not extend beyond the arrow box; long items are truncated.
- List-item font is proportional: system/small/mini. The intro label uses emphasized system/small/mini.
- Intro-label gap: **8 / 6 / 5 px**.
- Vertical stack spacing: at least **12 / 10 / 8 px**.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSComboBox`.

**Test checks.** Typed custom value is accepted but not persisted into the list; matching prefix highlights the
item; keyboard accept works; clicking outside closes without changing the value.

### Path controls (pp. 298-300)

**Purpose.** A path control displays the file-system path of the currently selected item, without being overly
technical. It can also let users retrace steps and open folders visited earlier.

**Styles.**
- **Standard** — regular size only.
- **Navigation bar** — regular, small, mini.
- **Pop up** — regular, small, mini.

**Contents and labeling.** All styles show text plus icons for applications, folders, and document types. The
pop-up style opens a menu of all locations plus a **Choose** item; Choose opens the Open dialog to view the
selected folder. If the path is too long, the folder names between the first and last locations are hidden
(Figure 15-39).

**Usage.** Use when the location matters but a raw path would be too technical. Do not use a path control as a
substitute for a simple label when only a name is needed.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSPathControl`; style is set in the Attributes pane.

**Test checks.** Long paths hide middle components, not the endpoints; pop-up Choose opens the Open dialog at
the selected folder.

### Color wells and image wells (pp. 300-301)

**Color well.** A small rectangular control showing the current color for a setting; clicking it opens the
Colors window to change that color. Multiple color wells may appear in one window. Pages uses three for fill,
outline, and shadow (Figure 15-40). Implementation: `NSColorWell`.

**Image well.** A drag-and-drop target for an icon or picture; useful for thumbnail sets such as a clip-art
catalog. Do not use image wells in place of push buttons or bevel buttons. Some image wells must always contain
an image (for example, the user picture in Accounts). If the user can clear one, provide standard Edit menu
commands and Clipboard support. Implementation: `NSImageView`.

**Test checks.** Color well click opens the shared Colors window and updates the setting live; image well accepts
the documented drag types and shows the image; a clearable well supports Cut/Copy/Paste/Delete.

### Date pickers (pp. 301-303)

**Purpose.** A date picker lets users select a specific date and time in a window.

**Styles.**
- **Text field + stepper** — useful when space is constrained and users make specific selections. Can show
  month/day/year or month/year, and hour/minute/second or hour/minute; can show date-only or time-only. Adjust by
  clicking the stepper arrows or selecting a field and typing.
- **Graphical calendar and clock** — use when browsing days in a calendar or a clock face suits the app. Show
  calendar, clock, or both. Change month with the left/right arrows, select a day by clicking its date, and set
  time by dragging the clock hands.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSDatePicker`; switch textual/graphical in the Attributes pane.

**Test checks.** Textual fields accept typing and stepper changes; graphical calendar cannot select an invalid
date; date and time remain consistent when either subcontrol changes.

### Command pop-down menus (pp. 303-305)

**Purpose.** A command pop-down menu is similar to a pull-down menu but appears inside a window. It presents
commands that affect the containing window's contents (for example, the Colors window's palette commands).

**Usage.**
- Use only when the containing window is shared among multiple windows or applications and the menu contains
  commands that affect that window's contents.
- Contains **3 to 12 commands**. Items do **not** have to be mutually exclusive.

**Contents and labeling.**
- No introductory label.
- The closed control always displays the same text, which acts as the menu title. This differs from a pop-up
  menu, which displays the current value.
- Single downward arrow. Checkmarks may appear to the left of all currently active selections.

**Specifications.** Same as pop-up menus (pp. 291-292).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSPopUpButton` with type Pull Down.

**Test checks.** Closed title never changes with the selected command; active commands show checkmarks; the
menu is not used for ordinary window commands.

### Sliders (pp. 305-309)

**Purpose.** A slider lets users choose from a continuous range of values. Sliders can be linear or circular.

**Usage.**
- Sliders support **live feedback** (live dragging), so they are useful when users should see the effect in real
  time (for example, Dock icon size).
- Choose linear vs. circular (and horizontal vs. vertical) from the user's mental model and real-world
  analogues. The circular shadow-angle slider both compacts 0-360° and mirrors the shadow's placement.
- Use tick marks when the scale matters or users need specific values. Omit them when users do not need to know
  the intermediate values (Dock size/magnification).
- Round thumb is recommended without tick marks; directional thumb is useful with tick marks because its point
  indicates the value. Specifying a nonzero tick count automatically changes a round thumb to directional.
- A circular slider has a small dimple; drag it clockwise or counterclockwise.
- Label at least the starting and ending values. If tick intervals are unequal, label the interior ticks too.
  An introductory label setting the context is recommended.

**Specifications.**
- Linear sizes: regular, small, mini. Circular: regular, small.
- Height, horizontal, directional thumb: **19 / 14 / 11 px** without ticks; **25 / 19 / 17 px** with ticks.
- Height, horizontal, round thumb: **15 / 12 / 10 px**.
- Width, vertical, directional thumb: **18 / 14 / 11 px** without ticks; **24 / 19 / 17 px** with ticks.
- Width, vertical, round thumb: **15 / 11 / 10 px**.
- Circular diameter: **32 / 22 px** with ticks; **24 / 18 px** without (regular/small).
- Range-label font: label font for regular/small; **9-point label font** for mini.
- Stacked linear slider spacing: at least **12 / 10 / 8 px**.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSSlider`.

**Test checks.** Live update while dragging; tick labels match the actual scale; round thumb has no ticks; value
is clamped at both ends; circular slider wraps through the start/end point as specified.

### Stepper controls (pp. 309-310)

**Purpose.** A stepper (little arrows) increments or decrements a value, usually paired with a text field that
shows the current value. The field may or may not be editable.

**Specifications.** Regular, small, mini; fixed dimensions per size. Gap between stepper and its text field:
**2 / 2 / 1 px** (Figure 15-53).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSStepper`.

**Test checks.** One click changes the value by one step; press-and-hold repeats at the system rate; the paired
field updates immediately and respects the same minimum/maximum.

### Placards (p. 310)

**Purpose.** A placard is a small control at the bottom of a window that displays information such as the
current page number or magnification. It is typically a pop-up menu to the left of the horizontal scroll bar in
a document window, used to change the view (page or magnification).

**Usage.** Do not add unrelated commands to a placard's menu; use an Action menu for commands that affect the
window contents in other ways.

**Specifications.** Not available in Interface Builder. Subclass `NSScrollView` (see the Sketch sample code).
Height **15 px**; text in **small system font or label font**.

**Test checks.** Placard stays at the bottom-left of the horizontal scrollbar; changing it changes page or
magnification only; no unrelated commands.

## Indicators (pp. 310-321)

Indicators show the status of something; users mostly do not interact with them. They are for the window body
only. (p. 311)

### Indicators at a glance

| Indicator | Use when | Avoid when | Sizes |
| --- | --- | --- | --- |
| Determinate progress bar | The full length is known and progress can be mapped to time | Duration is unknown | Regular, small |
| Indeterminate progress bar | Duration is unknown but the process has a focused dialog/window | Space is very constrained (use async); the process may become determinate (keep the bar) | Regular, small |
| Asynchronous progress indicator | Space is very constrained; background/async work near a control | The process may become determinate (use an indeterminate bar) | Regular, small, mini |
| Capacity indicator | A finite capacity with min/max (storage, battery) | Values have no meaningful min/max | Regular only; 16 px bar/segment height |
| Rating indicator | Ranking items relative to others in a list/table | A single item's rating in isolation | Standard system |
| Relevance indicator | Showing search-result relevance across a list/table | A single result in isolation | Standard system |

### Progress indicators (pp. 311-316)

Common rules:
- A progress dialog for an interruptible process should contain a **Cancel** button and support **Esc**. If
  interrupting may have side effects, label the button **Stop** instead of Cancel.
- Put progress indicators in consistent locations in windows/dialogs so users know where to check (Mail puts the
  asynchronous indicator at the far right of the To field).
- There are three types: determinate bar, indeterminate bar, asynchronous spinner.

**Determinate progress bar.**
- Use when the full operation length can be determined and you can tell the user how much is complete.
- Progress must accurately associate with time. A bar that reaches 90% in 5 seconds but needs 5 minutes for the
  last 10% is a defect.
- The fill moves left to right and should fill completely before dismissal. Minimum/maximum values are
  developer-controlled.
- An optional complete/partial-sentence label may explain the context; sentence-style capitalization.
- Regular and small sizes; height fixed, length variable. Figure 15-56 shows active and inactive fill.
- Implementation: `NSProgressIndicator`, bar style, indeterminate off.

**Indeterminate progress bar.**
- Use when the duration cannot be determined. If the duration becomes known, switch to a determinate bar.
- Works best in a dialog/window focused on the process. If the process is associated with a control or space is
  limited, use the asynchronous indicator instead.
- Displays a spinning striped cylinder; the system supplies the appearance.
- Optional label may end with an ellipsis to emphasize ongoing processing; sentence-style capitalization.
- Regular and small sizes; height fixed, length variable.
- Implementation: `NSProgressIndicator`, bar style, indeterminate on.

**Asynchronous progress indicator.**
- Use when space is very constrained (in a text field or near a control) and for background/asynchronous events
  such as retrieving mail.
- Do **not** use it for a process that starts indeterminate but may become determinate: the determinate bar is a
  different shape and takes much more space. Use an indeterminate bar instead.
- A label is usually unnecessary; if provided, it should briefly describe the process, use sentence-style
  capitalization, and may end with an ellipsis.
- Regular, small, mini.
- Implementation: `NSProgressIndicator`, spinning style, indeterminate on.

**Test checks.** Cancel returns to the prior state; Stop is used when cancellation has side effects; Esc maps to
Cancel/Stop; determinate fill never regresses or stalls at 90%; a type switch from indeterminate to determinate
keeps the same bar shape.

### Level indicators (pp. 316-321)

A level indicator shows the level or amount of something and can change color near critical values. Three
styles: capacity, rating, relevance.

**Capacity indicators.**
- Show a finite capacity with well-defined min/max (storage space, battery charge). Useful in dialogs and
  preference windows viewed briefly.
- **Continuous:** translucent track filled with a colored bar; fine-grained.
- **Discrete:** a row of equal rectangular segments equal to the maximum value; rounded to the nearest integer,
  segments uniformly stretched/shrunk, and each segment is completely filled or empty. Better for coarse values.
- Default fill is **green**. A warning level turns it **yellow**; a critical level turns it **red**.
- Critical orientation: if critical > warning, green below warning, yellow between, red above (approaching
  maximum, such as storage). If critical < warning, red below critical, yellow between, green above (approaching
  minimum, such as battery end).
- Tick marks may be shown above/below. Use ticks only on the **continuous** style; the discrete segments already
  provide scale context. If segments would be too small, use continuous instead.
- Label at least the first and last tick marks.
- Regular size only; bar/segment height **16 px**; width developer-controlled. Tick labels use label font,
  placed **3 px** below the lower edge of the ticks.
- Implementation: `NSLevelIndicator`, discrete or continuous capacity style.

**Rating indicators.**
- Show a number of stars corresponding to an item's rating; most useful in a list/table with many items because
  it conveys relative ranking.
- You can let users set ranking criteria or make the indicator editable to increase/decrease an item's rating.
- Default is stars; a custom image may replace them. No partial stars: the value is rounded to the nearest
  integer. Stars are not stretched or shrunk to fit, and no space is added between them.
- Implementation: `NSLevelIndicator`, rating style.

**Relevance indicators.**
- Show the relevance of items such as search results; especially useful in a list/table because relevance is
  easier to judge by comparison across items.
- Implementation: `NSLevelIndicator`, relevancy style.

**Test checks.** Capacity color thresholds match the configured warning/critical orientation; discrete segments
are never partially filled; rating shows whole stars only; relevance values are comparable across rows.

## Text controls (pp. 321-329)

These controls display text or accept text input. They are for the window body only; the single exception is
the search field, which may also be used in a toolbar. The combo box is covered under selection controls
(p. 295). (p. 321)

### Text controls at a glance

| Control | Use when | Avoid when | Core metrics |
| --- | --- | --- | --- |
| Static text field | Informational text the user should not edit | The text is a label for an adjacent control (use that control's label) | System/small/mini system font |
| Text input field | Collecting text from the user | Combining a text field with a menu by hand (use a combo box) | Height 22/19/15 px; label gap 8/6/5 px; stack gap 10/8/8 px |
| Token field | Address-like input that should become discrete tokens | Free-form prose | Token height 16/14/11 px |
| Search field | Searching within the application | A full search-results browser without a field | Height 22/19 px |
| Scrolling list | An arbitrarily large list of items to choose from | A small, fixed set of choices (use a pop-up menu) | Full line height; scroll one element |

### Static text fields (pp. 321-322)

**Purpose.** Informational text not intended to be modified by the user, in a dialog or window. States: active
and dimmed.

**Usage.** When it provides an obvious benefit, static text should be **selectable** so users can copy it: error
messages, serial numbers, IP addresses, and similar values.

**Specifications.** System font, small system font, or mini system font depending on the layout (Figure 15-69).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSTextField`.

**Test checks.** Non-editable; selectable only where copying is useful; dimmed state is legible and distinct.

### Text input fields (pp. 322-325)

**Purpose.** A rectangular field in which the user enters or modifies text. It can be active or disabled,
supports keyboard focus, and supports password entry.

**Usage.**
- Use to get information from the user, and perform appropriate edit checks.
- If a field accepts only digits, an application should alert when the user types anything else.
- Check data when the user clicks outside the field or presses **Return, Enter, or Tab**.
- Do **not** create a text field plus a menu by hand to offer choices; use a combo box.

**Contents and labeling.**
- Contains user-supplied text in a system font appropriate to the control size.
- A text input field can contain a **token field** control.
- Display an introductory label to explain the expected information; generally use **title-style
  capitalization**.
- Disabled state: use the system rendering; the label and field should read as unavailable.

**Specifications.**
- Heights: **22 / 19 / 15 px** (regular/small/mini).
- Width: long enough for the average expected input; multiple fields in one window should all be the same
  length.
- Intro-label gap: **8 / 6 / 5 px** from the colon to the field.
- Vertical stack spacing: at least **10 / 8 / 8 px**.
- Focus/insertion/selection appearances are shown in Figure 15-71; selection behavior follows "Selections in
  Text" (p. 115).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSTextField`.

**Test checks.** Edit check fires on blur, Return, Enter, and Tab; password entry masks characters; disabled
field cannot receive focus; all same-row fields share a width.

### Token fields (pp. 325-326)

**Purpose.** A control that turns input text into a token, similar to the Mail address field.

**Interaction.**
- As the user types, text completion is invoked after a developer-specified delay.
- Typing a comma or pressing **Return** or **Enter** transforms the preceding input into a token.
- A token is draggable. If the app supports a token menu, the token shows a disclosure triangle; pressing or
  clicking it reveals a contextual menu with information and token actions (Mail shows the address and
  Address Book actions).
- Figure 15-72 shows selected token, keyboard replacement, pre-commit input, and hover states.

**Specifications.** Fits inside the standard text input field sizes. Heights: **16 / 14 / 11 px**
(regular/small/mini); length follows the token.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSTokenField`.

**Test checks.** Comma/Return/Enter all commit a token; completion delay is configurable; token drag carries
the represented object; token menu appears only when implemented; backspace edits the token as specified.

### Search fields (pp. 326-328)

**Purpose.** A text field with rounded ends for entering or modifying search terms.

**Usage.**
- Use to search for terms within the application.
- Support keyboard focus. If searching is important, provide **Command-Option-F** to focus the search field
  without the mouse.
- The search may begin as soon as the user types, or when the user presses Return/Enter.
- A search field may be used in a toolbar (one of the three window-body controls allowed there).

**Contents and labeling.**
- Default: magnifying-glass icon at the left edge.
- Optional stop/clear icon if the user must click a button or press a key to start the search, especially if the
  search may take more than a second or two. Consider a progress indicator for lengthy searches.
- A menu may choose search types or scope, but **do not show search history** in it for privacy reasons;
  consider a scope bar instead.
- No introductory label is needed because users recognize the control. In a toolbar, supply the customization
  label **"Search"** for icon+text/text-only modes.

**Specifications.** Regular and small; heights **22 / 19 px**; length developer-controlled (Figure 15-75).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSSearchField`.

**Test checks.** Command-Option-F focuses the field; typing or Return starts search per the chosen mode; stop
icon cancels; no recent-search history is exposed; toolbar customization shows "Search".

### Scrolling lists (pp. 328-329)

**Purpose.** A list that uses scroll bars to reveal its contents.

**Interaction.**
- Scroll without selecting; click to select; **Shift-click** for a contiguous range; **Command-click** for a
  discontinuous selection.
- Arrow keys navigate; typing the first few characters performs type-ahead selection.
- The Finder's column-view columns behave as scrolling lists (Figure 15-81).

**Usage.**
- Use for an arbitrarily large number of items from which users choose.
- Do not use for a limited range of choices; a scrolling list may hide items and obscure the scope. Use a pop-up
  menu for a limited set.
- The list is not directly editable, but the app can provide editing that feeds items into it.

**Contents and labeling.**
- Long items get a **middle ellipsis**, preserving the beginning and end (version numbers often sit at the end).
- Background may be white or white with blue stripes; stripes help when many items look similar.
- Provide an introductory label in the regular system font; list items use the **view font (12-point Lucida
  Grande Regular)** by default.

**Specifications.** Developer-controlled size. Show full lines of text (do not clip horizontally); the scrolling
increment is one list element.

**Implementation (Mac OS X 10.6 AppKit; historical).** Start with `NSTableView`; size it so only the vertical scroller shows; set one column and
deselect Headers.

**Test checks.** Shift/Cmd selection semantics; type-ahead; middle ellipsis; one-element scroll increment; no
horizontal clipping.

## View controls (pp. 329-341)

These controls modify how information is presented in a window, or provide a frame for organizing and displaying
data. They are for the window body only. (p. 329)

### View controls at a glance

| Control | Use when | Avoid when | Core metrics |
| --- | --- | --- | --- |
| Disclosure triangle | Revealing more detail in a minimal/expanded dialog, or subordinate items in a hierarchy | Showing choices tied to a specific control (use a disclosure button) | 13×13 px |
| Disclosure button | Expanding a dialog/panel for choices related to a specific selection control | General window detail (use a triangle) | Align with the affected control |
| List view | Items plus multiple attributes in columns | Only a simple list of names (use a scrolling list) | One sort column; headers are short noun phrases |
| Column view | A deep hierarchy with one sort order | Flat data with attributes (use a list view) | No column headings; vertical scrollers between columns |
| Split view | Two or more resizable content views | Mixed vertical and horizontal subviews in one split view | 1 px zero-width or 9 px thick splitter |
| Tab view | A small number of panes in one place | More tabs than fit; multiple rows | 2-6 tabs; height 20/17/15 px |

### Disclosure triangles (pp. 329-331)

**Purpose.** Reveals information or functionality associated with primary information in a window.

**Usage.**
- Use in dialogs with a minimal and an expanded state (Figure 15-76), or to reveal subordinate items in a
  hierarchical list (Figure 15-80).
- Do **not** use a disclosure triangle for additional choices associated with a specific control such as a
  pop-up menu; use a disclosure button.

**Contents and labeling.**
- Closed by default (pointing right). Clicking points it down and displays the additional information.
- In dialogs, label what is disclosed or hidden; ideally the label changes, for example "Show advanced settings"
  when closed and "Hide advanced settings" when open.

**Specifications.** One size: **13×13 px** (Figure 15-77).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSButton` with bezel style `NSDisclosureBezelStyle`, button type
`NSPushOnPushOffButton`.

**Test checks.** Default closed; label toggles with state; disclosure does not act as a selection control.

### Disclosure buttons (pp. 331-332)

**Purpose.** Expands a dialog or panel to offer a wider range of choices related to a specific selection
control, such as a pop-up menu, combo box, or command pop-down menu. The minimal Save dialog is the canonical
example: the disclosure button reveals the file system without leaving the dialog.

**Usage.** Use only for additional options closely related to a specific list of choices. For general window
detail or hierarchical lists, use a disclosure triangle.

**Contents and labeling.** No label; the association with the adjacent control is the label. Closed by default
(pointing **down**); clicking expands the window and points it **up**.

**Specifications.** Align the button with the pop-up or other list-based control it affects, and place it close
enough to make the relationship clear.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSButton` with bezel style `NSRoundedDisclosureBezelStyle`, button type
`NSPushOnPushOffButton`.

**Test checks.** Closed points down; open points up; expansion preserves the nearby control's alignment; no
standalone use.

### List views (pp. 333-334)

**Purpose.** Displays ordered records in a table. Columns represent attributes and can be resized, rearranged,
and sometimes added or removed. The leftmost column shows all objects, including those contained in others when
the data is hierarchical; revealing hidden objects lengthens the list, and other columns shift right but keep
their headings and order.

**Usage.**
- Use when items need multiple attributes. If only names are shown, use a scrolling list.
- Sort rows by the selected column heading. Only one column is selected at a time; clicking an already selected
  heading toggles the sort direction. Secondary sorting may happen behind the scenes.
- Items may be editable depending on the app; Finder list view edits only the Name column.

**Contents and labeling.**
- Disclosure triangles may reveal a hierarchy, but only in **one column**.
- Column headers are **nouns or short noun phrases** describing the attribute.
- Icons are usually integral to the data items. Prefer an attributes column with text over icon-only columns.
- Selection follows standard list behavior: click, Shift-click for a range, Command-click for a discontinuous
  selection, arrow-key navigation, and type-ahead.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSTableView`; use `NSOutlineView` in column format for disclosure triangles.

**Test checks.** One active sort column; clicking it reverses direction; hierarchy appears in only one column;
headers are short noun phrases.

### Column views (pp. 334-336)

**Purpose.** Views and selects items from an organized hierarchy. Clicking an object reveals its descendants in
a column to the right; each column shows only descendants of the item selected in the previous column. A leaf
selection may show details in the rightmost column.

**Usage.**
- Use when there is only one way the data can be sorted, or when only one sort order should be presented.
- Useful for a deep hierarchy such as a file system where users move back and forth among levels.
- Show the root level in the leftmost column. As users select items, focus moves right; a terminal object may
  show additional information.
- Columns are usually resizable. Each pair of columns has a vertical scroll bar; a horizontal scroll bar runs
  along the bottom.

**Contents and labeling.**
- **No disclosure triangles.** The triangle beside an item only indicates that the item contains other objects;
  clicking anywhere in the row reveals them.
- **No column headings**; a column is a hierarchy node, not an attribute of every object.
- A label is not required, but showing the current position helps; Finder uses the parent object's name as the
  window title.
- Icons are usually integral to the items.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSBrowser`, or `NSOutlineView` in column format.

**Test checks.** Root in the leftmost column; each column contains only the previous selection's descendants;
no column headings; triangle is an indicator, not a disclosure control; horizontal and per-pair vertical
scrollers exist.

### Split views (pp. 336-338)

**Purpose.** Groups two or more views and lets the user adjust their relative width or height. A split view with
five subviews has four splitters.

**Specifications.**
- Zero-width splitter: **1 px** wide (the standard in 10.5+); the pointer changes to a move/resize pointer when
  hovering, depending on the allowed direction.
- Thick splitter: **9 px** wide, less common, with a circular dimple at its midpoint.
- Horizontal splitter stacks views; vertical splitter places them side by side.
- The whole splitter is a hot zone. For zero-width splitters, the hot zone includes **2 px on both sides**.

**Interaction.**
- Drag anywhere on the splitter to resize.
- If a **wide** splitter is dragged to the edge (or the next splitter), the subview disappears but the splitter
  stays visible to show where the subview is and make it easy to restore.
- A **zero-width** splitter does not remain visible when dragged far enough to hide the subview. Define minimum
  and maximum subview sizes so users cannot lose it, or provide a button that reopens the subview.

**Usage.** Use for two or more content views the user can resize. A single split view does not mix vertical and
horizontal subviews; one window may contain multiple split views with different orientations (Automator,
Figure 15-83).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSSplitView`; choose Thick/Thin divider in Interface Builder.

**Test checks.** Pointer changes across the entire hot zone; thick splitter remains after collapsing; zero-width
splitter has min/max or a restore button; no mixed orientation in one split view.

### Tab views (pp. 338-341)

**Purpose.** Presents information in a multipane format. Tabs are centered across the top of a content area;
clicking a tab shows its attached pane.

**Usage.**
- Use for a small number of different content views in one place. Depending on window size, use **2 to about 6
  tabs**.
- A pane's controls affect only the objects in that pane, not the rest of the window.
- Two placements:
  - **Extend** the sides and bottom to the window edges; the tabs manage the entire window-body area below the
    tab control.
  - **Inset** the tab view, leaving a margin of window body on all sides; use this when global controls below
    the tab view affect the whole window.
- Multiple rows of tabs are **not supported**.
- If there are too many tabs, a pop-up menu at the top of a group box is acceptable but not recommended; a
  segmented control is another alternative, but it is not attached to the panes.

**Contents and labeling.**
- Each tab needs a label describing its pane. Nouns or very short noun phrases are best; a verb/short verb
  phrase may fit some contexts.
- Tab labels use **title-style capitalization**.
- Panes may contain standard window-body controls, icons, and static text.

**Specifications.**
- Tab heights: **20 / 17 / 15 px** (regular/small/mini).
- Label margins inside the tab: **12 / 10 / 8 px** on each side; center the label.
- Place the top edge of the tab view **12 or 14 px** below the title bar (or toolbar).
- Inset style: **20 px** margin from the window sides and bottom; **16 px** is also acceptable.
- With controls below the tab view: controls sit **20 px** above the window bottom, with **12 px** between the
  tab view and the controls.
- Extended style: keep at least **20 px** between the pane content and the tab-view edges.
- Pop-up menu used instead of tabs: center it along the top of the group box (Figure 15-87).

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSTabView`.

**Test checks.** 2-6 tabs; single row; selected tab matches visible pane; pane controls do not affect other
panes; inset/extended margins match the chosen style.

## Grouping controls (pp. 341-345)

Grouping controls visually group other controls so users can distinguish logical collections. There are two
types: separators and group boxes. (p. 341)

### Grouping controls at a glance

| Control | Weight | Use when | Avoid when | Core metrics |
| --- | --- | --- | --- | --- |
| Separator | Light | Dividing a window body into categories/subgroups | Spanning the whole window; toolbar separation (use `NSToolbarSeparatorItem`) | ≥10 px from other controls; label 2 px from start |
| Group box | Heavy | A pronounced logical grouping of controls | Nesting; use a separator or white space instead | ≥20 px from window edge |

### Separators (pp. 342-344)

**Purpose.** A thin vertical or horizontal line with a lightweight appearance, good for separating controls into
categories or subgroups.

**Usage.**
- Place vertically or horizontally according to the window layout.
- Avoid stretching a separator across the entire width/height of a window; it can look like it slices the window
  into unrelated rows/columns. If categories are completely unrelated, consider a tab view instead.
- The separator control is not used in a toolbar; a toolbar's vertical separator is an
  `NSToolbarSeparatorItem`.

**Contents and labeling.**
- A label is optional. If present, use **title-style capitalization**, and place the separator line at the
  **base of the text**.
- Label font matches the surrounding controls: system font for regular controls, small system font for small,
  mini system font for mini.
- The label sits **2 px** from the beginning of the separator control.

**Specifications.**
- Single thickness; developer-controlled length.
- At least **10 px** away from other controls.
- Both ends equally distant from the window edges.
- Multiple separators with the same orientation must be the same length.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSBox`.

**Test checks.** Separator does not span the full window; labels sit on the line's base; spacing and length are
consistent across same-orientation separators.

### Group boxes (pp. 344-345)

**Purpose.** Breaks a window into distinct logical areas with a heavier look than a separator, giving a more
pronounced differentiation of content.

**Usage.**
- Use for logical groupings of controls in the window body, including inside tab-view panes.
- Avoid nesting group boxes: nesting wastes space and makes boundaries hard to perceive. Use a separator or
  white space inside a group box instead.
- Strive for roughly equal numbers of controls in each group box for visual balance.

**Contents and labeling.**
- Group boxes may be untitled or titled. Titles may be text-only, a checkbox, or a pop-up menu.
- If the title is a checkbox, the items in the group box are active **only when the checkbox is selected**.
- Group-box titles use **sentence-style capitalization**.

**Specifications.**
- No standard sizes; developer controls the boundaries.
- Default title font: **small system font**; another size may be used if it coordinates with the window.
- Leave at least **20 px** from the group-box edge to the window edge.
- If nesting is unavoidable, see "A Changeable Pane Dialog" (p. 350) for spacing guidance.

**Implementation (Mac OS X 10.6 AppKit; historical).** `NSBox`.

**Test checks.** No nested group boxes unless documented; checkbox title enables/disables the entire contents;
title uses sentence-style capitalization; 20 px window margin.

## Implementation implications

### What the 2009 source says (requirements for Mac OS X apps)

- Use system-provided controls rather than custom ones; their behavior and accessibility come for free and
  track OS updates (p. 255).
- Sizes are regular/small/mini only; most windows should use regular. Do not vertically resize controls
  (pp. 255, 265).
- Controls in this chapter belong in the window body; only icon buttons, action menus, and search fields are
  also allowed in window-frame areas (p. 265).
- An indeterminate action dims its button and shows progress feedback; opposing actions use two buttons rather
  than one dual-purpose button (p. 265).
- Return/Enter activates the default button; pressing a nondefault button gives it color and removes the
  default's color (p. 268).

### Historical Mac OS X 10.6 implementation detail (not a recreation requirement)

- AppKit classes named in each component section (`NSButton`, `NSSegmentedControl`, `NSTextField`,
  `NSTableView`, …) and Interface Builder instructions describe how Apple expected these controls to be built in
  2009. They explain the source's vocabulary; they do not bind a non-AppKit recreation.
- `NSTexturedRoundedBezelStyle`, `NSMomentaryPushInButton`, `NSActionTemplate`, and similar names are recorded
  only so the 2009 look can be identified.

### Interpretation

- The durable design rules are the *behavioral* ones: fixed-height sizes, no vertical stretching, immediate
  action vs. state, default-button semantics, and consistent spacing. Those can be implemented in any toolkit.
- The *visual* rules (bezel rendering, focus glow) are observable 10.6 appearance, not statements about
  geometry; where the HIG gives no number, the value must be measured from a capture rather than invented.

### Recreation-specific decisions / open questions

- **PENDING — control strategy:** native-host widgets vs. custom-drawn Aqua controls. The HIG's
  "use system-provided controls" advice assumes Mac OS X; the recreation's target platform is not yet fixed.
  Blocked by: target-platform decision. See [scope note](../notes/scope-and-evidence.md#how-to-treat-use-the-system-provided-control).
- **PENDING — fidelity target:** pixel-faithful 10.6 rendering, interaction-faithful (behavior/metrics), or
  terminology-only. Affects every control spec.
- **DECIDED — carry the measurements:** spacing/fidelity specs listed below are recorded as source-derived
  numbers regardless of strategy, because they are the measurable part of the guidance.
- **PENDING — control inventory:** which of these families the recreated app actually uses. See
  [component inventory](../notes/component-inventory.md).

### Measurements to carry into any implementation

- Push button spacing 12/10/8 px (regular/small/mini); slider spacing 12/10/8; stepper-to-text-field 2/2/1 px;
  group box ≥20 px from the window edge; separator ≥10 px from controls; tab label margins 12 px per side
  (regular, system font) (pp. 269, 305-310, 344-345, 338-341).

## Assets / examples to capture later

- [ ] Capture figures: Table 15-1 (window-frame control states, p. 256); Figures 15-1 through 15-11 (toolbar
      controls, buttons, icon buttons); Figures 15-48 through 15-60 (sliders, steppers, progress indicators);
      Figures 15-61 through 15-68 (capacity, rating, relevance indicators); Figures 15-69 through 15-75 (text
      controls); Figures 15-76 through 15-87 (disclosure, lists, tabs); Figures 15-88 through 15-90 (separators,
      group boxes).
- [ ] Capture control screenshots from `../images/` (e.g. System Preferences panes) for fidelity reference.
      See the [image inventory](../notes/image-inventory.md) for the exact rows and the capture matrix of
      missing regular/small/mini, mixed, disabled, focus, and warning/critical states.

## Open questions / follow-up extraction

- [ ] Which control families does the app being recreated actually use? See the pending control-inventory
      decision above and [component inventory](../notes/component-inventory.md).
- [ ] Native-host vs. custom-drawn control strategy (see recreation decisions above).
- [ ] Which window-frame controls (toolbar, bottom bar) does the recreation need in addition to the window-body
      controls documented here? See "Window-Frame Controls" (pp. 255-264) for the source specs.
- [ ] Hover/pressed artwork is not specified in the HIG for most window-body controls; measure from 10.6
      captures before implementing those states.

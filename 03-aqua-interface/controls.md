# Controls

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 255
- **Status:** Reviewed

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
  - Column Views (p. 335)
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
  single setting ("Choose Picture…" not "Choose…"); no "now" needed; ellipsis when action opens another window
  (e.g. Mail preferences opens .Mac preferences). Default button = safe action in dialog, Return/Enter
  activates; when user presses nondefault (e.g. Cancel), it acquires color and default loses color; system-
  provided buttons handle this automatically.
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

- p. 280+ — Selection controls: radio buttons, checkboxes, segmented controls, pop-up menus, combo boxes, path
  controls, color wells, image wells, date pickers, command pop-down menus, sliders, steppers, placards
  (grouped in the chapter; detailed source notes to be expanded as each sub-section is fully read).
- p. 310+ — Indicators: progress (determinate/indeterminate/asynchronous), level (capacity/rating/relevance),
  rating, relevance — for status feedback, capacity warnings, user ratings, search relevance.
- p. 321+ — Text controls: static text (informational, selectable in some cases), text input fields (edit checks
  on exit/Return/Tab; don't use text field+menu together — use combo box; heights 22/19/15; label spacing),
  token fields (completion after delay; comma/Return/Enter transforms input into token; token draggable; token
  menu with disclosure triangle), search fields (rounded ends; Command-Option-F focus shortcut; immediate or
  Return-triggered search; magnifying glass + stop-search icons; toolbar labels need "Search"; sizes 22/19),
  scrolling lists (Shift-click range, Command-click discontinuous, arrow-key nav, type-ahead; ellipsis in middle
  of long items preserving beginning/end).
- p. 329–341 — View controls: disclosure triangles (13×13 px; closed points right; open down; label changes,
  e.g. "Show advanced settings"↔"Hide advanced settings"; use disclosure button for control-associated options,
  not triangle); disclosure buttons (closed points down; use disclosure button for options closely related to a
  control like pop-up/combo); list views (sort by selected column; click selected column toggles direction;
  NSOutlineView for hierarchies; short noun-phrase column headers); column views (focus moves right on selection;
  Finder file hierarchy example); split views (zero-width 1 px splitter or thick 9 px; hot zone; subview hiding
  rules); tab views (2–6 tabs; tab height 20/17/15; labels nouns/short phrases, title-style capitalization;
  extend vs. inset styles; pane semantics); grouping controls: separators (light, vertical/horizontal, ≥10 px
  from other controls, label at base of text, system/small/mini font depending on controls), group boxes (heavier,
  untitled/titled, checkbox titles activate items, sentence-style title capitalization, ≥20 px from window edge,
  avoid nesting).
- p. 342–345 — Group boxes: use for logical grouping; avoid nesting (use separator/white space instead).

## Implementation implications

- Retro recreation should use system-provided controls where the recreation runs on a Mac-like platform; avoid
  custom control implementations except where the target era/platform lacks them.
- Control inventory for the recreation: push buttons, icon buttons, bevel buttons, gradient buttons, toggle/
  segmented toolbar controls, scope buttons, pop-up menus, combo boxes, path controls, color wells, image wells,
  date pickers, sliders, steppers, disclosure triangles/buttons, list views, column views, split views, tab
  views, separators, group boxes, progress/level/rating/relevance indicators, static/text/token/search/scrolling
  lists.
- Spacing/fidelity specs to carry into implementation: push button spacing 12/10/8 px (regular/small/mini);
  slider control spacing 12/10/8; stepper-to-text-field 2/2/1 px; group box ≥20 px from window edge; separator ≥10 px
  from controls; tab label margins (12 px each side regular, system font).
- Behavior: indeterminate process → dim + feedback; opposing functions → separate buttons; immediate action
  semantics (Return activates default); destructive action spacing from safe actions.

## Assets / examples to capture later

- [ ] Capture figures: Table 15-1 (window-frame control states, p. 256); Figures 15-1 through 15-11 (toolbar
      controls, buttons, icon buttons); Figures 15-48 through 15-60 (sliders, steppers, progress indicators);
      Figures 15-61 through 15-68 (capacity, rating, relevance indicators); Figures 15-69 through 15-75 (text
      controls); Figures 15-76 through 15-87 (disclosure, lists, tabs); Figures 15-88 through 15-90 (separators,
      group boxes).
- [ ] Capture control screenshots from `../images/` (e.g. System Preferences panes) for fidelity reference.

## Open questions / follow-up extraction

- [ ] Read remaining sub-section source notes in full (selection controls p. 280–310, indicators p. 310–321,
      text controls p. 321–328, view controls p. 329–341, grouping p. 341–345) so this chapter has complete
      source notes rather than an outline-level pass.
- [ ] Which control families does the app being recreated actually use? (Cross-reference with feature list.)
- [ ] Should the recreation implement custom controls at all, or only system-provided ones?

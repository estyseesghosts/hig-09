# Retro Recreation — Component / Pattern Inventory

Derived from HIG chapters reviewed so far (Parts I–III, Reference). Target: components the retro recreation
should implement or emulate.

**Spec status:** controls with a `controls.md` link have source-backed purpose, usage, metrics, states, and
test checks. Unlinked entries are still at source-note level. Page numbers refer to the printed HIG pages.

## Window types

- [ ] Document windows (naming: untitled, untitled 2; untitled naming p. 217, 247; save/close/quit dialogs p. 246–251)
- [ ] Application windows
- [ ] Panels (inspector, transparent, fonts/colors windows, About windows p. 227–235)
- [ ] Dialogs / alerts (types p. 235; sheets p. 236; alerts p. 237; appearance/behavior p. 240; dismissing p. 241;
      Apply button p. 242; expanded dialogs p. 242)
- [ ] Find windows (p. 243)
- [ ] Preferences windows (p. 243; resize/minimize clarifications p. 243)

## Menu bar

- [ ] Apple menu; Application menu (About, Preferences…, Services, Hide, Hide Others, Show All, Quit; title
      rules p. 177–179); File menu (New, Open, Open Recent, Close, Close File, Save, Save As, Export As, Save
      All, Revert to Saved, Print, Page Setup); Edit menu (Undo, Redo, Cut, Copy, Paste, Paste and Match Style,
      Delete, Select All, Find, Find Next, Spelling, Speech, Special Characters); Format menu (Show Fonts,
      Show Colors, Bold, Italic, Underline, Bigger, Smaller, Copy/Paste Style, Align, Ruler); View menu
      (Show/Hide Toolbar, Customize Toolbar); Help menu (p. 187); Window menu (Minimize, Zoom, Minimize All,
      Bring All to Front, Arrange in Front, open docs p. 186); Application-specific menus (between View and
      Window, p. 186); Menu Bar Extras (p. 188); contextual menus (p. 188); Dock menus (p. 190).

## Controls (window-body)

- [ ] Push buttons (text-only; verb labels; default button behavior; spacing p. 265–269; source notes in
      `controls.md`)
- [ ] Bevel buttons (image + text or menu; toolbar/bottom-bar use p. 277)
- [ ] Icon buttons (toolbar; hit target 10px margin, icon 24–32px; labels p. 269)
- [ ] Round buttons (Help button, etc. p. 276–279)
- [ ] Gradient buttons (source-list-related actions p. 273–276)
- [ ] Segmented controls (toggle-like behavior; iCal bottom bar p. 286) —
      [spec](../03-aqua-interface/controls.md#segmented-controls-pp-286-288), p. 286–288
- [ ] Icon/bevel button with pop-up menu —
      [spec](../03-aqua-interface/controls.md#icon-buttons-and-bevel-buttons-with-pop-up-menus-p-288), p. 288
- [ ] Scope buttons (recessed + round rectangle for scope bars p. 271–273)
- [ ] Sliders (linear/circular; tick marks; specs p. 305–309) —
      [spec](../03-aqua-interface/controls.md#sliders-pp-305-309), p. 305–309
- [ ] Stepper controls (p. 309–310) —
      [spec](../03-aqua-interface/controls.md#stepper-controls-pp-309-310), p. 309–310
- [ ] Pop-up menus (p. 289–293) —
      [spec](../03-aqua-interface/controls.md#pop-up-menus-pp-289-293), p. 289–293
- [ ] Combo boxes (p. 295) —
      [spec](../03-aqua-interface/controls.md#combo-boxes-pp-295-298), p. 295–298
- [ ] Action menus (p. 293) —
      [spec](../03-aqua-interface/controls.md#action-menus-pp-293-295), p. 293–295
- [ ] Command pop-down menus (p. 303–305) —
      [spec](../03-aqua-interface/controls.md#command-pop-down-menus-pp-303-305), p. 303–305
- [ ] Date pickers (p. 301–303) —
      [spec](../03-aqua-interface/controls.md#date-pickers-pp-301-303), p. 301–303
- [ ] Path controls (p. 298) —
      [spec](../03-aqua-interface/controls.md#path-controls-pp-298-300), p. 298–300
- [ ] Color wells (p. 300) —
      [spec](../03-aqua-interface/controls.md#color-wells-and-image-wells-pp-300-301), p. 300–301
- [ ] Image wells (p. 300) —
      [spec](../03-aqua-interface/controls.md#color-wells-and-image-wells-pp-300-301), p. 300–301
- [ ] Radio buttons (p. 280–283) —
      [spec](../03-aqua-interface/controls.md#radio-buttons-pp-280-283), p. 280–283
- [ ] Checkboxes (p. 283–286) —
      [spec](../03-aqua-interface/controls.md#checkboxes-pp-283-286), p. 283–286
- [ ] Placards (p. 310) —
      [spec](../03-aqua-interface/controls.md#placards-p-310), p. 310

## Indicators / feedback

- [ ] Progress indicators: determinate, indeterminate, asynchronous —
      [spec](../03-aqua-interface/controls.md#progress-indicators-pp-311-316), p. 311–316
- [ ] Capacity indicators: continuous and discrete —
      [spec](../03-aqua-interface/controls.md#level-indicators-pp-316-321), p. 316–321
- [ ] Rating indicators —
      [spec](../03-aqua-interface/controls.md#level-indicators-pp-316-321), p. 319
- [ ] Relevance indicators —
      [spec](../03-aqua-interface/controls.md#level-indicators-pp-316-321), p. 320

## Text / input

- [ ] Static text fields (p. 321) —
      [spec](../03-aqua-interface/controls.md#static-text-fields-pp-321-322), p. 321–322
- [ ] Text input fields (p. 322–325) —
      [spec](../03-aqua-interface/controls.md#text-input-fields-pp-322-325), p. 322–325
- [ ] Token fields (p. 325–326) —
      [spec](../03-aqua-interface/controls.md#token-fields-pp-325-326), p. 325–326
- [ ] Search fields (p. 326–329) —
      [spec](../03-aqua-interface/controls.md#search-fields-pp-326-328), p. 326–328
- [ ] Scrolling lists (p. 328–329) —
      [spec](../03-aqua-interface/controls.md#scrolling-lists-pp-328-329), p. 328–329

## View controls

- [ ] Disclosure triangles (p. 329–331) —
      [spec](../03-aqua-interface/controls.md#disclosure-triangles-pp-329-331), p. 329–331
- [ ] Disclosure buttons (p. 331–332) —
      [spec](../03-aqua-interface/controls.md#disclosure-buttons-pp-331-332), p. 331–332
- [ ] List views (p. 333–334) —
      [spec](../03-aqua-interface/controls.md#list-views-pp-333-334), p. 333–334
- [ ] Column views (p. 334–336) —
      [spec](../03-aqua-interface/controls.md#column-views-pp-334-336), p. 334–336
- [ ] Split views (p. 336–338) —
      [spec](../03-aqua-interface/controls.md#split-views-pp-336-338), p. 336–338
- [ ] Tab views (p. 338–341) —
      [spec](../03-aqua-interface/controls.md#tab-views-pp-338-341), p. 338–341

## Grouping controls

- [ ] Separators (p. 342–344) —
      [spec](../03-aqua-interface/controls.md#separators-pp-342-344), p. 342–344
- [ ] Group boxes (p. 344–345) —
      [spec](../03-aqua-interface/controls.md#group-boxes-pp-344-345), p. 344–345

## Input / interaction behaviors

- [ ] Mouse: click, double-click, press-and-hold, drag (p. 97–98)
- [ ] Keyboard: reserved vs recommended shortcuts, focus/navigation, type-ahead, key-repeat (p. 99-111; full
      Table A-1 reference in `04-reference/appendix-a-keyboard-shortcuts.md`)
- [ ] Selection: methods, text/spreadsheet/graphics (p. 112–117)
- [ ] Text editing: insert/delete/replace, intelligent cut/paste, passwords (p. 117–120)
- [ ] Drag and drop: semantics, feedback, destinations, clippings (p. 121–127)
- [ ] Pointers: standard cursors, hot spot/hot zone, custom pointers (p. 161–163)

## Window-frame controls

- [ ] Toolbar controls: rectangular-style, capsule-style, legacy (p. 255–265)
- [ ] Bottom bar controls (p. 212, 257, 365)

## Dialogs / sheets

- [ ] Save dialogs, Open dialogs, Choose dialogs, Print dialogs, Page Setup, alerts, sheets (p. 235–254)

## Layout

- [ ] Positioning: center equalization, spacing metrics, small/mini control layouts, grouping, bottom bars
      (p. 347–365)
- [ ] Bottom bars (p. 212, 213, 365)

## Assets / reference images

- [ ] Capture HIG figures (toolbar, buttons, progress, indicators, text controls, disclosure, lists, tabs,
      separators/group boxes, layout).
- [x] Catalogue every retained screenshot, its subject, dimensions, version evidence (known/unknown), and
      missing states in `notes/image-inventory.md`.
- [ ] Close the capture-matrix gaps: inactive windows, focus rings, mixed/disabled control states, sheets,
      inspectors, open menus, and capacity/rating/relevance indicators.

## Open items

- [ ] Which controls actually appear in the app being recreated (start with a minimal core set and expand).
- [ ] Custom vs system-provided control decision.
- [ ] Accessibility support (VoiceOver etc.) scope.

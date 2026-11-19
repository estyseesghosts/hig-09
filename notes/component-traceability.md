# Component Traceability Matrix

Links each component family to its chapter documentation, HIG pages, figures/retained assets, evidence status,
and a regression-test anchor. Specs exist for the seven-component vertical slice; the matrix also records the
families still at source-note level so the gap is explicit.

**Evidence status legend**

| Code | Meaning |
| --- | --- |
| **T** | HIG text is specific enough to write requirements |
| **M** | HIG gives numeric metrics |
| **F** | A HIG figure range documents appearance/usage |
| **C** | A retained 10.6 capture shows the component |
| **S** | A spec exists and has acceptance tests |

A component marked `T+M+F+C+S` has the strongest evidence; `T` alone means behavior is source-backed but
geometry and rendering are not.

## Core vertical slice (specified)

| Component | Spec | Chapter doc | HIG pages | Figures / retained assets | Evidence | Regression test example |
| --- | --- | --- | --- | --- | --- | --- |
| Push button | [CMP-01](../specs/push-button.md) | [Controls > Selection/buttons](../03-aqua-interface/controls.md#source-notes-with-page-refs) | 265-269, 241 | Fig 15-7 to 15-9; #8, #11, #17 | T+M(partial)+F+C+S | Return activates the default; destructive button is never default and is ≥24 px away |
| Toolbar item (rectangular) | [CMP-02](../specs/toolbar-item.md) | [Controls > Window-frame](../03-aqua-interface/controls.md#source-notes-with-page-refs) | 255-264 | Fig 15-1 to 15-6; #14, #19, #22, #33 | T+M(partial)+F+C+S | Bezel reflects window state while glyph reflects enabled state; 8 px spacing |
| Checkbox | [CMP-03](../specs/checkbox.md) | [Controls > Checkboxes](../03-aqua-interface/controls.md#checkboxes-pp-283-286) | 283-286 | Fig 15-23 to 15-25; #28, #29, #34 | T+M+F+C(partial)+S | Mixed dash on multi-object selection; dependent control disables with controller |
| Text input field | [CMP-04](../specs/text-input-field.md) | [Controls > Text input](../03-aqua-interface/controls.md#text-input-fields-pp-322-325) | 322-325 | Fig 15-70, 15-71; #7, #13 | T+M+F+C(partial)+S | Heights 22/19/15 px; validation on blur/Return, not per keystroke |
| Source list | [CMP-05](../specs/source-list.md) | [Windows > Source Lists](../03-aqua-interface/windows.md) | 208-212, 111 | Fig 14-22 to 14-24; #14, #20, #27, #33 | T+F+C(partial)+S | Blue only for a single primary list; max two hierarchy levels |
| Sheet | [CMP-06](../specs/sheet.md) | [Windows > Sheets](../03-aqua-interface/windows.md) | 236-237, 241-242 | Fig 14-46, 14-52; #7, #9, #13 (inferred) | T+F+C(inferred)+S | One sheet per window; Esc/Command-period cancel and restore focus |
| Menu item | [CMP-07](../specs/menu-item.md) | [Menus](../03-aqua-interface/menus.md) | 165-176, 131-132 | Fig 13-3 to 13-13; #15, #36 | T+F+C(partial)+S | Disabled items are not hover-highlighted; symbols use only defined meanings |

## Remaining inventory (source-note level unless noted)

| Component family | Chapter doc | HIG pages | Figures / assets | Evidence | Test anchor (from chapter) |
| --- | --- | --- | --- | --- | --- |
| Document/application windows | [Windows](../03-aqua-interface/windows.md) | 191-235 | #14, #19, #27, #37 | T+F+C | Window states, title/proxy rules |
| Panels (inspector, About) | [Windows](../03-aqua-interface/windows.md) | 227-235 | #12 | T+C(partial) | Panel vs. window behavior |
| Dialogs/alerts (app-modal) | [Windows](../03-aqua-interface/windows.md) | 235-254 | #8, #11, #17, #34 | T+F+C | Alert button order; default safety |
| Find/Preferences windows | [Windows](../03-aqua-interface/windows.md) | 243 | — | T | Non-modal behavior |
| Menu bar / menus | [Menus](../03-aqua-interface/menus.md) | 165-190 | Fig 13-1 to 13-25; #15, #36 | T+F+C(partial) | Menu composition; reserved shortcuts |
| Bevel buttons | [Controls](../03-aqua-interface/controls.md) | 277 | — | T | Image+text or menu behavior |
| Icon buttons | [Controls](../03-aqua-interface/controls.md) | 269-271 | #27, #33 | T+M+C | Hit target ≈10 px; icons 24-32 px |
| Round/gradient/scope buttons | [Controls](../03-aqua-interface/controls.md) | 271-279 | #19, #27 | T+F+C(partial) | Gradient-button placement at source-list bottom |
| Segmented controls | [Controls](../03-aqua-interface/controls.md) | 286-288 | #19, #21 | T+M+F+C | Equal segment widths; no icon/text mixing |
| Pop-up/action/command menus | [Controls](../03-aqua-interface/controls.md) | 288-295, 303-305 | — | T+M | Item inset/stacked gaps; action-menu placement |
| Combo boxes | [Controls](../03-aqua-interface/controls.md) | 295-298 | — | T+M | Stacked gap 12/10/8 |
| Path controls | [Controls](../03-aqua-interface/controls.md) | 298-300 | #32 | T+C | Path pop-up navigation |
| Color/image wells | [Controls](../03-aqua-interface/controls.md) | 300-301 | #28 | T+C | Drag target behavior |
| Date pickers | [Controls](../03-aqua-interface/controls.md) | 301-303 | — | T | Textual vs. graphical |
| Sliders | [Controls](../03-aqua-interface/controls.md) | 305-309 | #28, #35 | T+M+C | Height 19/14/11; spacing 12/10/8 |
| Steppers | [Controls](../03-aqua-interface/controls.md) | 309-310 | — | T+M | 2/2/1 px gap to text field |
| Placards | [Controls](../03-aqua-interface/controls.md) | 310 | — | T+M | 15 px high |
| Progress indicators | [Controls](../03-aqua-interface/controls.md) | 311-316 | #9, #25 | T+M+F+C(partial) | Determinate vs. indeterminate feedback |
| Capacity/rating/relevance | [Controls](../03-aqua-interface/controls.md) | 316-321 | — | T+M | Warning/critical color + redundant cue |
| Static text / token / search fields | [Controls](../03-aqua-interface/controls.md) | 321-328 | #18, #32 | T+M+F+C(partial) | Search-field cancel; token states |
| Scrolling lists | [Controls](../03-aqua-interface/controls.md) | 328-329 | #1, #14 | T+C | Full-row selection |
| Disclosure triangles/buttons | [Controls](../03-aqua-interface/controls.md) | 329-332 | #12, #32 | T+M+F+C(partial) | Expand/collapse keyboard parity |
| List/column/split/tab views | [Controls](../03-aqua-interface/controls.md) | 333-341 | #3, #5, #21, #31, #32 | T+M+F+C | Selection highlight levels; tab attachment |
| Separators / group boxes | [Controls](../03-aqua-interface/controls.md) | 342-345 | — | T+M | Group box 20 px from window edge |
| Mouse/keyboard/selection/text editing | [User Input](../03-aqua-interface/user-input.md) | 97-120 | — | T | Reserved shortcuts; focus order |
| Drag and drop | [Drag and Drop](../03-aqua-interface/drag-and-drop.md) | 121-127 | — | T | Drop feedback; Option semantics |
| Pointers | [Pointers](../03-aqua-interface/pointers.md) | 161-163 | — | T | Standard cursor meanings |
| Icons / icon genres | [Icons](../03-aqua-interface/icons.md) | 139-159 | #26, #33, #37 | T+F+C(partial) | Sizes and label rules |
| Layout metrics | [Layout](../03-aqua-interface/layout-guidelines.md) | 347-365 | #14, #27, #29 | T+M+C | Spacing/alignment rules |
| Save/Open/Choose/Print dialogs | [Windows](../03-aqua-interface/windows.md), [Installation](../02-macintosh-experience/software-installation-and-software-updates.md) | 235-254, 85-93 | #6, #7, #13, #32 | T+F+C | Default/cancel; destructive distance |

## Known evidence gaps that block pixel-faithful specs

- No controlled 10.6 measurements (pixel rulers, color values, font metrics). Screenshots are not measurements,
  and the HIG explicitly forbids measuring its own figures (p. 255).
- No captures of focus rings, inactive windows/selections, disabled or mixed controls, open submenus, or
  true document sheets ([image inventory](image-inventory.md#capture-matrix-central-aqua-components)).
- No animation evidence (sheet/drawer/menu timing), so motion specs cannot be written yet.
- No accessibility-tree evidence; A11Y hooks are derived from the HIG's requirements, not observed.

## Maintenance

- Add the spec link and mark **S** when a component gets a spec file.
- Keep one test example per row that is specific enough to implement; link the chapter section, not the whole
  chapter, when an anchor exists.
- If an evidence code changes (new capture/measurement), update both this matrix and the image inventory.

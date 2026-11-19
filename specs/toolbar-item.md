# Component Spec: Toolbar Item (Rectangular-Style Toolbar Control)

- **Spec ID:** CMP-02
- **HIG chapter(s):** Controls > Window-Frame Controls (pp. 255-264); toolbars (p. 203)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A toolbar item gives quick access to **frequently used commands or objects** affecting the active window.
The rectangular-style control is the general-purpose window-frame control: it can act as a push button, a
toggle, a segmented control, or a pop-up menu (p. 257). It may appear in the toolbar or in a bottom bar;
in a bottom bar it should only be used for controls that affect the window body's contents or organization
(pp. 257-258).

Never use it:

- in the window body (window-frame controls are designed for the frame surface only, p. 255);
- for a command that is not a frequent, window-scoped action;
- as a substitute for a window-body push button in a dialog.

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| Rectangular-style, push button | Frequent command in toolbar or bottom bar | regular (toolbar default), small (customization), mini | p. 260 |
| Rectangular-style, toggle | On/off view or mode; automatic on-state highlight | regular/small/mini | p. 259 |
| Rectangular-style, segmented | A small set of related choices | regular/small/mini | p. 257 |
| Rectangular-style, pop-up | Menu of related commands | regular/small/mini | p. 257 |
| Capsule-style | Toolbar only; alternative visual style | regular/small/mini | pp. 261-264 |
| Icon button | Toolbar only; no visible rectangular edge | regular/small/mini | pp. 269-271 |

Rules:

- Do not use capsule-style controls in a bottom bar; if both areas need controls, use rectangular-style in
  both to avoid mixing styles (p. 263).
- A toolbar may contain only icon buttons, action menus, search fields, and rectangular/capsule-style
  controls; remove any other control type (p. 265).
- Every toolbar item needs a descriptive **external label** so users can customize the toolbar to Icon & Text
  or Text Only (p. 260); bottom-bar rectangular controls do not need one.

## 3. Dimensions and geometry

| Property | Regular | Small | Mini | Source |
| --- | --- | --- | --- | --- |
| Height | not specified in the HIG | not specified | not specified | pp. 260-261 |
| Spacing between controls | 8 px | 8 px | 8 px | p. 261 |
| Icon button hit target | ≈10 px margin around icon/label | | | p. 270 |
| Icon size | 24-32 px (e.g. 32×32) | | | p. 270 |
| Minimum icon edge gap | ≥8 px for ≥24 px icons | | | p. 270 |
| Label font | system font | small system font | mini system font | pp. 260, 264 |

The 8 px spacing is automatic and may vary with the length of the external label (p. 261).

**Measured 10.6 values:** not measured. The HIG explicitly warns that its illustrations are not
measurement-accurate and must not be measured (p. 255). Toolbar height/bezel geometry must come from a
controlled 10.6 measurement, not from the PDF.

## 4. Text, fonts, and labels

- **Text content:** a noun/noun phrase describing an object, setting, or state, **or** a verb/verb phrase
  describing an action (p. 259, p. 264).
- **Capitalization:** title-style (pp. 259, 264).
- **Segments:** either all text or all icons; never mix within one segmented control (p. 259, p. 263).
- **Icons:** meaning must be clear and unambiguous; prefer system-provided images from 10.5+ (pp. 259, 263).
- **Toggles:** if using automatic on-state highlighting, provide two labels describing the on and off states
  below the control, and describe both states in the help tag (p. 259).
- **External label:** required for toolbar items; it is the text shown in Icon & Text / Text Only toolbar modes
  (pp. 260, 264).

## 5. States

The 10.6 model separates two independent signals (p. 256):

- **Bezel** reflects the **window's** active/inactive state.
- **Glyph** reflects the **control's** enabled/disabled state.

| State | Trigger | Visual requirement | Source |
| --- | --- | --- | --- |
| Enabled | command available | glyph in enabled appearance | p. 256 |
| Disabled | command unavailable | glyph in disabled appearance | p. 256 |
| Window inactive | window not key | bezel changes to inactive appearance | p. 256 |
| Inactive window + enabled, no click-through | window not key | glyph uses **disabled** appearance regardless of enabled state | p. 256 |
| On (toggle/segmented) | selected/on | automatic highlight; segmented "blue glow" in 10.6 | pp. 259, 261 |
| Pressed | pointer/key down | system pressed appearance; not quantified | p. 256 |
| Focused | keyboard focus | focus ring (A11Y-13) | p. 110 |
| Hover | pointer over | only documented for capsule controls that support click-through in an inactive window (bezel becomes active) | p. 256 |

## 6. Interaction and keyboard

- **Pointer:** click activates immediately. Click-through is a window-frame property: clicking a control in an
  inactive window may activate the control and the window together, or only the window. The HIG ties the glyph
  appearance to whether the control supports click-through (p. 256).
- **Keyboard:** Tab reaches toolbar items; Space activates (A11Y-17); see the menu-focus journey (J1) for
  menu-bar access.
- **Toggle/segmented:** selection changes on activation; no delayed commit.
- **Timing:** state highlight must update with the action; the HIG gives no animation timing.

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | External label (the customizable text), not a hidden tooltip (A11Y-28). |
| Role | Button / toggle button / segmented control / pop-up menu (A11Y-29). |
| State | Enabled/disabled, on/off, selected segment, window-inactive availability. |
| Focus | Focusable; visible ring (A11Y-13). |
| Announcements | On/off changes and enable/disable changes (A11Y-29). |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #14 (Finder toolbar), #19 (iCal toolbar + bottom bar), #22 (Safari 5), #33 (Xcode 3.2).
  These show icon+label and icon-only layouts and rounded/segmented shapes.
- HIG figures: 15-1 to 15-6 (pp. 257-263); Figure 15-4 shows the iCal toggle help tag.
- Gaps: disabled/window-inactive pairs, hover/click-through, focused state, exact sizes.

## 9. HIG source pages

- p. 255 — use standard controls, standard sizes, never vertically resize; do not measure the book's images.
- p. 256 — bezel vs. glyph state model; click-through exception; Table 15-1.
- pp. 257-258 — rectangular control roles; toolbar vs. bottom-bar use.
- p. 259 — contents/labels; toggle labels and help tag; segmented content consistency.
- p. 260 — external-label requirement; sizes; fonts.
- p. 261 — 8 px spacing; historical AppKit configuration.
- pp. 261-264 — capsule-style rules; legacy toolbar controls.

## 10. Recreation-specific decisions / open questions

- **PENDING:** rectangular vs. capsule style for the toolbar, and whether both ever coexist (the HIG permits
  rectangular in both areas; mixing styles in one window is discouraged).
- **PENDING:** reproduce click-through? It is a windowing-system behavior; a web/canvas recreation may need an
  explicit rule.
- **PENDING:** 10.6 toolbar height, bezel radius, and pressed artwork — measure before custom drawing.
- **DECIDED:** `NSTexturedRoundedBezelStyle`, `NSSegmentStyleTexturedRounded`, and Interface Builder names are
  historical implementation detail (recorded in [Controls](../03-aqua-interface/controls.md)), not requirements.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit pp. 255-264 |
| Geometry | Low-Medium | Only 8 px spacing and icon sizes are stated |
| Visual states | Medium | State model explicit; no measurement/captures of inactive/disabled |
| Keyboard behavior | Medium | Focus rules general (p. 110); toolbar-specific keys unstated |

## 12. Acceptance tests

1. **Role selection:** a toolbar item is a push button, toggle, segmented control, or pop-up; no other control
   type appears in a toolbar (p. 265).
2. **Label:** every toolbar item exposes an external descriptive label usable in Icon & Text/Text Only modes.
3. **No mixing:** a segmented toolbar control never mixes text and icon segments.
4. **Toggle clarity:** a toggle shows a distinct on state and both state meanings in its help tag.
5. **Spacing:** rendered gaps between rectangular/capsule items are 8 px (allowing label-driven variance).
6. **Window state:** when the window becomes inactive, the bezel changes while the glyph's enabled/disabled
   meaning remains correct (A11Y-29).
7. **Keyboard:** Tab reaches each toolbar item and Space activates it; focus is visible (A11Y-13/17).
8. **No vertical stretch:** toolbar items render at one of the three standard heights, never stretched.

# Icons

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 139
- **Status:** Source-verified

> **Scope:** the 2009 HIG's art direction and icon-asset rules for Mac OS X. Some rules are about how the OS
> renders assets (Finder hints, `.icns`, Cover Flow alignment); those are host details unless the recreation
> reproduces the renderer. Visual principles (genre, perspective, simplicity) remain transferable. See
> [Scope and evidence labels](../notes/scope-and-evidence.md).

## Why this matters (retro recreation)

Icons are the most visible part of the 2009 look: photo-illustrative application icons, flat black template
images in toolbars, document icons with folded corners, and distinct genres for apps vs. utilities. A
recreation that gets the controls right but uses flat modern vectors will not look like 10.6. This chapter
supplies the style rules, sizes, and rendering constraints.

## Key sections to review (from TOC)

- Icon Genres and Families (p. 139)
- Application Icons (p. 140): User Application, Viewer/Player/Accessory, Utility
- Document Icons (p. 142)
- Toolbar Icons (p. 143)
- Icons for Plug-ins, Hardware, and Removable Media (p. 144)
- Icon Perspectives and Materials (p. 145)
- Creating Icons (p. 147): Tips, Suggested Process, 10.5+ Icons, Scaling Artwork
- Designing Toolbar Icons (p. 152): Icon Buttons, Capsule-Style, Rectangular-Style
- System-Provided Images (p. 155)

## What the 2009 source says

### Style and genres (pp. 139-140)

- Aqua uses a **photo-illustrative** style: near-photographic realism, but illustrated to pack information
  into a small space. 512×512 px is available for detail; anti-aliasing, alpha, and translucency allow curves,
  shading, and dimensionality.
- Icons must scale well across Dock, Finder, Quick Look, and alerts.
- **Genres** communicate what an app does before it opens: user applications are colorful and inviting;
  utilities are serious/desaturated. A genre look helps users distinguish types in the Dock.
- An **icon family** carries a visual cue from the app icon into the icons for its associated files (iTunes'
  application, device, and playlist icons).

### Application icons (pp. 140-142)

- User application icons: vibrant, inviting, immediately conveying purpose. If the app creates/handles media,
  show the media; optionally add a closely related tool element (Preview's magnifier). Stickies needs no tool.
- Real text in an icon must be actual text, made unreadable by shrinking or layering—not wavy lines.
- User app icons appear to sit **on a desk in front of you**, with slightly diminishing perspective (wider at
  the bottom).
- Viewer/player/accessory icons: simplified, idealized representations of the object/symbol, not screenshots;
  straight-on perspective (Calculator, QuickTime Player, DVD Player).

### Utility icons (p. 142)

- More serious tone; color desaturated, predominantly gray, added only when needed to communicate.
- Few elements; one object representing the utility's task. Straight-on, "on a shelf" perspective.

### Document icons (pp. 142-143)

- Traditional paper shape with the top-right corner folded.
- Make the associated application obvious; Preview documents repeat the media but not the tool.
- Documents hover on the desktop with a shadow behind them.
- Badges must be integrated within the document shape, not pasted over the top and breaking the outline.

### Toolbar icons (p. 143)

- Toolbar icons are simpler than app icons: small, streamlined, sketch-like, with constrained shading and just
  enough detail. See "Designing Toolbar Icons" (p. 152).

### Plug-ins, hardware, removable media (p. 144)

- Plug-in icons look like stackable components: app identifier on the left, plug-in image on the right.
- Hardware icons show devices as seen on a desk; external devices have a region for a connector symbol
  (FireWire, USB).
- Removable media (CDs, floppies, PC cards) are straight-on, as held in front of you.

### Perspectives and materials (pp. 145-146)

- All interface elements share a **single light source directly above**.
- Perspectives: application = on a desk; utility = on a shelf (flat objects get a wall-like shadow); real 3-D
  objects sit on the ground/shelf with shadow below; toolbar = straight-on on a shelf.
- Represent real materials convincingly (plastic, glass, paper, metal), including weight and feel.
- Use transparency only when convincing and when it completes the icon's story (no transparent sneakers).

### Tips for designing icons (p. 147)

- Use a professional designer.
- Perspective and shadow matter most; one light source above.
- Use universal imagery; avoid secondary details (a postage stamp reads better than a rural mailbox for mail).
- Strive for simplicity: one object, start with a basic shape.
- Use color judiciously, with smooth gradients rather than sharp color divisions.
- Do **not** use Aqua interface elements in icons (they can be mistaken for the interface).
- Do **not** use replicas of Apple hardware (copyrighted, changes frequently).
- Do **not** reuse Mac OS X system icons for different meanings.

### Creating icons (pp. 147-152)

- Required files: **128×128** (all Finder versions), **512×512** (10.5+), and a **mask** defining clickable
  regions. Hints at **32×32** and **16×16** preserve detail in Finder (the Dock does not use hints; it
  resamples the 128×128). A fixed-size icon (bevel button) may be supplied only at its actual size.
- Process: sketch on paper → illustrate in software → add detail/color → add shadows → refine and create mask
  → convert to `.icns` (Icon Composer or third-party tools).
- The 512×512 version is its own resource, not an upscale: richer texture, more detail, more realism. Do not
  produce a "vectorized" enlargement.
- Cover Flow (black, reflective background): drop shadows must be fully black (gray reads as a glow); very
  dark/black-edged icons may need a slight inner glow; avoid high alpha in the lower half because the Finder
  aligns icons using the first opaque pixel and may clip below it.
- Scaling: supply **512, 128, 32, 16**. Build a master at a multiple (e.g. 1024×1024) with an 8-px grid; 2 px
  for more precision. For 32/16, redraw if scaling is unsatisfactory (32-px or 64-px grid on a 1024 master).

### Toolbar icons (pp. 152-155)

- Purpose: quick access to frequent commands; icons must be distinguishable and memorable.
- Three representations: standalone icon buttons, icons inside capsule-style controls, icons inside
  rectangular-style controls; or system-provided images in either control style.
- Preserve the meaning of recognizable system images (Colors/Fonts/iDisk); do not repurpose them.
- **Never use a system alert icon (e.g. yellow caution) in a toolbar**; it dilutes the icon's system meaning.
- Each toolbar icon should represent a unique object/action using a familiar metaphor; icons should harmonize
  in perspective, color, size, and visual weight while remaining distinct.
- **Icon buttons:** 32×32 px recommended; straight-on shelf perspective; recognizable system icons keep their
  standard appearance.
- **Capsule-style:** simple, colorful, low-detail; straight-on, minimal shadow; enough contrast against the
  control; bright clear colors; visually centered (not necessarily mathematically).
- **Rectangular-style:** streamlined **black** images conveying meaning by outline/contour, not internal
  detail; sharp outline; straight-on; full black plus a few grays; anti-aliased; visually centered; regular
  size **≤19×19 px**.

### System-provided images (pp. 155-159)

- Template images (black, for rectangular-style controls, processed by the button cell): Quick Look, Bluetooth,
  iChat Theater, slideshow, Action menu, smart item, icon/list/column/Cover Flow views, path, lock/unlock,
  go left/right, add/remove, enter/exit full screen, stop progress, refresh.
- Free-standing images (borderless buttons): invalid data, reveal, follow link, stop progress, refresh.
- Toolbar images: system entities (Bonjour, .Mac, computer, burnable/smart folder, network), preferences
  categories (Advanced, General, User Accounts), and Colors/Fonts/Info window images.
- Rule: use each image only for its documented meaning; if none fits, design a custom image rather than
  misusing a system one. The full constant-name tables are on pp. 156-159.

## Observed Mac OS X 10.6 behavior

- Application icon styles: #37 (Finder, Safari, Terminal, System Preferences in the Dock), #15 (Dock),
  #26 (Stacks), #33 (Xcode welcome), #36 (Pages/MathType).
- Document icons: #36 (Pages document), #14 (Finder files); folded-corner convention visible.
- Toolbar template images: #14 (Finder view controls, Action menu, Quick Look), #19 (iCal), #22 (Safari 5),
  #33 (Xcode).
- Utility style: #1 (Activity Monitor), #31 (System Profiler) — desaturated, single-object icons.
- Removable media/hardware: **not captured**.
- Cover Flow alignment/clipping: #10 shows Cover Flow but not the alpha-edge edge cases.
- 16/32/128/512 comparisons: **not captured**.

## Interpretation

- The transferable rules are: genre-specific tone (app vs. utility), single light source from above, consistent
  perspective per icon type, one clear object, integrated document badges, black outline-style toolbar
  templates, and meaning-preserving reuse.
- The OS-specific rules are asset-format and renderer behavior: `.icns`, masks, Finder hints, Dock resampling,
  Cover Flow opaque-pixel alignment. A recreation that draws icons at runtime should re-derive equivalents
  rather than copy the packaging.
- System-provided image constants are a vocabulary of meanings: the useful part is the mapping from image to
  action, not the AppKit constant names.

## Recreation-specific decision / open question

- **PENDING — asset pipeline:** bitmap icon set (512/128/32/16) vs. scalable/runtime-drawn. The HIG's hint and
  mask rules assume `NSImage`/`.icns`.
- **PENDING — fidelity target for icons:** photo-illustrative 10.6-style app icons are expensive to produce;
  decide whether app icons are in scope or only toolbar/document affordances.
- **PENDING — system-image policy:** reuse 10.6 artwork, redraw equivalents, or substitute modern icons. Any
  substitution must preserve meanings.
- **PENDING — Cover Flow equivalent:** whether the recreation has a reflective/black browsing view that
  requires the drop-shadow/inner-glow rules.
- **DECIDED — never repurpose a system icon's meaning**; if no match exists, draw a custom icon.
- **DECIDED — rectangular-style toolbar icons are black outline images ≤19×19 px** (p. 154) when that control
  style is used.
- **REJECTED — copy Apple hardware or Aqua elements into icons** (p. 147).

## Implementation implications

- Provide icon sizes 512/128/32/16 if a bitmap pipeline is used; generate a mask for clickable bounds.
- Toolbar icon sizes: 32×32 for icon buttons; ≤19×19 for regular rectangular-style; capsule-style small and
  colorful; all visually centered.
- One light source (above) and a consistent perspective per icon family.
- Document badges stay inside the document silhouette.
- Toolbar icons must not reuse alert icons or system images with different meanings.
- If a black-background view is implemented, all drop shadows must be pure black and lower-edge alpha must not
  be relied on for alignment.

## Assets / examples to capture later

- [ ] 16/32/128/512 px versions of one application icon side by side.
- [ ] Application vs. utility icon genres in the Dock (Figures 11-1, 11-2).
- [ ] Document icon with folded corner and an integrated badge (Figures 11-9, 11-10).
- [ ] Toolbar icon styles: icon button, capsule, rectangular (Figure 11-23).
- [ ] Black-background rendering of a dark-edged icon with an inner glow (Figure 11-21).
- [ ] Retained captures: #1, #14, #19, #22, #31, #33, #36, #37.
      See the [image inventory](../notes/image-inventory.md).

## Open questions / follow-up extraction

- [ ] Which icon families does the recreated app need (app, document, toolbar, source-list)?
- [ ] Does the target platform require multiple DPI variants beyond the 2009 sizes?
- [ ] Are any 10.6 system images licensed for reuse, or must they be redrawn?
- [ ] Does the recreation need a mask/clickable-region concept for irregular icons?

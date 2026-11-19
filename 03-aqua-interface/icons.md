# Icons

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 139
- **Status:** Summarized

## Why this matters (retro recreation)

The icon chapter is heavily visual/asset-oriented; for the retro recreation, icon style (photo-illustrative
Aqua, icon genres, perspectives/materials, toolbar icon styles, system-provided images) is a key fidelity
target. Existing reference screenshots are in `../images/`.

## Key sections to review (from TOC)

- Icon Genres and Families (p. 139)
  - Application Icons (p. 140)
    - User Application Icons (p. 140)
    - Viewer, Player, and Accessory Icons (p. 142)
    - Utility Icons (p. 142)
  - Document Icons (p. 142)
- Toolbar Icons (p. 143)
  - Designing Toolbar Icons (p. 152)
    - Designing Icons for Icon Buttons (p. 153)
    - Designing Icons for Capsule-Style Toolbar Controls (p. 154)
    - Designing Icons for Rectangular-Style Toolbar Controls (p. 154)
- System-Provided Images (p. 155)
  - System-Provided Images for Use in Controls (p. 156)
  - System-Provided Images for Use as Standalone Buttons (p. 157)
  - System-Provided Images for Use as Toolbar Items (p. 158)
  - System-Provided Images that Indicate Privileges (p. 160)
  - A System-Provided Drag Image (p. 160)
- Icon Perspectives and Materials (p. 145)
- Creating Icons (p. 147)
  - Tips for Designing Icons (p. 147)
  - A Suggested Process for Creating Icons (p. 148)
  - Creating Icons for Mac OS X v10.5 and Later (p. 149)
- Designing Toolbar Icons (p. 152)
  - Designing Icons for Icon Buttons (p. 153)
  - Designing Icons for Capsule-Style Toolbar Controls (p. 154)
  - Designing Icons for Rectangular-Style Toolbar Controls (p. 154)

## Source notes (with page refs)

- p. 139 — Aqua icon style: photo-illustrative, realism of photography via illustration, 512x512 detail,
  anti-aliasing, alpha channels/translucency; genres by role (user apps, utilities).
- p. 140 — User application icons vibrant/inviting, convey purpose immediately; TextEdit icon conveys text.
- p. 142 — Viewer/player/accessory icons use simplified idealized representation, straight-on perspective.
- p. 142 — Utility icons: serious tone, desaturated colors, single object focus, straight-on perspective.
- p. 142 — Document icons: piece of paper with folded corner; associated-app visual cue; badge as integrated
  element, not overlay.
- p. 143 — Toolbar icons: frequently used commands, smaller detail; styles: icon buttons, capsule-style,
  rectangular-style; system-provided images available; don't repurpose system icons (caution).
- p. 145 — Perspectives/materials: app icons "on a desk"; utility icons on shelf; toolbar straight-on; real
  materials, transparency only when convincing.
- p. 147 — Tips: professional designer; perspective/shadows most important; universal imagery; simplicity;
  judicious color; avoid Aqua elements in icons; don't reuse Apple hardware/system icons.
- p. 148 — Suggested process: sketch → software illustration → add detail/color → add shadows → mask → .icns;
  icon sizes 128, 512, plus hints 32, 16.
- p. 149 — 512x512 version is its own resource (not scaled-up 128); Cover Flow black background adjustments.
- p. 152–154 — Toolbar icon design details per style (capsule: straight-on, minimal shadow, bright colors;
  rectangular: sharp outline, full black + grays, anti-aliasing, ≤19x19 px).

## Implementation implications

- Recreated app icon should follow Aqua photo-illustrative genre rules; document icons with folded corner and
  app association.
- Toolbar icons: capsule vs. rectangular styles depending on app look; prefer system-provided images where
  meaning matches.

## Assets / examples to capture later

- [ ] Capture/curate icon assets for the recreated app; reuse HIG figures for reference.
- [ ] Use the [image inventory](../notes/image-inventory.md) for retained icon examples: Dock/Stacks (#15,
      #26), Xcode source-list icons (#33), and the 10.6.8 desktop (#37); capture the 16/32/48/128/512 px
      comparison and selected-label states listed as gaps there.

## Open questions / follow-up extraction

- [ ] Which icon assets are available to the retro recreation project (custom art vs. system-provided)?
- [ ] What is the recreated app's icon genre?

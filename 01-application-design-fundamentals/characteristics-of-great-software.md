# Characteristics of Great Software

- **Part:** Part I: Application Design Fundamentals
- **PDF start page:** 31
- **Status:** Reviewed

## Why this matters (retro recreation)

This chapter defines the quality bar the HIG held itself to. For a retro recreation, these translate into
concrete acceptance criteria for how faithful the recreation should be — especially the distinction between
perceived performance, ease of use, appearance, reliability, and adaptability.

## Key sections to review (from TOC)

- High Performance (p. 31)
- Ease of Use (p. 32)
- Attractive Appearance (p. 34)
- Reliability (p. 34)
- Adaptability (p. 36)
- Interoperability (p. 37)
- Mobility (p. 38)

## Source notes (with page refs)

- p. 31 — Performance is the *perceived* measure of speed/efficiency and is critical to software success.
  Guidelines: use metrics (e.g. Apple tools like Shark) to identify problems; don't wait until end of
  development cycle for tuning; choose modern APIs over legacy APIs; choose appropriate technologies for the
  task; use threads to improve responsiveness; avoid polling the system; eliminate unnecessary I/O; optimize
  memory usage for the virtual memory system; avoid loading resources until needed.
- p. 32 — Ease of Use: intuitive experience, elegant solutions, familiar paradigms; easy to install/configure
  via intelligent defaults and options; present context-relevant tools; warn against dangerous actions and
  provide undo.
  - p. 32 — Use metaphors representing concrete, familiar ideas; focus on solutions not features.
- p. 34 — Attractive Appearance: stylish design and attractive appearance draw users to the Mac platform;
  apps should use high-quality graphics (32-bit color, transparency, high-res icons); follow Part III layout
  and visual guidelines; adopt standard Aqua elements rather than custom controls; use 32-bit color;
  Interface Builder for UI design; render via modern APIs (Quartz, Cocoa, ATSUI, OpenGL); avoid QuickDraw.
- p. 34 — Reliability: earns user trust; preserves user data integrity, prevents data loss/corruption;
  handles complex situations without crashing; predictable UI behavior (same actions → same results); provide
  predictable document output; reduce data loss on import/export; test under varied conditions; anticipate
  errors and handle gracefully; validate user input; use Apple debugging tools; prefer modern APIs.
- p. 36 — Adaptability: program adjusts when surroundings change (e.g. network down); build forgiveness and
  intelligence into interface; avoid assumptions about hardware access or locale; use Bonjour for device
  discovery; be sensitive to screen availability/resolution changes; avoid custom device drivers.
- p. 37 — Interoperability: ability to communicate across environments (user or program level); uses pasteboard,
  drag and drop, AppleScript, Bonjour, Services; avoid custom file formats when possible; use same file format
  across platforms; support filename extensions; use standard protocols (XML preferred) for data interchange;
  save config via preferences system.
- p. 38 — Mobility: programs shouldn't waste battery polling/accessing peripherals unnecessarily; avoid
  requiring CD insertion; minimize hard-drive/optical-drive access; be forgiving if network volumes go
  offline; be sensitive to screen changes and monitor plug/unplug.

## Implementation implications

- Retro recreation should prioritize perceived performance cues (e.g. progress indicators, feedback) even
  though actual computation cost may be low.
- Appearance fidelity: 32-bit color, transparency, high-quality icons; adopt system-supplied controls rather
  than custom ones.
- Reliability expectations: Undo/Redo/Revert-to-Saved support likely in scope for the recreation.
- Adaptability: handle network/config changes that the 2009-era environment actually had (Bonjour, etc.).

## Assets / examples to capture later

- [ ] Capture screenshots of the "Attractive Appearance" guidelines figures (Part III figures, e.g. windows).

## Open questions / follow-up extraction

- [ ] Which characteristics are in tension for this particular app (e.g. high performance vs. attractive
      graphics)?
- [ ] Are there HIG figures per characteristic worth extracting?

# The Mac OS X Environment

- **Part:** Part II: The Macintosh Experience
- **PDF start page:** 61
- **Status:** Summarized

## Why this matters (retro recreation)

Context for how the recreated app should behave within the 2009-era Mac OS X system: display metrics,
Dock integration, Finder expectations, multiple users, resource management.

## Key sections to review (from TOC)

- The Always-On Environment (p. 61)
- Disk Size and Usage Information (p. 61)
- Displays (p. 61)
- The Dock (p. 62)
- The Finder (p. 63)

## Source notes (with page refs)

- p. 61 — The Mac OS X Environment chapter covers features influencing software design; system designed as
  "always ready to use"; energy-saving means computer often left on for long periods; avoid relying on
  reboot to clear temporary files; avoid startup/login items for user-level processes; avoid reboot for
  installation/update unless absolutely necessary.
- p. 61 — Disk size/usage: report values consistent with Finder/Activity Monitor; use GB (1,000,000,000 bytes)
  not GiB (1,073,741,824) when reporting disk sizes.
- p. 61 — Displays: avoid assumptions about display size; Mac OS X runs as small as 800x600 but optimize for
  1024x768; 640x480 available for iBook/Classic/games/multimedia; design UI for at least 800x600.
- p. 62 — Dock: when creating windows/resizing, take Dock position into account; new windows should not
  overlap Dock boundaries; prevent windows being moved/resized behind Dock; developers can use
  GetAvailableWindowPositioningBounds / NSScreen.
- p. 62 — Conveying info in Dock: badging (superimposed small image on Dock tile icon, e.g. Mail unread
  badge); Notification Manager (serious info, e.g. error conditions → Dock tile bounces; disable once resolved).
- p. 63 — Clicking in Dock: clicking open app icon always results in window becoming active; if not open,
  new window opens (new untitled for doc-based; main window otherwise); clicking open app's icon brings
  active, unminimized windows to front; minimized doc windows remain in Dock; if no unminimized windows,
  last minimized window expands; no windows → new window.
- p. 63 — Finder integration: .app extension required; CFM apps packaged in bundles; use Info property list
  to communicate with Finder; give files appropriate filename extensions; avoid changing creator type of
  existing docs; provide Quick Look generator for custom content types.

## Implementation implications

- Retro recreation should not place windows behind/overlapping the Dock; should use badging/notification
  behavior consistent with 2009 Dock.
- Should follow Finder bundle/file-extension conventions for recreated document types.

## Assets / examples to capture later

- [ ] Capture Dock screenshots (images exist in `../images/` e.g. Finder Menu/Stacks/Cover-Flow) for
      reference.

## Open questions / follow-up extraction

- [ ] How does the Dock Exposé/press-and-hold behavior (p. 63) factor into recreation?
- [ ] Multiple-user environment details for the recreation's assumptions (p. 65).

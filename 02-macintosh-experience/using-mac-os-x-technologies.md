# Using Mac OS X Technologies

- **Part:** Part II: The Macintosh Experience
- **PDF start page:** 67
- **Status:** Summarized

## Why this matters (retro recreation)

This chapter lists system technologies the HIG wanted apps to adopt instead of building custom solutions —
directly relevant when deciding which "recreated" features should be backed by system capabilities vs. custom
implementation in the retro project.

## Key sections to review (from TOC)

- Address Book (p. 67)
- Animation (p. 68)
- Automator (p. 70)
- Bonjour (p. 71)
- Colors (p. 71)
- Dashboard (p. 72)
- Fonts (p. 74)
- Preferences (p. 75)
- Printing (p. 76)
- Security (p. 76)
- Services (p. 77)
- Speech (p. 78)
- Spotlight (p. 78)
- User Assistance (p. 81)

## Source notes (with page refs)

- p. 67 — Address Book: use Address Book framework for contact info; user-facing picker names should be
  descriptive ("Addresses" / "Contacts"), not "people picker"/"picker".
- p. 68 — Animation: hallmark of Mac OS X; animation enhances user experience; ideal uses: communicating
  progress, providing meaningful feedback, clarifying process/concept; e.g. minimize to Dock, unfurl sheets,
  slide drawers; Core Animation in v10.5+; use wisely — subtle enhancement, not focus; avoid replicating
  Front Row/Time Machine animated UIs for content-creation tasks; avoid animating everything; avoid animating
  routine system-provided control actions (tab switching, view open/close, toolbar clicks).
- p. 70 — Automator: users stack actions; minimize vertical space (use pop-up menu not radio buttons);
  don't use group boxes; avoid tab views (use hidden tab views); don't use labels to repeat action title;
  use disclosure triangles; use small Aqua controls; 10-pixel margins; provide feedback; display example of
  action effect.
- p. 71 — Bonjour: avoid assumptions about network settings; use Bonjour instead of requiring user-typed IP
  address; automatic discovery of computers/devices/services; don't save settings based on IP address.
- p. 71 — Colors: use standard Colors window for picking colors (five color models); don't create custom
  color picker UI.
- p. 72 — Dashboard: widgets small/compact, single well-defined task; avoid aggressive branding/ads in
  widgets; not a miniaturized app window; use color to enhance; don't use Aqua controls on widget front;
  display info at once; default small, expandable if needed; minimal default info, no scrolling unless needed;
  readable fonts; Info button on back; Done button on back.
- p. 74 — Fonts: use Fonts window for user font selection; standard and minimized views; Typography inspector
  via action menu.
- p. 75 — Preferences: preference = infrequently changed setting; avoid preferences for features changed
  often (use modeless access instead); don't provide preferences toolbar item; put app-level prefs in
  Application menu, document-specific in File menu.

## Implementation implications

- Retro recreation: wherever the original app used system tech (Colors window, Fonts window, Dashboard,
  Spotlight, speech, printing system), the recreation should target the same system capability or mimic it.

## Assets / examples to capture later

- [ ] Capture figures: Address Book people-picker (p. 67), animation sequences (p. 68), Colors window (p. 71),
  Fonts windows (p. 74), Dashboard widgets (p. 72), Spotlight results (p. 79-80).
- [ ] Retained utility captures are catalogued in the
  [image inventory](../notes/image-inventory.md): Activity Monitor, AppleScript Editor, Automator, Console,
  Disk Utility, Network Utility, System Profiler, Help Viewer, and the 10.6.8 desktop.

## Open questions / follow-up extraction

- [ ] Which of these technologies were actually in use for the app being recreated?
- [ ] Speech/Speech tech feasibility for the retro platform (2009 iOS/macOS emulators?).

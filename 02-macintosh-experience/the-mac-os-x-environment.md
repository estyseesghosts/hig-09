# The Mac OS X Environment

- **Part:** Part II: The Macintosh Experience
- **PDF start page:** 61
- **Status:** Source-verified

> **Scope:** this chapter is system-integration advice for applications shipping on Mac OS X. It describes
> constraints of the 2009 host (Dock, Finder, display sizes, multiple users) that shape what the user could
> see and do. A recreation on another platform inherits the *visible* behavior only where it chooses to. See
> [Scope and evidence labels](../notes/scope-and-evidence.md).

## Why this matters (retro recreation)

The 2009 app did not live in a vacuum: it sat in a Dock, was launched from the Finder, had to survive
months of uptime, and shared the machine with other users. Several HIG rules in this chapter are directly
observable (window placement relative to the Dock, how a Dock click reopens windows, file extensions) and
therefore belong in a faithful recreation; others are implementation safety advice (cache cleanup, threading)
with no visible surface.

## Key sections to review (from TOC)

- The Always-On Environment (p. 61)
- Disk Size and Usage Information (p. 61)
- Displays (p. 61)
- The Dock (p. 62)
- The Finder (p. 63)
- File Formats and Filename Extensions (p. 64)
- Internationalization (p. 64)
- Multiple User Issues (p. 65)
- Resource Management (p. 66)
- Threads (p. 66)

## What the 2009 source says

### The Always-On Environment (p. 61)

- Mac OS X is designed to be always ready; energy saving means machines stay on for hours, days, weeks, or
  months.
- Don't rely on a restart to clear cached/temporary files — remove them when no longer needed.
- Don't rely on startup/login items to launch user-level processes: if the user quits such a process it stays
  unavailable until the next boot.
- Don't require a reboot for installation or update unless absolutely necessary; the user probably has other
  work open, so a restart is a rude interruption.

### Disk size and usage (p. 61)

- Report disk values consistent with the Finder and Activity Monitor.
- Calculate disk sizes in **GB (1,000,000,000 bytes)**, not GiB (1,073,741,824 bytes). Mixing them produces
  numbers that disagree with the system.

### Displays (pp. 61-62)

- Don't assume a display size. Systems can be as small as 800×600, and users may have multiple high-resolution
  displays.
- Optimize for **1024×768** unless the audience's display is known.
- 640×480 exists for iBook, Classic, games, and multimedia, but is **not** the minimum: design for at least
  800×600.
- Don't assume aspect ratio; rotation swaps it (800×600 → 600×800). Applications can observe screen
  reconfiguration callbacks (Quartz Display Services).

### The Dock (pp. 62-63)

- Account for the Dock when creating or resizing windows: new windows must not overlap the Dock's boundaries,
  and users must not be able to move or resize a window behind the Dock. Available screen area excludes the
  Dock and menu bar (Carbon `GetAvailableWindowPositioningBounds`; Cocoa `NSScreen`).
- **Badging:** superimpose a small image on the Dock tile to convey unobtrusive status (Mail's unread count).
- **Notification Manager:** use it for serious information such as errors; the Dock tile bounces. Stop the
  notification once the user has addressed the problem.
- **Clicking the Dock icon always activates a window:**
  - app not open → open a new window (untitled document window for document-based apps; main window otherwise);
  - app open → activate it and bring all unminimized windows forward; minimized windows stay in the Dock;
  - no unminimized windows → expand the last minimized window;
  - no windows at all → open a new window.
- **Press-and-hold** a running app's Dock icon → Exposé shows all its windows and a minimal Dock menu appears
  (Quit; Hide/Show; Show in Finder; Keep in Dock/Open at Login).
- Press-and-hold a non-running app → minimal menu (Open; Show in Finder; Remove from Dock/Open at Login).
- **Control-click** a running app's icon → a customizable Dock menu listing all open windows plus
  app-specific items (p. 190); for a non-running app it shows the minimal menu.

### The Finder (pp. 63-64)

- Application bundles must have a `.app` extension; the Finder shows or hides it per the "Show all file
  extensions" preference.
- Package CFM applications in a bundle.
- Use an information property list to describe the app and its document types.
- Give saved documents appropriate filename extensions; file/creator codes are optional but aid Classic
  interoperability.
- Don't change the creator type of documents created by other applications without explicit consent.
- If the app produces document types outside HTML, RTF, text, TIFF, PNG, JPEG, PDF, and QuickTime, supply a
  Quick Look generator so Cover Flow and Quick Look can preview them.

### File formats and filename extensions (p. 64)

- Prefer industry-standard file formats so data can move in and out.
- Store user-configurable data as plain text the user can modify; Mac OS X apps traditionally use XML
  (preferences system, Core Foundation/Cocoa XML support).
- Include a filename extension appropriate to the content, while respecting the user's extension-display
  preference.

### Internationalization (pp. 64-65)

Minimum checklist:

- implement the program as a bundle to get built-in localization support;
- support Unicode text;
- load user-visible strings from `.strings` files;
- store interface data in nib files.

### Multiple user issues (p. 65)

- Mac OS X supports multiple accounts and **fast user switching**: several users can be active at once.
- Shared memory, cache files, semaphores, and named pipes must be labeled with the session ID to avoid
  corruption across sessions.
- Apps cannot assume exclusive access to system resources such as a CD/DVD drive.
- Privileges differ: not every user can access all System Preferences panes, modify the Dock, change their
  password, burn discs, or open certain applications.
- A home directory may be on a network volume, not a local one.

### Resource management (p. 66)

- Bundles are the preferred distribution mechanism and must contain everything required to run.
- Localize only the resources that need localization; the bundle loader prefers the appropriate localized
  version.
- Put optional resources (templates, etc.) in an installer-managed Library subdirectory; most app files belong
  in an app-specific folder under `~/Library/Application Support` or `/Library/Application Support`.
- Do not store resources in the executable's resource fork; use individual files in the bundle.

### Threads (p. 66)

- Move long calculations off the main event loop to keep the UI responsive; threading can also speed work on
  multiprocessor systems, but requires care to avoid corrupting shared data.

## Observed Mac OS X 10.6 behavior

- Dock and menu bar: visible in #15 (full desktop with Finder menu open), #26 (Stack open), #37 (10.6.8
  desktop with About This Mac and utilities).
- Window placement vs. Dock: visible in #19 (iCal), #27 (System Preferences), #37; no capture shows a window
  clipped behind the Dock (the HIG forbids it).
- Badging: **not captured** (no unread-count badge in the retained set).
- Dock press-and-hold / Control-click menus: **not captured**.
- Finder file-extension display: **not captured**; #14 shows a Finder window but not extension settings.
- Multiple-user switching: **not captured**.
- Display rotation/800×600: **not captured**; #15/#26 are 1920×1080.

## Interpretation

- The externally testable rules are: windows never overlap or hide behind the Dock; Dock activation follows
  the four-step window rule; disk values use decimal GB; the UI is usable at 800×600 and designed for
  1024×768; document types carry extensions.
- Badging and bouncing are feedback channels (p. 42): they should be used for status and serious errors
  respectively, and must be cleared when resolved.
- Multiple-user, bundling, resource-fork, and threading rules govern implementation safety. They matter to a
  recreation only insofar as it has multiple user profiles or ship-time packaging.
- The chapter contains no visual metrics beyond the display minimums; it should not be used as a source for
  Dock pixel geometry.

## Recreation-specific decision / open question

- **PENDING — Dock emulation:** whether the recreation presents a Dock at all, and if so whether it reproduces
  the activation rules, press-and-hold Exposé, and Control-click menu. The source describes 10.6 behavior, not
  a requirement for this project.
- **PENDING — minimum viewport:** 800×600 is the 2009 floor; the recreation's own minimum is undecided. It
  should not silently assume modern large screens.
- **PENDING — disk-size formatting:** whether the recreated UI reports disk sizes at all; if it does, decimal
  GB is the source-consistent choice.
- **PENDING — document packaging:** whether recreated documents use filename extensions and Quick Look–style
  previews.
- **PENDING — multi-user:** whether more than one user/session can exist in the recreation.
- **DECIDED — no window behind the Dock:** if a Dock is drawn, window placement must respect its reserved
  area (p. 62).
- **REJECTED — treat AppKit/Carbon API names as requirements.** `NSScreen`, `CGDisplayReconfigurationCallBack`,
  `GetAvailableWindowPositioningBounds` are historical 10.6 implementation details.

## Implementation implications

- Reserve Dock + menu-bar space when computing the usable window area (p. 62); if the Dock auto-hides, the
  reserved area follows its current state.
- Dock activation is a state machine: no-windows → new window; minimized-only → expand last minimized;
  otherwise bring unminimized windows forward (p. 63).
- Use decimal GB in any storage/size display (p. 61).
- Layout must survive 800×600 without clipping critical controls (p. 62).
- Status badges and error notifications are separate channels: badge for unobtrusive counts, bounce/alert for
  errors, and clear both when resolved (p. 62).

## Assets / examples to capture later

- [ ] Dock: normal, badge, bouncing/notification, press-and-hold Exposé, Control-click menu (pp. 62-63).
- [ ] A window at the Dock boundary, showing the reserved area, and the same window with the Dock hidden
      (p. 62).
- [ ] 800×600 and 1024×768 layouts of the recreated window.
- [ ] Finder: extension hidden/shown, Get Info creator/type fields, Quick Look preview (pp. 63-64).
- [ ] Retained captures that help: #15, #26, #37 (Dock/desktop), #14 (Finder).
      See the [image inventory](../notes/image-inventory.md).

## Open questions / follow-up extraction

- [ ] Dock Exposé/press-and-hold behavior (p. 63): include or omit?
- [ ] Which multiple-user assumptions does the recreation make (p. 65)?
- [ ] Does the recreation produce any document type needing a Quick Look-equivalent preview?
- [ ] Where does the recreation store configuration data, and is it user-editable plain text (p. 64)?

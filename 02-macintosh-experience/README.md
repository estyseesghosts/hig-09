# Part II — The Macintosh Experience (p. 59)

Platform/environment context and Mac OS X technology guidance relevant to recreating the 2009-era experience.

## Chapters

- [The Mac OS X Environment](the-mac-os-x-environment.md) (p. 61) — Status: Source-verified
- [Using Mac OS X Technologies](using-mac-os-x-technologies.md) (p. 67) — Status: Source-verified
- [Software Installation and Software Updates](software-installation-and-software-updates.md) (p. 85) — Status: Source-verified

## Use in this wiki

Track environment behaviors, system integrations, and conventions that shape how apps should look and behave in
the target era.

## Research status

- **State:** all three chapters are **Source-verified**.
- **Remaining work:** these chapters contain little numeric visual evidence. Pixel appearance (Dock, menu bar,
  focus rings) still needs 10.6 captures rather than more reading. See the
  [image inventory](../notes/image-inventory.md) and [revision history](../04-reference/revision-history.md)
  for the edition boundary.

## Retro recreation takeaways

- Always-on environment: don't rely on reboot/login items for user-level processes; avoid temp-file buildup.
- Display floor: design for at least 800×600 and optimize for 1024×768; don't assume aspect ratio.
- Dock: reserve Dock/menu-bar space for windows; badge for unobtrusive status; Dock activation follows the
  no-windows → new window, minimized-only → expand last, otherwise bring-forward rule.
- Finder: `.app` bundles, document extensions, and Quick Look-style previews are the visible integration points.
- System technologies: the HIG tells Mac OS X apps to use OS frameworks; that is historical advice, not a
  mandate for a cross-platform recreation. Each technology is marked PENDING in the chapter.

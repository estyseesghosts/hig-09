# Introduction (HIG)

- **Part:** (preceding Parts I–III)
- **PDF start page:** 19
- **Status:** Source-verified

## Purpose

Foundational framing for the retro recreation: what the HIG is, why following it mattered, and how the document
is organized.

## Source notes (with page refs)

- p. 19 — The HIG is the primary user interface documentation for Mac OS X; combines mechanics of designing a
  great UI with fundamental software design principles and info on leveraging Mac OS X technologies.
- p. 19 — Guidelines designed to assist in developing products that provide Mac OS X users with a consistent
  visual and behavioral experience across applications and the OS. Benefits: faster learning, quicker task
  accomplishment, accessibility, modern appearance, easier documentation, reduced support calls, easier
  localization, better media reviews.
- p. 19 — Aqua is the overall appearance and behavior of Mac OS X; defines standard appearance of UI components
  (windows, menus, controls), anti-aliased text/graphics, shadowing, transparency, careful color; standardized
  consistent behaviors; clear status communication via animation/notifications/visual effects.
- p. 20 — Aqua available to Cocoa, Carbon, and Java; Interface Builder best for Cocoa/Carbon; Carbon Porting
  Guide for Mac OS 9 → Mac OS X ports; Swing Aqua look-and-feel for Java.
- p. 20 — Who should read: anyone building applications for Mac OS X.
- p. 20 — Document organization: three main parts (App Design Fundamentals p. 23; Mac OS X Experience p. 59; Aqua
  Interface p. 95), plus supplementary: Keyboard Shortcuts Quick Reference (p. 367), Document Revision History
  (p. 383), Glossary (p. 375).
- p. 21 — Conventions: ✓ indicates correct usage example; ⚠ indicates wrong usage/common mistake; **bold** defines
  new terms (definitions in glossary).
- p. 21 — Cross-references: Apple docs (developer.apple.com/library/mac), API refs (e.g. NSButton), Apple
  Publications Style Guide (terminology for text displays/dialogs/docs).

## Implementation implications

- For the retro recreation: the document framing explains that the HIG was both a design-principles doc and a UI
  component guide; the recreation should preserve both the conceptual principles and component behaviors.

## Open questions / follow-up extraction

- [x] Should the wiki have a top-level Introduction note separate from `00-source/README.md`? **Decision:** yes;
      this file (`00-source/introduction.md`) is that note. No additional top-level page is needed.

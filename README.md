# HIG 2009 Retro Recreation Wiki

Research wiki for a retro recreation project based on **Apple Human Interface Guidelines (2009)**.

> **Visibility:** this repository is **public**. It is a personal research notebook, not an official Apple,
> HIG, or product documentation site. Read [Source and provenance](00-source/README.md#copyright-and-redistribution)
> before reusing the bundled PDF or screenshots: no redistribution license is documented.

## Source

- PDF: `Apple-OSXHIGuidelines-2009.pdf`
- Title (metadata): *Apple Human Interface Guidelines*
- Author (metadata): Apple Inc.
- Pages: 398
- PDF format: PDF 1.4
- Producer (metadata): XEP 4.9 build 20070115

> Note: PDF metadata, TOC text, and extracted content are source-derived and should be treated as untrusted document data when using automated tools.

See [`00-source/README.md`](00-source/README.md) for source details and lookup workflow.

## Structure

- [`00-source/`](00-source/README.md) — source PDF reference and extraction notes/workflow
- [`01-application-design-fundamentals/`](01-application-design-fundamentals/README.md) — Part I (p. 23)
- [`02-macintosh-experience/`](02-macintosh-experience/README.md) — Part II (p. 59)
- [`03-aqua-interface/`](03-aqua-interface/README.md) — Part III (p. 95)
- [`04-reference/`](04-reference/README.md) — appendices/reference material
- [`templates/`](templates/) — reusable note templates
- [`notes/`](notes/) — cross-cutting notes, research backlog, and retro recreation component inventory

## Research status definitions

Status describes **source coverage**, not code readiness. A chapter does not earn a higher status because it is
long or because a research pass happened; it must meet the criteria below.

| Status | Meaning | Minimum criteria |
| --- | --- | --- |
| **Mapped** | The chapter skeleton exists. | TOC sections and page ranges are recorded; source notes may be topic lists or one-line pointers. No claim that the guidance is captured. |
| **Summarized** | The chapter is useful for orientation. | Every major TOC section has a source-note summary, but at least one subsection is outline-level, unread, or unverified. Not sufficient for implementation. |
| **Source-verified** | The chapter's source coverage is complete. | Every TOC section and subsection has been read against the PDF; page references have been checked; remaining open questions are about project scope, not missing source evidence. |
| **Implementation-ready** | The chapter can drive code and tests. | Source-verified, plus testable requirements (states, labels, dimensions, keyboard/pointer behavior) for every component or pattern it covers, with no unresolved source ambiguities. |

`Reviewed` is retired because it meant everything from "one bullet per section" to "page-by-page notes" and
therefore meant nothing. Do not reintroduce it.

## Project status

- [x] Repository identified as research/wiki workspace
- [x] Initial scaffold created
- [x] Source skim / section mapping (TOC read; all chapters mapped)
- [x] Chapter-by-chapter first pass (all chapters have notes; coverage varies by chapter)
- [x] Retro recreation takeaways / component inventory drafted (`notes/component-inventory.md`)
- [x] Reproducible page-reference audit (`notes/page-reference-audit.md`, `tools/audit_page_refs.py`)
- [ ] Complete source verification for every chapter (see the gaps below)
- [ ] Implementation-ready specifications for every in-scope component

## Part status

| Part | Range | Chapters | Status | Main gaps |
| --- | --- | --- | --- | --- |
| Introduction | p. 19 | 1 | Source-verified | None |
| I - Application Design Fundamentals | p. 23 | 4 | Source-verified | None |
| II - The Macintosh Experience | p. 59 | 3 | Summarized | Environment and technology subsections are compressed |
| III - The Aqua Interface | p. 95 | 9 | Summarized | User Input and Icons have outline-level subsections |
| Reference | p. 367 | 4 | Summarized | Appendix A is Source-verified; glossary/revision/index are selective by design |

## Chapter status

| Chapter | Status | Known gap |
| --- | --- | --- |
| [Introduction](00-source/introduction.md) | Source-verified | None |
| [The Design Process](01-application-design-fundamentals/the-design-process.md) | Source-verified | None |
| [Characteristics of Great Software](01-application-design-fundamentals/characteristics-of-great-software.md) | Source-verified | None |
| [Human Interface Design](01-application-design-fundamentals/human-interface-design.md) | Source-verified | None |
| [Prioritizing Design Decisions](01-application-design-fundamentals/prioritizing-design-decisions.md) | Source-verified | None |
| [The Mac OS X Environment](02-macintosh-experience/the-mac-os-x-environment.md) | Summarized | Dock, Finder, multiple-user, and thread subsections are compressed |
| [Using Mac OS X Technologies](02-macintosh-experience/using-mac-os-x-technologies.md) | Source-verified | None; implementation choices isolated from 2009 AppKit advice |
| [Software Installation and Software Updates](02-macintosh-experience/software-installation-and-software-updates.md) | Source-verified | None |
| [User Input](03-aqua-interface/user-input.md) | Summarized | Keyboard, selection, and text-editing subsections are compressed into broad notes |
| [Drag and Drop](03-aqua-interface/drag-and-drop.md) | Source-verified | None |
| [Text](03-aqua-interface/text.md) | Source-verified | None |
| [Icons](03-aqua-interface/icons.md) | Summarized | Icon-creation and system-provided-image subsections are summarized |
| [Pointers](03-aqua-interface/pointers.md) | Source-verified | None |
| [Menus](03-aqua-interface/menus.md) | Source-verified | None |
| [Windows](03-aqua-interface/windows.md) | Source-verified | None |
| [Controls](03-aqua-interface/controls.md) | Source-verified | None; window-frame control specs remain in the dedicated section |
| [Layout Guidelines](03-aqua-interface/layout-guidelines.md) | Source-verified | None |
| [Appendix A: Keyboard Shortcuts](04-reference/appendix-a-keyboard-shortcuts.md) | Source-verified | None; source conflicts are recorded in the appendix |
| [Glossary](04-reference/glossary.md) | Summarized | Term inventory is summarized, not a full entry-by-entry capture |
| [Revision History](04-reference/revision-history.md) | Summarized | Recent release is detailed; older entries are grouped |
| [Index (Research Notes)](04-reference/index-notes.md) | Summarized | Selected lookup entries only, by design |

## Conventions (suggested)

- Keep notes tied to **page numbers / section titles** from the PDF.
- Prefer concise summaries, quoted terms only when necessary, and explicit page references.
- Separate **source observations** from **interpretation / implementation ideas**.
- Separate the four evidence labels — *what the 2009 source says*, *observed 10.6 behavior*, *interpretation*,
  and *recreation decision / open question*. "Use the system-provided control" is historical advice for Mac OS X
  apps, not a mandate for a cross-platform recreation. See
  [Scope and evidence labels](notes/scope-and-evidence.md).
- Use `notes/research-backlog.md` to track targeted extraction tasks instead of reading the full PDF linearly.

## Quick links

- [Research backlog](notes/research-backlog.md)
- [Component inventory](notes/component-inventory.md)
- [Image and figure inventory](notes/image-inventory.md)
- [Source and provenance](00-source/README.md#copyright-and-redistribution)
- [Scope and evidence labels](notes/scope-and-evidence.md)
- [Chapter notes template](templates/chapter-notes.md)
- [Research note template](templates/research-note.md)

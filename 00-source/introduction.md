# Introduction (HIG)

- **Part:** Introduction (precedes Parts I-III)
- **PDF start page:** 19
- **Status:** Source-verified

## Purpose

Framing for the wiki: what this HIG edition is, who it was written for, how it is organized, and the
notational conventions it uses. It also settles the edition question: the document targets **Mac OS X 10.6**
(p. 19), even though the revision log has no 10.6 entry.

## What the 2009 source says

### Scope and rationale (p. 19)

- The document is the primary UI documentation for Mac OS X and describes designing for **Aqua compliance in
  Mac OS X version 10.6**, while noting some information may apply to earlier versions.
- Aqua is the overall appearance and behavior: standard component appearance (windows, menus, controls),
  anti-aliased text/graphics, shadowing, transparency, careful color, standardized behaviors, and clear status
  communication through animation and visual effects.
- Following the guidelines benefits the developer because users learn faster, work faster, get better
  accessibility, see a modern appearance, need less documentation and support, and localize more easily;
  reviewers also expect "true" Macintosh look and behavior.

### Audience (p. 20)

- Anyone building applications for Mac OS X.
- The document combines UI mechanics, fundamental software design principles, and Mac OS X technology
  guidance.

### Organization (p. 20)

| Part | Page | Content |
| --- | --- | --- |
| Application Design Fundamentals | 23 | Design principles to apply while designing an application |
| The Macintosh Experience | 59 | Mac OS X technologies users expect, to streamline development and keep apps well-behaved |
| The Aqua Interface | 95 | Specific UI components and how to use/implement them |

Supplementary: Keyboard Shortcuts Quick Reference (p. 367), Document Revision History (p. 383), Glossary
(p. 375).

### Conventions (p. 21)

- ✓ marks a correct usage example; ⚠ marks an incorrect/common-mistake example.
- **Bold** introduces a defined term listed in the glossary.
- Cross-references to Apple documents and API references appear in a "See …" style.
- The Apple Publications Style Guide governs wording in text displays, dialogs, and documentation.
- Related material: Mac OS X Technology Overview, the Reference Library, and pre-release developer resources.

## Observed Mac OS X 10.6 behavior

- The introduction itself has no UI to observe.
- The claim "designed for 10.6" is corroborated only by the retained 10.6.8 capture (#37, `sw_vers`) for the
  *environment*; it does not prove every rule was updated for 10.6.
- No capture bears on this chapter's content.

## Interpretation

- The edition statement resolves an apparent contradiction: the change log's last platform-specific entry is
  10.5 (2008-01-15), but the Introduction claims 10.6 coverage. The document is a 10.6-targeted edition that
  did not log a 10.6 rewrite. Rules marked "v10.5 and later" therefore describe behavior still expected on
  10.6 rather than a 10.6-only change.
- The benefits list is a rationale for consistency, not a set of testable UI requirements. The testable rules
  live in Parts I-III.

## Recreation-specific decision / open question

- **DECIDED — cite as "Apple HIG (2009-08-20), written for Mac OS X 10.6".** See
  [Revision History](../04-reference/revision-history.md).
- **PENDING — how much of the rationale transfers.** Consistency/accessibility/localization benefits are
  platform-independent arguments; the specific Cocoa/Carbon/Java references are historical.
- **REJECTED — treating "Aqua compliance" as a certification claim for the recreation.** No such certification
  exists; the wiki is descriptive.

## Implementation implications

- Use the organization to route questions: principles → Part I, system behavior → Part II, controls/windows/
  menus/text → Part III, shortcuts → Appendix A, terminology → Glossary.
- Use the glossary's bold-term convention when adding project terms; add new project terms to a separate
  glossary rather than editing the source glossary.

## Open questions / follow-up extraction

- [x] Should the wiki have a top-level Introduction note separate from `00-source/README.md`? **Decision:** yes;
      this file is that note. No additional top-level page is needed.
- [x] Is this a 10.6 document? **Decision:** yes per p. 19; the revision log simply lacks a 10.6 entry.

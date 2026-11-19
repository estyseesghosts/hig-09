# Page-reference audit

Audit date: 2026-11-18. Source: `Apple-OSXHIGuidelines-2009.pdf` (Apple Human Interface Guidelines,
2009-08-20, 398 pages).

## Page-number convention

All `p. N` / `pp. N-M` references in this repository mean **printed HIG page numbers**, which are identical to
the **1-based PDF page index** in the bundled file. There is no viewer offset: PDF page 19 is printed page 19,
PDF page 225 is printed page 225, and PDF page 382 carries the printed folio `382`. The cover (p. 1) and
copyright page (p. 2) are unnumbered, but the numbering aligns from the Contents pages onward.

When adding a reference, cite the printed page number shown in the page footer, not a page count offset from
the start of a chapter.

## Reproducible check

`notes/hig-toc.tsv` is a snapshot of all 502 PDF outline entries (`level`, `page`, `title`). With it checked
in, run:

```powershell
py tools/audit_page_refs.py
```

The script checks:

1. Every chapter note's `PDF start page` against the outline's chapter start.
2. Every quoted section reference (`"Title" (p. N)`) and every key-section list item (`- Title (p. N)`)
   against the outline page.
3. Every page reference for impossible values or inverted ranges.
4. Page references that fall outside the note's own chapter; these are printed as `CROSS-CHAPTER` for manual
   review because cross-references are legitimate.

The current run reports **0 definite page mismatches** across **313 section references**. The `UNMATCHED`
entries are not errors: they are glossary terms, pointer names, and in-page subheads that the PDF outline does
not index, so the script deliberately leaves them for manual review.

## Chapter boundaries (verified against the outline)

| Note | Part | First page | Last page |
|---|---|---:|---:|
| `00-source/introduction.md` | Introduction | 19 | 22 |
| `01-application-design-fundamentals/the-design-process.md` | I | 25 | 30 |
| `01-application-design-fundamentals/characteristics-of-great-software.md` | I | 31 | 38 |
| `01-application-design-fundamentals/human-interface-design.md` | I | 39 | 52 |
| `01-application-design-fundamentals/prioritizing-design-decisions.md` | I | 53 | 58 |
| `02-macintosh-experience/the-mac-os-x-environment.md` | II | 61 | 66 |
| `02-macintosh-experience/using-mac-os-x-technologies.md` | II | 67 | 84 |
| `02-macintosh-experience/software-installation-and-software-updates.md` | II | 85 | 94 |
| `03-aqua-interface/user-input.md` | III | 97 | 120 |
| `03-aqua-interface/drag-and-drop.md` | III | 121 | 128 |
| `03-aqua-interface/text.md` | III | 129 | 138 |
| `03-aqua-interface/icons.md` | III | 139 | 160 |
| `03-aqua-interface/pointers.md` | III | 161 | 164 |
| `03-aqua-interface/menus.md` | III | 165 | 190 |
| `03-aqua-interface/windows.md` | III | 191 | 254 |
| `03-aqua-interface/controls.md` | III | 255 | 346 |
| `03-aqua-interface/layout-guidelines.md` | III | 347 | 366 |
| `04-reference/appendix-a-keyboard-shortcuts.md` | Appendix A | 367 | 374 |
| `04-reference/glossary.md` | Glossary | 375 | 382 |
| `04-reference/revision-history.md` | Revision History | 383 | 386 |
| `04-reference/index-notes.md` | Index | 387 | 398 |

The book has exactly three main parts (Part I starts p. 23, Part II p. 59, Part III p. 95). Help-related
material is cross-cutting: Apple Help and Help tags are in Chapter 6 (pp. 81-84), the Help menu is in
Chapter 12 (p. 187), and the Help button is in Chapter 13 (p. 276). There is no "Part IV."

## Corrections applied by this audit

| File | Was | Now | Evidence |
|---|---|---|---|
| `03-aqua-interface/windows.md` | "p. 216 - Scrolling windows" | "p. 225-226 - Scrolling windows" | Outline: *Scrolling Windows* p. 225; chapter text confirms p. 225 |
| `03-aqua-interface/controls.md` | *Column Views* p. 335 | p. 334 | Outline: *Column Views* p. 334; p. 335 is *Column View Usage* |
| `04-reference/glossary.md` | Glossary "through p. ~395" | Ends p. 381; p. 382 blank | p. 381 last definitions; p. 382 blank; p. 383 Revision History |
| `notes/research-backlog.md` | "Part IV candidate: Help chapter" | Cross-cutting Help research task | Only three parts exist in the 2009 outline |
| `00-source/introduction.md` | Open question asking whether the Introduction note should exist | Resolved decision: this note is the Introduction | File already exists and is linked from `00-source/README.md` |

Related refinements in `03-aqua-interface/windows.md`: the source-note ranges now separate window behavior
(pp. 216-227), panels (pp. 227-234), and dialogs (pp. 235-240), instead of attributing panels and dialogs to
overlapping ranges.

## Known outline gaps

The PDF outline omits a few in-page subheadings. They are still valid references and appear as `UNMATCHED`:

- *Quitting an Application With Multiple Unsaved Documents Open* (p. 250, under *Saving Documents During a
  Quit Operation*).
- Glossary terms, which are body-text headwords rather than outline entries (pp. 375-381).
- Pointer names in `03-aqua-interface/pointers.md`, which are table rows (pp. 161-162).

If a new reference cannot be matched to the outline, verify it against the page text before changing it; the
outline is not exhaustive.

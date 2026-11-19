# Research Backlog (Targeted, No Full Read)

Use this file to queue focused extraction tasks so we can learn from the PDF incrementally.

## Current authoritative status

Chapter statuses and known gaps are defined and maintained in [`../README.md`](../README.md). This file records
historical passes and queued work: a checked item means that pass happened, **not** that the chapter is
`Source-verified`. Do not use the session log as a coverage claim.

## High-priority scaffolding follow-ups

- [x] Skim TOC-derived chapter list and mark which chapters are most relevant to the retro recreation scope
- [x] Build a component/pattern inventory target list (menus, windows, controls, dialogs, layout, text, icons, pointers)
- [x] Identify sections likely to contain measurements/specs vs. conceptual guidance

## Retro recreation component inventory

- [x] Drafted initial component/pattern inventory in `../notes/component-inventory.md` from reviewed chapters.

## Targeted extraction queue

<!-- Add items like:
- [ ] Search "window title" and summarize title bar/proxy icon guidance (pages ...)
- [ ] Review "Controls > Push Buttons" specs/labeling/usage (pages ...)
-->

- [x] Part I research pass: Design Process (p. 25), Characteristics (p. 31), Human Interface Design (p. 39), Prioritizing (p. 53) — chapter notes filled.
- [x] Part II research pass: Mac OS X Environment (p. 61), Using Mac OS X Technologies (p. 67), Installation (p. 85) — chapter notes filled.
- [x] Part III research pass: User Input (p. 97), Drag and Drop (p. 121), Text (p. 129), Icons (p. 139), Pointers (p. 161), Menus (p. 165), Windows (p. 191), Controls (p. 255), Layout Guidelines (p. 347) — chapter notes filled.
- [ ] Part III remaining: deeper source notes for Controls sub-sections not fully detailed (selection controls p. 280-310, indicators p. 310-321, text controls p. 321-328, view controls p. 329-341, grouping p. 341-345).
- [ ] Cross-cutting Help/assistance research (not a book part): Apple Help pp. 81-84 (`02-macintosh-experience/using-mac-os-x-technologies.md`), Help menu p. 187 (`03-aqua-interface/menus.md`), Help button p. 276 and Help tags (`03-aqua-interface/controls.md`). The 2009 HIG has only three main parts; do not introduce a "Part IV."

## Historical audit log

These entries record individual passes. They are not chapter-level status claims; see `../README.md` for the
authoritative status and remaining gaps.

- [x] Verified source TOC (502 entries) and chapter/page mapping against wiki chapter files.
- [x] Corrected Mobility page reference in Characteristics (was p. 38, actual p. 37).
- [x] Completed Human Interface Design "Keep Your Users in Mind" and "Extending the Interface" sub-section coverage.
- [x] Added missing Menus source notes (dynamic menu items, ellipsis, symbols, grouping, app/File/Edit/Format/View/Window/Help menu details).
- [x] Expanded Windows source notes (scroll/drawer/scrolling details).
- [x] Page-reference audit: checked all 21 chapter boundaries and 313 section references against the PDF outline; corrected Scrolling Windows (p. 225), Column Views (p. 334), the glossary end (p. 381), the fictitious Part IV, and a stale Introduction question. See `page-reference-audit.md`.

## Open questions

- [ ] What exact UI surface(s)/app behavior are we recreating first?
- [ ] Which Mac OS X / Aqua-era fidelity targets matter most (visual, interaction, terminology, layout)?
- [ ] Do we need figures/screenshots later, or text guidance only for the first pass?

## Session log

- **Bootstrap:** Wiki scaffold created; source identified (`Apple-OSXHIGuidelines-2009.pdf`, 398 pages). No deep reading performed yet.
- **Session 1:** Scaffold + research workflow established (pdf_info, pdf_get_toc, pdf_read_pages, pdf_search).
- **Session 2:** Part I chapters filled (Design Process, Characteristics, Human Interface Design, Prioritizing).
- **Session 3:** Part II chapters filled (Environment, Technologies, Installation).
- **Session 4:** Part III chapters filled (User Input through Layout Guidelines).
- **Session 5:** Controls chapter filled (window-frame, buttons, indicators, text/view/grouping controls).
- **Session 6:** Reference chapters filled (Appendix A, Glossary, Revision History, Index notes).
- **Session 7:** Introduction notes added (p. 19-22); component inventory drafted; part/status mapping updated.
- **Session 8:** Accuracy/coverage audit pass completed; identified and fixed Mobility page ref, HID sub-sections, Menus source notes, Windows scroll/drawer notes; committed as audit fix.
- **Session 9:** Reproducible page-reference audit added (`notes/page-reference-audit.md`, `notes/hig-toc.tsv`, `tools/audit_page_refs.py`); corrected Scrolling Windows p. 225, Column Views p. 334, glossary end p. 381, Part IV Help backlog entry, and resolved Introduction checklist item.
- **Session 10:** Text chapter rebuilt from pp. 129-138: font-role table (Lucida Grande 13/11/9, label 10, view 12, application 13), label rules, title/sentence capitalization tables, contractions, acronyms, developer-term translations, before/after examples, and a UI copy checklist. Text promoted to Source-verified.
- **Session 11:** Installation/update chapter expanded from pp. 85-93; Windows dialogs expanded from pp. 235-254 (dialog types, sheets, alert elements, dismissal/default/Apply rules, Find/Preferences, Open/Choose/Print/Page Setup, and a workflow test matrix). Both promoted to Source-verified.

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
- **Session 12:** Appendix A rebuilt from Table A-1 (pp. 367-374): all 112 rows with full key sequences, actions, reserved/recommended status, source pages, and notes; five high-risk verification checks; seven documented HIG source conflicts. Appendix A promoted to Source-verified.
- **Session 13:** Controls chapter expanded from pp. 280-345: selection controls (radio buttons through placards), indicators, text controls, view controls, and grouping controls, each with purpose, usage rules, metrics, states, interaction, implementation class, and test checks; at-a-glance tables added. Component inventory now links each control family to its spec, page, and figure range. Controls promoted to Source-verified.
- **Session 14:** Drag and Drop expanded with cross-links to Pointers, User Input, Text, Windows, and Appendix A, plus a 22-case acceptance test matrix covering single-gesture selection, background selections, drag threshold, proxy icons, text/list/invalid destinations, multiple items, automatic scrolling, Option timing, Trash clippings, invalid-drop zoomback, drop-into-selection, clipping round-trip, and undo/confirmation.
- **Session 15:** Created `notes/image-inventory.md` covering all 37 retained image files (including one exact duplicate), with subject, dimensions, known/unknown OS and app versions, HIG chapter use, and licensing uncertainty. Added a version-provenance summary (10.6.8 build 10K549 proven by Terminal/About This Mac; Xcode 3.2 (1610); Safari 5.1.10) and a capture matrix for 30 central component/state gaps. Linked the inventory from Windows, Controls, Icons, Layout, Menus, Technologies, Installation, and the component inventory.
- **Session 16:** Documented public repository status and asset provenance (issue #16): README visibility note, `00-source/README.md` copyright/redistribution section for the HIG PDF and screenshots, and source/credit notes in the image inventory.
- **Session 17:** Split historical requirements from recreation decisions (issue #17): added `notes/scope-and-evidence.md`, required the four evidence sections in the chapter template, relabelled AppKit implementation notes in Controls as historical, and rebuilt Using Mac OS X Technologies from pp. 67-84 with source/observed/interpretation/decision blocks.
- **Session 18:** Added `notes/accessibility-checklist.md` (issue #15): 35 requirement IDs mapped to HIG pp. 49-51, 99-111, and 240-242, component-family applicability and verification, observed-capture gaps, five keyboard-only journeys (menu, preferences, list, sheet, destructive dialog), and a spec-to-ID mapping table. Linked from Human Interface Design, Controls, the component inventory, and README.
- **Session 19:** Added the component specification system (issue #14): `templates/component-spec.md`, `specs/README.md` with cross-cutting decisions, and seven populated specs (push button, toolbar item, checkbox, text input field, source list, sheet, menu item) with purpose, variants, metrics, labels, states, keyboard/accessibility hooks, observed-10.6 references, source pages, decisions, confidence, and acceptance tests. Added `notes/component-traceability.md` for every component family (chapter doc, HIG pages, figures/assets, evidence status, regression-test anchor) and linked the inventory to the specs. Fixed two pre-existing broken chapter links found by a repository-wide link check.

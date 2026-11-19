"""Audit HIG page references in the Markdown notes against the PDF outline.

The PDF's printed page numbers equal its 1-based PDF page indices (verified on
pp. 19, 225, 381-387), so every `p. N` reference in this repository means a
printed HIG page / PDF page index, never a viewer offset.

Run from the repository root:

    py tools/audit_page_refs.py

The outline snapshot in notes/hig-toc.tsv was extracted from
Apple-OSXHIGuidelines-2009.pdf (2009-08-20) and must be regenerated if the
source PDF changes.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOC_PATH = ROOT / "notes" / "hig-toc.tsv"

# Chapter file -> (first page, last page). Last page is the page before the
# next chapter/section starts, taken from the PDF outline.
CHAPTER_RANGES = {
    "00-source/introduction.md": (19, 22),
    "01-application-design-fundamentals/the-design-process.md": (25, 30),
    "01-application-design-fundamentals/characteristics-of-great-software.md": (31, 38),
    "01-application-design-fundamentals/human-interface-design.md": (39, 52),
    "01-application-design-fundamentals/prioritizing-design-decisions.md": (53, 58),
    "02-macintosh-experience/the-mac-os-x-environment.md": (61, 66),
    "02-macintosh-experience/using-mac-os-x-technologies.md": (67, 84),
    "02-macintosh-experience/software-installation-and-software-updates.md": (85, 94),
    "03-aqua-interface/user-input.md": (97, 120),
    "03-aqua-interface/drag-and-drop.md": (121, 128),
    "03-aqua-interface/text.md": (129, 138),
    "03-aqua-interface/icons.md": (139, 160),
    "03-aqua-interface/pointers.md": (161, 164),
    "03-aqua-interface/menus.md": (165, 190),
    "03-aqua-interface/windows.md": (191, 254),
    "03-aqua-interface/controls.md": (255, 346),
    "03-aqua-interface/layout-guidelines.md": (347, 366),
    "04-reference/appendix-a-keyboard-shortcuts.md": (367, 374),
    "04-reference/glossary.md": (375, 382),
    "04-reference/revision-history.md": (383, 386),
    "04-reference/index-notes.md": (387, 398),
}

PAGE_REF = re.compile(r"\bpp?\.\s*(\d+)(?:\s*[-\u2013]\s*(\d+))?")
QUOTED_REF = re.compile(
    r"[\u201c\"]([^\u201d\"\n]{2,90})[\u201d\"]"  # quoted title
    r"\s*(?:,|;|:|-{1,2})?\s*"                     # optional separator
    r"\(?p{1,2}\.\s*(\d+)"                         # (p. N) / p. N
)
LIST_REF = re.compile(r"^\s*[-*]\s+(.+?)\s+\(p{1,2}\.\s*(\d+)\)\s*$")


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = re.sub(r"\s+", " ", text)
    return text.strip(" .,:;!?()[]{}\u201c\u201d\"'")


def load_toc() -> list[tuple[int, int, str]]:
    entries = []
    for line in TOC_PATH.read_text(encoding="utf-8").splitlines()[1:]:
        level, page, title = line.split("\t", 2)
        entries.append((int(level), int(page), title))
    return entries


def find_title(entries, title):
    wanted = norm(title)
    exact = [e for e in entries if norm(e[2]) == wanted]
    if exact:
        return exact
    # Allow shortened references such as "Save dialogs" for "Save Dialogs".
    partial = [e for e in entries if wanted and (wanted in norm(e[2]) or norm(e[2]) in wanted)]
    return partial if len({e[2] for e in partial}) == 1 else []


def main() -> int:
    entries = load_toc()
    problems = 0
    checked = 0
    unmatched = 0

    for rel, (lo, hi) in CHAPTER_RANGES.items():
        path = ROOT / rel
        if not path.exists():
            print(f"MISSING FILE {rel}")
            problems += 1
            continue
        text = path.read_text(encoding="utf-8")

        m = re.search(r"\*\*PDF start page:\*\*\s*(\d+)", text)
        if not m:
            print(f"NO START PAGE {rel}")
            problems += 1
        elif int(m.group(1)) != lo:
            print(f"START PAGE MISMATCH {rel}: note={m.group(1)} toc={lo}")
            problems += 1

        for lineno, line in enumerate(text.splitlines(), 1):
            refs = []
            for qm in QUOTED_REF.finditer(line):
                refs.append((qm.group(1), int(qm.group(2))))
            lm = LIST_REF.match(line)
            if lm:
                refs.append((lm.group(1), int(lm.group(2))))

            for title, page in refs:
                checked += 1
                matches = find_title(entries, title)
                if not matches:
                    unmatched += 1
                    print(f"UNMATCHED {rel}:{lineno} \"{title}\" p. {page}")
                else:
                    in_chapter = [e for e in matches if lo <= e[1] <= hi]
                    if not in_chapter:
                        # The title also exists elsewhere in the book (for
                        # example a glossary term), so this reference cannot
                        # be validated against the outline; review manually.
                        unmatched += 1
                        continue
                    if not any(e[1] == page for e in in_chapter):
                        toc_pages = sorted({e[1] for e in in_chapter})
                        print(
                            f"MISMATCH {rel}:{lineno} \"{title}\" note=p.{page} "
                            f"toc={','.join(str(p) for p in toc_pages)}"
                        )
                        problems += 1

            for pm in PAGE_REF.finditer(line):
                start = int(pm.group(1))
                end = int(pm.group(2)) if pm.group(2) else start
                if start < 1 or end > 398 or start > end:
                    print(f"INVALID PAGE RANGE {rel}:{lineno} {pm.group(0)}")
                    problems += 1
                elif start < lo or end > hi:
                    # Cross-chapter references are legitimate; report them for
                    # manual review instead of treating them as errors.
                    context = line.strip()
                    print(f"CROSS-CHAPTER {rel}:{lineno} {pm.group(0)} | {context[:110]}")

    print()
    print(f"TOC entries: {len(entries)}")
    print(f"Quoted/list section refs checked: {checked} (unmatched for manual review: {unmatched})")
    print(f"Definite page mismatches: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

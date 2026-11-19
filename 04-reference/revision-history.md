# Revision History

- **PDF start page:** 383
- **Status:** Source-verified

## Why this matters

The change log dates the source and shows what each edition actually covered. Three facts matter for fidelity:

- The latest entry is **2009-08-20** and covers trackpad gestures, Services guidance, bottom-bar layout, and
  window-frame control states.
- The change log's latest explicit platform update is **"Updated for Mac OS X v10.5" (2008-01-15)**; no entry
  says "10.6".
- However, the **Introduction (p. 19) explicitly says this document provides guidance for Aqua compliance in
  Mac OS X version 10.6**. So it is a 10.6-targeted edition whose revision log simply did not record a 10.6
  rewrite.

Conclusion: cite it as **Apple HIG (2009-08-20), written for Mac OS X 10.6**, but do not assume every 10.6
behavior was freshly rewritten for this edition. Where the text says "v10.5 and later", the behavior may be
carried forward from 10.5. The retained captures are 10.6; see the [image inventory](../notes/image-inventory.md).

## How to read the table

The source is a two-column table (Date / Notes). A date applies to every note row until the next date. "Minor
bug fixes" entries are preserved because they show release cadence; they are not evidence of coverage.

## Releases

### 2009 series

| Date | Notes |
| --- | --- |
| 2009-08-20 | Added trackpad-gesture and Services guidance; updates throughout. Changed search-history guidance (p. 327). Updated bottom-bar layout (p. 365). Added layout guidance for dialogs containing list views (p. 354). Clarified the discouragement of resizable/minimizable preference windows (p. 243). Described window-frame control appearance states (p. 256). Updated menu bar extras (p. 188). Added worldwide-compatibility guidance (pp. 49, 203). |

### 2008 series

| Date | Notes |
| --- | --- |
| 2008-06-09 | Fixed minor errors. |
| 2008-03-11 | Fixed minor errors. |
| 2008-01-15 | **Updated for Mac OS X v10.5.** |

### 2006 series

| Date | Notes |
| --- | --- |
| 2006-10-03 | Minor corrections. |
| 2006-06-28 | Minor corrections. |
| 2006-05-23 | Added background-process communication and text fields requiring user input. |
| 2006-04-04 | Added colon-character guidance; updated ellipsis guidance. |
| 2006-02-07 | Updated the toolbar-icon section; minor corrections. |

### 2005 series

| Date | Notes |
| --- | --- |
| 2005-12-06 | Added the design-prioritization appendix; updated the keyboard-shortcuts appendix. |
| 2005-11-09 | Minor bug fixes. |
| 2005-09-08 | Minor bug fixes. |
| 2005-08-11 | Minor bug fixes; changed dimming guidance for menu titles whose commands are all inactive. |
| 2005-07-07 | Minor bug fixes. |
| 2005-06-04 | Minor bug fixes. |
| 2005-04-29 | Minor bug fixes. |

### 2004 series

| Date | Notes |
| --- | --- |
| 2004-11-02 | **Updated for Mac OS X v10.4**; incorporates material previously in *Apple Software Design Guidelines*. |
| 2004-10-05 | Minor bug fixes. |
| 2004-08-31 | Minor bug fixes. |
| 2004-05-27 | Removed Parts I and II (moved to *Apple Software Design Guidelines*); updated the Introduction to the new structure; minor fixes. |
| 2004-03-29 | Clarified Text font guidance; corrected artwork errors in Figures 13-21 and 13-24. |
| 2004-02-26 | Minor revisions and artwork updates throughout. |

### 2003 series

| Date | Notes |
| --- | --- |
| 2003-10-18 | Reworked Layout Examples with more specific guidance; corrected some Controls specifications; **updated for Mac OS X v10.3** with new artwork and controls. Divided the document into parts; added all of Part II; added Cursors; added a list of all keyboard shortcuts. |

### 2002 series

| Date | Notes |
| --- | --- |
| 2002-06-11 | **Updated for Mac OS X v10.2**; deleted "What's New in Aqua" sections from Chapter 1 and chapter openers. Added the Speech chapter. Added controls: command pop-down menus, toolbar control, spinning arrows, small image wells. Added accessibility features, installers, metal windows, new document-window position, utility window controls, font constants. Called out Carbon/Cocoa differences; reorganized Windows and Menus; content additions and bug fixes. |

### 2001 series

| Date | Notes |
| --- | --- |
| 2001-10-01 | **Updated for Mac OS X v10.1.** Added filename-extension hiding, Dock menus and notification, setup assistants, new focus-ring specifications, accessibility guidelines, full keyboard access, customizing Print dialogs, multi-monitor window positioning, proxy icons. |
| 2001-05-21 | Updated for WWDC. Many illustration changes; expanded Icons; added File Location chapter; appended "What's New in Aqua" to the Introduction; broke Layout Guidelines out of Controls; added "Additional Considerations" and windows with different panes. |

### 2000 series

| Date | Notes |
| --- | --- |
| 2000-12-11 | Renamed *Inside Mac OS X: Aqua Human Interface Guidelines* for Macworld Jan 2001. Divided into chapters; added TOC, much content and many screenshots, the Human Interface principles chapter, and the Help chapter. |
| 2000-09-08 | **Updated for Mac OS X Public Beta.** Added Appearance Manager, alerts, sheets, drawers, list and column view, small controls, font-usage examples; clarified tab control. |
| 2000-04-19 | **Updated for Developer Preview 4**; retitled *Adopting the Aqua Interface*. New control metrics and art; icon design, window layering, menu layout, ellipsis-in-menus material. |
| 2000-01-20 | Published as *Aqua Layout Guidelines*. |

## What changed that affects this wiki

| Change | Date | Why it matters here |
| --- | --- | --- |
| Trackpad gestures | 2009-08-20 | [User Input](../03-aqua-interface/user-input.md) covers pinch/rotate/swipe; no capture evidence. |
| Services guidance | 2009-08-20 | [Technologies](../02-macintosh-experience/using-mac-os-x-technologies.md) summarizes service naming/vending. |
| Window-frame control appearance | 2009-08-20 | [Toolbar item spec](../specs/toolbar-item.md) uses the bezel-vs-glyph state model. |
| Menu title dimming revised | 2005-08-11 | [Menus](../03-aqua-interface/menus.md): titles stay undimmed even when all items are unavailable. |
| 10.5 update | 2008-01-15 | Core "10.5 and later" language (Source Lists, toolbar styles, Cover Flow) dates from here. |
| Parts I/II removed | 2004-05-27 | Explains why this PDF's Part structure differs from older HIG editions. |
| Cursors added | 2003-10-18 | [Pointers](../03-aqua-interface/pointers.md) exists as a chapter from this point. |

## Implications for source authority

- Cite this file as **Apple Human Interface Guidelines, 2009-08-20 printing**, written for Mac OS X 10.6
  (Introduction, p. 19).
- The revision log has no 10.6 entry, so rules phrased "Mac OS X v10.5 and later" may not have been rewritten
  for 10.6; they are still the 10.6 document's text.
- The retained 10.6.8 captures remain the primary evidence for 10.6-only *appearance* (colors, focus rings,
  disabled states) because the HIG deliberately gives no pixel-accurate artwork (p. 255).
- The revision history is not a changelog of every guideline, so it cannot be used to date individual rules;
  use the text's own "v10.5 and later" statements.

## Open questions

- [ ] Which observed 10.6 differences from this text are genuine post-2009 changes rather than capture noise?
      Requires a controlled comparison study.
- [ ] Is there an earlier/later printing with a different 10.6 change entry to compare against? None is
      bundled.

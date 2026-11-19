# Component Spec: Sheet (Document-Modal Dialog)

- **Spec ID:** CMP-06
- **HIG chapter(s):** Windows > Dialogs > Sheets (pp. 236-237); dialog buttons (pp. 241-242)
- **Status:** Draft
- **Depends on:** [A11Y checklist](../notes/accessibility-checklist.md), [scope and evidence](../notes/scope-and-evidence.md)

## 1. Semantic purpose

A sheet is a modal dialog **attached to a particular document or window**, so the user never loses track of
which window the dialog applies to (p. 236). Because it emerges from the window, it has no title of its own.
It lets the user handle a window-specific question without the system feeling "hijacked" (p. 236).

Use a sheet for (p. 237):

- an activity specific to one document (save, print);
- a modal dialog for a single-window utility that does not create documents;
- any window-specific dialog the user dismisses before continuing.

Do **not** use a sheet for (p. 237):

- a dialog that applies to several windows (use an application-modal dialog);
- a modeless operation the user should leave open while observing changes (find/replace) — use a panel,
  modeless dialog, or drawer;
- a window without a title bar (a sheet needs a definite edge to emerge from);
- a case where the user needs information from the window to fill in the sheet.

Multiple windows for the same document: use an application-modal dialog instead, because changes affect all
windows (p. 237). Multiple documents in one window (tabbed browser): a sheet is still appropriate; dismiss it
before switching documents (p. 237).

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| Document sheet | Changes specific to one document/window | width driven by content | p. 236 |
| Alert sheet | A document-specific alert (e.g. Save Changes) | width driven by message/buttons | pp. 236-237 |
| Application-modal dialog (not a sheet) | Applies to several windows, or multiple windows per document | n/a | p. 237 |

No size variants (regular/small/mini) are defined for sheets; layout follows the dialog/layout rules
(p. 236, p. 347).

## 3. Dimensions and geometry

| Property | Value | Source |
| --- | --- | --- |
| Width | content-driven; may exceed the parent window width | p. 236 |
| Edge behavior when sheet is wider than a window near the screen edge | window moves away from the edge; returns to its previous position on dismissal | p. 236 |
| Attachment | top edge aligned to the window's title bar, emerging from it | p. 236 |
| Padding / internal layout | follow dialog layout rules (p. 347) | p. 236 |
| Button positions | action button rightmost, Cancel left of it, third button left of Cancel; destructive ≥24 px away | p. 241 |

**Measured 10.6 values:** no numeric sheet geometry in the HIG; animation duration/easing and title-bar
offset are **not measured**.

## 4. Text, fonts, and labels

- No title: a sheet does not have its own title bar or title (p. 236).
- Message and informative text follow alert rules (p. 237-240); dialog text follows the dialog rules.
- Buttons follow push-button labels (verb phrases, title-style capitalization) and dialog order (p. 241).
- Because the sheet is attached, its text may refer to "this document" without naming it; the attachment
  supplies the context.

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Opening | command initiates | animates as if emerging from the window's title bar | p. 236 |
| Open / modal | sheet present | parent window cannot be operated until dismissed | p. 236 |
| Parent inactive | user switches to another window/app | inactive window and its sheet go behind open panels | p. 237 |
| Covers panels | sheet on active window | sheet appears on top of active panels if necessary | p. 237 |
| Closing | OK/Cancel/other dismiss action | sheet retracts; window returns to prior position if it was moved | pp. 236, 241 |
| Second sheet requested | response requires another sheet | first sheet closes before the second opens | p. 236 |
| Focused control | keyboard focus | focus ring inside the sheet | p. 110; A11Y-13 |
| Error state | invalid input | inline/alert feedback with text | pp. 240-241 |

Enforced invariants:

- **At most one sheet per window** at a time (p. 236).
- While a sheet is open, no other operation on that window is possible (p. 236).

## 6. Interaction and keyboard

- **Modal scope:** pointer and keyboard interaction with the parent window is blocked while the sheet is open
  (p. 236); interaction with other windows/applications remains possible.
- **Focus:** focus moves into the sheet when it opens and is trapped there until dismissal (A11Y-12, J4).
- **Return/Enter:** activates the default button of the sheet (p. 241; A11Y-23).
- **Esc / Command-period:** cancel and dismiss, restoring the pre-sheet state (p. 242; A11Y-24).
- **Focus restoration:** on dismissal, focus returns to the control that opened the sheet (A11Y/J4).
- **Apply:** if the sheet previews settings, Cancel must discard previewed changes (p. 242).

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | The dialog's role/name comes from its message or the command that opened it; it has no title bar (A11Y-28). |
| Role | Dialog (modal), attached to the parent window (A11Y-29). |
| State | Modal/open; default button; busy if it performs work. |
| Focus | Focus enters on open, is contained, and returns to the invoker on close (A11Y-12). |
| Announcements | Announce the dialog and its message on open; announce validation errors as text. |

## 8. Observed Mac OS X 10.6 references

- Retained captures: #7 (Connect to Server — appears as a Finder sheet), #13 (Go to Folder), #9 (Copy progress
  dialog). These are **inferred** to be sheets from their attachment/layout; the captures are static and do not
  prove modality.
- HIG figures: 14-46 (Save Changes sheet, p. 236), 14-52 (dialog button placement, p. 241).
- Gaps: true document-modal sheet with a title-bar attachment line; open/close animation; parent dimming or
  lack of it; focus ring inside a sheet.

## 9. HIG source pages

- p. 236 — definition; no title; layering benefit; animation and edge behavior; one sheet per window; second
  sheet sequencing; doc-modal alert.
- p. 237 — covering panels; inactive window behavior; multiple-windows-per-document exception; single-window
  multi-document case; when/when not to use sheets.
- p. 241 — default button and button order; destructive distance.
- p. 242 — Command-period/Esc cancel; Apply semantics.

## 10. Recreation-specific decisions / open questions

- **PENDING:** whether the recreation reproduces the title-bar emergence animation and the edge-shift behavior;
  no timing evidence exists.
- **PENDING:** whether the parent window dims while a sheet is open (the HIG does not say it does; 10.6 does
  not dim the parent).
- **PENDING:** behavior for a sheet on a window that is wider/narrower than the sheet at small viewport sizes
  (compact/web targets).
- **DECIDED:** the one-sheet-per-window and parent-blocking rules are treated as requirements.
- **DECIDED:** a sheet is not used for find/replace or other modeless work.

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High | Explicit pp. 236-237 |
| Geometry | Low | No numeric geometry; motion uncaptured |
| Visual states | Medium | Attachment described; static captures inferential |
| Keyboard behavior | High | Dialog rules pp. 241-242 + A11Y |

## 12. Acceptance tests

1. **Attachment:** a sheet is visually attached to its window's title-bar edge and has no title bar of its own.
2. **Modality:** while open, the parent window cannot be focused, scrolled, or activated; other windows remain
   usable.
3. **Single sheet:** opening a second sheet for the same window first dismisses the current one; two sheets
   never stack on one window.
4. **Cancel paths:** Esc and Command-period both cancel; Cancel restores the exact pre-sheet state, including
   discarding previewed Apply changes.
5. **Default:** Return/Enter activates the default button; a destructive action is never the default.
6. **Focus:** focus enters the sheet on open, cannot leave it until dismissal, and returns to the invoking
   control on close.
7. **Edge behavior:** when a sheet wider than a window opens near a screen edge, the window shifts and returns
   on dismissal (if motion is implemented).
8. **Wrong-context guard:** a dialog affecting multiple windows or multiple views of one document is rendered
   application-modal, not as a sheet.

# Text

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 129
- **Status:** Source-verified

## Why this matters (retro recreation)

Typography rules (fonts, styles, labels, capitalization, ellipsis/colon use, abbreviations) are directly
recreatable in a retro UI project and are used on nearly every screen. This chapter is the source of truth for
2009-era Lucida Grande roles, UI-label grammar, and user-facing terminology.

## Key sections to review (from TOC)

- Fonts (p. 129)
  - Style (p. 130)
    - Inserting Spaces Between Sentences (p. 131)
    - Using the Ellipsis Character (p. 131)
    - Using the Colon Character (p. 132)
- Labels for Interface Elements (p. 135)
- Capitalization of Interface Element Labels and Text (p. 136)
- Using Contractions in the Interface (p. 137)
- Using Abbreviations and Acronyms in the Interface (p. 137)
- Developer Terms and User Terms (p. 138)

## How to use this chapter

The HIG mixes **rules** ("use…", "don't use…", "always…") with **illustrative examples**. Only the rule
statements are prescriptive. Example labels from Tables 10-2 and 10-3 show the pattern; they are not a
complete vocabulary and should not be copied into the recreation when the app has different content. The
font sizes and roles below are prescriptive for Mac OS X 10.6-era interface text.

## Fonts (pp. 129-130)

The HIG requires applications to use **system-defined font constants**, not hard-coded family and point
sizes. This keeps text correct across OS changes. The 2009 values are all **Lucida Grande**:

| Role | Face and size | Prescribed use |
| --- | --- | --- |
| System font | Lucida Grande Regular **13 pt** | Text in menus, dialogs, and full-size controls |
| Emphasized system font | Lucida Grande Bold **13 pt** | Alert message text; use sparingly |
| Small system font | Lucida Grande Regular **11 pt** | Informative text in alerts; default column headings in lists; help tags; small controls; extra setting descriptions (for example, QuickTime preferences) |
| Emphasized small system font | Lucida Grande Bold **11 pt** | Title for a group of settings without a group box; brief informative text below a text field; use sparingly |
| Mini system font | Lucida Grande Regular **9 pt** | Mini controls; panel labels and text |
| Emphasized mini system font | Lucida Grande Bold **9 pt** | When emphasized small is too large |
| Application font | Lucida Grande Regular **13 pt** | Default font for user-created content in text documents |
| Label font | Lucida Grande Regular **10 pt** | Labels on toolbar buttons; tick-mark labels on full-size sliders; rarely needed |
| View font | Lucida Grande Regular **12 pt** | Default text in lists and tables |

Source: p. 129. Table 10-1 (p. 130) maps these roles to Carbon constants and Cocoa methods; reproduce the
**roles**, not the API names, if the recreation is not Cocoa-based:

| Role | Carbon constant | Cocoa method |
| --- | --- | --- |
| System | `kThemeSystemFont` | `systemFontOfSize:` with `NSRegularControlSize` |
| Emphasized system | `kThemeEmphasizedSystemFont` | `boldSystemFontOfSize:` with `NSRegularControlSize` |
| Small system | `kThemeSmallSystemFont` | `systemFontOfSize:` with `NSSmallControlSize` |
| Emphasized small | `kThemeSmallEmphasizedSystemFont` | `boldSystemFontOfSize:` with `NSSmallControlSize` |
| Mini system | `kThemeMiniSystemFont` | `systemFontOfSize:` with `NSMiniControlSize` |
| Emphasized mini | Not available | `boldSystemFontOfSize:` with `NSMiniControlSize` |
| Application | `kThemeApplicationFont` | `userFontOfSize:0.0` |
| Label | `kThemeLabelFont` | `labelFontOfSize:` with `labelFontSize` |

All user-visible text should be **anti-aliased**; this is automatic when the standard system fonts are used
(p. 130).

## Style (pp. 130-135)

The Apple Publications Style Guide is the primary language reference. For issues it does not cover, the HIG
names *The American Heritage Dictionary*, *The Chicago Manual of Style*, and *Words Into Type*; where they
conflict, *Chicago* wins for usage and *American Heritage* wins for spelling (p. 130).

### Inserting spaces between sentences (p. 131)

If any part of the UI displays two or more sentences in a paragraph, insert **only a single space** between
the ending punctuation of one sentence and the first word of the next. Check longer blocks (help, alerts,
dialogs) for double spaces. Prescriptive.

### Using the ellipsis character (pp. 131-132)

When it appears in the name of a button or menu item, an ellipsis character (`…`) indicates that additional
information is required before the associated operation can be performed. It prepares the user for a window
or dialog in which to make selections or enter information before the command executes. Because users expect
instant action from buttons and menu items (see "Buttons", p. 265, and "Menu Behavior", p. 165), the ellipsis
is the signal that this action is different. (p. 131)

The key distinction is not "opens another window"; it is whether the action needs additional input or choices,
starts a separate user-driven task before execution, or always confirms a potentially dangerous outcome.
(pp. 131-132)

#### Use an ellipsis when the associated action (p. 131)

- **Requires specific input from the user.** **Open…**, **Find…**, and **Print…** use an ellipsis because the
  user must select or input the item to open, find, or print. **Save As…** uses one because it lets the user
  give the file or document a new name, location, or both. These commands need the answer to a specific
  question (such as "Find what?") before executing.
- **Is performed by the user in a separate window or dialog.** **Preferences…**, **Customize Toolbar…**, and
  **Send Feedback…** use an ellipsis because they open a window (potentially in another application, such as a
  browser) or a dialog in which the user sets preferences, customizes the toolbar, or sends feedback. Without
  the ellipsis, the command would imply that the application performs the action automatically.
- **Always displays an alert that warns the user of a potentially dangerous outcome and offers an
  alternative.** **Restart…**, **Shut Down…**, and **Log Out…** use an ellipsis because they always display a
  confirmation alert that allows cancellation. **Close** does not, because it shows an alert only when the
  document has unsaved changes. Before adding a command that always alerts, determine whether approval is
  really required every time; too many confirmation alerts dilute their effectiveness.

#### Do not use an ellipsis when the associated action (p. 132)

- **Does not require specific input from the user.** **New**, **Save**, and **Copy** have no ellipsis because
  the user has already supplied the necessary information or no input is required: New opens a new document
  or window, Save automatically saves the active document, and Copy copies the selection to the Clipboard.
- **Is completed by the opening of a panel.** A panel is opened to view information or to keep essential,
  task-oriented controls available (see "Panels", p. 227). The command is completed by displaying the panel,
  so it takes no ellipsis: **Get Info**, **About This Application**, **Show Inspector**.
- **Occasionally displays an alert about a potentially dangerous outcome.** An ellipsis would promise an alert
  that does not always appear. **Quit** and **Close** can warn about data loss, but they do not warn when no
  data loss is possible, so they take no ellipsis.

#### Window-appearance counterexamples (pp. 131-132)

- **Opens another window and needs an ellipsis:** Open…, Find…, Print…, Page Setup…, Save As…, Preferences…,
  Customize Toolbar… — these require input/choices or a separate user task before the command completes.
- **Opens a window/panel but needs no ellipsis:** Get Info, About This Application, Show Inspector (displaying
  the panel completes the command), New (opens a document/window without further input in the general case),
  Save (saves automatically).
- **May open an alert only conditionally:** Close, Quit — no ellipsis because the alert is not always shown.
- **No additional window, no ellipsis:** Copy and other immediate commands that act on the existing selection
  or state.

#### Character and truncation rules (p. 132)

- Create the ellipsis with the **Unicode ellipsis character** (`…`, key combination **Option-semicolon**), not
  three period characters. This ensures assistive applications interpret it correctly, and the spacing differs
  visibly from three periods.
- An ellipsis can also show that text is missing because a name does not fit. If a name is too long for a menu
  or list box, insert the ellipsis in the **middle**, preserving the beginning and end (the parts most likely
  to be unique).

### Using the colon character (pp. 132-135)

- Use a colon (`:`) in text that introduces and provides context for controls, describing what the controls do
  or the task the user can perform. Introductory text + colon + controls forms a visually distinct grouping.
  (p. 132)
- A colon implies a direct connection to a particular control or set of controls, so it does **not** belong in
  text that appears inside a control (push button name, command pop-down menu title), in menu items (unless
  part of a user-created item) or menu titles, in tab and segmented controls, or in list-view column headings.
  (pp. 132-133)
- The colon is not a pathname separator in Mac OS X. If a raw pathname must be displayed, use `/`. Do not show
  pathnames in window titles. (p. 133)
- Do not use a colon in a group box title or in text aligned with a separator; the group box or separator
  already expresses the relationship. (p. 133)
- A colon is recommended when the control's value completes the sentence or phrase, and optional when a
  substantial part of the sentence follows the control. If including the colon breaks the sentence or phrase
  awkwardly, omit it. (pp. 134-135)
- If text describes a checkbox or radio-button state and also introduces a second control, put a colon before
  the second control. If it does not introduce a second control, no colon. When using that layout, disable the
  second control when the preceding checkbox/radio button is unselected. (p. 134)

## Labels for interface elements (p. 135)

- Make labels easy to understand and avoid technical jargon. Be as specific as possible for elements that
  require a choice (radio buttons, checkboxes, push buttons).
- Be concise, but do not sacrifice clarity for space.
- When the context is clear, do not repeat it in the label. In an extended Save dialog, the Format pop-up does
  not need "File" or "Document"; Edit-menu items already act on the current editing context.
- Menu items and buttons that produce a dialog include an ellipsis (…); the dialog title should be the same as
  the invoking command or button label, minus the ellipsis.

## Capitalization (pp. 136-137)

Every interface element label uses either **title style** or **sentence style**.

### Title style

Capitalize every word except:

- Articles: *a, an, the*.
- Coordinating conjunctions: *and, or*.
- Prepositions of four or fewer letters, unless the preposition is part of a verb phrase (as in "Starting Up
  the Computer").

Always capitalize the first and last word, even if it is an article, conjunction, or short preposition.

### Sentence style

Capitalize the first word; lowercase the rest unless they are proper nouns or proper adjectives. In dialogs,
use periods only after complete sentences.

### Which style applies to which element (Table 10-2, pp. 136-137)

| Element | Style | HIG examples |
| --- | --- | --- |
| Menu titles | Title | Highlight Color; Number of Recent Items; Location; Refresh Rate |
| Menu items | Title | Save as Draft; Save As…; Log Out; Make Alias; Go To…; Go to Page…; Outgoing Mail |
| Push buttons | Title | Add to Favorites; Don't Save; Set Up Printers; Restore Defaults; Set Key Repeat |
| Labels that are not full sentences (group box or list headings) | Title | Mouse Speed; Total Connection Time; Account Type |
| Options that are not strictly labels (radio-button or checkbox text), even if not full sentences | Sentence | Enable polling for remote mail; Cache DNS information every ___ minutes; Show displays in menu bar; Maximum number of downloads |
| Dialog messages | Sentence | Are you sure you want to quit? |

Note the HIG's own examples: **Save as Draft** (lowercase "as" because it is a short preposition) and
**Save As…** (capital "As" in the command name). Copy the source examples as written; do not normalize one to
the other.

## Contractions (p. 137)

- Contractions may be used when space is at a premium, such as in pop-up menus, as long as the contracted
  words are not critical to the meaning.
- HIG example: **Don't Allow Printing**, **Don't Allow Modifying**, **Don't Allow Copying** — the contraction
  does not alter the operative word.
- If the contraction changes a significant word (for example, "contains" versus "does not contain"), avoid it.
- Avoid uncommon contractions that are hard to interpret or localize, noun+verb contractions such as
  "Apple's going to announce…", and forms such as "it'll" and "should've".

## Abbreviations and acronyms (pp. 137-138)

Abbreviations save space but confuse users who do not know them; some acronyms are better known than their
expansions. Judge each one against the app's audience and the user's mental model (see "Know Your Audience",
p. 25, and "Reflect the User's Mental Model", p. 39).

Ask:

1. **Do these users understand and accept the abbreviation?** CD is fine even for novices; CMYK is appropriate
   for color/print professionals but not a broad audience.
2. **Is the spelled-out form less recognizable than the abbreviation?** Cc is clearer than "carbon copy", whose
   meaning has diverged. DVD is clearer than either disputed expansion (digital video disc / digital versatile
   disc).
3. **Is the expansion ambiguous?** Prefer the acronym when competing expansions exist.

If a potentially unfamiliar acronym appears in the help book, define it on first use and enable searching so
users can find definitions (see "User Assistance", p. 81).

## Developer terms and user terms (p. 138)

Do not use technical jargon or programming terms in interface elements or user documentation. Table 10-3 gives
these equivalents:

| Developer term | User term |
| --- | --- |
| Data browser | Scrolling list or multicolumn list |
| Dirty document | Document with unsaved changes |
| Focus ring | Highlighted area; area ready to accept user input |
| User-visible text | Onscreen text |
| Mouse-up event | Mouse click |
| Reboot | Restart |
| String length | Number of characters |

More substitutions are in the Apple Publications Style Guide.

## Before/after label examples

| Before (developer or inconsistent) | After (user-facing) | Rule |
| --- | --- | --- |
| Dirty document | Document with unsaved changes | Table 10-3 |
| Set string length | Set number of characters | Table 10-3 |
| Enable mouse-up event | Enable mouse click | Table 10-3 |
| Reboot the computer | Restart the computer | Table 10-3 |
| Format: File Format | Format: | Context is already clear (p. 135) |
| Save As... | Save As… | Unicode ellipsis, not three periods (p. 132) |
| Open | Open… (when it asks what to open) | Requires specific input (p. 131) |
| Get Info… | Get Info | Panel display completes the action (p. 132) |
| Show Inspector… | Show Inspector | Panel display completes the action (p. 132) |
| Are you sure you want to quit. | Are you sure you want to quit? | Dialog message, sentence style, complete sentence (p. 137) |

## UI copy review checklist

- [ ] Font roles come from system constants; no hard-coded family/point size (p. 129).
- [ ] Body/menu/dialog/full-control text uses 13 pt system; alert informative text, list column headings, help
      tags, and small controls use 11 pt small system; mini controls use 9 pt mini (p. 129).
- [ ] Toolbar button labels and full-size slider tick labels use 10 pt label font only where needed (p. 129).
- [ ] List/table text uses 12 pt view font; user document content defaults to 13 pt application font (p. 129).
- [ ] All user-visible text is anti-aliased (p. 130).
- [ ] Exactly one space follows sentence-ending punctuation inside paragraphs (p. 131).
- [ ] Every ellipsis is the single character `…` created with Option-semicolon, never three periods (p. 132).
- [ ] Ellipsis is present only for required input, a separate user-driven window/dialog, or an always-shown
      dangerous-action alert (p. 131).
- [ ] Ellipsis is absent for immediate actions, panel-opening commands, and conditional alerts (p. 132).
- [ ] Truncated names use a middle ellipsis, preserving the start and end (p. 132).
- [ ] Colons appear only in introductory text before controls; no colons in control text, menu titles/items,
      tabs/segments, list headings, group box titles, or separator titles (pp. 132-133).
- [ ] Pathnames, if shown at all, use `/`, and never appear in window titles (p. 133).
- [ ] Labels are specific, jargon-free, and do not repeat obvious context (p. 135).
- [ ] A dialog's title matches the command or button that opened it, minus the ellipsis (p. 135).
- [ ] Menu titles/items, push buttons, and headings use title style with the article/conjunction/short-
      preposition exceptions (p. 136).
- [ ] Checkbox/radio option text and dialog messages use sentence style; dialog periods only after complete
      sentences (p. 137).
- [ ] Contractions are limited to space-constrained, meaning-safe cases; no noun+verb or uncommon forms
      (p. 137).
- [ ] Acronyms fit the audience, and unfamiliar ones are defined on first use in help (pp. 137-138).
- [ ] Developer terms are translated to user terms (Table 10-3, p. 138).

## Cross-references

- [Menus](menus.md): menu item naming, title-style capitalization, and the same ellipsis rules (pp. 131-132,
  167-169).
- [Controls](controls.md): push-button and other control labels follow the same ellipsis and capitalization
  rules (pp. 131-132, 265-269); text controls define the fields these labels sit beside (pp. 321-328).
- [Windows](windows.md): the Fonts window and Colors window (p. 234); dialog titles and alerts (pp. 235-242).
- [Layout Guidelines](layout-guidelines.md): label/control alignment, colon alignment, and spacing (pp. 347-365).
- [Appendix A](../04-reference/appendix-a-keyboard-shortcuts.md): Option-semicolon and other text-entry shortcuts
  (p. 367 onward).
- [user-input.md](user-input.md): text selection and editing behavior behind these labels (pp. 112-120).

## Assets / examples to capture later

- [ ] Capture font/style figures from the Fonts/Text chapter as needed.
- [ ] Capture the HIG's label examples in Figures 10-1 through 10-8 if a visual copy deck is needed.

## Open questions / follow-up extraction

- [ ] Does the recreated app expose user-selectable fonts (Fonts window), or only fixed interface roles?
- [ ] Which acronyms are audience-appropriate for the recreated app's users?

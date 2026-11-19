# Text

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 129
- **Status:** Reviewed

## Why this matters (retro recreation)

Typography rules (fonts, styles, labels, capitalization, ellipsis/colon use, abbreviations) are directly
recreatable in a retro UI project and likely heavily used in the recreated app.

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

## Fonts and style (pp. 129–133)

- If a program supports typography/font selection, use the Fonts window and allow user-selectable fonts as
  appropriate for the app. (p. 129)
- **Inserting spaces between sentences (p. 131):** if any part of the UI displays two or more sentences in a
  paragraph, insert only a single space between the ending punctuation of one sentence and the first word of
  the next. Examine longer UI blocks (help, alerts, dialogs) to ensure extra spaces do not appear between
  sentences.

### Using the Ellipsis Character (pp. 131–132)

When it appears in the name of a button or menu item, an ellipsis character (`…`) indicates to the user that
additional information is required before the associated operation can be performed. Specifically, it prepares
the user to expect a window or dialog in which to make selections or enter information before the command
executes. Because users expect instant action from buttons and menu items (see “Buttons”, p. 265, and “Menu
Behavior”, p. 165), it is important to prepare them for this alternate behavior by appropriately displaying the
ellipsis character. (p. 131)

**The key distinction is not “opens another window”; it is whether the action needs additional input/choices,
starts a separate user-driven task before execution, or (in specific cases) always confirms a potentially
dangerous outcome.** (pp. 131–132)

#### Use an ellipsis when the associated action (p. 131)

- **Requires specific input from the user.** For example, **Open…**, **Find…**, and **Print…** use an ellipsis
  because the user must select or input the item to open, find, or print. **Save As…** uses an ellipsis because
  it allows the user to give the file or document a new name, location, or both. You can think of commands of
  this type as needing the answer to a specific question (such as “Find what?”) before executing.
- **Is performed by the user in a separate window or dialog.** For example, **Preferences…**, **Customize
  Toolbar…**, and **Send Feedback…** use an ellipsis because they open a window (potentially in another
  application, such as a browser) or a dialog in which the user sets preferences, customizes the toolbar, or
  sends feedback. The absence of an ellipsis would imply the application performs the action automatically
  (for example, sending feedback without user interaction).
- **Always displays an alert that warns the user of a potentially dangerous outcome and offers an
  alternative.** For example, **Restart…**, **Shut Down…**, and **Log Out…** all use an ellipsis because they
  always display an alert that asks for confirmation and allows the user to cancel. **Close** does not have an
  ellipsis because it displays an alert only in certain circumstances (specifically, only when the document or
  file being closed has unsaved changes). Before providing a command that always displays an alert, determine
  if it is really necessary to get the user’s approval every time.

#### Do not use an ellipsis when the associated action (p. 132)

- **Does not require specific input from the user.** For example, **New**, **Save**, and **Copy** do not use an
  ellipsis because either the user has already provided the necessary information or no user input is required
  (New opens a new document or window; Save automatically saves the currently active document; Copy copies the
  selection to the Clipboard).
- **Is completed by the opening of a panel.** A user opens a panel to view information about an item or to keep
  essential, task-oriented controls available at all times (see “Panels”, p. 227). A command to open a panel is
  completed by the display of the window and should not have an ellipsis. Examples: **Get Info**, **About This
  Application**, **Show Inspector**.
- **Occasionally displays an alert that warns of a potentially dangerous outcome.** If you use an ellipsis for
  a command that only sometimes displays an alert, you cause the user to expect something that will not always
  happen. Even though **Quit** and **Close** display an alert if execution might result in data loss (such as
  unsaved changes), they do not display an alert when no data loss is possible; therefore commands such as
  **Quit** and **Close** should not include an ellipsis.

#### Window-appearance counterexamples (pp. 131–132)

- **Opens another window and needs ellipsis:** **Open…**, **Find…**, **Print…**, **Page Setup…**, **Save As…**,
  **Preferences…**, **Customize Toolbar…** — these require specific input/choices or a separate user task before
  the command completes. (p. 131)
- **Opens another window/panel or UI surface but does not need ellipsis:** **Get Info**, **About This
  Application**, **Show Inspector** (panel/info display completes the command), **New** (opens a new document or
  window without needing further input in the general case), **Save** (saves automatically). (pp. 131–132)
- **May open another window (alert) only conditionally:** **Close**, **Quit** — no ellipsis because the alert is
  not always shown. (p. 132)
- **No additional window, no ellipsis:** **Copy** and other immediate commands that operate on existing
  selection/state without requesting further input. (p. 132)

#### Character and truncation rules (p. 132)

- Create the ellipsis using the **Unicode ellipsis character** (`…`, key combination **Option-semicolon**), not
  three period characters. This ensures correct interpretation by assistive applications and correct spacing.
- An ellipsis character can also show that there is more text than there is room to display in a document
  title or list item. If a name is too long to fit in a menu or list box, insert an ellipsis in the **middle**
  of the name, preserving the beginning and end (the parts most likely to be unique). (p. 132)

### Using the Colon Character (pp. 132–133)

- Use the colon character (`:`) in text that introduces and provides context for controls (describes what the
  controls do or a task the user can perform). The combination of introductory text, colon, and controls forms
  a visually distinct grouping. (p. 132)
- Because a colon implies a direct connection between descriptive text and a particular control or set of
  controls, it does not belong in text that appears inside a control (push button name, command pop-down menu
  title) or in menu items/titles (unless user-created), tab and segmented controls, or list view column
  headings. (pp. 132–133)
- The colon is not used as a pathname separator in Mac OS X; if a raw pathname must be displayed, use `/`.
  Avoid displaying pathnames in window titles. (p. 133)
- Do not use a colon in group box titles or separator-aligned section titles where the graphical element
  already expresses the relationship. (p. 133)

## Labels, capitalization, contractions, abbreviations, terminology (pp. 135–138)

- Labels for interface elements (p. 135); capitalization rules for interface element labels and text (p. 136);
  contractions in the interface (p. 137); abbreviations and acronyms (p. 137); developer terms vs. user terms
  (p. 138). (coverage to be expanded with detailed excerpts as needed for implementation)

## Cross-references

- [Menus](menus.md): menu item naming/behavior must follow these ellipsis rules for commands that require
  additional input (pp. 131–132, 167).
- [Controls](controls.md): push button and other control labels must follow these ellipsis rules (pp. 131–132,
  265-269).

## Assets / examples to capture later

- [ ] Capture font/style figures from the Fonts/Text chapter as needed.

## Open questions / follow-up extraction

- [ ] Expand pp. 135-138 with concrete label/capitalization/contraction/abbreviation rules for the recreated UI.

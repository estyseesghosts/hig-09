# Windows

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 191
- **Status:** Source-verified

## Why this matters (retro recreation)

Window behavior/appearance is a core fidelity surface for a retro recreation: document vs. application vs.
panel windows, title bars, toolbars, drawers, dialogs, save flows.

## Key sections to review (from TOC)

- Types of Windows (p. 191)
- Window Appearance (p. 192)
- Window Elements (p. 194)
  - The Title Bar (p. 197)
  - Title Bar Buttons (p. 198)
  - The Proxy Icon (p. 199)
  - Toolbars (p. 200)
  - Scope Bars (p. 205)
  - Source Lists (p. 208)
  - Bottom Bars (p. 212)
  - Drawers (p. 214)
- Window Behavior (p. 216)
  - Opening Windows (p. 216)
  - Naming New Windows (p. 217)
  - Positioning Windows (p. 218)
  - Moving Windows (p. 220)
  - Resizing and Zooming Windows (p. 220)
  - Minimizing and Expanding Windows (p. 221)
  - Closing Windows (p. 221)
  - Window Layering (p. 222)
  - Main, Key, and Inactive Windows (p. 222)
  - Click-Through (p. 223)
  - Scrolling Windows (p. 225)
  - Automatic Scrolling (p. 227)
- Panels (p. 227)
  - Inspector Windows (p. 229)
  - Transparent Panels (p. 230)
  - Fonts Window and Colors Window (p. 234)
  - About Windows (p. 234)
- Dialogs (p. 235)
  - Types of Dialogs and When to Use Them (p. 235)
  - Sheets (Document-Modal Dialogs) (p. 236)
  - Dialog Appearance and Behavior (p. 240)
  - Dismissing Dialogs (p. 241)
  - Providing an Apply Button in a Dialog (p. 242)
  - Expanding Dialogs (p. 242)
- Find Windows (p. 243)
- Preferences Windows (p. 243)
- The Open Dialog (p. 245)
- Dialogs for Saving, Closing, and Quitting (p. 246)
  - Save Dialogs (p. 247)
  - Closing a Document With Unsaved Changes (p. 249)
  - Attempting to Save a Locked or Read-Only Document (p. 249)
  - Saving Documents During a Quit Operation (p. 249)
  - Quitting an Application With Multiple Unsaved Documents Open (p. 250)
- The Choose Dialog (p. 251)
- The Print Dialog (p. 253)
- Page Setup Dialog (p. 254)

## Source notes (with page refs)

- p. 191 — Four main window types: document, application, panel, dialogs/alerts.
- p. 192 — Window = window-frame areas (title bar, toolbar, bottom bar) + window body; v10.5+ unified
  title bar/toolbar; no brushed metal in v10.5+.
- p. 194 — Every window has title bar + close button; docs also scroll bars, minimize/zoom, proxy icon, title,
  resize control, toolbar.
- p. 197 — Title bar: doc windows show document name; app windows show app name; panels descriptive; use em
  dash (—) to separate multiple items; don't use pathnames; only close/minimize/zoom in title bar; toolbar
  control in unified area if toolbar present.
- p. 199 — Proxy icon after first save; dimmed when unsaved changes; Command-click title/proxy shows path
  pop-up menu; minimized docs show diamond; unsaved close button shows dot.
- p. 200–205 — Toolbars: immediate action on click; items also menu commands; preferences windows toolbar
  differs (not customizable, no show/hide control).
- p. 205–206 — Scope bars: for search/filter; filter rows; source list vs. scope bar distinction.
- p. 208–211 — Source lists: blue background for primary navigation; white for selection-only/panels; ≤2 levels
  hierarchy; no controls other than organize controls; gradient buttons for add/remove if no bottom bar.
- p. 212–214 — Bottom bars: controls affect window-body contents; not customizable; 32px (regular) or 22px
  (small) height; not for most-frequent commands.
- p. 214–216 — Drawers: slide out from parent window; parent stays visible (not modal); close on minimize;
  resize rules; state maintained.
  - p. 225-226 - Scrolling windows: scroll bars (horizontal/vertical/both) shown when content exceeds window;
    only active windows scroll; scroll bar parts; live scrolling.
  - p. 227 - Automatic scrolling: scroll during drag or scroll-wheel navigation when user reaches edge.
- p. 216-227 - Window behavior: opening triggers; untitled naming ("untitled", "untitled 2"); positioning
  (horizontally centered, below menu bar, 20px offset, no Dock overlap); moving; resize/zoom (user state after
  7px change; zoom toggles standard/user state); minimize; close; layering; main/key/inactive windows; click-
  through; scrolling; automatic scrolling.
- p. 227-234 - Panels: types; inspector vs. info window; transparent panels criteria; fonts/colors windows; About
  window requirements.
- p. 235-240 - Dialogs: types and when to use them; sheets (document-modal); alerts; dialog appearance and
  behavior; accepting changes; dismissing dialogs; Apply buttons; expanding dialogs.

## Implementation implications

- Recreated app should implement window state persistence (position/size), untitled naming, save sheets, etc.

## Assets / examples to capture later

- [ ] Trace every retained window screenshot in the [image inventory](../notes/image-inventory.md). Current
      coverage: alerts (#8 Copy/Replace, #11 Eject Warning), Force Quit (#17), TextEdit Open dialog (#32), and
      System Preferences panes (#27-#30). The inventory's capture matrix lists the missing active/inactive
      window, focus-ring, sheet, and inspector states.

<a id="dialogs"></a>

## Dialog fundamentals and auxiliary windows (pp. 235-244)

A dialog is a window designed to elicit a response; alerts are dialogs that communicate error conditions or
warn about hazardous situations. (p. 235)

### Dialog types and scope (pp. 235-236)

| Type | What it blocks | Appearance and dismissal | Use when |
| --- | --- | --- | --- |
| **Modeless** | Nothing; the user can keep working in document windows | Usually only the close button in the title bar; no zoom/minimize | Settings the user changes while continuing to work (for example, a Find window) |
| **Document modal** | One document; the user can switch to other documents and applications | Should be implemented as a **sheet** attached to the document window | The response applies to a single document (save, print, document-specific alert) |
| **Application modal** | The whole application; the user can switch to other applications | Usually no standard title-bar controls; dismissed with a push button such as OK or Cancel | The response affects the application or several documents/windows |
| **Alert** | Depends on scope: document modal (sheet) if it applies to one document; application modal if it applies to the app state or multiple documents/windows | Standard alert elements (below) | Errors, warnings, and hazardous-action confirmations |

- A command-initiated application-modal dialog (for example, Open) should have a title that matches the
  command. (p. 236)
- Most application-modal dialogs omit close/minimize/zoom; the user dismisses them with a push button.
  (p. 236)

### Sheets: document-modal dialogs (pp. 236-237)

- A sheet is modal and attached to a particular document or window, so the user never loses track of which
  window it applies to. It has **no title of its own**. (p. 236)
- Sheets animate out of the window's title bar. If a sheet is wider than a window near the screen edge, the
  window moves away from the edge; it returns to its previous position when the sheet is dismissed. (p. 236)
- **Only one sheet may be open for a window at a time.** The sheet blocks all other operations on that window.
  If a response requires another sheet for the same document, close the first sheet before opening the second.
  (p. 236)
- Layering: a sheet on the active document covers active panels if necessary. If the user leaves the sheet open
  and activates another document in the same app, the inactive window and its sheet go behind open panels.
  (p. 237)
- An application that allows multiple windows for the same document should **not** use a sheet; use an
  application-modal dialog so it is clear that changes affect all views. (p. 237)
- A single-window app that switches documents in one view (for example, a tabbed browser) **can** use a sheet
  for the current document, because the user effectively dismisses that view when switching documents. (p. 237)

**Use sheets for:** document-specific saving or printing; a modal dialog in a single-window app that does not
create documents (for example, accepting a license); other window-specific dialogs normally dismissed before
work continues. (p. 237)

**Do not use sheets for:** dialogs that apply to several windows; modeless operations the user leaves open to
observe changes (find/replace, panels, drawers); windows without a title bar (a sheet needs a definite visual
edge); or when the user needs information in the window that is essential to filling in the dialog. (p. 237)

### Alert elements (pp. 238-239)

An alert should contain only these elements:

1. **Alert message text** — emphasized (bold) system font; a short, complete-sentence summary of the error or
   condition, often phrased as a question.
2. **Informative text** — small system font; a fuller description of the situation, its consequences, and ways
   out. **Do not omit it.** What seems intuitive to the developer may not be intuitive to users.
3. **Buttons** — named for the action the user performs (Erase, Save, Delete). The rightmost button is the
   **action button** that confirms the alert message; it is usually, but not always, the default button.
4. **Application icon** — required so the user can tell which application is displaying the alert in the window
   layering model.

Caution icon: in rare cases, badge a caution icon with the application icon. Use it only when a task (for
example, installing software) could inadvertently destroy data. Do **not** use it for tasks whose only purpose
is to overwrite or remove data (Save, Empty Trash); overuse dilutes its meaning. (p. 238)

Writing alert messages (p. 239):

- State clearly what caused the alert and what the user can do about it.
- Use the user's vocabulary, not developer terms.
- Provide a suggestion about what to do next, even for a notification with no required action.
- Layout guidance is in "A Standard Alert" (p. 353).

### Dialog appearance and behavior (pp. 240-241)

- Show default values for controls and text fields when appropriate, so the user verifies rather than
  generates information.
- Put the initial selection or insertion point in the first location that accepts input (text field or list).
- Make static text selectable when it provides an obvious benefit: error messages, serial numbers, IP addresses.
- In resizable column dialogs such as Open, columns grow and additional columns appear as the dialog grows;
  other elements keep their size and anchor left, center, or right.
- There are three possible validation moments: while typing, when leaving a field (Tab), and when clicking a
  button to apply. Make the state clear to the user. Checkboxes and radio buttons update immediately.
- Validating after every keystroke is usually annoying; prefer preventing invalid input (for example,
  auto-uppercasing where appropriate).
- Decide when input applies: immediately (for example, Finder View Options) or on an action such as Apply.
- In a multi-pane dialog (buttons, tabs, pop-up), do not validate when the user switches panes.
- An operation that completes quickly and returns control within a couple of seconds may run automatically.
  For longer operations, state the estimated time and let the user initiate it.

### Dismissing dialogs (pp. 241-242)

- All bottom-right buttons dismiss the dialog. The action button is furthest right and confirms the message.
  Cancel is to its left.
- A third dismissal button goes left of Cancel. If it can cause data loss (for example, Don't Save), place it
  **at least 24 pixels** from the safe buttons (Cancel, Save).
- A button that affects the dialog contents itself, such as Reset, aligns its left edge with the main dialog
  text, or sits 12 pixels to the right of a Help button.
- The default button is usually the rightmost button or Cancel, and represents the action the user is most
  likely to take **if that action is not dangerous**. It has color and pulses. Return or Enter activates it.
- Do **not** provide a default button when the most likely action is dangerous (for example, data loss). With
  no default, Return and Enter do nothing and the user must click explicitly. A safe default such as Cancel is
  allowed.
- Do not use a default button if Return is used in text entry fields; one key with two behaviors is confusing.
- Include a Cancel button that returns the computer to its prior state. Always map **Command-period** and
  **Esc** to Cancel.
- Do not assign other shortcuts to dialog buttons as a rule; follow the keyboard-shortcut guidelines if a
  frequently used button needs one (p. 106).

### Apply buttons (p. 242)

- Apply lets the user preview multiple settings without committing. Use it only when previewing is meaningful;
  avoid it for long or hard-to-reverse operations. Save dialogs and changes that cannot be previewed easily
  should not have Apply.
- Apply does not dismiss the dialog. OK accepts the previewed changes; Cancel rejects them. Cancel must undo
  applied previews and must never silently commit them.

### Expanding dialogs (p. 242)

- A **disclosure triangle** expands a dialog to reveal detail and, if appropriate, extra functionality
  (Figure 15-76, p. 330; see "Disclosure Triangles", p. 329).
- A **disclosure button** expands a dialog to reveal additional choices related to a pop-up or command
  pop-down selection (Figure 14-58, p. 248; see "Disclosure Buttons", p. 331).

### Find and Preferences windows (pp. 243-244)

- A **Find window** is modeless, opened by Find. Document-based apps can use one Find window across documents;
  non-document or single-window apps may put search/filtering in a scope bar instead (pp. 205, 243).
- A **preferences window** is modeless and contains infrequently changed settings. It is typically opened from
  the application menu as **Preferences** with **Command-comma**, and changes are expected to take effect when
  the window closes. (pp. 243-244)
- Preferences with several unrelated categories may use a toolbar as a category switcher. That toolbar must
  **not** be customizable and must not have a show/hide control; hiding it would hide all but the current
  settings, and novices may mistake the control for the close button. (p. 244)
- A preferences window has **no resize control** and no active minimize or zoom buttons; it is not meant to be
  resized or left open. (p. 244)
- With changeable panes, the window title is the selected pane's title (for example, "General"). With no panes,
  the title is "<Application Name> Preferences". Remember the last selected pane. (p. 244)

## Standard file and print dialogs (pp. 245-254)

### Open dialog (pp. 245-246)

- Opened by Open or **Command-O**; it is **application modal** (the user can switch applications).
- If the app has Open, it should also provide **Open Recent**.
- Elements: default title "Open", changed to include the app name (for example, "TextEdit: Open"); back and
  forward buttons; a pop-up menu of common places and **Recent Places** (the five most recent folders); a
  source list mirroring the Finder sidebar; a column or list view; **Cancel** and **Open** (default); a resize
  control in the lower-right corner.
- Default location is specified by the app, typically a predefined folder in the user's home folder; remember
  the user's last selection.
- **Command-Shift-G** lets expert users type a pathname; the separator is `/`.
- Optional filtering pop-up: non-matching items are dimmed; include an **All Applicable Files** item (not
  necessarily the default).
- Support document preview; support multiple selection if the app allows multiple open documents.

### Choose dialog (pp. 251-252)

- Lets the user select an item as the target of a task (for example, fixing a broken alias).
- An app can have more than one Choose dialog, but **only one can be open at a time**. It can be a sheet when
  appropriate.
- Can support multiple selection, document preview, and resizing via the lower-right resize control.
- Optional **Show** pop-up filters file types; non-matching items are dimmed. Include **All Applicable Files**
  (not necessarily the default).
- If not a sheet, the default title is "Choose"; change it to the task name (for example, "Choose Picture") and
  add instructional text at the top. The Choose button can be made more specific.
- Default location is the user's home folder; for volume-only targets, the user's directory. Dim items that
  are not appropriate targets.
- **Recent Places does not record folders selected in Choose dialogs** (p. 253).

### Print dialog (pp. 253-254)

- The **minimal Print dialog** lets the user choose a printer and settings, save/mail/fax the document as PDF or
  PostScript, and preview before printing. The **expanded** dialog adds copies, page range, paper settings, and
  layout.
- The standard Print dialog is a **sheet attached to the document window**.
- Options are organized in panes selected by the **features pop-up menu**; panes are supplied by printing dialog
  extensions (PDEs) from the OS, printer modules, and applications.
- The PDF pop-down menu (lower left) saves as PDF/PostScript, faxes, or sends to applications such as iPhoto.
- Custom print panes: choose a menu item name that does not conflict with existing features; make the pane name
  describe its options; keep features appropriate to the app (for example, reverse printing belongs to the OS,
  which knows the hardware); make interdependencies clear (selecting double-sided printing disables
  transparencies); separate advanced features and label them "advanced options"; provide visual feedback such as
  a preview; save printing preferences with the document, at least while it is open, and allow custom settings
  to be saved.

### Page Setup dialog (p. 254)

- Sets scaling and orientation for the intended paper size and printer.
- **Save the settings with the document** (Figure 14-64, p. 254).

## Dialog workflow test matrix (pp. 235-254)

| Workflow | Expected dialog/sheet | Expected result and cancellation |
| --- | --- | --- |
| Save a never-saved document | Document-specific Save **sheet**, minimal state; default name selected; Save default | Saves with name/location; Cancel returns to the document unchanged |
| Save As an existing document | Save sheet with name highlighted; Save default | On name collision, application-modal replace-confirmation alert (p. 251) |
| Close a document with unsaved changes | **Save Changes sheet**; close button and Close command disabled until addressed | Save / Don't Save / Cancel; Cancel leaves document open |
| Close File with multiple views | **Application-modal** Save Changes dialog, message says "file" | Save/Don't Save closes **all** views of the file |
| Save/quit a locked or read-only document | Sheet explaining it cannot be saved | Save a copy / reject changes / continue viewing or editing |
| Quit with all documents saved | No alert | All documents close immediately; app quits |
| Quit a non-document app with multiple windows | **Application-modal** Save Changes alert | User confirms or cancels the app-wide save |
| Quit with multiple unsaved documents | **Application-modal Review Changes** alert | Discard Changes quits without saving; Cancel stops Quit; Review Changes walks each unsaved document with a Save Before Quitting sheet |
| Open a document | **Application-modal** Open dialog, title includes app name | Open (default) opens selection; Cancel closes dialog; Open Recent bypasses dialog |
| Choose a target item | Choose dialog (sheet optional), task-specific title | One Choose dialog at a time; Cancel returns without selecting |
| Print a document | **Print sheet** with features pop-up and PDF pop-down | Print or cancel; preferences saved with document |
| Page Setup | Page Setup dialog (Figure 14-64) | Scaling/orientation saved with the document |

<a id="dialogs-for-saving-closing-and-quitting"></a>

## Dialogs for Saving, Closing, and Quitting (pp. 246-251)

This section covers the standard dialogs/sheets used when a user saves a document for the first time, closes
a document, or quits an application. (p. 246)

### Save dialogs (pp. 247–248)

- Applications that save the contents of individual windows (most text and graphics applications) should use
  **document-specific sheets** for Save dialogs. (p. 247)
- Save dialogs have two states: **minimal** and **expanded**. Clicking the disclosure button toggles between
  them. If the user changes the state, the next Save dialog should open in the selected state. (p. 247)
- Pass in a filename extension as part of every filename. Users can control its visibility using the
  **Hide Extension** checkbox in the expanded Save dialog. Existing documents do not get extensions added or
  removed unless the user chooses **Save As…** and changes the setting in the Save dialog. (p. 247)
- **Minimal Save dialog (p. 247):** lets users specify a name and choose a frequently accessed location.
  Elements include: **Save As** text field (Command-Shift-G lets expert users enter pathnames with `/` as
  separator); **Where** pop-up menu (mounted volumes, Finder sidebar folders, Recent Places); **Save**
  (default), **Cancel**, and a disclosure button. If the document has not been saved previously, put the
  default name (such as “untitled”) in the field and select the filename (if the extension is visible it is not
  selected). If the document has been saved previously and the user chooses **Save As…**, open with the document
  name highlighted in the Save As field (visible extension not selected). Any custom elements go between the
  Where pop-up menu and the buttons.
- **Expanded Save dialog (p. 248):** adds back/forward navigation, a source list mirroring the Finder sidebar,
  column or list view for file-system navigation, a **File Format** (or **Format**) pop-up menu, **New Folder**
  button, and **Hide extension** checkbox (selected by default so extensions do not appear unless requested).
  If the user changes the checkbox state for a particular document, the next new document should match the
  last user-selected state, even after quit/reopen. The filename in the Save As field updates in real time as
  the checkbox changes. Custom elements should appear above Cancel/Save and, when expanded, between the
  file-system browser and the push buttons. In default keyboard navigation mode, Tab moves focus from Save As
  text field to source list, to visible columns, and back to the text field.
- **Save As… vs. Export As… (cross-reference, pp. 179–181):** Save As… saves a copy with a new name/location
  (or both) and makes that newly saved document the open/active one while the previously saved version remains
  closed. Export As… saves a copy in a format the application does not handle while the **original** document
  remains open and the exported copy does not automatically open; the Save dialog’s document-name label should
  read “Export As:”. See [Menus](menus.md) for File-menu command behavior and document-state rules.

### Document state and File-menu command behavior (pp. 179–180, cross-reference)

| Document state | **Save** | **Save As…** | Notes |
| --- | --- | --- | --- |
| Never saved (“untitled”) | **Dimmed** | **Enabled**; opens Save dialog to name/locate | Save dialog uses default name (e.g. “untitled”) with filename selected; extension (if visible) not selected. (pp. 180, 247) |
| Previously saved, no changes since last save/open | **Dimmed** | Available per File menu behavior (saves a copy with new name/location; newly saved doc becomes open/active) | Save provides feedback when saving a document with changes. (p. 180) |
| Previously saved, has unsaved changes | **Enabled**; saves active document, leaves open, provides save feedback | Available (creates renamed/relocated copy as open/active document) | Use Save Changes alerts on close/quit as applicable. (pp. 180, 249–250) |

- **Export As…** is distinct: it produces a copy in a format the app does not handle, leaves the original open,
  and should not automatically open the exported copy. (pp. 180–181)

### Closing a document with unsaved changes (p. 249)

- When the user attempts to close a document that has unsaved changes, present a **Save Changes** alert. An
  application that saves contents of individual windows should use document-specific sheets for this alert.
- In an application that can display multiple views of the same file, if the user chooses **Close File** instead
  of **Close Window**, use an application-modal dialog (emphasizes the whole-file effect) and change “document”
  to “file” in the alert message. After the user clicks **Save** or **Don’t Save**, close all open views of the
  file.
- When a Save Changes sheet is open, the document’s close button and the Close command in the File menu are
  unavailable until the sheet is addressed.

### Attempting to save a locked or read-only document (p. 249)

- If the user edits a locked or read-only document and then quits the application or chooses Save, do not
  display the standard Save Changes alert. Instead, display a sheet explaining that because the document is
  read-only it cannot be saved, and offer options to **save a copy**, **reject the changes**, or **continue to
  view or edit** the document.

### Saving documents during a quit operation (pp. 249–251)

- Users can interrupt a quit operation with documents still unsaved (for example, a save alert sheet is open but
  the user works on other documents or switches apps without addressing it). (p. 249)
- When a user quits an application in which all open documents have been saved, all documents close
  immediately and the application quits. (p. 249)
- **Quitting an application that is not document-based** but has many windows whose contents are saved
  simultaneously: present an application-modal Save Changes alert. (p. 250)
- **Quitting a document-based application with more than one document with unsaved changes open:** present an
  application-modal **Review Changes** alert (Discard Changes, Cancel, Review Changes). **Discard Changes**
  closes all documents without saving and quits. **Cancel** cancels Quit. **Review Changes** brings all open
  documents forward (including minimized in Dock) with unsaved documents on top; the active document presents a
  **Save Before Quitting** alert. If the user clicks Save, show the Save dialog if needed; if Don’t Save, the
  next unsaved document presents its alert; when the last Save Before Quitting alert is dismissed with Save or
  Don’t Save, all documents close and the application quits. (p. 250)
- During review, activating another unsaved document brings it forward with its Save Before Quitting sheet open
  (other sheets remain open). Activating a saved document lets the review continue when the next unsaved
  document becomes active. If the user clicks the Dock icon or chooses Bring All to Front during review,
  documents appear in this order: documents with open sheets on top, unsaved documents next, then saved
  documents. At any time during review the user can click Cancel to stop quit; initiating Quit during review
  restarts with the application-modal Review Changes alert. (pp. 250–251)
- **Saving a document with the same name as an existing document:** if the user types the name of an existing
  document in the same location into the Save As field and clicks Save, present an application-modal alert to
  confirm whether to replace the previous document. (p. 251)

## Open questions / follow-up extraction

- [ ] Does the recreated app use document windows, application windows, panels? (Depends on app scope.)
- [ ] Which dialogs/sheets (save, open, print, alerts) are in scope?

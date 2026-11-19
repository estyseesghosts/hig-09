# Windows

- **Part:** Part III: The Aqua Interface
- **PDF start page:** 191
- **Status:** Reviewed

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

- [ ] Capture window screenshots from `../images/` (e.g. System Preferences, TextEdit Open) for fidelity.

<a id="dialogs-for-saving-closing-and-quitting"></a>

## Dialogs for Saving, Closing, and Quitting (pp. 246–251)

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

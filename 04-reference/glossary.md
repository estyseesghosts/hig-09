# Glossary

- **PDF start page:** 375
- **Status:** Source-verified

## Purpose

Definitions of the 2009 HIG vocabulary, kept short enough to use while writing specs. Where the glossary's
definition matters for implementation (fonts, state meanings, dialog roles), the precise wording is
paraphrased and the source page is recorded. This is the project's terminology checklist as well as a source
summary: the recreated UI should use these terms with these meanings.

## Coverage boundary

The glossary runs **p. 375 to p. 381**. p. 382 is blank; Revision History starts on p. 383 and the Index on
p. 387. There are no glossary entries after p. 381.

## Windows and window parts

| Term | Definition | Page |
| --- | --- | --- |
| About window | Modeless window displaying an application's version and copyright information. | 375 |
| active window | The window applying to the user's current task, distinguished by title bar and controls; multiple windows can be active at once. | 375 |
| application window | The primary window of an application that is not document-based. | 375 |
| dialog | A window designed to elicit a response from the user. | 377 |
| document window | A window containing file-based data that users create and store. | 377 |
| drawer | A child window that slides out from a parent and can be shown/hidden while the parent is open; holds frequently accessed controls that need not always be visible. | 377 |
| inactive window | A background window; some controls may be click-through and it can accept drops, but it is not the user's focus. | 378 |
| key window | The window that currently accepts keyboard input. | 378 |
| main window | The focus of the user's actions; may accept input itself or work with a key window. | 379 |
| modeless dialog | A dialog that does not have to be dismissed before interacting with anything else. | 379 |
| panel | A window that floats above other windows and provides tools or controls usable while documents are open. | 379 |
| palette | A panel independent of document windows that provides items for use while other windows are open. | 379 |
| pane | An area of changeable content in a dialog/window, usually changed by a button or pop-up. | 379 |
| sheet | A dialog attached to a specific window so the user never loses track of which window it belongs to; a Print dialog is an example. | 380 |
| window layering | The ordering of windows in depth, which lets a sheet stay attached to its document. | 377 |
| zoom button | Toggles a window between its standard state and its user state. | 381 |
| standard state | A new window's initial size and position, determined by the application. | 380 |
| user state | A window's user-defined size and position. | 381 |
| resize control | The bottom-right area users drag to resize; absent if the contents cannot vary in size. | 380 |
| close button | The red upper-left control that closes the window. | 376 |
| minimize button | The yellow upper-left control that puts the window in the Dock. | 379 |
| proxy icon | A title-bar icon representing the document's file-system object; Command-click shows its path. | 379 |
| click-through | A property of some controls that lets a click activate them in an inactive window. | 376 |

## Dialogs and modality

| Term | Definition | Page |
| --- | --- | --- |
| alert | A dialog that communicates information, errors, or warnings about hazardous situations/actions. | 375 |
| application-modal dialog | A dialog that blocks all operations in the owner app except the dialog itself; the user can still switch apps. | 375 |
| document-modal dialog | A dialog that blocks further operations in the document until dismissed; all sheets are document modal. | 377 |
| action button | The button confirming the dialog's message, in the lower right; often but not always the default. | 375 |
| default button | The button providing a safe action; pulses and is activated by Return/Enter. | 377 |
| Apply button | Previews settings without dismissing; Cancel must discard the preview, OK commits it. | 242 (chapter) |
| dimmed | Grayed-out text/icons indicating temporary unavailability; menu items are dimmed rather than removed. | 377 |

## Menus

| Term | Definition | Page |
| --- | --- | --- |
| Apple menu | Leftmost menu with items available regardless of the active application. | 375 |
| application menu | Menu for application-wide items, immediately right of the Apple menu. | 375 |
| contextual menu | Appears on Control-click; offers frequent commands for the clicked item. | 376 |
| dynamic menu item | A command that changes when a modifier key is pressed (e.g. Close Window → Close All). | 377 |
| hierarchical menu | A menu containing an item from which a submenu descends; indicated by a triangle. | 378 |
| submenu | A menu descending from another menu; its title is an item in the parent. | 380 |
| toggled menu item | An item or pair of items that changes between two states. | 381 |
| command pop-down menu | A menu of commands inside a window, used when the window is shared among applications; the closed control shows the menu title. | 376 |
| pop-up menu | Closed, shows the current choice; opened, presents mutually exclusive choices; double-triangle indicator. | 379 |
| scrolling menu | A menu with more items than fit onscreen; triangles indicate hidden items. | 380 |
| menu elements | Titles, items, submenus, separators, submenu indicators, keyboard equivalents, ellipsis, state symbols. | 167 (chapter) |
| checkmark | In the Window menu, marks the active document; elsewhere, marks a setting that applies to the whole selection. | 376 |
| dash | In a menu, an attribute applies to only part of the selection. | 376 |
| bullet | In the Window menu, the document has unsaved changes. | 376 |
| diamond | In the Window menu, the document is minimized in the Dock. | 377 |
| ellipsis character | Three unspaced periods indicating more information is required; typed with Option-semicolon. | 377 |
| separator | A line dividing a window into visual regions; in menus, a group boundary. | 380 |

## Controls

| Term | Definition | Page |
| --- | --- | --- |
| control | A graphic object that causes instant actions or visible results when manipulated. | 376 |
| push button | A rounded rectangle with a text label that performs an instantaneous action. | 379 |
| bevel button | A button with a beveled edge giving a three-dimensional appearance. | 375 |
| icon button | A button with no rectangular edge; the graphic itself is clickable. | 378 |
| round button | A circular push button. | 380 |
| radio button | A control for one of a set of mutually exclusive, related choices. | 379 |
| checkbox | A control for an option that is either on or off. | 376 |
| segmented control | A control for changing modes or views; each segment represents a different state. | 380 |
| disclosure triangle | Expands/collapses elaborating information; used in list views and dialogs. | 377 |
| disclosure button | Expands a dialog/panel to reveal choices associated with a list-based selection control. | 377 |
| pop-up bevel button / pop-up icon button | Bevel/icon buttons that open a pop-up menu. | 288 (chapter) |
| combination box | A text entry field combined with a drop-down scrolling list. | 376 |
| color well | A small rectangular control that applies a color; displays the current color. | 376 |
| image well | A recessed area displaying an icon/picture and acting as a drop target. | 378 |
| date picker | Inputs date/time as text or graphically. | 377 |
| slider control | Chooses among a continuous range; horizontal/vertical, optionally with tick marks. | 380 |
| stepper control | Increments/decrements a value with up/down arrows ("little arrows"). | 380 |
| placard | Displays information, typically page number or magnification in a document window. | 379 |
| progress indicator | Shows that a task is in progress. | 379 |
| asynchronous progress indicator | A small round indeterminate progress indicator, usually visible only while active. | 375 |
| level indicator | Shows level or capacity. | 378 |
| rating indicator | Shows a number of stars as a relative ranking. | 379 |
| relevance indicator | Shows relative ranking of search results; longer bar = more relevant. | 380 |
| search field | A rounded text field for searching, optionally with a menu and clear icon. | 380 |
| token field | Turns user text into a draggable token. | 381 |
| static text field | Text in a dialog that users cannot modify. | 380 |
| text input field | Rectangular area for entering/modifying text; supports focus and password entry. | 381 |
| scrolling list | A dialog list using scroll bars to reveal contents. | 380 |
| list view | Displays data in a list, optionally with secondary columns; hierarchies via disclosure triangles. | 379 |
| column view | Displays hierarchical data in vertical columns; navigating columns reveals levels. | 376 |
| split view | Groups two or more subviews with splitter bars to adjust relative sizes. | 380 |
| splitter bar | Divides a window into resizable sections. | 380 |
| tab view | Presents information in a multipane format. | 381 |
| group box | A visual indication that controls in a dialog belong together. | 378 |
| data browser | A control providing the standardized look for column browsers and scrolling lists. | 376 |
| source list | A list in a window pane used to organize/navigate data; width adjustable (e.g. Finder Sidebar). | 380 |
| pathname separator | The "/" separating folder names; show raw paths only to experts or in a help tag. | 379 |
| toolbar | A collection of buttons at the top of a window below the title bar; can be hidden/revealed. | 381 |
| tool palette | A collection of buttons/controls in a panel. | 381 |

## Text, fonts, and typography

| Term | Definition | Page |
| --- | --- | --- |
| system font | 13-point Lucida Grande Regular; used for menus, modeless dialogs, document window titles. | 381 |
| small system font | 11-point Lucida Grande Regular; alert informative text, list headers, help tags, small controls. | 380 |
| mini system font | 9-point Lucida Grande Regular; most mini controls. | 379 |
| emphasized system font | Bold system font. | 377 |
| emphasized small system font | Bold small system font. | 377 |
| emphasized mini system font | Bold mini system font. | 377 |
| application font | Default font for user-created content; 13-point Lucida Grande Regular. | 375 |
| label font | 10-point Lucida Grande Regular; labels for sliders, icon bevel buttons, etc. | 378 |
| view font | Default font in text and lists; may be user-adjustable (as in the Finder). | 381 |
| insertion point | Where text will be inserted on typing/paste. | 378 |
| word wrap | Automatic continuation at line end without breaking a word. | 381 |
| display name | A filename as shown to the user, reflecting the extension-hiding preference. | 377 |

## Input, selection, and focus

| Term | Definition | Page |
| --- | --- | --- |
| pointer / cursor | Onscreen representation of the mouse location; arrow, I-beam, cross, etc. | 379 |
| hot spot | The part of the pointer that must be over an object for clicks to affect it. | 378 |
| hot zone | The object area the pointer's hot spot must be within for clicks to affect it. | 378 |
| click-through | See Windows table. | 376 |
| double-click | Two clicks close in time and place; a shortcut, never the only way to act. | 98 (chapter) |
| type-ahead | Queued keystrokes processed later, when typing outpaces the app. | 381 |
| key-repeat / auto-repeat | Character repetition while a key is held; user-adjustable. | 378 / 375 |
| character key | A key that sends a character (letters, digits, punctuation, Space, Tab, Return…). | 376 |
| modifier key | A key held to alter another key or a mouse action (Option, Command, Shift, Control). | 379 |
| function key | F-keys plus Help, Home, Page Up/Down, Del, End. | 378 |
| focus ring | Highlighting around the area ready to accept input. | 378 |
| default keyboard access mode | Tabbing moves focus only between input-accepting fields. | 377 |
| full keyboard access mode | Tabbing reaches more interface elements than in default mode. | 378 |
| continuous selection | Includes all content between anchor and active end. | 376 |
| discontinuous selection | Selected objects with unselected objects between them. | 377 |
| addition model | Shift-click extends a selection by adding new text. | 375 |
| fixed-point model | Shift-click extends a selection on either side of the insertion point. | 378 |
| anchor point | Where the mouse button is pressed to start a range selection. | 375 |
| active end | Where the mouse button is released to finish a range selection. | 375 |
| Shift-click | Clicking with Shift to select multiple objects or extend a selection. | 380 |
| background selection | A selection in an inactive window, shown in the secondary highlight color. | 375 |
| destination region | The part of a document that accepts dropped data. | 377 |
| drag and drop | Dragging an item and dropping it on a suitable destination. | 377 |
| clipping | Data dragged from an application to the Finder desktop. | 376 |
| Clipboard | Storage for cut/copied data, available to all applications. | 376 |

## Layout and design vocabulary

| Term | Definition | Page |
| --- | --- | --- |
| center equalization | Placement such that controls are visually balanced across the window's vertical center line. | 376 |
| center justification | Every item centered on an imaginary vertical line. | 376 |
| mutually exclusive attribute group | Attribute choices where only one can be selected (e.g. font size). | 379 |
| accumulating attribute group | Attribute choices where multiple can be selected (e.g. Bold and Italic). | 375 |
| icon genre | A group of icons sharing visual characteristics for a category of items. | 378 |
| About window | See Windows table. | 375 |
| action button | See Dialogs table. | 375 |

## Help and assistance

| Term | Definition | Page |
| --- | --- | --- |
| Apple Help | Enables apps to display HTML help in Help Viewer. | 375 |
| help book | The collection of HTML files providing an app's onscreen help. | 378 |
| Help Viewer | The simple browser displaying Apple Help HTML. | 378 |
| Help button | A round question-mark button opening Help Viewer at the relevant content. | 378 |
| help tag | Brief explanatory text shown after hovering a few seconds. | 378 |
| setup assistant | A small application guiding users through hardware/software setup. | 380 |

## Other terms

| Term | Definition | Page |
| --- | --- | --- |
| Bonjour | Dynamic discovery of computers, devices, and services over IP. | 376 |
| Dock | User-configurable launcher for apps/documents; also holds minimized windows and the Trash. | 377 |
| fast user switching | Lets multiple logged-in users trade use of the machine without quitting apps. | 378 |
| Apple Help | See Help table. | 375 |
| Interface Builder | Apple's UI-building application (historical). | 378 |
| speech recognition | Computer understanding of spoken commands/responses. | 380 |
| speech synthesis / text-to-speech | Computer conversion of text into audible speech. | 380 / 381 |
| Keychain Services | Mac OS X secure storage for passwords/secrets. | 77 (chapter) |

## Related chapter links

- [Windows](../03-aqua-interface/windows.md) — window types, sheets, dialogs.
- [Menus](../03-aqua-interface/menus.md) — menu items and state symbols.
- [Controls](../03-aqua-interface/controls.md) — control behavior and metrics.
- [Text](../03-aqua-interface/text.md) — font roles and capitalization.
- [User Input](../03-aqua-interface/user-input.md) — selection, focus, keyboard.

## Extraction targets

- [x] Confirm the glossary's true end page (p. 381) and the start of the next back-matter section (Revision
      History, p. 383).
- [x] Provide actual definitions instead of a topic list.
- [ ] Map glossary terms onto the recreated app's own terminology (a project glossary), where it differs.

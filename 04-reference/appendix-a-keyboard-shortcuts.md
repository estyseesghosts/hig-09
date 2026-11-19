# Appendix A: Keyboard Shortcuts Quick Reference

- **Part:** Reference
- **PDF start page:** 367
- **Status:** Source-verified

## Purpose

This is the implementation reference for **Mac OS X 10.6-era keyboard shortcuts** (HIG 2009-08-20). It
transcribes all of Table A-1 (pp. 368-374) with the full key sequence, the associated action, whether Mac OS X
reserves the sequence, and the printed source page. It also records where the HIG contradicts itself so the
recreation does not inherit an ambiguity silently.

For the behavior of single keys (Tab, Return, Enter, Delete, Esc, arrow keys in text, Home/End, Page Up/Page
Down, function keys as key equivalents), see [User Input](../03-aqua-interface/user-input.md), pp. 100-106.

## How to read Table A-1 (p. 367)

Table A-1 has two purposes:

1. **Reserved sequences.** Mac OS X uses them system-wide, including for accessibility. Users rely on them to
   work the same way in every application. **Do not override them.**
2. **Recommended sequences.** They are not reserved, but users expect them to mean the same thing from
   application to application. Provide the shortcut if the application performs the associated task. If it does
   not, think carefully before assigning that sequence to something else.

In the printed table, an **Apple icon** beside a sequence means the operating system uses it, so it must not be
overridden. A sequence with **no icon** is recommended for applications that perform the associated task.
Table 8-3 (p. 107) repeats the core reserved list; Table 8-4 (p. 108) covers international input; Tables 8-5
and 8-6 (p. 109) explain recommended Shift and Option variants.

Two details matter for implementation:

- Except for the system-reserved function keys, Table A-1 lists only combinations of two or more keys. The
  table itself also lists **F8** as a single key (p. 369), which the p. 367 note does not mention. F8 is
  included below exactly as printed.
- A sequence absent from Table A-1 may be available for a frequently used application command, but Apple may
  reserve more sequences later. See "Creating Your Own Keyboard Shortcuts" (p. 108).

## Notation

| Notation | Meaning |
| --- | --- |
| `Command` | Command key (⌘) |
| `Shift` | Shift key (⇧) |
| `Option` | Option key (⌥) |
| `Control` | Control key (⌃) |
| `hyphen` | The `-` key |
| `pipe` | The vertical-bar key |
| `Right Arrow`, `Left Arrow`, `Up Arrow`, `Down Arrow` | The arrow keys |

Modifier order follows the glyph order in Table A-1, which is also the order menus display:
**Shift-Option-Control-Command-key**. Thus `Shift-Option-Command-Q` is the printed sequence ⇧⌥⌘Q. The same
physical shortcut can be written in another order; the canonical form here is the HIG's.

## Table A-1: complete reference (pp. 368-374)

Status **Reserved** reproduces the Apple icon. Status **Recommended** means the row has no icon.

Row count: **112** total — **65 reserved** and **47 recommended**.

| Primary key | Key sequence | Associated action | Status | Page | Notes |
| --- | --- | --- | --- | ---: | --- |
| Space bar | `Command-Space` | Show or hide the Spotlight search field. When multiple languages are installed, may rotate through enabled script systems. | Reserved | 368 | Table 8-4 (p. 108) describes the international rotation behavior. |
| | `Shift-Command-Space` | Apple reserved. | Reserved | 368 | No application action. |
| | `Option-Command-Space` | Show the Spotlight search results window. When multiple languages are installed, may rotate through keyboard layouts and input methods within a script. | Reserved | 368 | |
| | `Control-Command-Space` | Apple reserved. | Reserved | 368 | No application action. |
| Tab | `Shift-Tab` | Navigate through controls in a reverse direction. | Reserved | 368 | See "Keyboard Focus and Navigation" (p. 110). |
| | `Command-Tab` | Move forward to the next most recently used application in the list of open applications. | Reserved | 368 | Table 8-3 (p. 107). |
| | `Shift-Command-Tab` | Move backward through the list of open applications (sorted by recent use). | Reserved | 368 | |
| | `Control-Tab` | Move focus to the next grouping of controls in a dialog or the next table (when Tab moves to the next cell). | Reserved | 368 | Accessibility behavior. |
| | `Shift-Control-Tab` | Move focus to the previous grouping of controls. | Reserved | 368 | Accessibility behavior. |
| Esc | `Command-Esc` | Open Front Row. | Reserved | 368 | High-risk: verify in the checklist below. |
| | `Option-Command-Esc` | Open the Force Quit dialog. | Reserved | 368 | Table 8-3 (p. 107). |
| Eject | `Control-Command-Eject` | Quit all applications (after giving the user a chance to save changes to open documents) and restart the computer. | Reserved | 368 | |
| | `Control-Option-Command-Eject` | Quit all applications (after giving the user a chance to save changes to open documents) and shut the computer down. | Reserved | 368 | |
| F1 | `Control-F1` | Toggle full keyboard access on or off. | Reserved | 368 | Table 8-3 calls this "full keyboard navigation." |
| F2 | `Control-F2` | Move focus to the menu bar. | Reserved | 368 | Accessibility behavior. |
| F3 | `Control-F3` | Move focus to the Dock. | Reserved | 368 | Accessibility behavior. |
| F4 | `Control-F4` | Move focus to the active (or next) window. | Reserved | 368 | Accessibility behavior. |
| | `Shift-Control-F4` | Move focus to the previously active window. | Reserved | 368 | Accessibility behavior. |
| F5 | `Control-F5` | Move focus to the toolbar. | Reserved | 369 | Accessibility behavior. |
| | `Command-F5` | Turn VoiceOver on or off. | Reserved | 369 | Table 8-3 (p. 107). High-risk. |
| F6 | `Control-F6` | Move focus to the first (or next) panel. | Reserved | 369 | Accessibility behavior. |
| | `Shift-Control-F6` | Move focus to the previous panel. | Reserved | 369 | Accessibility behavior. |
| F7 | `Control-F7` | Temporarily override the current keyboard access mode in windows and dialogs. | Reserved | 369 | Table 8-3 (p. 107). |
| F8 | `F8` | Tile or untile all enabled spaces. | Reserved | 369 | Single key; see discrepancy 1 below. |
| F9 | `F9` | Tile or untile all open windows. | Reserved | 369 | Single key explicitly allowed by p. 367. |
| F10 | `F10` | Tile or untile all open windows in the currently active application. | Reserved | 369 | Single key explicitly allowed by p. 367. |
| F11 | `F11` | Hide or show all open windows. | Reserved | 369 | Single key explicitly allowed by p. 367. |
| F12 | `F12` | Hide or display Dashboard. | Reserved | 369 | Single key explicitly allowed by p. 367. |
| Grave accent | ``Command-` `` | Activate the next open window in the frontmost application. | Reserved | 369 | See "Window Layering" (p. 222). |
| | ``Shift-Command-` `` | Activate the previous open window in the frontmost application. | Reserved | 369 | See "Window Layering" (p. 222). |
| | ``Option-Command-` `` | Move focus to the window drawer. | Reserved | 369 | |
| Hyphen (-) | `Command-hyphen` | Decrease the size of the selected item (equivalent to the Smaller command). | Reserved | 369 | See "The Format Menu" (p. 183). |
| | `Option-Command-hyphen` | Zoom out when screen zooming is on. | Reserved | 369 | Accessibility behavior. |
| Left bracket ({) | `Command-{` | Left-align a selection (equivalent to the Align Left command). | Recommended | 369 | Format menu p. 183. |
| Right bracket (}) | `Command-}` | Right-align a selection (equivalent to the Align Right command). | Recommended | 369 | Format menu p. 183. |
| Pipe (vertical bar) | `Command-pipe` | Center-align a selection (equivalent to the Align Center command). | Recommended | 369 | Sequence is Command and the vertical-bar key. Format menu p. 183. |
| Colon (:) | `Command-:` | Display the Spelling window (equivalent to the Spelling command). | Recommended | 369 | Edit menu p. 181. |
| Semicolon (;) | `Command-;` | Find misspelled words in the document (equivalent to the Check Spelling command). | Recommended | 369 | Edit menu p. 181. |
| Comma (,) | `Command-,` | Open the application's preferences window (equivalent to the Preferences command). | Recommended | 370 | Application menu p. 177. |
| | `Option-Control-Command-,` | Decrease screen contrast. | Reserved | 370 | Accessibility behavior. |
| Period (.) | `Option-Control-Command-.` | Increase screen contrast. | Reserved | 370 | Accessibility behavior. |
| Question mark (?) | `Command-?` | Open the application's help in Help Viewer. | Recommended | 370 | Same physical sequence as Command-Shift-/ (p. 106). |
| Forward slash (/) | `Option-Command-/` | Turn font smoothing on or off. | Reserved | 370 | |
| Equal sign (=) | `Shift-Command-=` | Increase the size of the selected item (equivalent to the Bigger command). | Reserved | 370 | Format menu p. 183. |
| | `Option-Command-=` | Zoom in when screen zooming is on. | Reserved | 370 | Accessibility behavior. |
| 3 | `Shift-Command-3` | Capture the screen to a file. | Reserved | 370 | |
| | `Shift-Control-Command-3` | Capture the screen to the Clipboard. | Reserved | 370 | |
| 4 | `Shift-Command-4` | Capture a selection to a file. | Reserved | 370 | |
| | `Shift-Control-Command-4` | Capture a selection to the Clipboard. | Reserved | 370 | |
| 8 | `Option-Command-8` | Turn screen zooming on or off. | Reserved | 370 | Accessibility behavior. |
| | `Option-Control-Command-8` | Invert the screen colors. | Reserved | 370 | Accessibility behavior. |
| A | `Command-A` | Highlight every item in a document or window, or all characters in a text field (Select All). | Recommended | 370 | Edit menu p. 181. |
| B | `Command-B` | Boldface the selected text or toggle boldfaced text on and off (Bold). | Recommended | 370 | Edit menu p. 181. |
| C | `Command-C` | Duplicate the selected data and store it on the Clipboard (Copy). | Recommended | 370 | Edit menu p. 181. |
| | `Shift-Command-C` | Display the Colors window (Show Colors). | Recommended | 370 | Format menu p. 183. |
| | `Option-Command-C` | Copy the style of the selected text (Copy Style). | Recommended | 370 | Format menu p. 183. |
| | `Control-Command-C` | Copy the formatting settings of the selected item and store them on the Clipboard (Copy Ruler). | Recommended | 371 | Format menu p. 183. |
| D | `Option-Command-D` | Show or hide the Dock. | Reserved | 371 | Table 8-3 (p. 107); Dock p. 62. |
| | `Command-Control-D` | Display the definition of the selected word in the Dictionary application. | Recommended | 371 | |
| E | `Command-E` | Use the selection for a find operation. | Recommended | 371 | Find windows p. 243. |
| F | `Command-F` | Open a Find window (Find). | Recommended | 371 | Edit menu p. 181. |
| | `Option-Command-F` | Jump to the search field control. | Recommended | 371 | Search fields p. 326. |
| G | `Command-G` | Find the next occurrence of the selection (Find Next). | Recommended | 371 | Edit menu p. 181. |
| | `Shift-Command-G` | Find the previous occurrence of the selection (Find Previous). | Recommended | 371 | Edit menu p. 181. |
| H | `Command-H` | Hide the windows of the currently running application (Hide ApplicationName). | Recommended | 371 | **Conflict:** Table 8-3 (p. 107) reserves it. Treat as reserved. |
| | `Option-Command-H` | Hide the windows of all other running applications (Hide Others). | Recommended | 371 | **Conflict:** Table 8-3 (p. 107) reserves it. Treat as reserved. |
| I | `Command-I` | Italicize the selected text or toggle italic text on or off (Italic). | Recommended | 371 | **Duplicate:** the next row uses the same sequence. |
| | `Command-I` | Display an Info window. | Recommended | 371 | **Duplicate** of Italic; the HIG lists both. Resolve per application context. |
| | `Option-Command-I` | Display an inspector window. | Recommended | 371 | Inspector windows p. 229. |
| J | `Command-J` | Scroll to a selection. | Recommended | 371 | |
| M | `Command-M` | Minimize the active window to the Dock (Minimize). | Recommended | 371 | Window menu p. 186. |
| | `Option-Command-M` | Minimize all windows of the active application to the Dock (Minimize All). | Recommended | 371 | Window menu p. 186. |
| N | `Command-N` | Open a new document (New). | Recommended | 371 | File menu p. 179. |
| O | `Command-O` | Display a dialog for choosing a document to open (Open). | Recommended | 371 | File menu p. 179. |
| P | `Command-P` | Display the Print dialog (Print). | Recommended | 371 | File menu p. 179. |
| | `Shift-Command-P` | Display a dialog for specifying printing parameters (Page Setup). | Recommended | 372 | File menu p. 179. |
| Q | `Command-Q` | Quit the application (Quit). | Recommended | 372 | Application menu p. 177. |
| | `Shift-Command-Q` | Log out the current user (Log Out). | Reserved | 372 | Table 8-3 (p. 107). |
| | `Shift-Option-Command-Q` | Log out the current user without confirmation. | Reserved | 372 | Table 8-3 adds a Control variant; see discrepancy 4. |
| S | `Command-S` | Save the active document (Save). | Recommended | 372 | File menu p. 179. |
| | `Shift-Command-S` | Display the Save dialog (Save As). | Recommended | 372 | File menu p. 179. |
| T | `Command-T` | Display the Fonts window (Show Fonts). | Recommended | 372 | Format menu p. 183. |
| | `Option-Command-T` | Show or hide a toolbar (Show/Hide Toolbar). | Recommended | 372 | View menu p. 184; toolbars p. 200. |
| U | `Command-U` | Underline the selected text or turn underlining on or off (Underline). | Recommended | 372 | Format menu p. 183. |
| V | `Command-V` | Insert the Clipboard contents at the insertion point (Paste). | Recommended | 372 | File menu p. 179. |
| | `Option-Command-V` | Apply the style of one object to the selected object (Paste Style). | Recommended | 372 | Format menu p. 183. |
| | `Option-Shift-Command-V` | Apply the style of the surrounding text to the inserted object (Paste and Match Style). | Recommended | 372 | Edit menu p. 181. |
| | `Control-Command-V` | Apply formatting settings to the selected object (Paste Ruler). | Recommended | 372 | Format menu p. 183. |
| W | `Command-W` | Close the active window (Close). | Recommended | 372 | File menu p. 179. |
| | `Shift-Command-W` | Close a file and its associated windows (Close File). | Recommended | 372 | File menu p. 179. |
| | `Option-Command-W` | Close all windows in the application (Close All). | Recommended | 372 | File menu p. 179. |
| X | `Command-X` | Remove the selection and store it on the Clipboard (Cut). | Recommended | 372 | Edit menu p. 181. |
| Z | `Command-Z` | Reverse the effect of the user's previous operation (Undo). | Recommended | 373 | Edit menu p. 181. |
| | `Shift-Command-Z` | Reverse the effect of the last Undo command (Redo). | Recommended | 373 | Edit menu p. 181. |
| Right arrow | `Command-Right Arrow` | Change the keyboard layout to the current layout of Roman script. | Reserved | 373 | International input. |
| | `Shift-Command-Right Arrow` | Extend selection to the next semantic unit, typically the end of the current line. | Reserved | 373 | |
| | `Shift-Right Arrow` | Extend selection one character to the right. | Reserved | 373 | |
| | `Shift-Option-Right Arrow` | Extend selection to the end of the current word, then to the end of the next word. | Reserved | 373 | |
| | `Control-Right Arrow` | Move focus to another value or cell within a view, such as a table. | Reserved | 373 | Accessibility behavior. |
| Left arrow | `Command-Left Arrow` | Change the keyboard layout to the current layout of system script. | Reserved | 373 | International input. |
| | `Shift-Command-Left Arrow` | Extend selection to the previous semantic unit, typically the beginning of the current line. | Reserved | 373 | |
| | `Shift-Left Arrow` | Extend selection one character to the left. | Reserved | 373 | |
| | `Shift-Option-Left Arrow` | Extend selection to the beginning of the current word, then to the beginning of the previous word. | Reserved | 373 | |
| | `Control-Left Arrow` | Move focus to another value or cell within a view, such as a table. | Reserved | 373 | Accessibility behavior. |
| Up arrow | `Shift-Command-Up Arrow` | Extend selection upward in the next semantic unit, typically the beginning of the document. | Reserved | 373 | |
| | `Shift-Up Arrow` | Extend selection to the line above, to the nearest character boundary at the same horizontal location. | Reserved | 373 | |
| | `Shift-Option-Up Arrow` | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. | Reserved | 373 | |
| | `Control-Up Arrow` | Move focus to another value or cell within a view, such as a table. | Reserved | 373 | Accessibility behavior. |
| Down arrow | `Shift-Command-Down Arrow` | Extend selection downward in the next semantic unit, typically the end of the document. | Reserved | 373 | |
| | `Shift-Down Arrow` | Extend selection to the line below, to the nearest character boundary at the same horizontal location. | Reserved | 373 | |
| | `Shift-Option-Down Arrow` | Extend selection to the end of the current paragraph, then to the end of the next paragraph. Include the paragraph terminator (such as Return) in cut, copy, and paste operations. | Reserved | 374 | |
| | `Control-Down Arrow` | Move focus to another value or cell within a view, such as a table. | Reserved | 374 | Accessibility behavior. |

## High-risk shortcut verification checklist

Use this after implementing key handling. Each check must pass with the application frontmost, with a text
field focused, and with a modal dialog open where applicable.

- [ ] **Command-Esc opens Front Row.** It must not reach the application as an app-defined command. Source:
      Table A-1, p. 368 (Reserved). Not listed in Table 8-3; the A-1 Apple icon is the authority.
- [ ] **Option-Command-Esc opens Force Quit.** No application command may intercept it. Source: Table A-1,
      p. 368 (Reserved); Table 8-3, p. 107.
- [ ] **Control-F1 toggles full keyboard access.** It must not type a function character or trigger an
      application toolbar command. Source: Table A-1, p. 368 (Reserved); Table 8-3, p. 107 (wording: "full
      keyboard navigation").
- [ ] **Control-F2 moves focus to the menu bar.** The menu bar must become keyboard-navigable and the
      application must not receive a plain F2. Source: Table A-1, p. 368 (Reserved).
- [ ] **Command-F5 toggles VoiceOver.** It must not be assigned to another application command. Source:
      Table A-1, p. 369 (Reserved); Table 8-3, p. 107.
- [ ] **Control-F7 temporarily overrides the keyboard access mode** in windows and dialogs. Source:
      Table A-1, p. 369 (Reserved); Table 8-3, p. 107.

## Source inconsistencies found while transcribing

These are contradictions in the 2009 HIG itself, not transcription errors. The resolution column states what
the recreation should do.

| # | Issue | Table A-1 | Other HIG passage | Resolution |
| ---: | --- | --- | --- | --- |
| 1 | Single-key rows | Table A-1 lists **F8** alone (p. 369). | p. 367 says only F9-F12 are single-key exceptions. | Include F8; the table is the concrete list. |
| 2 | Hide shortcuts | `Command-H` and `Option-Command-H` have **no Apple icon**, so A-1 treats them as recommended (p. 371). | Table 8-3 (p. 107) lists both as **reserved**. | Treat both as reserved. The explicit reserved list is the safer, more specific statement. |
| 3 | Duplicate Command-I | `Command-I` appears twice, as **Italic** and as **Info window**, both recommended (p. 371). | No disambiguating note. | Do not assume a unique Command-I. Decide which meaning the app uses; keep the other on `Option-Command-I` or another sequence. |
| 4 | Logout variants | A-1 has `Shift-Command-Q` (Log Out) and `Shift-Option-Command-Q` (log out without confirmation) (p. 372). | Table 8-3 (p. 107) also lists **Shift-Option-Control-Command-Q** — "Force log out without confirmation." | Implement all three; A-1 omits the force-logout Control variant. |
| 5 | Command-Space meaning | A-1: show/hide Spotlight; with multiple languages, may rotate through script systems (p. 368). | Table 8-4 (p. 108): "Rotate through enabled script systems." | Follow A-1: Spotlight is primary; rotation is the multilingual fallback. |
| 6 | Space-bar reserved variants | A-1 marks `Shift-Command-Space` and `Control-Command-Space` "Apple reserved" (p. 368). | Table 8-4 (p. 108) generalizes to "Command-modifier key-Space bar: Apple reserved." | Same rule; never assign these to application commands. |
| 7 | Help shortcut | A-1 lists `Command-?` (p. 370). | p. 106 says `Command-Shift-/` (sometimes shortened to `Command-?`) should always show help. | They are the same physical sequence on a US keyboard. Support both descriptions and never override it. |

The previous version of this note claimed that Command-Option-Space and Command-Control-Space open Help
Viewer. That was wrong: those sequences are reserved for input-source/Spotlight behavior in Table A-1, and help
is `Command-?` (p. 370).

## Cross-checks with repository notes

- [User Input](../03-aqua-interface/user-input.md) — its Table 8-3/8-4/8-5 summaries match A-1 except for the
  Hide-shortcut conflict recorded above. User Input also covers the single-key functions that A-1 deliberately
  omits (pp. 100-106).
- [Menus](../03-aqua-interface/menus.md) — the documented menu shortcuts match A-1: Save As (Shift-Command-S),
  Page Setup (Shift-Command-P), Print (Command-P), Show Fonts (Command-T), Show Colors (Shift-Command-C), Bold
  (Command-B), Italic (Command-I), Underline (Command-U), Bigger (Shift-Command-=), Smaller (Command-hyphen),
  Copy/Paste Style (Option-Command-C/V), Align Left/Center/Right (Command-{/pipe/}), Show/Hide Toolbar
  (Option-Command-T), Minimize All (Option-Command-M), Close All (Option-Command-W).
- [Component Inventory](../notes/component-inventory.md) — the keyboard checklist item now points here for the
  reserved/recommended split.

## Implementation implications

- Build a single key-handling table from the master table above. Mark every **Reserved** sequence as
  non-overridable before dispatching application commands.
- Do not ship an application shortcut that shadows a reserved sequence, even if the OS currently does nothing
  visible in the recreation environment. The HIG treats these as system-owned.
- Treat recommended sequences as the default menu equivalents. If the application does not implement the
  command, leave the sequence unassigned rather than reusing it for an unrelated command.
- Menu equivalents should be displayed with the same modifier set as this table. The recreation's menu code
  should use a single canonical formatter so glyph order and punctuation cannot drift between menus and this
  reference.
- International layouts can change which character a physical key produces. The HIG therefore restricts custom
  shortcuts to Command plus alphabetic characters when an additional modifier is needed (p. 109).

## Open questions / follow-up extraction

- [ ] Does the recreated application need to honor F8-F12 window-management keys, or only the five high-risk
      accessibility shortcuts?
- [ ] Should the app resolve the duplicate Command-I by using Italic or Info window as the primary meaning?
- [ ] Does the recreation target a US keyboard layout only, or must it preserve the international input
      shortcuts in Table 8-4 (p. 108)?

# Reference Image and HIG Figure Inventory

- **Status:** Source-verified (inventory); visual coverage incomplete by design (see capture matrix)
- **Scope:** every file currently in `images/` (37 files, one exact duplicate)
- **Companion:** [Component inventory](component-inventory.md) for component-to-spec traceability

## Purpose and provenance rules

This inventory makes each retained image traceable: what it shows, where it came from, what version evidence it
carries, and which chapter it supports. It deliberately separates **known** facts from **unknown** facts.

- **Capture date.** The file timestamp is 2026-11-18 for every image. That is the date the files were added to
  this repository, not necessarily the date the screen was captured.
- **OS version.** Only one image contains direct build evidence: `Screenshot 2026-11-18 220259.png` shows
  **Mac OS X 10.6.8, build 10K549** in Terminal (`sw_vers`) and About This Mac. Images whose filename begins
  `10-6-Snow-Leopard-` assert 10.6 in the filename; they do **not** independently prove a build. Any other image
  is marked **unknown**.
- **Application version.** Recorded only where the UI displays it (Xcode 3.2 (1610), Safari 5.1.10, Pages '09
  evaluation window). Everything else is **unknown**.
- **Origin.** These are repository-supplied captures of a running Mac OS X environment, not scans of HIG
  figures. The person/device that produced them is not recorded. No license or redistribution grant is
  documented; see [Source and provenance](../00-source/README.md).
- **HIG figures.** No HIG figure bitmap is stored in the repository. HIG figure ranges are cited in the chapter
  notes; the capture matrix below records where a screenshot is standing in for a missing figure.

## Inventory

Dimensions are pixels. "HIG use" names the chapter(s) the image can support; it is not a claim that the image
depicts the HIG's own example.

| # | File | Subject | Type | Dimensions | Version provenance | HIG use / notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | [10-6-Snow-Leopard-Activity-Monitor.png](../images/10-6-Snow-Leopard-Activity-Monitor.png) | Activity Monitor: process table and resource tabs | Screenshot | 807×652 | Filename says 10.6; build unknown | Technologies (pp. 67-84); list views (pp. 333-334) |
| 2 | [10-6-Snow-Leopard-AppleScript-Editor.png](../images/10-6-Snow-Leopard-AppleScript-Editor.png) | AppleScript Editor window with a script | Screenshot | 682×718 | Filename says 10.6; build unknown | Technologies; text input (pp. 322-325) |
| 3 | [10-6-Snow-Leopard-Automator.png](../images/10-6-Snow-Leopard-Automator.png) | Automator workflow with library and action columns | Screenshot | 1080×957 | Filename says 10.6; build unknown | Split views (pp. 336-338); layout |
| 4 | [10-6-Snow-Leopard-Console.png](../images/10-6-Snow-Leopard-Console.png) | Console log window | Screenshot | 880×564 | Filename says 10.6; build unknown | Technologies; list views |
| 5 | [10-6-Snow-Leopard-Disk-Utility.png](../images/10-6-Snow-Leopard-Disk-Utility.png) | Disk Utility with disk list and action tabs | Screenshot | 820×721 | Filename says 10.6; build unknown | Technologies; tab views (pp. 338-341) |
| 6 | [10-6-Snow-Leopard-Finder-Connect-to-iDisk.png](../images/10-6-Snow-Leopard-Finder-Connect-to-iDisk.png) | Connect to iDisk dialog | Screenshot | 487×272 | Filename says 10.6; build unknown | Windows/dialogs (pp. 235-254) |
| 7 | [10-6-Snow-Leopard-Finder-Connect-to-Server.png](../images/10-6-Snow-Leopard-Finder-Connect-to-Server.png) | Connect to Server dialog | Screenshot | 568×308 | Filename says 10.6; build unknown | Windows/dialogs; text input |
| 8 | [10-6-Snow-Leopard-Finder-Copy-Replace.png](../images/10-6-Snow-Leopard-Finder-Copy-Replace.png) | Copy alert: item already exists, Stop/Replace | Screenshot | 479×200 | Filename says 10.6; build unknown | Alerts (p. 237); destructive-action spacing |
| 9 | [10-6-Snow-Leopard-Finder-Copy.png](../images/10-6-Snow-Leopard-Finder-Copy.png) | Copy progress dialog with cancel button | Screenshot | 479×170 | Filename says 10.6; build unknown | Progress indicators (pp. 311-316); sheets |
| 10 | [10-6-Snow-Leopard-Finder-Cover-Flow.png](../images/10-6-Snow-Leopard-Finder-Cover-Flow.png) | Finder Cover Flow view | Screenshot | 1104×768 | Filename says 10.6; build unknown | View controls; split views |
| 11 | [10-6-Snow-Leopard-Finder-Eject-Warning.png](../images/10-6-Snow-Leopard-Finder-Eject-Warning.png) | Eject warning alert | Screenshot | 500×289 | Filename says 10.6; build unknown | Alerts (p. 237); icon use |
| 12 | [10-6-Snow-Leopard-Finder-Get-Info.png](../images/10-6-Snow-Leopard-Finder-Get-Info.png) | Get Info inspector panel | Screenshot | 345×997 | Filename says 10.6; build unknown | Inspector windows (p. 229); disclosure triangles |
| 13 | [10-6-Snow-Leopard-Finder-Go-To.png](../images/10-6-Snow-Leopard-Finder-Go-To.png) | Go to Folder dialog | Screenshot | 509×229 | Filename says 10.6; build unknown | Windows/dialogs; text input |
| 14 | [10-6-Snow-Leopard-Finder-Home.png](../images/10-6-Snow-Leopard-Finder-Home.png) | Finder window showing the Home folder, sidebar, and file list | Screenshot | 977×751 | Filename says 10.6; build unknown | List views; toolbars; window layout |
| 15 | [10-6-Snow-Leopard-Finder-Menu.png](../images/10-6-Snow-Leopard-Finder-Menu.png) | Full desktop with the Finder application menu open | Screenshot | 1920×1080 | Filename says 10.6; build unknown; menu bar clock visible | Menus (pp. 165-190); app menu (pp. 177-179); menu states |
| 16 | [10-6-Snow-Leopard-Finder-Network.png](../images/10-6-Snow-Leopard-Finder-Network.png) | Finder Network browse window | Screenshot | 850×517 | Filename says 10.6; build unknown | Finder/environment (pp. 59-66); list views |
| 17 | [10-6-Snow-Leopard-Force-Quit.png](../images/10-6-Snow-Leopard-Force-Quit.png) | Force Quit Applications dialog | Screenshot | 426×364 | Filename says 10.6; build unknown | Dialogs (p. 235); Appendix A (Option-Command-Esc) |
| 18 | [10-6-Snow-Leopard-Help-Search.png](../images/10-6-Snow-Leopard-Help-Search.png) | Help Viewer search results for "File" | Screenshot | 494×463 | Filename says 10.6; build unknown | Help (pp. 81-84); search fields (pp. 326-328) |
| 19 | [10-6-Snow-Leopard-iCal.png](../images/10-6-Snow-Leopard-iCal.png) | iCal calendar window with toolbar and bottom bar | Screenshot | 1095×592 | Filename says 10.6; build unknown | Toolbars (pp. 255-264); segmented controls; bottom bars (p. 365) |
| 20 | [10-6-Snow-Leopard-Mail-RSS.png](../images/10-6-Snow-Leopard-Mail-RSS.png) | Mail window with RSS mailbox and message list | Screenshot | 1078×687 | Filename says 10.6; build unknown | Split views; list views; source list |
| 21 | [10-6-Snow-Leopard-Network-Utility.png](../images/10-6-Snow-Leopard-Network-Utility.png) | Network Utility with tabbed panes | Screenshot | 718×465 | Filename says 10.6; build unknown | Tab views (pp. 338-341); text controls |
| 22 | [10-6-Snow-Leopard-Safari-v5-RSS.png](../images/10-6-Snow-Leopard-Safari-v5-RSS.png) | Safari 5 RSS reader view | Screenshot | 1261×955 | Filename says 10.6; Safari 5 visible; exact version not in image | Toolbars; layout; typography |
| 23 | [10-6-Snow-Leopard-Software-Update-Details (1).png](../images/10-6-Snow-Leopard-Software-Update-Details%20%281%29.png) | Software Update details list | Screenshot | 592×700 | Filename says 10.6; build unknown | Software update (pp. 85-93); **exact duplicate of #24** |
| 24 | [10-6-Snow-Leopard-Software-Update-Details.png](../images/10-6-Snow-Leopard-Software-Update-Details.png) | Software Update details list | Screenshot | 592×700 | Filename says 10.6; build unknown | Software update (pp. 85-93); list views |
| 25 | [10-6-Snow-Leopard-Software-Update.png](../images/10-6-Snow-Leopard-Software-Update.png) | Software Update main window | Screenshot | 572×280 | Filename says 10.6; build unknown | Software update (pp. 85-93); progress indicators |
| 26 | [10-6-Snow-Leopard-Stacks.png](../images/10-6-Snow-Leopard-Stacks.png) | Desktop with a Stack open | Screenshot | 1920×1080 | Filename says 10.6; build unknown | Dock (p. 62); menus; icon layout |
| 27 | [10-6-Snow-Leopard-System-Preferences-0.png](../images/10-6-Snow-Leopard-System-Preferences-0.png) | System Preferences main window with Show All | Screenshot | 748×539 | Filename says 10.6; build unknown | Preferences windows (p. 243); icon buttons; layout |
| 28 | [10-6-Snow-Leopard-System-Preferences-Desktop-and-Screen-Saver.png](../images/10-6-Snow-Leopard-System-Preferences-Desktop-and-Screen-Saver.png) | Desktop & Screen Saver preferences pane | Screenshot | 748×658 | Filename says 10.6; build unknown | Controls (radio buttons, sliders, image wells); layout |
| 29 | [10-6-Snow-Leopard-System-Preferences-Parental-Controls.png](../images/10-6-Snow-Leopard-System-Preferences-Parental-Controls.png) | Parental Controls preferences pane | Screenshot | 748×732 | Filename says 10.6; build unknown | Checkboxes; tab views; layout |
| 30 | [10-6-Snow-Leopard-System-Preferences-Print-and-Fax.png](../images/10-6-Snow-Leopard-System-Preferences-Print-and-Fax.png) | Print & Fax preferences pane | Screenshot | 748×607 | Filename says 10.6; build unknown | Controls; layout; bottom bar |
| 31 | [10-6-Snow-Leopard-System-Profiler.png](../images/10-6-Snow-Leopard-System-Profiler.png) | System Profiler with hardware tree and detail table | Screenshot | 830×602 | Filename says 10.6; build unknown | Technologies; list views; split views |
| 32 | [10-6-Snow-Leopard-TextEdit-Open.png](../images/10-6-Snow-Leopard-TextEdit-Open.png) | TextEdit Open dialog in column view with preview pane and encoding options | Screenshot | 922×660 | Filename says 10.6; build unknown | Open dialogs (pp. 246-252); column views; disclosure button |
| 33 | [Screenshot 2026-11-18 220229.png](../images/Screenshot%202026-11-18%20220229.png) | Welcome to Xcode window | Screenshot | 1520×992 | **Xcode 3.2 (1610)** visible | Windows; layout; icon buttons; source list |
| 34 | [Screenshot 2026-11-18 220237.png](../images/Screenshot%202026-11-18%20220237.png) | Xcode/iOS SDK installer (Dutch UI) with Installation Alert naming iTunes | Screenshot | 1300×624 | Installer content; OS build unknown | Installation (pp. 85-93); alerts; sheets |
| 35 | [Screenshot 2026-11-18 220247.png](../images/Screenshot%202026-11-18%20220247.png) | GarageBand project window with tracks, piano roll, and inspector | Screenshot | 1592×1172 | Application version unknown | Split views; toolbars; sliders; layout |
| 36 | [Screenshot 2026-11-18 220253.png](../images/Screenshot%202026-11-18%20220253.png) | Pages document with MathType equation window and File menu open | Screenshot | 1501×834 | Pages '09 evaluation; MathType version unknown | Menus; windows; dialogs; toolbars |
| 37 | [Screenshot 2026-11-18 220259.png](../images/Screenshot%202026-11-18%20220259.png) | Mac OS X 10.6.8 desktop with About This Mac, Utilities, Terminal `sw_vers`, System Profiler, and Safari 5.1.10 | Screenshot | 1904×1277 | **Mac OS X 10.6.8 build 10K549** in Terminal and About This Mac; **Safari 5.1.10** | Environment (pp. 59-66); menu bar; Dock; About window; version provenance benchmark |

## Version provenance summary

| Claim | Evidence | Confidence |
| --- | --- | --- |
| The capture environment includes Mac OS X 10.6.8 build 10K549 | Image #37: `sw_vers` output and About This Mac | **Direct** |
| The `10-6-Snow-Leopard-*` images are from a 10.6 environment | Filename only | **Filename claim**, not independently verified |
| Xcode is 3.2 (1610) | Image #33 title area | **Direct** |
| Safari is 5.1.10 | Image #37 About Safari window | **Direct** |
| The generic `Screenshot 2026-11-18 22xxxx` images share one desktop/session | Visual consistency with #37 (menu bar, Dock, wallpaper) | **Inferred**, not proven |
| Any image is a HIG figure | No image matches a HIG figure scan; all are independent captures | **No HIG figures stored** |
| Images may be redistributed | No license or permission record | **Unknown** — treat as all rights reserved until documented |

## Capture matrix: central Aqua components

The matrix records whether a representative screenshot exists for the states the spec work depends on. "Gap"
means no retained image demonstrates the state; the HIG text or figure range is the only current source.

| Component / state | Have | Gap / next capture |
| --- | --- | --- |
| Menu bar, application menu open | #15 | Open File/Edit/View menus; disabled item; checked item; submenu; keyboard-highlighted item |
| Standard window, active | #14, #19, #27 | Active vs. inactive title bar side by side |
| Standard window, inactive | — | Inactive title bar, controls, and background selection |
| Focus ring / keyboard focus | — | Text field, button, list, and tab view with visible focus ring |
| Push button: regular/small/mini | #27 (regular) | Small and mini buttons at 100% scale; default vs. non-default |
| Checkbox: off/on/mixed/disabled | #34 (on) | Mixed and disabled states; small/mini sizes |
| Radio buttons: selected/unselected/disabled | #28 (selected/unselected) | Disabled group; small/mini sizes |
| Slider: regular/small/mini, with/without ticks | #28, #35 (regular) | Small/mini; ticked slider; circular slider |
| Progress: determinate/indeterminate/asynchronous | #9, #25 (determinate) | Indeterminate bar, asynchronous spinner, Stop vs. Cancel |
| Capacity/rating/relevance indicators | — | All three; warning/critical colors |
| Text field: active/disabled/focus/selection | #7, #13 | Disabled field; focus ring; selection; password field |
| Search field: regular/small | #18, #32 | Toolbar search field; small size; active search |
| Token field | — | Token, selected token, token menu |
| Pop-up menu: closed/open/checked | — | Closed control, open menu with checkmark, disabled item |
| Combo box: closed/open/typed match | — | All three states |
| Disclosure triangle closed/open | #12 (inspector sections) | Dialog minimal/expanded pair |
| Disclosure button closed/open | #32 (closed) | Open state in a Save/Open dialog |
| List view: selected rows, sort column | #1, #14, #24 | Active vs. inactive selection; sort indicator; editable cell |
| Column view | #32 | Deep hierarchy; preview column; hidden intermediate path components |
| Split view: zero-width and thick | #3, #20, #31, #35 | Thick splitter with dimple; collapsed subview |
| Tab view: top tabs, selected/unselected | #5, #21, #29 | Disabled tab; small/mini tab heights; inset vs. extended |
| Sheet attached to a window | #7, #13, #34 (installer alert is separate) | True document-modal sheet; save sheet; print sheet |
| Alert: message, informative text, buttons | #8, #11, #17 | Alert with icon, suppression checkbox, expanded details |
| Inspector / Get Info | #12 | Inspector with tabs; multiple inspectors |
| Toolbar: icons, labels, overflow | #14, #19, #22, #33 | Icon-only vs. icon+text; customized toolbar; overflow menu |
| Bottom bar | #19, #35 | Bottom-bar controls at small/mini sizes |
| Dock: normal, Stacks, magnification | #15, #26, #37 | Dock menu; minimized window; running indicator |
| Icon sizes and labels | #26, #33, #37 | 16/32/48/128 px comparison; selected icon label |

## Related chapter links

- [Windows](../03-aqua-interface/windows.md) — dialogs, alerts, sheets, and window states.
- [Controls](../03-aqua-interface/controls.md) — control sizes, states, and metrics.
- [Icons](../03-aqua-interface/icons.md) — icon sizes, labels, and application icons.
- [Layout Guidelines](../03-aqua-interface/layout-guidelines.md) — spacing and pane layout.
- [Menus](../03-aqua-interface/menus.md) — menu states and menu bar composition.
- [Software Installation and Software Updates](../02-macintosh-experience/software-installation-and-software-updates.md) — installer and update windows.
- [Using Mac OS X Technologies](../02-macintosh-experience/using-mac-os-x-technologies.md) — bundled utilities and Help.

## Maintenance rules

- Add a row for every new image before linking it from a chapter.
- Never infer a build number from a filename; record `unknown` unless the UI shows it.
- Keep the duplicate pair (#23/#24) until one is removed deliberately; the inventory records the duplication
  rather than hiding it.
- If an image is replaced, update its row and the capture matrix in the same commit.

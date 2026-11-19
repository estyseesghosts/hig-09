# Using Mac OS X Technologies

- **Part:** Part II: The Macintosh Experience
- **PDF start page:** 67
- **Status:** Source-verified

> **Scope:** the HIG's advice in this chapter is to applications **shipping on Mac OS X**, where these
> technologies are provided by the OS. It is evidence of Apple's 2009 intent, not a statement that this
> recreation must call those same APIs. See [Scope and evidence labels](../notes/scope-and-evidence.md).

## Why this matters (retro recreation)

The chapter is a list of "don't build this yourself" advice: Address Book, animation, Automator, Bonjour,
Colors, Dashboard, Fonts, Preferences, Printing, Security, Services, Speech, Spotlight, and user assistance.
For a recreation, each item poses the same question in a different form: **is the visible behavior part of the
interface to reproduce, or is it a host capability that can be replaced wholesale?** The HIG's answer
("use the system framework") only applies on Mac OS X.

## Key sections to review (from TOC)

- Address Book (p. 67)
- Animation (p. 68)
- Automator (p. 70)
- Bonjour (p. 71)
- Colors (p. 71)
- Dashboard (p. 72)
- Fonts (p. 74)
- Preferences (p. 75)
- Printing (p. 76)
- Security (p. 76)
- Services (p. 77)
- Speech (p. 78)
- Spotlight (p. 78)
- User Assistance (p. 81)

## What the 2009 source says

### Address Book (p. 67)

- If the app stores or uses contact information (names, phone/fax numbers, email addresses), use the Address
  Book framework rather than a private contact store.
- The framework's people-picker window is customizable so only relevant fields appear (Mail shows email
  addresses only, Figure 6-1).
- Do **not** expose framework terminology in the UI: "people picker" and "picker" are unacceptable names.
  Name the window for what it contains in this app, e.g. "Addresses" or "Contacts".

### Animation (pp. 68-70)

- Animation is a Mac OS X hallmark: minimize-to-Dock, unfurling sheets, sliding drawers, Cover Flow, Dock
  stacks, iChat buddy arrival (Figure 6-2).
- It is appropriate for: communicating progress; giving meaningful feedback; clarifying a process or concept;
  helping users understand the consequence of an action **before** committing (Dock items move aside);
  marking a change of interaction mode (Time Machine); showing an object's transition between properties;
  and slowing an action that happens too fast to track (minimize).
- Core Animation is available from v10.5.
- Use it as a subtle enhancement, never as the focus. Explicitly avoid: Front Row/Time Machine-style animated
  full-screen UIs for text-heavy or content-creation work; animating everything; and animating **routine**
  actions already handled by system controls — switching tabs, opening/closing views, clicking toolbar items
  (p. 70).

### Automator (pp. 70-71)

- Actions are discrete, narrowly defined tasks exposed as plug-ins so users can stack them into workflows.
- Action UIs should minimize vertical space because screens are wider than tall: use a pop-up menu instead of
  radio buttons even for two choices; no group boxes; avoid tab views (use hidden tab views); don't repeat the
  action title in a label; use a disclosure triangle for optional settings; use small Aqua controls; use 10 px
  margins.
- Provide progress feedback for long actions (see progress indicators, p. 311) and, where possible, preview the
  effect of settings.

### Bonjour (p. 71)

- Don't assume the user's network configuration. IP addresses can change during a session, so never persist
  settings keyed to an IP address.
- Use Bonjour for automatic discovery of computers, devices, and services instead of asking users to type IP
  addresses.

### Colors (p. 71)

- Use the standard Colors window (Figure 6-3), which supports five color models, instead of a custom color
  picker.

### Dashboard (pp. 72-74)

- A widget performs one lightweight, well-defined task; its purpose must be immediately apparent.
- Not an advertising/branding surface; not a miniaturized app window; show only essential controls.
- Use color to convey task character (bright/saturated for playful tasks, muted for utilitarian ones), but
  **do not use Aqua controls on the widget front**.
- Display information immediately; default size small but expandable if the task needs it; default content
  minimal and non-scrolling (optional scroll bar if the widget is information-heavy); use clearly readable
  fonts.
- Options, if any, live on the back: Info button in the lower-right quadrant, subdued color scheme, and a
  Done button to return to the front.

### Fonts (p. 74)

- Use the system Fonts window for user font selection; it provides standard (Figure 6-5) and minimized
  (Figure 6-6) views and is already implemented.
- Advanced typography (Figure 6-7, Zapfino example) is reached from the window's action menu, not a custom
  Fonts menu.

### Preferences (p. 75)

- A preference is a user-defined setting remembered between sessions. Be selective: don't implement every
  possible preference.
- Reserve preferences for settings changed infrequently. If users may change an attribute many times per
  session, give modeless access (menu item, palette, or window control) instead.
- Do not add a Preferences toolbar item. Application-level preferences go in the application menu; document
  preferences go in the File menu.

### Printing (p. 76)

- Use the standard printing dialogs so users recognize the options; the system provides print, fax, and
  Save-as-PDF ("digital paper") automatically (Figure 6-8).

### Security (pp. 76-77)

- Factor privileged code into a separate process; don't load plug-ins from privileged code; don't call
  dangerous functions such as `system`/`popen` from privileged code.
- Don't store passwords or secrets in plain-text files; use Keychain Services.
- Don't invent authentication schemes; use the authorization APIs. Don't rely solely on passwords; smart
  cards and (future) biometrics may be available.
- Don't assume a single logged-in user (fast user switching) or that keychains are files.
- Keychain benefits: consistent password UX, group or per-activity keychains with activation settings, and
  Keychain Access as a ready-made management UI.

### Services (pp. 77-78)

- Services let apps share capabilities; the application menu's Services submenu lists services appropriate to
  the current selection and includes a command that opens Keyboard Shortcuts preferences.
- Vend services with: supported data types, the command title, and an optional shortcut. If a service shortcut
  conflicts with the running app's shortcut, the app's shortcut wins.
- Service titles: short, focused, unique, title-style capitalization, generally no articles ("Look Up in
  Dictionary", "Make New Sticky Note"). Identical titles get the app name appended automatically.
- Avoid "Open in <Application Name>" services; users should use Finder's Open With.

### Speech (p. 78)

- Speech recognition and text-to-speech (TTS) are both provided with APIs and built-in UI. Recognition lets
  users perform multi-step tasks in one spoken command; TTS delivers information without shifting attention
  and is important for users with vision or attention disabilities.

### Spotlight (pp. 78-80)

- Metadata embedded by the creating app powers attribute-based search (audience, image orientation, musical
  key). Spotlight indexes files and is available to apps for finding files, plug-ins, and data.
- Entry points: Spotlight icon at the right end of the menu bar (Figure 6-9); Control-click contextual menu
  for a selected word or phrase (Figure 6-10); results window grouped into adjustable categories
  (Figure 6-11).
- Quick Look shows thumbnails/full previews for common types (HTML, RTF, text, TIFF, PNG, JPEG, PDF,
  QuickTime); custom types need a Quick Look generator.
- Apps may reuse Spotlight from a search field (p. 326) or a button to search selected text, and may run
  queries behind the scenes (for example to find plug-ins).

### User Assistance (pp. 81-84)

- Use the system help mechanisms, not a private help UI: users are already frustrated when they open help.
- **Apple Help**: HTML in Help Viewer, reachable via the Help menu (Spotlight For Help search field, then
  "ApplicationName Help"), a Help button that sends a search term or anchor, and a contextual-menu Help item
  when relevant content exists. Don't add a Help button if there is no relevant content.
- **Help tags** (tooltips): appear after a hover, vanish when the pointer leaves, and auto-hide after about
  10 seconds. Text should be ≤60-75 characters, one concept, directly about the hovered element; don't repeat
  the on-screen name; don't tag standard window/scroll-bar chrome; a verb fragment ("Restores default
  settings") is fine, and a full sentence ends with a period. Localization grows text 20-30%, so keep it short.

## Observed Mac OS X 10.6 behavior

- Menu-bar Spotlight icon: visible in the 10.6.8 desktop capture (image #37) and the Finder menu capture
  (#15); the results window itself is **not** captured.
- Help Viewer: captured searching for "File" (#18), showing the search-results layout described above.
- Fonts/Colors windows: **not captured**; `controls.md` records the text-field/color-well controls but the
  panels themselves are absent.
- Dashboard: **not captured**.
- Speech, Services, Bonjour: **not observable** in the retained still images (no motion, no network UI).
- Animation: cannot be observed in stills. The sheet/stack/Dock descriptions are HIG figures, not captures.

## Interpretation

- Most of this chapter is **host-capability substitution**: where the 2009 app called an OS framework, the
  recreation either implements equivalent behavior or drops the feature. The interface-visible part is usually
  small (a picker window's name, a font panel, a print dialog's standard panes).
- The transferable **UI rules** are the naming and layout constraints: don't leak framework jargon into labels;
  keep help tags short and element-specific; put infrequently changed settings in Preferences and frequent ones
  in the window; don't advertise in widgets; don't animate routine actions.
- The **security** advice is about implementation safety, not the visual interface, and applies to any platform
  in spirit (don't store plain-text secrets, don't over-privilege).
- Animation is the highest-risk item for fidelity: reproducing 2009 motion requires explicit timing/easing
  evidence that this repository does not yet have.

## Recreation-specific decision / open question

- **PENDING — which technologies are in scope:** the recreated app's feature set is not fixed. Address Book,
  Dashboard, Automator, Services, Speech, and Spotlight are probably irrelevant unless the recreated app
  depends on them; Printing, Preferences, Fonts, Colors, and Help almost certainly are in scope. Blocked by:
  target-app definition.
- **PENDING — host substitution policy:** for each technology, choose "native host feature", "custom
  re-creation", or "out of scope". No default is assumed.
- **PENDING — animation fidelity:** whether motion is reproduced, and if so from what timing evidence.
- **REJECTED — "recreation must use the system-provided technology."** That is HIG advice for Mac OS X apps
  (pp. 67-84 passim) and assumes APIs the recreation may not have.
- **DECIDED — keep the transferable UI rules:** framework-jargon-free labels, ≤60-75 character help tags,
  preference-frequency rule, widget minimalism, no animation of routine actions.

## Implementation implications

- Preference windows: **no Preferences toolbar item** (p. 75). The recreated Preferences path belongs in the
  application menu; document settings in the File menu.
- Help: if a Help button is shown, it must have contextually relevant content; otherwise omit it (p. 81).
- Help tags: one short functional sentence, no standard chrome (p. 82).
- Animation: do not animate tab switching, view opening/closing, or toolbar clicks (p. 70); animating these
  is a defect even if the motion is visually plausible.
- Dashboard-style surfaces: no Aqua controls on the front, options on the back with Info/Done (pp. 73-74).

## Assets / examples to capture later

- [ ] Colors window, standard and minimized Fonts window, Typography inspector (pp. 71, 74; Figures 6-3,
      6-5, 6-6, 6-7).
- [ ] Dashboard widget front/back, including Info and Done controls (pp. 72-74; Figure 6-4).
- [ ] Spotlight results window and contextual-menu search (Figures 6-9 to 6-11).
- [ ] A help tag in place, and a Help button with its anchor target (Figures 6-12, p. 81).
- [ ] Standard Print dialog and its panes (p. 76; Figure 6-8; see [Windows](windows.md#print-dialogs)).
- [ ] Retained utility captures are catalogued in the [image inventory](../notes/image-inventory.md):
      Activity Monitor, AppleScript Editor, Automator, Console, Disk Utility, Network Utility, System
      Profiler, Help Viewer, and the 10.6.8 desktop.

## Open questions / follow-up extraction

- [ ] Which of these technologies were actually used by the app being recreated?
- [ ] Speech/Speech-tech feasibility on the recreation's target platform.
- [ ] Animation timing evidence (durations, easing) — none in the HIG text; needs capture or external
      specification.
- [ ] Does any retained capture show the Fonts or Colors panel? (Current inventory says no.)

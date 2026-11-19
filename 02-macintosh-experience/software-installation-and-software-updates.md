# Software Installation and Software Updates

- **Part:** Part II: The Macintosh Experience
- **PDF start page:** 85
- **Status:** Source-verified

## Why this matters (retro recreation)

First impressions are lasting: users judge an application before they run it, based on packaging and
installation, and they judge the update mechanism by how easily and conveniently they get fixes. If either
flow is confusing, support costs rise. This chapter defines the 2009-era installation, setup-assistant, and
update workflows the recreation should mirror if those surfaces are in scope.

**Historical scope:** this is Mac OS X 10.6-era guidance (2009). It describes Internet-enabled disk images,
PackageMaker, launch-time update checks, and setup-assistant conventions of that period. It is not a
recommendation for modern deployment.

## Key sections to review (from TOC)

- Packaging (p. 85)
  - Identify System Requirements (p. 85)
  - Bundle Your Software (p. 85)
- Installation (p. 86)
  - Use Internet-Enabled Disk Images (p. 86)
  - Drag-and-Drop Installation (p. 86)
  - Installation Packages (p. 87)
  - General Installer Guidelines (p. 87)
- Setup Assistants (p. 88)
- Updating Installed Applications (p. 90)

## Packaging (p. 85)

- Packaging, whether a box or an online presentation, should be **aesthetically pleasing and informative**;
  users begin assessing the app from the package before installation.
- **State system requirements:** required Mac OS X version; whether the app targets PowerPC, Intel, or both;
  any known incompatible configurations. Test on as wide a variety of configurations as possible. Apple's
  Developer Compatibility Labs were the 2009 resource for testing across supported hardware and OS versions.
- **Ship the app as an application bundle.** A bundle structures executables, resources, and configuration
  files, simplifies the user's interaction with the app, and makes it harder to delete critical resources
  accidentally. Bundles are required even for apps that also support earlier Mac OS versions.

## Installation (pp. 86-88)

### Universal installation rule

Do **not** create application-specific subfolders in the user's Downloads folder. The Downloads folder is a
Dock stack in 2009; adding subfolders degrades the stack because clicking it no longer accurately represents
the folder's contents. (p. 86)

### Internet-enabled disk images (p. 86)

- A downloadable app can be packaged in an **Internet-enabled disk image**. The image compresses its contents,
  so a separate archive is unnecessary.
- After download, Mac OS X automatically opens and mounts the image on the desktop. The user then copies the
  desired files or runs the installer.
- This is the distribution wrapper for the drag-and-drop path below, not a separate installation mechanism.

### Drag-and-drop installation (pp. 86-87)

Bundles make drag-and-drop installation possible, and the HIG calls it the **preferred** way to install an
application because:

- It is easy for users to install and uninstall.
- It takes only as long as copying the bundle.
- The developer does not have to build an installer.

First-run support files:

- Drag-and-drop installation does not prevent placing files in specific system locations. On first launch,
  the app can copy needed support files to appropriate places.
- Do **not** use this technique to install additional executable code. Use it for preference files, document
  templates, or other resources that can be regenerated and are not required for the app to run.
- Install such files in obvious places, such as **Application Support**, inside a directory named for the
  application, so users can find them if they uninstall.

### Installation packages (p. 87)

Support drag-and-drop when the bundle contains everything needed to run. Create an **installation package**
when any of these is true:

- Frameworks or other files must be installed in specific locations on the user's system.
- Software must be installed on a part of the system that requires administrative access.
- The product is not an application and its install location requires it. Example: a screen saver that places
  files in the user's Library or the local Library.

PackageMaker (part of Xcode Tools) was the 2009 packaging tool.

### General installer guidelines (pp. 87-88)

- Before installing, check the destination volume for previously installed components.
- Always provide a simple default **Easy Install**; most products should also offer a **Custom** installation so
  a user can restore one missing file without reinstalling everything. The app can also check for required
  files at every launch and reinstall missing ones automatically.
- Provide choices and explain their impact in user terms. Example: one option is faster but uses more disk
  space; another uses less space but is slower.
- Always let the user choose a specific destination folder. Do not require a particular install location.
- Install files only in recommended locations. Users often uninstall by dragging the app to the Trash, so avoid
  leaving remnant files; if an installer is used, include an uninstall option that removes all associated
  files.
- Warn about data that may be overwritten and provide a way to back it up first. Do not overwrite previous user
  preferences. Handle version and format differences the first time the updated app opens.
- Provide help where appropriate. In a custom-install pane, a **More Info** button should explain why the
  component is useful and what happens if it is not installed.
- Do not uninstall Apple system software in `/System`.
- If installing software that may already exist, install only a newer version. Show the installed version and
  the required version, and allow skipping that component.
- Indicate progress: current stage and time remaining (see "Feedback and Communication", p. 42).
- Provide **Cancel**. If canceling would compromise system stability, disable the button during those periods.
  On cancel, restore the destination disk to its pre-install state by deleting files installed before the
  cancellation.
- Consider installing supporting files at first launch instead of building an installer; this also allows the
  app to restore files the user accidentally deletes.
- Match the audience. Children commonly install their own games, so instructions must avoid technical terms.

## Setup assistants (pp. 88-90)

A **setup assistant** is a small application that guides users through complex setup options. Store it where
the app can find it, such as inside the application bundle. Open it automatically when appropriate (new
hardware detected, first launch of the app). Ideally the user sees it only once.

### Appearance

- The assistant's icon combines the setup-assistant icon with the app icon badged in the **lower-right
  corner** (Figure 7-1, p. 88).
- The window layout is shown in Figure 7-2 (p. 89).

### Behavior and layout rules

- While active, show **only the application menu** (About and Quit) and the **Edit menu** (standard text-entry
  items). Do **not** provide a Help menu or Help button; the assistant is the help.
- Provide **Go Back** and **Continue** for navigation.
- Title bar: **dimmed close**, **available minimize**, **dimmed zoom**.
- First pane is titled **"Introduction"** and explains the purpose of later panes.
- Last pane is titled **"Conclusion"**, tells users what changed and how to modify it, has a default **Done**
  button, and has a **dimmed Go Back** button.
- Ask only **one question per pane** in most cases.
- Prefer selection controls that do not support an empty selection, to avoid asking for the same information
  twice.
- Do not put an asterisk or custom icon beside every required field up front. Validate when the user clicks
  Continue; if a field is empty, return to the pane and show the marker then.
- Use system applications and services for intelligent defaults where possible (for example, Bonjour to
  determine an IP address).
- Limit questions to the minimum. The best assistant gets users running quickly; the main app can expose
  refinements later.
- Provide feedback when relevant. A progress bar can sit next to Go Back, with its left edge aligned to the
  pane's left edge.
- Do not fill the entire screen; users must be able to reach other parts of the system.

## Updating installed applications (pp. 90-93)

### Update installer behavior

- An update installer modifies **only the files required** for the new version.
- Files may have been renamed or moved: do not look only in the Applications directory and do not rely
  exclusively on filenames. Identify files by creation/modification dates, version numbers, file size, and
  similar attributes.
- If multiple versions are detected, show information about each (location, creation date) and let the user
  choose which one to update.

### Do not imitate Software Update

Mac users know **Software Update** in System Preferences for OS and system software. Upgrading the OS differs
from upgrading a third-party app, and the experiences must reflect that. Third-party apps should **not**
duplicate the Software Update experience; they should provide a streamlined, consistent update flow.

### Launch-time-only update checks (p. 90)

The goal is convenient but unobtrusive. Perform update procedures **at launch time only**. Do not check for
updates from a background process or a standalone faceless utility that runs independently of the app: if the
process survives after the app quits, update notifications appear at unexpected times and unsettle users.

Exception: during a first-time experience such as a setup assistant, check for updates while the user is
engaged; if one is available, let the user upgrade immediately before working with the installed version.

### The launch-cycle algorithm (pp. 90-91)

1. On the first full launch after installation, start a **separate thread** that checks for updates.
2. If a newer version exists, record that fact in the app. Do **not** notify the user yet.
3. On each later launch, check the recorded state first. If an update is available, notify immediately.
   If not, start a separate thread to check, record the result, and do not notify.

The app repeats step 3 at every launch. If the user installs a newer version, the upgraded app starts again
at step 1.

Why this shape:

- The network check does not slow launch; it runs off the main thread after launch.
- Notifications arrive consistently and immediately at launch, not randomly during work, because display
  depends on a quick internal-state check, not on a lengthy search completing.
- No extra "check while running?" dialogs are needed.
- Users are not startled by notifications outside the app's running context.

### Preferences (p. 91)

Allow the user to customize update behavior in the preferences window: enable/disable automatic software
updates and check for updates immediately. Figure 7-3 (p. 91) shows a sample preferences window.

### Free-update alert (pp. 91-92)

When the launch-time state check finds an update, show an alert describing the type and availability of the
update and offering to get it. Figure 7-4 (p. 92) defines the free-update alert; **every element shown is
required**. In most cases only the application and company names change, and the caution icon is badged with
the app icon.

- Main message: **emphasized (bold) system font**.
- Explanatory text: **small system font**.
- The **caution icon is required** because installing software can destroy user data (see "The Elements of an
  Alert", p. 238).
- A simplified alert with only the main message is not acceptable; it does not give enough information to
  customize the update.
- You may replace "newer version of" with wording such as "minor update to" when appropriate.

The three required buttons and their behaviors:

| Button | Behavior |
| --- | --- |
| **Change Preferences** (default) | Removes the alert and opens the software-update preferences window; after the user dismisses preferences, the app resumes. |
| **Ask Again Later** | Leaves the internal update state unchanged and removes the alert; the alert appears again at the next launch. |
| **Upgrade Now** | Resets the internal state, removes the alert, and starts downloading the new software. When the download completes, the app asks the user to save all open documents and updates with the downloaded version. |

### For-purchase upgrade alert (pp. 92-93)

Use the Figure 7-5 alert (p. 93), which differs in two ways:

- The main message clearly says the new version is **for purchase**, and the question leads interested users to
  **Learn More**.
- **Learn More** resets the internal state, removes the alert, and opens the company website where the user can
  learn about the update and choose a purchase option. If the user upgrades, download the bundle or installer
  **independently of the running app**, so the user can install it when convenient.

## Decision table: which mechanism?

| Situation | 2009 mechanism | What the UI must communicate |
| --- | --- | --- |
| Self-contained app bundle; no admin access; no fixed system locations | Internet-enabled disk image + drag-and-drop to Applications | Mounted image, app icon, drag target; no installer steps |
| Needs frameworks/files in specific locations, or admin access, or is non-app software (for example, a screen saver) | Installer package (PackageMaker) | Easy Install vs. Custom, destination folder, component impact/More Info, progress, Cancel/rollback, uninstall option |
| Complex first-run choices or new hardware setup | Setup assistant | Introduction → one-question panes → Conclusion; Go Back/Continue; no Help |
| Previously installed app needs a new version | Update installer modifying only changed files, plus launch-time check | Preferences (automatic/check now), required update alert, save-documents step before install |

## State checklist for the recreation

Installation:

- [ ] Package/download presented; system requirements readable before install.
- [ ] Destination chosen by the user; no forced location.
- [ ] Easy Install available; Custom available when components are optional.
- [ ] Previous components detected before writing.
- [ ] Progress with stage/time remaining; Cancel available or deliberately disabled with explanation.
- [ ] Cancel restores the pre-install state.
- [ ] Overwrite warning and backup path offered; preferences not overwritten.
- [ ] Uninstall path removes all associated files.
- [ ] First launch installs only regenerable support resources, not executable code.

Setup assistant:

- [ ] First pane "Introduction"; last pane "Conclusion" with default Done and dimmed Go Back.
- [ ] One question per pane; required-field validation on Continue.
- [ ] Only application and Edit menus; no Help.
- [ ] Close and zoom dimmed; minimize available; window not full-screen.
- [ ] Progress feedback aligned with Go Back when needed.

Updates:

- [ ] Check runs at launch only, on a separate thread, never from a persistent background/faceless process.
- [ ] Update availability is recorded and announced at the next launch.
- [ ] Preferences allow automatic updates and a manual check.
- [ ] Free-update alert includes bold main message, small explanatory text, badged caution icon, and all three
      buttons with the specified behaviors.
- [ ] Paid-update alert uses Learn More and downloads independently of the running app.
- [ ] Before installing, the app asks the user to save all open documents.

## Cross-references

- [Text](../03-aqua-interface/text.md): alert typography (bold system message, small system explanation) and
  label/capitalization rules.
- [Windows](../03-aqua-interface/windows.md): alerts and dialog behavior (pp. 235-242), including the caution icon
  and element requirements (p. 238).
- [Icons](../03-aqua-interface/icons.md): application icons and badging conventions for assistant/update alerts.
- [Menus](../03-aqua-interface/menus.md): application and Edit menu contents used by setup assistants (pp. 177-183).
- [Controls](../03-aqua-interface/controls.md): selection controls that avoid empty selections (pp. 280-310) and
  progress indicators (pp. 311-316).
- [User Input](../03-aqua-interface/user-input.md): text entry and validation behavior in assistant panes.

## Assets / examples to capture later

- [ ] Figure 7-1: setup-assistant icons with lower-right app badge (p. 88).
- [ ] Figure 7-2: setup-assistant window layout (p. 89).
- [ ] Figure 7-3: application-update preferences window (p. 91).
- [ ] Figure 7-4: free-update alert (p. 92).
- [ ] Figure 7-5: for-purchase upgrade alert (p. 93).
- [ ] Retained installer/update captures are catalogued in the
      [image inventory](../notes/image-inventory.md): Software Update main window and details (#23-#25) and the
      Xcode/iOS SDK installer with Installation Alert (#34).

## Open questions / follow-up extraction

- [ ] Is installation/update UI in scope for the retro recreation, or only runtime UI?
- [ ] If in scope, does the recreation ship as a bundle (drag-install) or need an installer package?

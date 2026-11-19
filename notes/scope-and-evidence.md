# Scope and Evidence Labels

This project mixes three different kinds of statement, and they must not be read as one:

1. what Apple's 2009 HIG required of software **targeting Mac OS X**,
2. what Mac OS X 10.6 actually did (observed, or reconstructed from the HIG and retained captures), and
3. what **this retro recreation** intends to do on its own target platform.

The recreation is not assumed to run on macOS, to use AppKit, or to use contemporary host widgets. Statements
about those are decisions, not requirements inherited from the source.

## The four labels

Use these headings (or prefixes) in chapters, templates, and specifications.

| Label | Contains | Rules |
| --- | --- | --- |
| **What the 2009 source says** | Summaries/quotations of HIG requirements and recommendations, with page numbers. | No project opinion. Keep Apple's own "should"/"must" wording distinguishable from ours. Cite the page for every claim. |
| **Observed Mac OS X 10.6 behavior** | Behavior actually visible in a 10.6 environment or capture, or explicitly reconstructed from the HIG's own screenshots. | Say which: `observed in image #N`, `HIG figure 15-N`, or `not observed — inferred`. Never present reconstruction as observation. |
| **Interpretation** | What the source means for design intent, translated out of 2009 AppKit vocabulary. | May generalize ("the default button is the Return-activated action"), but must not add new requirements. |
| **Recreation-specific decision / open question** | A choice this project makes for its target platform, with rationale and status. | Mark **DECIDED**, **PENDING**, or **REJECTED**. A pending item must name the decision owner or blocking input. |

## How to treat "use the system-provided control"

The HIG says, repeatedly, that Mac OS X applications should use system-provided controls rather than custom
ones (pp. 255, 265, 280, and throughout the Controls chapter). That is **historical advice to developers
targeting Mac OS X**, where the benefit was automatic OS updates, standard behavior, and accessibility
integration.

It is **not** a requirement that a cross-platform recreation must use the host OS's contemporary widgets, and
it is **not** evidence that the recreation's controls must be AppKit controls. Both of the following are valid,
provided the choice is explicit:

- **Native-host strategy:** use the host toolkit's controls and accept its visual/interaction drift from 10.6.
- **Custom-drawn strategy:** implement Aqua-like controls for pixel/interaction fidelity, and accept the
  accessibility, scaling, and maintenance cost.

A statement such as "the recreation should use system-provided controls" without a stated strategy is a bug in
the notes. Rewrite it as a decision with rationale, or mark it pending.

## Claim hygiene

- Every **requirement** claim has a page reference (`p. 267`).
- Every **implementation** claim has a label: `HIG`, `10.6 observed`, `AppKit API (historical)`, `recreation
  decision`, or `inference`.
- API names (`NSButton`, `NSTexturedRoundedBezelStyle`, Interface Builder) are recorded as **historical Mac OS X
  implementation** detail. They explain how Apple expected the control to be built in 2009; they do not bind
  the recreation.
- Do not launder a project preference into a source claim by writing "the HIG requires" when the HIG merely
  recommends, or when the claim is our inference.
- Where the HIG is silent (hover/pressed artwork for many controls, focus-ring metrics), write **not specified
  in the HIG** instead of inventing a value.

## Worked examples

| Before (ambiguous) | After (labeled) |
| --- | --- |
| "Retro recreation should use system-provided controls." | **Recreation decision (PENDING):** native-host vs. custom-drawn control strategy. HIG pp. 255, 265 advise system controls for Mac OS X apps; that advice assumes AppKit and does not decide this project's platform. |
| "Use `NSButton` with type `NSRadioButton`." | **Implementation (Mac OS X 10.6 AppKit; historical):** `NSButton` type `NSRadioButton`. Recreation mapping: not yet chosen. |
| "Sheets animate down from the title bar." | **What the 2009 source says:** sheets appear attached to the window and animate into place (p. 236). **Observed 10.6:** sheet animation visible in installers; no retained capture of a document-modal sheet (image inventory gap). |
| "Buttons are 19 px high." | **What the 2009 source says:** height is fixed per size (p. 268); the HIG gives no numeric height in this section. **10.6 measurement:** not yet taken — see capture matrix. |

## Where this is applied

- [Chapter notes template](../templates/chapter-notes.md) — required section skeleton.
- [Controls](../03-aqua-interface/controls.md) — control specs, historical API notes, and recreation decisions.
- [Using Mac OS X Technologies](../02-macintosh-experience/using-mac-os-x-technologies.md) — system-technology
  advice vs. recreation feasibility.
- [Component specifications](../specs/README.md) — per-component source/observed/decision blocks.
- [Accessibility checklist](accessibility-checklist.md) — separates 2009 obligations from host-platform choices.

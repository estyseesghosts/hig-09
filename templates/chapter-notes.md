# <Chapter Title>

- **Part:** <Part name>
- **PDF start page:** <page>
- **Status:** Mapped | Summarized | Source-verified | Implementation-ready
<!--
Status measures source coverage, not effort:
- Mapped: TOC skeleton and page ranges only; notes may be topic lists.
- Summarized: every major section has a summary, but some subsections are unread/unverified.
- Source-verified: every TOC section/subsection read against the PDF; page refs checked; no extraction gaps.
- Implementation-ready: source-verified plus testable states/labels/dimensions/behaviors for every component.
Do not use "Reviewed": it does not identify a coverage level.
-->

## Why this matters (retro recreation)

<!-- Why this chapter matters for the project. -->

## Key sections to review (from TOC)

- <Section> (p. <x>)
- <Section> (p. <x>)

## What the 2009 source says

<!--
HIG requirements and recommendations only, with page refs. No project opinion, no AppKit advice presented as
a requirement. Quote or summarize Apple's own "should"/"must" carefully.
-->

- p. <x> — <requirement/recommendation>

## Observed Mac OS X 10.6 behavior

<!--
Only what was actually observed or is explicitly reconstructed. Label each item:
- observed in image #<N> (`../images/...`)
- HIG figure <N>
- inferred from <...> (say so)
Do not present a reconstruction as an observation.
-->

- <observation or "not observed — no capture">

## Interpretation

<!--
What the source means for design intent, translated out of 2009 Macintosh vocabulary. May generalize; must not
add new requirements.
-->

- <meaning for the recreation's design>

## Recreation-specific decision / open question

<!--
Every statement about how THIS project will implement the behavior belongs here. Label it:
- DECIDED: <choice> — rationale; target platform assumption
- PENDING: <question> — blocked by / owner
- REJECTED: <choice> — why
"Use the system-provided control" is historical advice for Mac OS X apps, not a mandate for a cross-platform
recreation. See notes/scope-and-evidence.md.
-->

- PENDING: <decision needed>

## Implementation implications

<!-- Historical/technical details that inform a decision, clearly labeled as AppKit-era detail. -->

- <pattern/behavior/constraint (HIG p. <x>)>
- <terminology/measurement/state rule>

## Assets / examples to capture later

- [ ] Figures/tables/diagrams worth revisiting (page refs)

## Open questions / follow-up extraction

- [ ] <question or targeted lookup>
- [ ] <question or targeted lookup>

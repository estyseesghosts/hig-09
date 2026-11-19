# The Design Process

- **Part:** Part I: Application Design Fundamentals
- **PDF start page:** 25
- **Status:** Reviewed

## Why this matters (retro recreation)

This chapter is the meta-process any retro recreation should mirror: how the original app's design
decisions were made, in what order, and with what weighting of user research vs. feature ambition. For a
recreation, re-deriving these steps helps decide which features actually made it into the original design
and which were added via feature cascade.

## Key sections to review (from TOC)

- Involving Users in the Design Process
  - Know Your Audience (p. 25)
  - Analyze User Tasks (p. 26)
  - Build Prototypes (p. 26)
  - Observe Users (p. 26)
  - Guidelines for Conducting User Observations (p. 27)
- Making Design Decisions (p. 28)
  - Avoid Feature Cascade (p. 29)
  - Apply the 80 Percent Solution (p. 29)

## Source notes (with page refs)

- p. 25 — Design process begins with "careful analysis of the needs of your users"; the best way to ensure
  the product meets needs is to expose designs to user scrutiny during *every* phase of the design process.
  Early user exposure can reveal unanticipated usability problems, saving time and money later.
- p. 25 — Know Your Audience: useful to create scenarios describing a "typical day of a person who uses the
  type of software product" you are designing; visit actual workplaces and study how people perform the tasks.
- p. 26 — Analyze User Tasks: discover the mental/conceptual model users associate with the task; look at
  how users perform similar tasks *without* the computer; design to reflect users' terminology, concepts,
  objects, and gestures, but don't insist on replicating each non-computer step.
- p. 26 — Build Prototypes: use task/component-step info to create initial design, then prototype it; test
  aspects of design and verify how well they will work for users; techniques include storyboards and
  prototyping software; keep prototypes quick and only for improving design; do not reuse prototype code in
  final product.
- p. 27 — Observe Users: let target users try prototype; limit test scope to key areas; focus on tasks
  identified during task analysis; instructions to participants should be clear/complete but should not
  explain how to do things being tested; watch for patterns; don't blame users for mistakes; review results
  with cross-functional team (product management, marketing, engineering, design, docs, QA).
- p. 28 — Making Design Decisions: weigh costs (not all financial) against potential benefits when adding
  features; adding features can make app larger, slower, more complex, require more dev time, increase
  documentation/help scope, risk adverse effects on existing features, increase validation time.
- p. 29 — Avoid Feature Cascade: tempting to add features not wholly relevant to original intent; can lead
  to bloated interface that is slow and difficult to use; best products have features tightly integrated with
  solutions they provide, not merely the most features.
- p. 29 — Apply the 80 Percent Solution: design to meet needs of at least 80% of users; avoid designing for
  the 20% power users at the expense of the majority; involve broad range of users to find the 80% solution.

## Implementation implications

- Retro recreation should trace the original app's feature set back to the design process: which user tasks
  were analyzed, prototyped, and tested before features were added.
- The "80 Percent Solution" is a useful retro filter: trim features that only serve the top 20% if the
  recreation targets the mainstream 2009 user.
- Feature decisions in a recreation should document cost/benefit tradeoffs rather than assuming the original
  shipped everything it set out to.

## Assets / examples to capture later

- [ ] Capture original screenshots/mockups used as prototypes (if any are archived in `../images/`).

## Open questions / follow-up extraction

- [ ] Which of these design-process steps map most directly onto the recreation's own iteration workflow?
- [ ] Do we have access to the original design documents/mockups, or only the shipped behavior?

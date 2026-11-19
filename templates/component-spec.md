# Component Spec: <Name>

- **Spec ID:** CMP-<n>
- **HIG chapter(s):** <chapter, pp. x-y>
- **Status:** Draft | Reviewed | Implementation-ready
- **Depends on:** [accessibility checklist](../notes/accessibility-checklist.md) (A11Y IDs),
  [scope and evidence](../notes/scope-and-evidence.md)

<!--
Fill every section. "Unknown" and "not specified in the HIG" are acceptable values; omission is not.
Keep source claims page-referenced. Do not turn a recreation decision into a HIG requirement.
-->

## 1. Semantic purpose

<!-- What user goal this element serves and what it must never be used for. One short paragraph + bullets. -->

## 2. Variants and sizes

| Variant | When to use | Sizes | Source |
| --- | --- | --- | --- |
| <variant> | <use> | <regular/small/mini or n/a> | p. <x> |

## 3. Dimensions and geometry

| Property | Regular | Small | Mini | Source |
| --- | --- | --- | --- | --- |
| Height | <px or "not specified"> | | | p. <x> |
| Width | <rule> | | | p. <x> |
| Label gap | <px> | | | p. <x> |
| Neighbor spacing | <px> | | | p. <x> |

**Measured 10.6 values:** <value + image #, or "not measured — capture gap">

## 4. Text, fonts, and labels

- Label content rule:
- Capitalization:
- Font per size:
- Ellipsis rule (if the label can open a window): see
  [Text](../03-aqua-interface/text.md#using-the-ellipsis-character-pp-131-132) and p. <x>.
- Localization: <constraint>

## 5. States

| State | Trigger | Visual requirement | Source / evidence |
| --- | --- | --- | --- |
| Enabled | default | | p. <x> |
| Disabled | action unavailable | | p. <x> |
| Focused | keyboard focus | focus ring | p. <x> / A11Y-13 |
| Pressed | pointer/key down | | p. <x> or "not specified" |
| Hover | pointer over | | p. <x> or "not specified in HIG" |
| Active/selected | control has value | | p. <x> |
| Mixed | multi-object selection | dash | p. <x> |

## 6. Interaction and keyboard

- Pointer:
- Keyboard: (cite A11Y-08, A11Y-13, A11Y-14, A11Y-17, A11Y-21/23 as applicable)
- Default/cancel semantics (dialogs only):
- Timing/feedback:

## 7. Accessibility hooks

| Hook | Requirement |
| --- | --- |
| Name | <where the accessible name comes from> |
| Role | <role to expose> |
| State | <states to expose> |
| Focus | <focusable? ring?> |
| Announcements | <what changes are announced> |

## 8. Observed Mac OS X 10.6 references

- Retained capture: <image # / none>
- HIG figure: <figure number / none>
- Gaps: <states or geometry with no evidence>

## 9. HIG source pages

- p. <x> — <what this page establishes>

## 10. Recreation-specific decisions / open questions

- **DECIDED:** <choice + rationale>
- **PENDING:** <question + blocker>

## 11. Confidence

| Area | Confidence | Why |
| --- | --- | --- |
| Text/usage rules | High / Medium / Low | <source coverage> |
| Geometry | | <numbers vs. unstated> |
| Visual states | | <capture coverage> |
| Keyboard behavior | | <HIG explicit vs. inferred> |

## 12. Acceptance tests

1. <Given/When/Then, observable outcome>
2. <…>

# Evidence rules

How to tier, cite, and fight with evidence. These rules are the part of
the skill that, if broken, turns the whole exercise into confident
fabrication.

## The hierarchy

Every proposition you work with sits at exactly one tier:

| Tier | Name | Meaning |
| --- | --- | --- |
| 1 | Established fact | Verified against the environment (documents you have read, tools you have run, dates you have checked). |
| 2 | Document assertion | Something a supplied document states, not independently verified. |
| 3 | Inference | Follows from tier 1–2 material by reasoning you can state. |
| 4 | Assumption | Taken for grant; not established by anything available. |
| 5 | Unknown | Nothing available settles it either way. |
| 6 | Contradicted proposition | Two or more available sources conflict and no resolution is available. |

Rules of movement:

- **Silent promotion is forbidden.** A tier-2 assertion becomes tier 1
  only when you can say what you checked to verify it. Say so.
- **Demotion is free.** When in doubt about a tier, use the lower one.
  The cost of under-claiming is one extra question; the cost of
  over-claiming is a decision made on a falsehood.
- **Tier 6 is a decision, not a dead end.** A contradiction between
  documents is a frontier item: name both sides, cite both sources, and
  put the resolution on the frontier — or investigate it if you can
  (a third document, a date check, a tool) and report what you found.
  Never pick a side silently, even when one side feels more plausible.
- **Dates and versions are evidence.** If two documents bear on the same
  fact and one postdates the other, the newer document's claim is
  presumptively current — but record the supersedure explicitly, because
  a stale document the user still treats as live is itself a decision
  to surface.

## Citation

Cite whenever a document changes a question, a recommendation, or a
tier. The format depends on what the host provides:

1. If the host offers citation spans or document references, use them.
2. Otherwise: **document name + location** — section heading, page
   number, line number, sheet/cell range, whichever the format
   supports. Example:
   `Quote 2026.pdf, p. 4 "Budget summary"` or
   `budget.xlsx, sheet Q3, cells B12:B18`.
3. Keep quotes short: the key phrase plus the pointer, not a block
   copy. The user can open the document; you cannot.

**The anti-fabrication rule:** if you are not sure a document says
something, say "I cannot confirm that from the documents I have". A
grill built on an invented quotation collapses at the synthesis stage —
when the user checks the evidence base — and no amount of earlier
thoroughness redeems it.

## The evidence map

Maintain a running map, in working memory, of for each decision in the
tree:

- **Supporting** — tier-1/2 material pointing one way (with citations).
- **Contrary** — material pointing the other way (with citations).
- **Unresolved** — what is still tier 4/5 and what would settle it.
- **Assumptions** — what is being taken for grant, flagged.
- **Dependencies** — which other decisions this one hangs off.

When the user says *show me the evidence*, render this map. When you
reach the synthesis, the **Evidence base** section is this map,
condensed to the settled decisions.

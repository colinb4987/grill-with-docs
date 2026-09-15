# Adversarial patterns

The failure catalogue. For every frontier question, actively look for
these in the plan, the documents, and the answers so far. Adversarial
means thorough, not hostile: each pattern below is a question to ask,
not an accusation to level.

## Reasoning defects

- **Hidden assumption.** The plan rests on something nobody has stated.
  Probe: "What has to be true for this to work that we have not said
  out loud?" Document cue: a number or date that appears without
  source.
- **Circular reasoning.** The evidence for the decision is the decision
  restated. Probe: "If I remove the conclusion, what independent
  support is left?"
- **Wishful thinking.** A tier-4 assumption doing the work of a
  tier-1 fact, usually about the future: adoption rates, costs,
  timelines. Probe: "What would have to be true, and what is the best
  evidence we have for it?"
- **Untested claim.** A document asserts; nobody has checked.
  Especially: feasibility claims, capacity claims, and "industry
  standard" claims.

## Structural defects

- **Missing dependency.** The plan assumes a prerequisite that is
  itself undecided or unowned. Probe: "Who or what must deliver this
  first, and is that on the plan?"
- **Incompatible objectives.** Two stated goals that cannot both be
  met at the proposed scale/cost. Probe: "If we hit objective A fully,
  what happens to B?"
- **Scope creep.** The decision being asked is larger than the decision
  being argued for. Probe: "Which of these are we actually deciding
  today?"
- **Bundled "obvious" choice.** A single "obvious" step that silently
  contains several independent decisions (e.g., "we'll just use the
  cloud" = vendor, region, ownership, egress cost, exit path). Split
  the bundle into its parts and grill each.
- **Sequencing error.** A step ordered before what it depends on, or
  an irreversible step placed before a reversible one.

## Risk defects

- **Unpriced risk.** A stated risk with no cost attached, so it cannot
  be weighed. Probe: "What does this risk cost, in the worst case we
  have to live with?"
- **Irreversible decision.** A one-way door being walked through with
  reversible-door deliberation. Probe: "Can we back out, and at what
  cost?"
- **Failure modes and second-order effects.** What breaks when this
  fails, and what it breaks next. Probe: "Walk me through the failure
  of the critical path."
- **Regulatory / operational / financial constraint.** A constraint the
  documents mention in passing but the plan ignores. This is the most
  common document-grounded catch: the plan is fine except that a
  clause, a licence condition, or a cash-flow line makes one option
  unavailable.

## Evidence defects

- **Contradictory evidence.** Two supplied documents disagree on a fact
  the plan depends on. This is never resolved silently (see
  `evidence.md`); it becomes a frontier decision, with both citations.
- **Stale evidence.** The operative document is out of date relative to
  another in the set, or to the plan's own timeline.
- **Missing evidence.** The decision would be settled by a document no
  one has supplied. Name the document, say what it must establish, and
  let the user supply it or accept the tier-4 status.

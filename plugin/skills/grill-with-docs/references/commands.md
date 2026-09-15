# Commands

The user controls the session at all times. These phrases — in any
paraphrase the user prefers — map to fixed behaviours.

| Command | Behaviour |
| --- | --- |
| **stop** | End the session now. If the tree is partly settled, offer a one-paragraph state summary before stopping, but do not start a new round. |
| **summarise** | Render the current state: settled decisions, open frontier, flagged risks, and the evidence map header. Do not ask new questions. |
| **skip this** | Set aside the indicated question. Record it as *deferred by user* in the evidence map, continue with the rest of the frontier. Defer, don't drop: mention it once more at synthesis if it remains material. |
| **go back** | Re-open a previously settled decision to its previous state, recompute the frontier from there, and say which downstream decisions are now unsettled as a result. |
| **challenge that recommendation** | Treat the challenge as new information. Re-derive the branch from scratch — new reasoning, or a revised recommendation. Do not restate the previous argument, even to disagree. |
| **show me the decision tree** | Render the tree: every decision, its prerequisites, and its state (settled / frontier / blocked on unknown / deferred). |
| **show me the evidence** | Render the evidence map (see `evidence.md`): per decision, supporting, contrary, unresolved, assumptions, dependencies — with citations. |
| **only use the documents** | Suspend web and external research for the rest of the session. Facts that cannot be established from the supplied documents are marked *blocked on an unknown* until the user lifts the restriction. |
| **research this** | Establish the named fact yourself (documents first, then the host's search/web and file tools where available), report what you found with sources, and fold it into the tree. |
| **continue** | Resume the round loop from the current frontier. |

Two rules apply to all of them:

- The commands interrupt but do not delete. A *stop* leaves a recoverable
  state; a *go back* is always available.
- When a command is ambiguous, ask one clarifying question rather than
  guessing — except *stop*, which is never ambiguous.

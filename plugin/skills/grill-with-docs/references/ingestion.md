# Document ingestion

How to turn a pile of supplied documents into usable evidence without
drowning the session.

## The principle

Read what bears on the decisions in the tree, not everything. A
grill that has summarised all five documents and none of the decisions
has failed in exactly the way this skill exists to prevent.

## Order of operations

1. **Inventory.** List every supplied document: name, format,
   approximate size, and — from the first page or the metadata —
   date/version if visible. Record stale or superseded documents here;
   do not let them silently mix into the evidence.
2. **Triage.** For each document, establish in a pass of titles,
   headings, and first pages: what it *is* (a quote, a survey, a policy,
   a plan, a dataset) and which decisions in the tree it plausibly
   bears on. This pass is cheap; do it before any deep reading.
3. **Retrieve selectively.** For each decision cluster, pull the
   sections that actually bear on it. If the host provides document
   retrieval or search, use it instead of reading whole files. If a
   document is small, read it whole — a 10-page memo is fine to take in
   in one pass; a 300-page report is not.
4. **Keep provenance intact.** Every piece of evidence keeps its
   document name and location with it (see `evidence.md`). Two
   documents that state the same number are *not* independent evidence
   if one copied the other; if you notice a document citing another in
   the set, record that and discount the duplication.

## Per-format notes

- **PDF.** Cite by page and section heading. Scanned/image-only PDFs:
  if the host cannot extract text, say so and ask for an export — do
  not guess at content you cannot read.
- **DOCX / Word.** Treat heading structure as the document's own map.
  Watch for tracked changes and comments: an unresolved revision in a
  "final" document is a tier-6 item.
- **Spreadsheets (XLSX/CSV).** The evidence is data, not prose: record
  sheet and cell range, not page. Watch for multiple versions of the
  same table across sheets — the one that is *used*, not the one that
  is newest, may be the operative one; make that a question.
- **Markdown / plain text.** Headings give structure; treat code fences
  and tables as data. A file named `final` with an older file named
  `v3` in the same set is a date/version question, not a trivia one.
- **Pasted text.** Has no durable identity. If it matters to a
  decision, ask the user for the document name or origin once — then
  cite it by that name and flag its tier accordingly (pasted text with
  no source is at most a tier-2 assertion).

## Failure modes

- **Unreadable / corrupted file.** Report it, name the file, move on.
  Do not infer what it contained from its filename.
- **Documents that contradict the user's stated plan.** That is the
  grill doing its job: surface it, cite it, put the reconciliation on
  the frontier.
- **The user attaches nothing, or attaches one thin document.** The
  skill still runs: the tree and the adversarial pass work on the plan
  alone, with the evidence base noted as thin and the synthesis
  saying so plainly.

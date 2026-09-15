# grill-with-docs

A ChatGPT/Codex plugin that stress-tests a plan, proposal, design,
strategy, or decision against the documents that bear on it.

It runs an adversarial design-review interview: the model builds a
decision tree from your plan, works it in rounds of numbered questions
each with a recommended answer, uses your documents as tiered evidence
(fact / assertion / inference / assumption / unknown / contradicted),
surfaces conflicts instead of silently resolving them, and ends with a
synthesis — settled decisions, open risks, explicit assumptions, and
the plan as it now stands.

Built as a **skill-only plugin**: pure instructions, no MCP server,
no runtime dependencies.

## Provenance

Adapted from the `grilling` and `grill-with-docs` skills in
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT). The
upstream version pairs grilling with domain modelling (ADR + glossary
output); this version replaces that pairing with document-grounded
evidence handling and ends in a synthesis rather than an ADR. The
round/frontier mechanics are upstream's; the evidence hierarchy,
citation rules, adversarial catalogue, ingestion strategy, and
command table here are new.

## Layout

```
plugin/
├── plugin.json                     # Agent Plugins v1.0.0 manifest
└── skills/grill-with-docs/
    ├── SKILL.md                    # the skill (front matter + method)
    └── references/
        ├── evidence.md             # evidence hierarchy, citations, conflicts
        ├── ingestion.md            # how to work supplied documents
        ├── adversarial.md          # the failure-pattern catalogue
        ├── commands.md             # user control commands
        └── examples.md             # a complete worked session
.agents/plugins/marketplace.json    # local marketplace entry (for dev)
tests/                              # spec-conformance + packaging tests
```

The manifest targets [Agent Plugins
v1.0.0](https://agent-plugins.org) (portable across ChatGPT, Codex,
and other clients); the `extensions.com.openai` object carries the
OpenAI install-surface metadata (display name, brand colour, starter
prompts).

## Install

**Local (ChatGPT / Codex desktop).** This repo is its own local
marketplace. From this checkout:

```
codex plugin marketplace add /path/to/grill-with-docs
```

or point a personal/repo marketplace at it (see
`.agents/plugins/marketplace.json` for the entry format), restart the
desktop app, and install **Grill with Docs** from the Plugins
Directory.

**ChatGPT (Work mode).** The skill is invoked explicitly — it does not
auto-trigger on any mention of a plan:

> Use $grill-with-docs to stress-test the plan or decision I describe,
> using the documents I attach as evidence.

**OpenAI API.** The skill bundle uploads directly:

```bash
cd /path/to/grill-with-docs/plugin/skills
zip -r /tmp/grill-with-docs.zip grill-with-docs
curl -X POST https://api.openai.com/v1/skills \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F files=@/tmp/grill-with-docs.zip
```

then reference it from a Responses API shell tool or Agents API
capability directory.

## Develop

```
pip install -r requirements-dev.txt
pytest
```

- `tests/test_package.py` — hermetic conformance checks against the
  Agent Plugins and Agent Skills specs (manifest closedness, name
  rules, front-matter limits, reference-file coherence, zip packaging
  limits).
- `tests/test_behavioral.py` — live smoke test; runs only with
  `OPENAI_API_KEY` set. Uploads the bundle, asserts acceptance,
  deletes the artifact.

## License

MIT. Upstream attribution above applies to the adapted material.

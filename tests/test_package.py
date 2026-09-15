"""Structural validation for the grill-with-docs plugin package.

Hermetic: no network, no API keys. Checks the package against the two
standards a host validates it with at load time:

- Agent Plugins v1.0.0 (agent-plugins.org) for ``plugin.json`` — the
  manifest schema is closed; unknown top-level fields must not exist.
- Agent Skills (agentskills.io/specification) for ``SKILL.md`` — front
  matter field constraints and directory layout.

Plus packaging rules a ChatGPT/Codex uploader enforces: one
``SKILL.md`` per bundle, a single top-level folder in the upload zip,
and the size/count limits from the OpenAI skills guide.
"""
from __future__ import annotations

import io
import json
import re
import zipfile
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugin"
SKILL_DIR = PLUGIN / "skills" / "grill-with-docs"
SKILL_MD = SKILL_DIR / "SKILL.md"

PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"

# Agent Plugins v1.0.0 §5.2: the manifest schema is closed.
MANIFEST_KEYS = {
    "$schema", "name", "version", "description", "author",
    "homepage", "repository", "license", "keywords", "extensions",
}

# Agent Skills spec: name is 1-64 chars, lowercase alphanumerics and
# hyphens, no leading/trailing hyphen, no consecutive hyphens.
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9]*[-][a-z0-9]+)*[a-z0-9]?$")


def _manifest() -> dict:
    return json.loads((PLUGIN / "plugin.json").read_text())


def _frontmatter(path: Path) -> dict:
    text = path.read_text()
    assert text.startswith("---\n"), f"{path} must start with YAML front matter"
    end = text.index("\n---\n", 4)
    return yaml.safe_load(text[4:end])


def _body(path: Path) -> str:
    text = path.read_text()
    return text[text.index("\n---\n", 4) + len("\n---\n"):]


# --- plugin.json (Agent Plugins v1.0.0, §5) ---------------------------------


def test_manifest_schema_identifier():
    assert _manifest()["$schema"] == PLUGINS_SCHEMA


def test_manifest_name():
    name = _manifest()["name"]
    assert 1 <= len(name) <= 64, "name must be 1-64 characters"
    assert NAME_RE.match(name), f"name violates character-set rules: {name!r}"
    assert "--" not in name and ".." not in name
    assert name[0].isalnum() and name[-1].isalnum()


def test_manifest_keys_are_closed():
    unknown = set(_manifest()) - MANIFEST_KEYS
    assert not unknown, f"unknown top-level manifest fields: {sorted(unknown)}"


def test_manifest_author():
    author = _manifest().get("author")
    if author is None:
        pytest.skip("no author field")
    assert isinstance(author, dict)
    assert set(author) <= {"name", "email", "url"}
    assert all(isinstance(v, str) for v in author.values())


def test_manifest_keywords():
    kw = _manifest().get("keywords")
    if kw is None:
        pytest.skip("no keywords")
    assert isinstance(kw, list) and all(isinstance(k, str) for k in kw)


def test_openai_extension_is_object():
    ext = _manifest().get("extensions")
    if ext is None:
        pytest.skip("no extensions")
    assert isinstance(ext, dict)
    openai = ext.get("com.openai")
    if openai is not None:
        assert isinstance(openai, dict)


# --- SKILL.md (Agent Skills specification) ----------------------------------


def test_skill_frontmatter_parses():
    fm = _frontmatter(SKILL_MD)
    assert isinstance(fm, dict)


def test_skill_name():
    name = _frontmatter(SKILL_MD)["name"]
    assert 1 <= len(name) <= 64
    assert NAME_RE.match(name), f"name violates Agent Skills rules: {name!r}"
    assert name == SKILL_DIR.name, "name must match the parent directory"


def test_skill_description():
    desc = _frontmatter(SKILL_MD)["description"]
    assert isinstance(desc, str)
    assert 1 <= len(desc) <= 1024, "description must be 1-1024 characters"
    lowered = desc.lower()
    assert "use when" in lowered or "invoke" in lowered, (
        "description must state when to use the skill, not only what it does"
    )


def test_skill_license():
    lic = _frontmatter(SKILL_MD).get("license")
    if lic is None:
        pytest.skip("no license field")
    assert isinstance(lic, str)
    assert 1 <= len(lic) <= 500


def test_skill_body_size():
    # Progressive disclosure: the body loads on activation; the spec
    # recommends under 5000 tokens. ~4 chars/token keeps a safe margin.
    assert len(_body(SKILL_MD)) < 20_000, (
        "SKILL.md body exceeds the 5000-token recommendation; move detail "
        "into references/"
    )


# --- coherence: what the body points at must exist --------------------------


def test_body_references_exist():
    body = _body(SKILL_MD)
    refs = set(re.findall(r"(?:references|scripts|assets)/[\w./-]+\.\w+", body))
    assert refs, "SKILL.md should point at its supporting files"
    missing = sorted(r for r in refs if not (SKILL_DIR / r).is_file())
    assert not missing, f"referenced but missing: {missing}"


def test_single_skill_md_per_bundle():
    skill_mds = sorted(p.relative_to(PLUGIN) for p in PLUGIN.rglob("SKILL.md"))
    assert len(skill_mds) == 1, f"exactly one SKILL.md per bundle: {skill_mds}"


def test_skill_discovery_layout():
    # Agent Plugins §7.1: skills/ is the fixed discovery location; each
    # immediate child directory is a skill only if it contains SKILL.md.
    skills = PLUGIN / "skills"
    assert skills.is_dir(), "portable plugins discover skills from skills/"
    for child in sorted(skills.iterdir()):
        if child.is_dir():
            assert (child / "SKILL.md").is_file(), f"{child} has no SKILL.md"


# --- packaging: the upload zip ----------------------------------------------


def _bundle_zip() -> zipfile.ZipFile:
    """Zip the skill bundle the way an OpenAI uploader would: a single
    top-level folder containing SKILL.md and its supporting files."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(SKILL_DIR.rglob("*")):
            if p.is_file():
                z.write(p, arcname=Path(SKILL_DIR.name) / p.relative_to(SKILL_DIR))
    buf.seek(0)
    return zipfile.ZipFile(buf)


def test_bundle_zip_single_top_level_folder():
    with _bundle_zip() as z:
        tops = {n.split("/")[0] for n in z.namelist()}
        assert tops == {SKILL_DIR.name}, f"single top-level folder: {tops}"


def test_bundle_zip_limits():
    # OpenAI skills limits: 500 files, 25 MB per file, 50 MB per zip.
    with _bundle_zip() as z:
        names = z.namelist()
        assert len(names) <= 500, f"{len(names)} files exceeds 500"
        for info in z.infolist():
            assert info.file_size <= 25 * 1024 * 1024, f"too large: {info.filename}"
        assert sum(i.file_size for i in z.infolist()) <= 50 * 1024 * 1024
        assert any(n.endswith("SKILL.md") for n in names)

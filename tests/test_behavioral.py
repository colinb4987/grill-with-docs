"""Live acceptance smoke test against the OpenAI Skills API.

Optional: runs only when ``OPENAI_API_KEY`` is set. Uploads the skill
bundle as a zip to ``POST /v1/skills``, asserts the API accepts it
(front matter, single SKILL.md, size limits all hold), then deletes the
artifact so the test leaves no residue.

This is the real acceptance gate — the hermetic suite in
``test_package.py`` checks the same rules offline.
"""
from __future__ import annotations

import io
import os
import zipfile
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "plugin" / "skills" / "grill-with-docs"
API = "https://api.openai.com/v1/skills"


def _zip() -> io.BytesIO:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(SKILL_DIR.rglob("*")):
            if p.is_file():
                z.write(p, arcname=Path(SKILL_DIR.name) / p.relative_to(SKILL_DIR))
    buf.seek(0)
    return buf


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set",
)
def test_skills_api_accepts_bundle():
    headers = {"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"}
    buf = _zip()
    resp = requests.post(
        API,
        headers=headers,
        files={"files": (f"{SKILL_DIR.name}.zip", buf, "application/zip")},
        timeout=60,
    )
    assert resp.status_code in (200, 201), f"upload rejected: {resp.text}"
    skill_id = resp.json().get("id")
    if skill_id:
        cleanup = requests.delete(f"{API}/{skill_id}", headers=headers, timeout=30)
        assert cleanup.status_code in (200, 204), f"cleanup failed: {cleanup.text}"

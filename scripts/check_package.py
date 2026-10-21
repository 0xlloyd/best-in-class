"""Small offline integrity checks for this repository; not a model evaluation."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "best-in-class"
errors = []
text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
parts = text.split("---", 2)
if len(parts) != 3 or parts[0].strip():
    errors.append("SKILL.md must start with YAML frontmatter")
else:
    fields = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            errors.append("Unexpected frontmatter line: " + line)
            continue
        k, v = line.split(":", 1)
        fields[k.strip()] = v.strip().strip('\"').strip("'")
    if fields.get("name") != SKILL.name:
        errors.append("Skill name must match its folder")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")):
        errors.append("Invalid skill name")
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append("Description must be 1–1024 characters")
    if set(fields) != {"name", "description"}:
        errors.append("This core intentionally uses only name and description")
expected_files = {"SKILL.md", "agents/openai.yaml"}
actual_files = {p.relative_to(SKILL).as_posix() for p in SKILL.rglob("*") if p.is_file()}
if actual_files != expected_files:
    errors.append("Skill package must contain only SKILL.md and agents/openai.yaml")
if len(text.splitlines()) >= 500:
    errors.append("Keep core instructions below 500 lines")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    body = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if target and not (md.parent / target).exists():
            errors.append(f"Broken local link in {md.relative_to(ROOT)}: {target}")
for required in ["README.md", "LICENSE", "evals/RESULTS.md", "evals/scenarios.md"]:
    if not (ROOT / required).is_file():
        errors.append("Missing " + required)
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: core metadata, local documentation links, package structure and instruction length")

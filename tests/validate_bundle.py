from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise AssertionError(f"missing frontmatter: {path.relative_to(ROOT)}")
    return yaml.safe_load(text.split("---", 2)[1])


def main() -> None:
    files = [path for path in ROOT.rglob("*") if path.is_file()]

    for path in files:
        if path.suffix in {".yaml", ".yml"}:
            yaml.safe_load(path.read_text())
        elif path.suffix == ".md" and path.read_text().startswith("---\n"):
            frontmatter(path)

    agents = {path.stem for path in (ROOT / "agents").glob("*.md")}
    for path in (ROOT / "agents").glob("*.md"):
        meta = frontmatter(path)["meta"]
        assert len(meta["description"].split()) > 100, f"short agent description: {path.name}"

    recipes = list((ROOT / "recipes").glob("*.yaml"))
    for path in recipes:
        recipe = yaml.safe_load(path.read_text())
        assert recipe.get("name") and recipe.get("version") and recipe.get("steps"), path.name
        outputs: set[str] = set()
        for step in recipe["steps"]:
            assert step.get("id") and step.get("agent") and step.get("prompt"), (path.name, step)
            assert step["agent"].split(":")[-1] in agents, (path.name, step["agent"])
            assert step.get("timeout", 0) > 0, (path.name, step["id"])
            if step.get("output"):
                outputs.add(step["output"])

    modes = {}
    for path in (ROOT / "modes").glob("*.md"):
        mode = frontmatter(path)["mode"]
        name = mode["name"]
        assert name == path.stem, (path.name, name)
        assert name not in modes, name
        assert mode.get("description") and mode.get("shortcut"), name
        if mode.get("contributes", {}).get("agents"):
            assert "delegate" in mode.get("tools", {}).get("safe", []), name
        if mode.get("contributes", {}).get("skills"):
            assert "load_skill" in mode.get("tools", {}).get("safe", []), name
        modes[name] = mode

    for name, mode in modes.items():
        for target in mode.get("allowed_transitions", []):
            assert target in modes, (name, target)

    mentions = []
    for path in files:
        if path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        for match in re.findall(r'@ux-ergonomist:([^\s"\]]+)', path.read_text()):
            mentions.append((path, match))
            target = ROOT / match
            if target.exists():
                continue
            if (target.with_suffix(".md")).exists():
                continue
            if (target / "SKILL.md").exists():
                continue
            raise AssertionError(f"unresolved mention in {path.relative_to(ROOT)}: {match}")

    expected_flow = [
        "ergonomics-frame",
        "ergonomics-research",
        "ergonomics-review",
        "ergonomics-recommend",
        "ergonomics-verify",
        "ergonomics-finish",
    ]
    assert set(modes) == set(expected_flow), sorted(modes)
    for current, following in zip(expected_flow, expected_flow[1:]):
        assert following in modes[current].get("allowed_transitions", []), (current, following)

    print(
        f"validated {len(files)} files, {len(agents)} agents, {len(recipes)} recipes, "
        f"{len(modes)} modes, {len(list((ROOT / 'skills').glob('*/SKILL.md')))} skills, "
        f"and {len(mentions)} namespaced mentions"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise

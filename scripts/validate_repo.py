#!/usr/bin/env python3
"""Validate this package's discovery, explicit-only policy and local resources.

Use --schema with the published, versioned Agent Plugins JSON schema for full
portable-manifest validation. No network access or model calls are performed.
This checks structure and arithmetic, not creative quality or factual accuracy.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import yaml

SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAMES = {"nutshell-script", "nutshell-art", "nutshell-animation", "nutshell-video"}


def unique_object(pairs: list[tuple]) -> dict:
    """Reject overwritten JSON fields consistently with the timeline reader."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def validate_repo(root: Path, schema: dict | None = None) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def read_json(relative: str) -> dict:
        try:
            value = load_json(root / relative)
            if not isinstance(value, dict):
                raise ValueError("expected JSON object")
            return value
        except (OSError, ValueError) as error:
            errors.append(f"{relative}: {error}")
            return {}

    def local_file(relative: str, base: Path, label: str) -> Path | None:
        path = (base / relative).resolve()
        if not path.is_relative_to(root):
            errors.append(f"{label}: path leaves the package: {relative}")
            return None
        if not path.is_file():
            errors.append(f"{label}: missing file: {relative}")
            return None
        return path

    manifest = read_json("plugin.json")
    require(manifest.get("$schema") == SCHEMA_URL, "plugin.json: wrong portable schema")
    require(manifest.get("name") == "nutshell-studio", "plugin.json: unexpected plugin name")
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", "")))), "plugin.json: version must be a release number")
    author = manifest.get("author")
    require(isinstance(author, dict) and bool(author.get("name")), "plugin.json: author must be an object with a name")
    require(not ({"skills", "commands", "command"} & manifest.keys()), "plugin.json: portable skills are discovered from skills/, not a custom command registry")
    require(not (root / ".codex/plugin.json").exists(), "Remove unsupported .codex/plugin.json")
    if schema is not None:
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(schema)
        for error in Draft202012Validator(schema).iter_errors(manifest):
            errors.append(f"plugin.json schema: {error.json_path}: {error.message}")

    extensions = manifest.get("extensions", {})
    openai = extensions.get("com.openai", {}) if isinstance(extensions, dict) else {}
    interface = openai.get("interface", {}) if isinstance(openai, dict) else {}
    if not isinstance(interface, dict):
        interface = {}
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(isinstance(interface.get(key), str) and bool(interface[key].strip()), f"plugin.json: missing interface.{key}")
    for key in ("logo", "composerIcon"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.startswith("./"):
            errors.append(f"plugin.json: interface.{key} must use a ./ path")
            continue
        path = local_file(value, root, f"interface.{key}")
        if path and path.suffix == ".svg":
            try:
                svg = ET.parse(path).getroot()
                _, _, width, height = map(float, svg.attrib["viewBox"].split())
                require(width == height and width >= 48, f"{value}: icon must be square and at least 48 units")
            except (ET.ParseError, KeyError, ValueError) as error:
                errors.append(f"{value}: invalid SVG: {error}")

    catalog = read_json(".agents/plugins/marketplace.json")
    require(catalog.get("name") == "nutshell-studio", "Marketplace name must match the documented selector")
    entries = catalog.get("plugins", [])
    require(isinstance(entries, list) and len(entries) == 1, "Marketplace must expose this one plugin")
    for entry in entries if isinstance(entries, list) else []:
        if not isinstance(entry, dict):
            errors.append("Marketplace entry must be an object")
            continue
        require(entry.get("name") == manifest.get("name"), "Marketplace plugin name does not match manifest")
        source = entry.get("source", {})
        if not isinstance(source, dict):
            source = {}
        require(source.get("source") == "local", "Repo marketplace should use its local package snapshot")
        relative = source.get("path")
        require(isinstance(relative, str) and relative.startswith("./") and (root / relative).resolve() == root,
                "Marketplace source.path must point to this package root using ./")
        require(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Marketplace policy differs from the documented install-on-request package")
        require(entry.get("category") == "Productivity", "Marketplace category is missing or inconsistent")

    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    require({path.parent.name for path in skill_files} == NAMES, "Expected exactly the four canonical skill folders")
    names = []
    for path in skill_files:
        label = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append(f"{label}: missing YAML frontmatter")
            continue
        try:
            front = yaml.safe_load(match.group(1))
            if not isinstance(front, dict):
                raise ValueError("frontmatter must be a mapping")
            name = front.get("name")
            description = front.get("description")
            require(name == path.parent.name, f"{label}: name must match folder")
            if isinstance(name, str):
                names.append(name)
            require(isinstance(description, str) and 0 < len(description.strip()) <= 1024,
                    f"{label}: description must be nonempty and at most 1024 characters")
            metadata = yaml.safe_load((path.parent / "agents/openai.yaml").read_text(encoding="utf-8"))
            require(isinstance(metadata, dict) and isinstance(metadata.get("policy"), dict)
                    and metadata["policy"].get("allow_implicit_invocation") is False,
                    f"{label}: explicit-only policy must be boolean false")
        except (OSError, yaml.YAMLError, ValueError) as error:
            errors.append(f"{label}: {error}")
    require(len(names) == len(set(names)), "Duplicate skill names")

    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        fence = None
        prose = []
        for line in text.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if marker:
                token, tail = marker.groups()
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence) and not tail.strip():
                    fence = None
                continue
            if fence is None:
                prose.append(line)
        require(fence is None, f"{path.relative_to(root)}: unclosed Markdown fence")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", "\n".join(prose)):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            if parsed.path:
                local_file(unquote(parsed.path), path.parent, str(path.relative_to(root)))

    helper = root / "skills/nutshell-video/scripts/validate_timeline.py"
    example = root / "skills/nutshell-video/references/example-storyboard.json"
    if helper.is_file() and example.is_file():
        spec = importlib.util.spec_from_file_location("nutshell_timeline_validation", helper)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        try:
            data = load_json(example)
            errors.extend(f"Example timeline: {error}" for error in module.validate_timeline(data))
        except (OSError, ValueError) as error:
            errors.append(f"Example timeline: {error}")
    else:
        errors.append("Timeline helper or illustrative storyboard is missing")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--schema", type=Path, help="Downloaded published Agent Plugins 1.0.0 schema")
    args = parser.parse_args()
    try:
        schema = load_json(args.schema) if args.schema else None
        errors = validate_repo(args.root, schema)
    except (OSError, ValueError) as error:
        print(f"Validation could not run: {error}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    scope = "including published manifest schema" if schema else "without external manifest schema"
    print(f"Package, four explicit-only skills, resources and example timeline are valid ({scope}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

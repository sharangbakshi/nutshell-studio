"""Regression tests for discovery and invocation invariants, not prose wording."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_repo", ROOT / "scripts/validate_repo.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__"))

    def errors(self):
        return MODULE.validate_repo(self.root)

    def test_valid_package(self):
        self.assertEqual(self.errors(), [])

    def test_string_false_does_not_disable_implicit_invocation(self):
        policy = self.root / "skills/nutshell-art/agents/openai.yaml"
        policy.write_text('policy:\n  allow_implicit_invocation: "false"\n')
        self.assertTrue(any("boolean false" in error for error in self.errors()))

    def test_missing_invocation_policy_is_rejected(self):
        (self.root / "skills/nutshell-art/agents/openai.yaml").unlink()
        self.assertTrue(any("openai.yaml" in error for error in self.errors()))

    def test_marketplace_cannot_point_outside_package(self):
        path = self.root / ".agents/plugins/marketplace.json"
        catalog = json.loads(path.read_text())
        catalog["plugins"][0]["source"]["path"] = "./../elsewhere"
        path.write_text(json.dumps(catalog))
        self.assertTrue(any("source.path" in error for error in self.errors()))

    def test_missing_resource_is_rejected(self):
        skill = self.root / "skills/nutshell-script/SKILL.md"
        with skill.open("a") as stream:
            stream.write('\nRead [missing resource](references/missing.md).\n')
        self.assertTrue(any("missing.md" in error for error in self.errors()))

    def test_folder_and_frontmatter_must_agree(self):
        skill = self.root / "skills/nutshell-art/SKILL.md"
        skill.write_text(skill.read_text().replace("name: nutshell-art", "name: accidental-name", 1))
        self.assertTrue(any("name must match folder" in error for error in self.errors()))

    def test_manifest_author_must_be_object(self):
        path = self.root / "plugin.json"
        manifest = json.loads(path.read_text())
        manifest["author"] = "Placeholder"
        path.write_text(json.dumps(manifest))
        self.assertTrue(any("author must be an object" in error for error in self.errors()))

    def test_example_reader_rejects_duplicate_json_keys(self):
        path = self.root / "skills/nutshell-video/references/example-storyboard.json"
        path.write_text(path.read_text().replace('"schema_version": 1', '"schema_version": 2, "schema_version": 1', 1))
        self.assertTrue(any("duplicate JSON key" in error for error in self.errors()))

    def test_manifest_reader_rejects_duplicate_json_keys(self):
        path = self.root / "plugin.json"
        path.write_text(path.read_text().replace('"name": "nutshell-studio"', '"name": "wrong", "name": "nutshell-studio"', 1))
        self.assertTrue(any("duplicate JSON key" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()

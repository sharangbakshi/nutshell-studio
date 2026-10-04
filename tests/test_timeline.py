"""Arithmetic and input-failure regression tests; no claim of media or creative QA."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "nutshell-video"
SPEC = importlib.util.spec_from_file_location("validate_timeline", SKILL / "scripts" / "validate_timeline.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
FIXTURE = json.loads((SKILL / "references" / "example-storyboard.json").read_text(encoding="utf-8"))


class TimelineTests(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(FIXTURE)

    def assert_invalid(self, fragment):
        errors = MODULE.validate_timeline(self.data)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_estimated_fixture_is_contiguous(self):
        self.assertEqual([], MODULE.validate_timeline(self.data))

    def test_explicit_silence_can_occupy_timeline(self):
        self.data["shots"][0]["narration"] = {"kind": "silence", "text": ""}
        self.assertEqual([], MODULE.validate_timeline(self.data))

    def test_measured_status_does_not_open_media_or_prove_alignment(self):
        self.data["timing"].update(status="measured", audio_source="/not-a-real-recording.wav", basis="Declared test metadata only.")
        self.assertEqual([], MODULE.validate_timeline(self.data))

    def test_gap_is_rejected(self):
        self.data["shots"][1]["start"] += 0.25
        self.assert_invalid("gap")

    def test_overlap_is_rejected(self):
        self.data["shots"][1]["start"] -= 0.25
        self.assert_invalid("overlap")

    def test_missing_start_coverage_is_rejected(self):
        self.data["shots"][0]["start"] = 1
        self.assert_invalid("gap")

    def test_final_length_mismatch_is_rejected(self):
        self.data["timing"]["audio_duration_seconds"] = 19
        self.assert_invalid("does not match declared audio duration")

    def test_duration_limit_is_enforced(self):
        self.data["duration_limit_seconds"] = 17
        self.assert_invalid("exceeds duration_limit_seconds")

    def test_events_cannot_escape_shot(self):
        for key, value in (("start", 5), ("end", 13)):
            with self.subTest(key=key):
                self.data = copy.deepcopy(FIXTURE)
                self.data["shots"][1]["events"][0][key] = value
                self.assert_invalid("outside shot bounds")

    def test_nonfinite_and_boolean_times_are_rejected(self):
        for value in (float("nan"), float("inf"), float("-inf"), True, 10 ** 400):
            with self.subTest(value=str(value)):
                self.data = copy.deepcopy(FIXTURE)
                self.data["shots"][0]["events"][0]["end"] = value
                self.assert_invalid("finite")

    def test_nonpositive_duration_is_rejected(self):
        self.data["shots"][1]["end"] = self.data["shots"][1]["start"]
        self.assert_invalid("end must be greater than start")

    def test_duplicate_shot_ids_are_rejected(self):
        self.data["shots"][1]["id"] = self.data["shots"][0]["id"]
        self.assert_invalid("duplicate ID")

    def test_missing_visual_intent_is_rejected(self):
        self.data["shots"][1]["visual_purpose"] = "  "
        self.assert_invalid("visual_purpose")

    def test_unknown_asset_reference_is_rejected(self):
        self.data["shots"][1]["asset_ids"].append("unregistered-character")
        self.assert_invalid("unknown ID")

    def test_verified_claim_needs_a_source(self):
        self.data["claims"][0]["status"] = "verified"
        self.assert_invalid("requires a source reference")

    def test_missing_and_malformed_structures_return_errors(self):
        for value in (None, [], {}, {"schema_version": True, "shots": [None]}):
            with self.subTest(value=value):
                self.assertTrue(MODULE.validate_timeline(value))

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            json.loads('{"start": 0, "start": 5}', object_pairs_hook=MODULE._unique_object)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Validate Nutshell timeline structure and arithmetic, not media or creative quality."""

import argparse
import json
import math
from pathlib import Path
import sys


EPSILON = 1e-6


def validate_timeline(data):
    """Return actionable errors for the version-1 contract; never access media files."""
    errors = []

    def text_value(obj, key, label, allow_empty=False):
        value = obj.get(key)
        if not isinstance(value, str) or (not allow_empty and not value.strip()):
            errors.append(f"{label}.{key}: expected {'a string' if allow_empty else 'a nonempty string'}")
            return None
        return value

    def number(obj, key, label, positive=False):
        value = obj.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{label}.{key}: expected a finite number")
            return None
        try:
            finite = math.isfinite(value)
        except OverflowError:
            finite = False
        if not finite or value < 0 or (positive and value <= 0):
            errors.append(f"{label}.{key}: expected a finite {'positive' if positive else 'nonnegative'} number")
            return None
        return value

    def array(obj, key, label, nonempty=False):
        value = obj.get(key)
        if not isinstance(value, list) or (nonempty and not value):
            errors.append(f"{label}.{key}: expected {'a nonempty' if nonempty else 'an'} array")
            return []
        return value

    def enum_value(obj, key, label, choices):
        value = text_value(obj, key, label)
        if value is not None and value not in choices:
            errors.append(f"{label}.{key}: expected one of {', '.join(sorted(choices))}")
        return value

    def unique_id(obj, label, seen):
        identifier = text_value(obj, "id", label)
        if identifier is not None:
            if identifier in seen:
                errors.append(f"{label}.id: duplicate ID {identifier!r}")
            seen.add(identifier)
        return identifier

    def references(obj, key, label, known):
        seen = set()
        for index, value in enumerate(array(obj, key, label)):
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{key}[{index}]: expected a nonempty ID string")
            elif value not in known:
                errors.append(f"{label}.{key}[{index}]: unknown ID {value!r}")
            elif value in seen:
                errors.append(f"{label}.{key}[{index}]: repeated ID {value!r}")
            if isinstance(value, str):
                seen.add(value)

    if not isinstance(data, dict):
        return ["timeline: expected an object"]
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        errors.append("timeline.schema_version: expected integer 1")
    text_value(data, "project_title", "timeline")

    timing = data.get("timing")
    duration = None
    if not isinstance(timing, dict):
        errors.append("timeline.timing: expected an object")
    else:
        enum_value(timing, "status", "timing", {"estimated", "measured"})
        text_value(timing, "audio_source", "timing")
        text_value(timing, "basis", "timing")
        duration = number(timing, "audio_duration_seconds", "timing", positive=True)
    if "duration_limit_seconds" in data:
        limit = number(data, "duration_limit_seconds", "timeline", positive=True)
        if limit is not None and duration is not None and duration > limit + EPSILON:
            errors.append("timing.audio_duration_seconds: exceeds duration_limit_seconds")

    asset_ids = set()
    for index, asset in enumerate(array(data, "assets", "timeline")):
        label = f"assets[{index}]"
        if not isinstance(asset, dict):
            errors.append(f"{label}: expected an object")
            continue
        unique_id(asset, label, asset_ids)
        text_value(asset, "kind", label)
        enum_value(asset, "status", label, {"planned", "generated", "approved"})
        text_value(asset, "source", label)

    claim_ids = set()
    for index, claim in enumerate(array(data, "claims", "timeline")):
        label = f"claims[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{label}: expected an object")
            continue
        unique_id(claim, label, claim_ids)
        text_value(claim, "statement", label)
        status = enum_value(claim, "status", label, {"verified", "provisional", "disputed", "illustrative"})
        sources = array(claim, "sources", label)
        for source_index, source in enumerate(sources):
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{label}.sources[{source_index}]: expected a nonempty source reference")
        if status == "verified" and not sources:
            errors.append(f"{label}.sources: a verified claim requires a source reference")
        text_value(claim, "qualification", label, allow_empty=status == "verified")

    shot_ids = set()
    previous_end = 0
    shots = array(data, "shots", "timeline", nonempty=True)
    for index, shot in enumerate(shots):
        label = f"shots[{index}]"
        if not isinstance(shot, dict):
            errors.append(f"{label}: expected an object")
            previous_end = None
            continue
        unique_id(shot, label, shot_ids)
        for key in ("sequence_id", "visual_purpose", "incoming_state", "outgoing_state", "transition"):
            text_value(shot, key, label)
        start = number(shot, "start", label)
        end = number(shot, "end", label)
        if start is not None and end is not None and end <= start:
            errors.append(f"{label}: end must be greater than start")
        if start is not None and previous_end is not None and abs(start - previous_end) > EPSILON:
            problem = "gap" if start > previous_end else "overlap or out-of-order shot"
            errors.append(f"{label}.start: {problem}; expected {previous_end}, got {start}")
        previous_end = end
        if duration is not None and end is not None and end > duration + EPSILON:
            errors.append(f"{label}.end: exceeds declared audio duration")

        narration = shot.get("narration")
        if not isinstance(narration, dict):
            errors.append(f"{label}.narration: expected an object")
        else:
            kind = enum_value(narration, "kind", f"{label}.narration", {"spoken", "silence"})
            text = text_value(narration, "text", f"{label}.narration", allow_empty=kind == "silence")
            if kind == "silence" and text is not None and text != "":
                errors.append(f"{label}.narration.text: silence requires an empty string")
        references(shot, "asset_ids", label, asset_ids)
        references(shot, "claim_ids", label, claim_ids)
        for event_index, event in enumerate(array(shot, "events", label, nonempty=True)):
            event_label = f"{label}.events[{event_index}]"
            if not isinstance(event, dict):
                errors.append(f"{event_label}: expected an object")
                continue
            event_start = number(event, "start", event_label)
            event_end = number(event, "end", event_label)
            text_value(event, "action", event_label)
            text_value(event, "narration_cue", event_label)
            if event_start is not None and event_end is not None and event_end <= event_start:
                errors.append(f"{event_label}: end must be greater than start")
            if event_start is not None and start is not None and event_start < start - EPSILON:
                errors.append(f"{event_label}.start: event begins outside shot bounds")
            if event_end is not None and end is not None and event_end > end + EPSILON:
                errors.append(f"{event_label}.end: event ends outside shot bounds")

    if shots and duration is not None and previous_end is not None and abs(previous_end - duration) > EPSILON:
        errors.append(f"shots: final end {previous_end} does not match declared audio duration {duration}")
    return errors


def _unique_object(pairs):
    """Reject duplicate JSON keys rather than silently accepting overwritten values."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("timeline", type=Path, help="Path to a version-1 JSON timeline")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.timeline.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"FAIL: cannot read timeline: {exc}", file=sys.stderr)
        return 1
    errors = validate_timeline(data)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(data['shots'])} shots cover {data['timing']['audio_duration_seconds']} seconds "
          f"({data['timing']['status']}); structure and arithmetic only, media not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Audit current supersonic-noise evidence states.

The script keeps binding rules, proposals, developing standards, and research
programs separate so future work cannot count them as equivalent evidence.
"""
import csv
from collections import Counter

INPUT = "noise_evidence.csv"
OUTPUT = "noise_evidence_summary.csv"
REQUIRED_COLUMNS = {
    "gate_id",
    "domain",
    "jurisdiction",
    "evidence_state",
    "high_speed_specific",
    "claim",
    "source_id",
    "accessed",
    "limitation",
}
FINAL_PASS_STATES = {"final_pass_threshold", "commercial_acceptance_demonstrated"}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing columns: {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError("noise evidence table is empty")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('gate_id', '<unknown>')} has blank {field}")
        if row["evidence_state"] == "proposed_not_final" and not row["limitation"].lower().startswith("proposed rule"):
            raise ValueError(f"{row['gate_id']} must explicitly identify proposal limitation")
    return rows


def summarize(rows):
    states = Counter(row["evidence_state"] for row in rows)
    final_high_speed_pass = sum(
        row["high_speed_specific"].lower() == "yes"
        and row["evidence_state"] in FINAL_PASS_STATES
        for row in rows
    )
    return {
        "total_rows": len(rows),
        "current_binding_rows": states["current_binding"],
        "proposed_not_final_rows": states["proposed_not_final"],
        "standards_in_development_rows": states["standards_in_development"],
        "empirical_program_in_progress_rows": states["empirical_program_in_progress"],
        "unresolved_rows": states["unresolved"],
        "certified_subsonic_aircraft_record_rows": states["certified_subsonic_aircraft_record"],
        "final_high_speed_pass_threshold_rows": final_high_speed_pass,
    }


def run():
    summary = summarize(load_rows())
    for key, value in summary.items():
        print(f"{key}={value}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerows(summary.items())


if __name__ == "__main__":
    run()

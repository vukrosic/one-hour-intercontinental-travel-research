#!/usr/bin/env python3
"""Validate and summarize the airport-compatibility close read."""
import csv

INPUT = "airport_compatibility_close_read.csv"
OUTPUT = "airport_compatibility_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "context",
    "framework_or_precedent",
    "extracted_claim",
    "requires_candidate_characteristics",
    "current_generic_pass",
    "evidence_status",
    "what_it_supports",
    "what_it_does_not_support",
}
ALLOWED_STATUSES = {"framework_current", "historical_precedent", "prospective_standard"}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid airport close-read table")
    ids = set()
    for row in rows:
        if row["entry_id"] in ids:
            raise ValueError(f"duplicate entry_id: {row['entry_id']}")
        ids.add(row["entry_id"])
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {row['entry_id']}")
        if row["requires_candidate_characteristics"] not in {"yes", "no"}:
            raise ValueError(f"invalid candidate-characteristics field: {row['entry_id']}")
        if row["current_generic_pass"] not in {"no", "historical_only"}:
            raise ValueError(f"invalid current_generic_pass: {row['entry_id']}")
        if row["evidence_status"] not in ALLOWED_STATUSES:
            raise ValueError(f"unknown evidence status: {row['entry_id']}")
        if row["current_generic_pass"] == "no" and row["evidence_status"] == "historical_precedent":
            raise ValueError("historical precedent must remain explicitly historical_only")
        if row["current_generic_pass"] != "no" and row["evidence_status"] != "historical_precedent":
            raise ValueError("only historical precedent may use historical_only")
    return rows


def summarize(rows):
    return {
        "airport_close_read_rows": len(rows),
        "current_framework_rows": sum(row["evidence_status"] == "framework_current" for row in rows),
        "historical_precedent_rows": sum(row["evidence_status"] == "historical_precedent" for row in rows),
        "prospective_standard_rows": sum(row["evidence_status"] == "prospective_standard" for row in rows),
        "candidate_characteristics_required_rows": sum(
            row["requires_candidate_characteristics"] == "yes" for row in rows
        ),
        "current_generic_high_speed_pass_rows": sum(
            row["current_generic_pass"] == "yes" for row in rows
        ),
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

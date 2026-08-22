#!/usr/bin/env python3
"""Validate and summarize cabin-environment requirement close reads."""
import csv

INPUT = "cabin_environment_close_read.csv"
OUTPUT = "cabin_environment_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "context",
    "requirement_type",
    "quantity_or_criterion",
    "applicability",
    "high_speed_specific",
    "evidence_status",
    "high_speed_serviceability_pass",
    "what_it_supports",
    "what_it_does_not_support",
}
ALLOWED_STATUSES = {
    "supported",
    "supported_failure_case",
    "supported_emergency",
    "partial",
    "unresolved",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid cabin close-read table")
    ids = set()
    for row in rows:
        if row["entry_id"] in ids:
            raise ValueError(f"duplicate entry_id: {row['entry_id']}")
        ids.add(row["entry_id"])
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {row['entry_id']}")
        if row["evidence_status"] not in ALLOWED_STATUSES:
            raise ValueError(f"unknown evidence status: {row['entry_id']}")
        if row["high_speed_specific"] not in {"yes", "no"}:
            raise ValueError(f"invalid high_speed_specific: {row['entry_id']}")
        if row["high_speed_serviceability_pass"] != "no":
            raise ValueError("cabin close read cannot assert a high-speed pass")
    return rows


def summarize(rows):
    return {
        "cabin_close_read_rows": len(rows),
        "normal_certification_rows": sum(row["evidence_status"] == "supported" for row in rows),
        "failure_or_emergency_rows": sum(
            row["evidence_status"] in {"supported_failure_case", "supported_emergency"} for row in rows
        ),
        "partial_qualitative_rows": sum(row["evidence_status"] == "partial" for row in rows),
        "high_speed_specific_rows": sum(row["high_speed_specific"] == "yes" for row in rows),
        "comfort_threshold_rows": sum(
            "comfort threshold" in row["what_it_supports"].lower() for row in rows
        ),
        "high_speed_serviceability_pass_rows": sum(
            row["high_speed_serviceability_pass"] == "yes" for row in rows
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

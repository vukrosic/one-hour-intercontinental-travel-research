#!/usr/bin/env python3
"""Audit high-level airport-compatibility evidence coverage.

The script does not calculate airport dimensions, aircraft categories, runway
requirements, rescue indices, or operating procedures.
"""
import csv
from collections import Counter

INPUT = "airport_compatibility.csv"
OUTPUT = "airport_compatibility_summary.csv"
REQUIRED_COLUMNS = {
    "gate_id",
    "domain",
    "evidence_state",
    "high_speed_specific",
    "requires_candidate_characteristics",
    "current_generic_pass",
    "source_id",
    "claim",
    "limitation",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid airport compatibility table")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('gate_id', '<unknown>')} has blank {field}")
        if row["requires_candidate_characteristics"] == "yes" and row["current_generic_pass"] == "yes":
            raise ValueError(f"{row['gate_id']} cannot pass generically without candidate characteristics")
    return rows


def summarize(rows):
    states = Counter(row["evidence_state"] for row in rows)
    return {
        "total_rows": len(rows),
        "framework_exists_rows": states["framework_exists"],
        "supported_historical_rows": states["supported_historical"],
        "prospective_standard_rows": states["prospective_standard"],
        "evidence_missing_rows": states["evidence_missing"],
        "rows_requiring_candidate_characteristics": sum(row["requires_candidate_characteristics"] == "yes" for row in rows),
        "current_generic_high_speed_pass_rows": sum(
            row["high_speed_specific"] == "yes" and row["current_generic_pass"] == "yes" for row in rows
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

#!/usr/bin/env python3
"""Audit passenger-environment evidence coverage.

This script summarizes source coverage and prevents emergency safety limits
from being silently reused as normal-flight passenger comfort thresholds.
"""
import csv
from collections import Counter

INPUT = "passenger_environment.csv"
OUTPUT = "passenger_environment_summary.csv"
REQUIRED_COLUMNS = {
    "gate_id",
    "domain",
    "evidence_kind",
    "applicability",
    "high_speed_specific",
    "source_id",
    "status",
    "limitation",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing columns: {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError("passenger evidence table is empty")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('gate_id', '<unknown>')} has blank {field}")
    return rows


def summarize(rows):
    status_counts = Counter(row["status"] for row in rows)
    high_speed_specific = sum(row["high_speed_specific"].lower() == "yes" for row in rows)
    universal_comfort_thresholds = sum(
        row["domain"] in {"ride comfort", "cruise buffet"}
        and row["status"] == "supported"
        and row["high_speed_specific"].lower() == "yes"
        for row in rows
    )
    return {
        "total_rows": len(rows),
        "supported_rows": status_counts["supported"],
        "partial_rows": status_counts["partial"],
        "unresolved_rows": status_counts["unresolved"],
        "supported_not_comfort_rows": status_counts["supported_not_comfort"],
        "high_speed_specific_rows": high_speed_specific,
        "supported_high_speed_comfort_thresholds": universal_comfort_thresholds,
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

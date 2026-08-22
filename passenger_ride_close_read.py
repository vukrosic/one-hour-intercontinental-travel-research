#!/usr/bin/env python3
"""Validate and summarize close-read passenger ride-quality evidence."""
import csv

INPUT = "passenger_ride_close_read.csv"
OUTPUT = "passenger_ride_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "context",
    "primary_measurement",
    "frequency_or_scope",
    "empirical_signal",
    "transferability",
    "threshold_status",
    "high_speed_practical_pass",
    "what_it_supports",
    "what_remains_unproven",
}
ALLOWED_TRANSFERABILITY = {
    "medium_with_review",
    "low_for_high_speed",
    "high_for_certification_context",
}
SPEED_SPECIFIC_THRESHOLD_STATUSES = {"speed-specific threshold demonstrated"}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid close-read table")
    ids = set()
    for row in rows:
        if row["entry_id"] in ids:
            raise ValueError(f"duplicate entry_id: {row['entry_id']}")
        ids.add(row["entry_id"])
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {row['entry_id']}")
        if row["transferability"] not in ALLOWED_TRANSFERABILITY:
            raise ValueError(f"unknown transferability: {row['transferability']}")
        if row["high_speed_practical_pass"] != "no":
            raise ValueError("close-read table cannot assert a high-speed pass")
    return rows


def summarize(rows):
    return {
        "close_read_rows": len(rows),
        "empirical_rows": sum(row["threshold_status"].startswith("study-specific") for row in rows),
        "frequency_explicit_rows": sum("Hz" in row["frequency_or_scope"] for row in rows),
        "multi_factor_rows": sum(
            any(term in row["empirical_signal"].lower() for term in ("multi-factor", "combined", "noise/motion"))
            for row in rows
        ),
        "medium_or_low_transferability_rows": sum(
            row["transferability"] in {"medium_with_review", "low_for_high_speed"} for row in rows
        ),
        "speed_specific_threshold_rows": sum(
            row["threshold_status"] in SPEED_SPECIFIC_THRESHOLD_STATUSES for row in rows
        ),
        "high_speed_practical_pass_rows": sum(row["high_speed_practical_pass"] == "yes" for row in rows),
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

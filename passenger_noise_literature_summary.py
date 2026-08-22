#!/usr/bin/env python3
"""Summarize passenger/noise literature by context and transferability."""
import csv
from collections import Counter

INPUT = "passenger_noise_literature.csv"
OUTPUT = "passenger_noise_literature_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "domain",
    "source_id",
    "context",
    "measure_type",
    "transferability",
    "evidence_state",
    "high_speed_practical_pass",
    "what_it_can_support",
    "what_it_cannot_support",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid passenger/noise literature table")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('entry_id', '<unknown>')} has blank {field}")
        if row["high_speed_practical_pass"] != "no":
            raise ValueError("literature map cannot assert a practical pass")
    return rows


def summarize(rows):
    return {
        "literature_rows": len(rows),
        "passenger_ride_rows": sum(row["domain"] == "passenger ride quality" for row in rows),
        "noise_rows": sum(row["domain"] in {"cabin noise and vibration", "community noise"} for row in rows),
        "certification_context_rows": sum(row["evidence_state"] == "certification_guidance" for row in rows),
        "empirical_historical_rows": sum(row["evidence_state"] == "empirical_historical" for row in rows),
        "empirical_recent_rows": sum(row["evidence_state"] == "empirical_recent" for row in rows),
        "research_in_progress_rows": sum(row["evidence_state"] == "research_in_progress" for row in rows),
        "high_speed_practical_pass_rows": sum(row["high_speed_practical_pass"] == "yes" for row in rows),
        "medium_or_low_transferability_rows": sum(
            row["transferability"] in {"medium_with_review", "low_for_high_speed"} for row in rows
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

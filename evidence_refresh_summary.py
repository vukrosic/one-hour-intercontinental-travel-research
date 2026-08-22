#!/usr/bin/env python3
"""Summarize the dated regulatory and evidence refresh table."""
import csv
from collections import Counter

INPUT = "evidence_refresh.csv"
OUTPUT = "evidence_refresh_summary.csv"
REQUIRED_COLUMNS = {
    "audit_id",
    "domain",
    "source_id",
    "observed_claim",
    "evidence_state",
    "temporal_status",
    "high_speed_practical_pass",
    "what_it_supports",
    "what_it_does_not_support",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid evidence refresh table")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('audit_id', '<unknown>')} has blank {field}")
        if row["high_speed_practical_pass"] != "no":
            raise ValueError("refresh table cannot assert a high-speed practical pass")
    return rows


def summarize(rows):
    states = Counter(row["evidence_state"] for row in rows)
    return {
        "audit_rows": len(rows),
        "supported_current_rows": states["supported_current"],
        "prospective_policy_rows": states["prospective_policy"],
        "research_in_progress_rows": states["research_in_progress"],
        "supported_general_rows": states["supported_general"],
        "high_speed_practical_pass_rows": sum(
            row["high_speed_practical_pass"] == "yes" for row in rows
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

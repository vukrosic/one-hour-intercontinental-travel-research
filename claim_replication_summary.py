#!/usr/bin/env python3
"""Validate the direct-page public-claim replication register."""
import csv
from collections import Counter

INPUT = "claim_replication.csv"
OUTPUT = "claim_replication_summary.csv"
REQUIRED_COLUMNS = {
    "claim_id",
    "domain",
    "source_id",
    "public_url",
    "accessed",
    "replication_method",
    "replicated_claim",
    "evidence_state",
    "high_speed_practical_pass",
    "what_remains_unproven",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid claim replication register")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('claim_id', '<unknown>')} has blank {field}")
        if row["replication_method"] != "direct_page_read":
            raise ValueError("unexpected replication method")
        if row["high_speed_practical_pass"] != "no":
            raise ValueError("claim replication cannot assert a practical pass")
    return rows


def summarize(rows):
    states = Counter(row["evidence_state"] for row in rows)
    return {
        "claim_rows": len(rows),
        "observed_current_rows": states["observed_current"],
        "observed_prospective_rows": states["observed_prospective"],
        "observed_research_in_progress_rows": states["observed_research_in_progress"],
        "observed_general_rows": states["observed_general"],
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

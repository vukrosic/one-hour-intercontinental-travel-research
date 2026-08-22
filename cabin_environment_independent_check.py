#!/usr/bin/env python3
"""Independent bookkeeping check for cabin-environment close-read summary."""
import csv

INPUT = "cabin_environment_close_read.csv"
REFERENCE_OUTPUT = "cabin_environment_close_read_summary.csv"
OUTPUT = "cabin_environment_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    return {
        "cabin_close_read_rows": len(rows),
        "normal_certification_rows": sum(row["evidence_status"] == "supported" for row in rows),
        "failure_or_emergency_rows": sum(
            row["requirement_type"].startswith("cabin pressure") and "failure" in row["context"]
            or row["evidence_status"] == "supported_failure_case"
            or row["evidence_status"] == "supported_emergency"
            for row in rows
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


def compare():
    independent = independently_summarize(read_rows())
    reference = read_reference()
    return [
        {
            "metric": metric,
            "independent_value": value,
            "reference_value": reference.get(metric),
            "pass": value == reference.get(metric),
        }
        for metric, value in independent.items()
    ]


def run():
    rows = compare()
    for row in rows:
        print(f"{row['metric']} independent={row['independent_value']} pass={row['pass']}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

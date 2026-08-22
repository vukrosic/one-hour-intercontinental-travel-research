#!/usr/bin/env python3
"""Independent bookkeeping check for airport close-read summary."""
import csv

INPUT = "airport_compatibility_close_read.csv"
REFERENCE_OUTPUT = "airport_compatibility_close_read_summary.csv"
OUTPUT = "airport_compatibility_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    return {
        "airport_close_read_rows": len(rows),
        "current_framework_rows": sum(row["evidence_status"] == "framework_current" for row in rows),
        "historical_precedent_rows": sum(row["current_generic_pass"] == "historical_only" for row in rows),
        "prospective_standard_rows": sum(row["evidence_status"] == "prospective_standard" for row in rows),
        "candidate_characteristics_required_rows": sum(
            row["requires_candidate_characteristics"] == "yes" for row in rows
        ),
        "current_generic_high_speed_pass_rows": sum(
            row["current_generic_pass"] == "yes" for row in rows
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

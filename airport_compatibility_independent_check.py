#!/usr/bin/env python3
"""Independent cross-check of the airport-compatibility summary counts."""
import csv
from collections import Counter

INPUT = "airport_compatibility.csv"
REFERENCE_OUTPUT = "airport_compatibility_summary.csv"
OUTPUT = "airport_compatibility_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def recompute(rows):
    states = Counter(row["evidence_state"] for row in rows)
    return {
        "total_rows": len(rows),
        "framework_exists_rows": states["framework_exists"],
        "supported_historical_rows": states["supported_historical"],
        "prospective_standard_rows": states["prospective_standard"],
        "evidence_missing_rows": states["evidence_missing"],
        "rows_requiring_candidate_characteristics": sum(
            row["requires_candidate_characteristics"] == "yes" for row in rows
        ),
        "current_generic_high_speed_pass_rows": sum(
            row["high_speed_specific"] == "yes" and row["current_generic_pass"] == "yes"
            for row in rows
        ),
    }


def compare():
    independent = recompute(read_rows())
    reference = read_reference()
    return [
        {
            "metric": metric,
            "independent_value": value,
            "reference_value": reference[metric],
            "pass": value == reference[metric],
        }
        for metric, value in independent.items()
    ]


def run():
    rows = compare()
    for row in rows:
        print(
            f"{row['metric']} independent={row['independent_value']} "
            f"reference={row['reference_value']} pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

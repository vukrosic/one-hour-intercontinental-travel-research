#!/usr/bin/env python3
"""Independent bookkeeping check for close-read passenger evidence summary."""
import csv

INPUT = "passenger_ride_close_read.csv"
REFERENCE_OUTPUT = "passenger_ride_close_read_summary.csv"
OUTPUT = "passenger_ride_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    return {
        "close_read_rows": len(rows),
        "empirical_rows": sum(row["threshold_status"].startswith("study-specific") for row in rows),
        "frequency_explicit_rows": sum("Hz" in row["frequency_or_scope"] for row in rows),
        "multi_factor_rows": sum(
            "combined" in row["empirical_signal"].lower()
            or "multi-factor" in row["empirical_signal"].lower()
            or "noise/motion" in row["empirical_signal"].lower()
            for row in rows
        ),
        "medium_or_low_transferability_rows": sum(
            row["transferability"] in {"medium_with_review", "low_for_high_speed"} for row in rows
        ),
        "speed_specific_threshold_rows": sum(
            row["threshold_status"] == "speed-specific threshold demonstrated" for row in rows
        ),
        "high_speed_practical_pass_rows": sum(row["high_speed_practical_pass"] == "yes" for row in rows),
    }


def compare():
    rows = read_rows()
    independent = independently_summarize(rows)
    reference = read_reference()
    results = []
    for metric, value in independent.items():
        reference_value = reference.get(metric)
        results.append(
            {
                "metric": metric,
                "independent_value": value,
                "reference_value": reference_value,
                "pass": value == reference_value,
            }
        )
    return results


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

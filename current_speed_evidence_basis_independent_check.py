#!/usr/bin/env python3
"""Independent arithmetic check for current speed evidence-basis summary."""
import csv

INPUT = "current_speed_evidence_basis.csv"
REFERENCE_OUTPUT = "current_speed_evidence_basis_summary.csv"
OUTPUT = "current_speed_evidence_basis_independent_check.csv"
MISSING = "not_reported"
TOLERANCE = 1e-12


def optional(value):
    return None if value == MISSING else float(value)


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def independently_summarize(rows):
    parsed = [
        (
            optional(row["top_or_max_mach"]),
            optional(row["explicit_high_speed_cruise_mach"]),
            optional(row["explicit_long_range_or_typical_cruise_mach"]),
        )
        for row in rows
    ]
    gaps = [top - high for top, high, _ in parsed if top is not None and high is not None]
    top_values = [top for top, _, _ in parsed if top is not None]
    cruise_values = [value for _, high, long_range in parsed for value in (high, long_range) if value is not None]
    return {
        "current_speed_evidence_basis_rows": len(rows),
        "rows_with_top_or_max_speed": sum(top is not None for top, _, _ in parsed),
        "rows_with_explicit_high_speed_cruise": sum(high is not None for _, high, _ in parsed),
        "rows_with_explicit_long_range_or_typical_cruise": sum(long_range is not None for _, _, long_range in parsed),
        "rows_with_top_and_high_speed_cruise": len(gaps),
        "highest_top_or_max_mach": max(top_values),
        "highest_explicit_cruise_mach": max(cruise_values),
        "largest_top_minus_high_speed_cruise_gap": max(gaps),
    }


def read_reference(path=REFERENCE_OUTPUT):
    values = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            value = row["value"]
            values[row["metric"]] = float(value) if "." in value else int(value)
    return values


def compare():
    independent = independently_summarize(read_rows())
    reference = read_reference()
    return [
        {
            "metric": metric,
            "independent_value": value,
            "reference_value": reference.get(metric),
            "absolute_delta": abs(value - reference.get(metric)),
            "pass": abs(value - reference.get(metric)) <= TOLERANCE,
        }
        for metric, value in independent.items()
    ]


def run():
    rows = compare()
    for row in rows:
        print(f"{row['metric']} delta={row['absolute_delta']:.3e} pass={row['pass']}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

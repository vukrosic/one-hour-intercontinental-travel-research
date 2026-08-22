#!/usr/bin/env python3
"""Independent check for speed-basis time context."""
import csv
import math

EVIDENCE_INPUT = "current_speed_evidence_basis.csv"
CONSISTENCY_INPUT = "mach_speed_consistency_inputs.csv"
REFERENCE_OUTPUT = "current_speed_basis_time_context_summary.csv"
OUTPUT = "current_speed_basis_time_context_independent_check.csv"
MISSING = "not_reported"
TOLERANCE = 1e-12


def read_values(path):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def optional(value):
    return None if value == MISSING else float(value)


def read_rows(path=EVIDENCE_INPUT):
    with open(path, newline="") as f:
        source_rows = list(csv.DictReader(f))
    result = []
    for row in source_rows:
        for basis, field in (
            ("top_or_max", "top_or_max_mach"),
            ("explicit_high_speed_cruise", "explicit_high_speed_cruise_mach"),
            ("explicit_long_range_or_typical_cruise", "explicit_long_range_or_typical_cruise_mach"),
        ):
            mach = optional(row[field])
            if mach is not None:
                result.append({"entry_id": row["entry_id"], "speed_basis": basis, "mach": mach})
    return result


def independently_summarize(rows):
    top = [row for row in rows if row["speed_basis"] == "top_or_max"]
    cruise = [row for row in rows if row["speed_basis"] != "top_or_max"]
    g700_top = next(row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "top_or_max")
    g700_high = next(
        row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "explicit_high_speed_cruise"
    )
    savings = lambda mach: (1.0 - 0.85 / mach) * 100.0
    return {
        "current_speed_basis_time_context_rows": len(rows),
        "top_or_max_basis_rows": len(top),
        "explicit_cruise_basis_rows": len(cruise),
        "highest_top_or_max_mach": max(row["mach"] for row in top),
        "highest_explicit_cruise_mach": max(row["mach"] for row in cruise),
        "highest_explicit_cruise_saving_percent": max(savings(row["mach"]) for row in cruise),
        "g700_top_or_max_saving_percent": savings(g700_top["mach"]),
        "g700_high_speed_cruise_saving_percent": savings(g700_high["mach"]),
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

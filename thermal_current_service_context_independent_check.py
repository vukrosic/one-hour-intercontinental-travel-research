#!/usr/bin/env python3
"""Independent arithmetic check for current-speed thermal context."""
import csv

SPEED_INPUT = "current_civilian_speed_close_read.csv"
THERMAL_INPUT = "thermal_inputs.csv"
REFERENCE_OUTPUT = "thermal_current_service_context_summary.csv"
OUTPUT = "thermal_current_service_context_independent_check.csv"
TOLERANCE = 1e-12


def read_key_values(path):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def read_speeds(path=SPEED_INPUT):
    with open(path, newline="") as f:
        return [float(row["reference_speed_mach"]) for row in csv.DictReader(f)]


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        values = {}
        for row in csv.DictReader(f):
            value = row["value"]
            values[row["metric"]] = float(value) if "." in value else int(value)
        return values


def independently_summarize():
    values = read_key_values(THERMAL_INPUT)
    speeds = read_speeds() + [2.0]
    gamma = values["gamma"]
    low = values["static_temperature_low"]
    high = values["static_temperature_high"]
    rows = [
        (
            speed,
            (1.0 + 0.5 * (gamma - 1.0) * speed**2) * low,
            (1.0 + 0.5 * (gamma - 1.0) * speed**2) * high,
        )
        for speed in speeds
    ]
    current = rows[:-1]
    historical = rows[-1]
    highest_current_high = max(row[2] for row in current)
    return {
        "thermal_current_service_context_rows": len(rows),
        "current_reference_rows": len(current),
        "mach2_comparison_rows": 1,
        "mach2_lower_bound_K": historical[1],
        "highest_current_reference_upper_bound_K": highest_current_high,
        "mach2_lower_to_highest_current_upper_ratio": historical[1] / highest_current_high,
        "mach2_lower_exceeds_highest_current_upper": int(historical[1] > highest_current_high),
    }


def compare():
    independent = independently_summarize()
    reference = read_reference()
    results = []
    for metric, value in independent.items():
        reference_value = reference.get(metric)
        delta = abs(value - reference_value)
        results.append(
            {
                "metric": metric,
                "independent_value": value,
                "reference_value": reference_value,
                "absolute_delta": delta,
                "pass": delta <= TOLERANCE,
            }
        )
    return results


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

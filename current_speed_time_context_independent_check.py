#!/usr/bin/env python3
"""Independent arithmetic check for current speed/time context."""
import csv
import math

SPEED_INPUT = "current_civilian_speed_close_read.csv"
CONSISTENCY_INPUT = "mach_speed_consistency_inputs.csv"
REFERENCE_OUTPUT = "current_speed_time_context_summary.csv"
OUTPUT = "current_speed_time_context_independent_check.csv"
TOLERANCE = 1e-12


def read_values(path):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def read_machs(path=SPEED_INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return [float(row["reference_speed_mach"]) for row in rows] + [2.0]


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        result = {}
        for row in csv.DictReader(f):
            value = row["value"]
            result[row["metric"]] = float(value) if "." in value else int(value)
        return result


def independently_summarize():
    values = read_values(CONSISTENCY_INPUT)
    machs = read_machs()
    sound_speeds = [
        math.sqrt(gamma * values["specific_gas_constant"] * temperature) * 3.6
        for gamma in (values["gamma_low"], values["gamma_high"])
        for temperature in (values["static_temperature_low"], values["static_temperature_high"])
    ]
    speed_low = min(sound_speeds)
    speed_high = max(sound_speeds)
    airline = machs[0]
    savings = [(1.0 - airline / mach) * 100.0 for mach in machs]
    return {
        "current_speed_time_context_rows": len(machs),
        "current_reference_rows": len(machs) - 1,
        "mach2_comparison_rows": 1,
        "airline_reference_saving_percent": savings[0],
        "global7500_reference_saving_percent": savings[1],
        "g700_reference_saving_percent": savings[2],
        "g8000_reference_saving_percent": savings[3],
        "mach2_speed_only_saving_percent": savings[4],
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

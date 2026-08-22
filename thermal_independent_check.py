#!/usr/bin/env python3
"""Independent cross-check of the bounded ideal thermal sensitivity."""
import csv

INPUT = "thermal_inputs.csv"
REFERENCE_OUTPUT = "thermal_sensitivity.csv"
OUTPUT = "thermal_independent_check.csv"
TOLERANCE = 1e-12


def read_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return {row["key"]: float(row["value"]) for row in rows}


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(values, mach):
    ratio = 1.0 + 0.5 * (values["gamma"] - 1.0) * mach**2
    return {
        "mach_bin": mach,
        "independent_ratio": ratio,
        "independent_low_K": ratio * values["static_temperature_low"],
        "independent_high_K": ratio * values["static_temperature_high"],
    }


def compare():
    values = read_inputs()
    rows = []
    for reference_row in read_reference():
        mach = float(reference_row["mach_bin"])
        independent = recompute(values, mach)
        deltas = {
            "ratio": independent["independent_ratio"]
            - float(reference_row["ideal_total_to_static_temperature_ratio"]),
            "low_K": independent["independent_low_K"]
            - float(reference_row["ideal_total_temperature_low_K"]),
            "high_K": independent["independent_high_K"]
            - float(reference_row["ideal_total_temperature_high_K"]),
        }
        max_delta = max(abs(delta) for delta in deltas.values())
        rows.append(
            {
                **independent,
                "reference_ratio": reference_row["ideal_total_to_static_temperature_ratio"],
                "reference_low_K": reference_row["ideal_total_temperature_low_K"],
                "reference_high_K": reference_row["ideal_total_temperature_high_K"],
                "max_absolute_delta": max_delta,
                "pass": max_delta <= TOLERANCE,
            }
        )
    return rows


def run():
    rows = compare()
    for row in rows:
        print(
            f"Mach {row['mach_bin']:.2f} "
            f"max_absolute_delta={row['max_absolute_delta']:.3e} "
            f"pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

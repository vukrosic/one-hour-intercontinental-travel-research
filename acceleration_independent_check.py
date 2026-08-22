#!/usr/bin/env python3
"""Independent reproduction of the abstract acceleration sensitivity table."""
import csv
import math

INPUTS = "acceleration_inputs.csv"
REFERENCE_OUTPUT = "acceleration_sensitivity.csv"
OUTPUT = "acceleration_independent_check.csv"
TOLERANCE = 1e-12


def read_inputs(path=INPUTS):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(row, inputs):
    distance_m = inputs["reference_distance_km"] * 1000.0
    speed_kmh = float(row["speed_kmh"])
    acceleration_fraction = float(row["acceleration_fraction_g"])
    speed_mps = speed_kmh / 3.6
    acceleration_mps2 = acceleration_fraction * inputs["standard_gravity"]
    half_phase_time_s = speed_mps / acceleration_mps2
    accel_decel_distance_m = speed_mps**2 / acceleration_mps2
    distance_fraction = accel_decel_distance_m / distance_m
    cruise_only_time_s = distance_m / speed_mps
    if accel_decel_distance_m <= distance_m:
        cruise_time_s = (distance_m - accel_decel_distance_m) / speed_mps
        total_time_s = 2 * half_phase_time_s + cruise_time_s
        profile = "accelerate-cruise-decelerate"
    else:
        cruise_time_s = 0.0
        total_time_s = 2 * math.sqrt(distance_m / acceleration_mps2)
        profile = "no-cruise-lower-bound"
    return {
        "half_phase_time_s": half_phase_time_s,
        "accel_decel_distance_km": accel_decel_distance_m / 1000.0,
        "accel_decel_distance_fraction": distance_fraction,
        "cruise_time_s": cruise_time_s,
        "cruise_only_time_s": cruise_only_time_s,
        "total_idealized_time_s": total_time_s,
        "acceleration_time_overhead_fraction": (total_time_s - cruise_only_time_s)
        / cruise_only_time_s,
        "profile_regime": profile,
    }


def compare():
    inputs = read_inputs()
    rows = []
    numeric_fields = (
        "half_phase_time_s",
        "accel_decel_distance_km",
        "accel_decel_distance_fraction",
        "cruise_time_s",
        "cruise_only_time_s",
        "total_idealized_time_s",
        "acceleration_time_overhead_fraction",
    )
    for reference in read_reference():
        independent = recompute(reference, inputs)
        deltas = [
            abs(independent[field] - float(reference[field])) for field in numeric_fields
        ]
        profile_match = independent["profile_regime"] == reference["profile_regime"]
        rows.append(
            {
                "speed_bin": reference["speed_bin"],
                "speed_kmh": reference["speed_kmh"],
                "acceleration_fraction_g": reference["acceleration_fraction_g"],
                "max_absolute_delta": max(deltas),
                "profile_match": profile_match,
                "pass": max(deltas) <= TOLERANCE and profile_match,
            }
        )
    return rows


def run():
    rows = compare()
    for row in rows:
        print(
            f"{row['speed_bin']} a={float(row['acceleration_fraction_g']):.2f}g "
            f"max_absolute_delta={row['max_absolute_delta']:.3e} pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

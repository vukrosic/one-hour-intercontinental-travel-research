#!/usr/bin/env python3
"""Non-actionable acceleration/time sensitivity for abstract speed bins.

This is a kinematic thought experiment. It contains no aircraft geometry,
trajectory, control law, route, or passenger-comfort threshold.
"""
import csv
import math

INPUTS = "acceleration_inputs.csv"
SCENARIOS = "acceleration_scenarios.csv"
OUTPUT = "acceleration_sensitivity.csv"


def load_inputs(path=INPUTS):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    values = {row["key"]: float(row["value"]) for row in rows}
    if values["reference_distance_km"] <= 0 or values["standard_gravity"] <= 0:
        raise ValueError("inputs must be positive")
    return values


def load_scenarios(path=SCENARIOS):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("scenario table is empty")
    for row in rows:
        if float(row["speed_kmh"]) <= 0 or float(row["acceleration_fraction_g"]) <= 0:
            raise ValueError("speed and acceleration must be positive")
    return rows


def calculate(inputs=None, scenarios=None):
    inputs = load_inputs() if inputs is None else inputs
    scenarios = load_scenarios() if scenarios is None else scenarios
    distance_m = inputs["reference_distance_km"] * 1000.0
    g = inputs["standard_gravity"]
    result = []
    for scenario in scenarios:
        speed_kmh = float(scenario["speed_kmh"])
        speed_mps = speed_kmh / 3.6
        acceleration_fraction = float(scenario["acceleration_fraction_g"])
        acceleration_mps2 = acceleration_fraction * g
        half_phase_time_s = speed_mps / acceleration_mps2
        accel_decel_distance_m = speed_mps**2 / acceleration_mps2
        distance_fraction = accel_decel_distance_m / distance_m
        cruise_only_time_s = distance_m / speed_mps
        if accel_decel_distance_m <= distance_m:
            cruise_distance_m = distance_m - accel_decel_distance_m
            cruise_time_s = cruise_distance_m / speed_mps
            total_time_s = 2 * half_phase_time_s + cruise_time_s
            profile = "accelerate-cruise-decelerate"
        else:
            cruise_time_s = 0.0
            total_time_s = 2 * math.sqrt(distance_m / acceleration_mps2)
            profile = "no-cruise-lower-bound"
        result.append(
            {
                "speed_bin": scenario["speed_bin"],
                "speed_kmh": speed_kmh,
                "acceleration_fraction_g": acceleration_fraction,
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
        )
    return result


def run():
    rows = calculate()
    for row in rows:
        print(
            f"{row['speed_bin']} a={row['acceleration_fraction_g']:.2f}g "
            f"distance_fraction={row['accel_decel_distance_fraction']:.3f} "
            f"overhead={row['acceleration_time_overhead_fraction']:.3f} "
            f"profile={row['profile_regime']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

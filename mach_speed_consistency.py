#!/usr/bin/env python3
"""Audit Mach-to-speed consistency and its kinematic sensitivity.

The model uses the ideal speed-of-sound relation only to check whether the
repository's nominal km/h bins are compatible with the declared Mach and
static-temperature intervals. It is not a vehicle, trajectory, route, or
operating model.
"""
import csv
import math

INPUT = "mach_speed_consistency_inputs.csv"
SPEED_OUTPUT = "mach_speed_consistency.csv"
ACCELERATION_OUTPUT = "mach_speed_acceleration_ranges.csv"
MACH_CLASSES = (
    ("subsonic_reference", 0.85, 900.0),
    ("Concorde_historical", 2.0, 2160.0),
    ("Mach_3_conceptual_bin", 3.0, 3240.0),
    ("Mach_5_conceptual_bin", 5.0, 5400.0),
)
ACCELERATION_FRACTIONS_G = (0.05, 0.10, 0.20)


def load_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    values = {row["key"]: float(row["value"]) for row in rows}
    required = {
        "static_temperature_low",
        "static_temperature_high",
        "gamma_low",
        "gamma_high",
        "specific_gas_constant",
        "reference_distance_km",
        "standard_gravity",
    }
    if required - values.keys():
        raise ValueError("consistency inputs missing required keys")
    if values["static_temperature_low"] >= values["static_temperature_high"]:
        raise ValueError("static-temperature interval is not increasing")
    if values["gamma_low"] <= 1.0 or values["gamma_high"] <= values["gamma_low"]:
        raise ValueError("gamma interval is invalid")
    return values


def speed_of_sound_kmh(values, gamma, temperature):
    return math.sqrt(gamma * values["specific_gas_constant"] * temperature) * 3.6


def calculate(values=None):
    values = load_inputs() if values is None else values
    speed_rows = []
    acceleration_rows = []
    for speed_bin, mach, nominal_speed in MACH_CLASSES:
        speeds = []
        for gamma in (values["gamma_low"], values["gamma_high"]):
            for temperature in (values["static_temperature_low"], values["static_temperature_high"]):
                speed = mach * speed_of_sound_kmh(values, gamma, temperature)
                speeds.append(speed)
                speed_rows.append(
                    {
                        "speed_bin": speed_bin,
                        "mach": mach,
                        "nominal_speed_kmh": nominal_speed,
                        "gamma": gamma,
                        "static_temperature_K": temperature,
                        "derived_speed_kmh": speed,
                    }
                )
        speed_low = min(speeds)
        speed_high = max(speeds)
        nominal_within = speed_low <= nominal_speed <= speed_high
        for acceleration_fraction_g in ACCELERATION_FRACTIONS_G:
            acceleration = acceleration_fraction_g * values["standard_gravity"]
            distance_m = values["reference_distance_km"] * 1000.0
            distance_fraction_low = (speed_low / 3.6) ** 2 / acceleration / distance_m
            distance_fraction_high = (speed_high / 3.6) ** 2 / acceleration / distance_m
            acceleration_rows.append(
                {
                    "speed_bin": speed_bin,
                    "mach": mach,
                    "acceleration_fraction_g": acceleration_fraction_g,
                    "derived_speed_low_kmh": speed_low,
                    "derived_speed_high_kmh": speed_high,
                    "nominal_speed_kmh": nominal_speed,
                    "nominal_within_derived_interval": nominal_within,
                    "accel_decel_distance_fraction_low": distance_fraction_low,
                    "accel_decel_distance_fraction_high": distance_fraction_high,
                }
            )
    return speed_rows, acceleration_rows


def write_rows(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run():
    speed_rows, acceleration_rows = calculate()
    for row in acceleration_rows:
        print(
            f"{row['speed_bin']} a={row['acceleration_fraction_g']:.2f}g "
            f"speed={row['derived_speed_low_kmh']:.0f}–{row['derived_speed_high_kmh']:.0f} km/h "
            f"phase_distance_fraction={row['accel_decel_distance_fraction_low']:.3f}–"
            f"{row['accel_decel_distance_fraction_high']:.3f}"
        )
    write_rows(SPEED_OUTPUT, speed_rows)
    write_rows(ACCELERATION_OUTPUT, acceleration_rows)


if __name__ == "__main__":
    run()

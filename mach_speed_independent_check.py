#!/usr/bin/env python3
"""Independent reproduction of the Mach-to-speed consistency tables."""
import csv
import math

INPUT = "mach_speed_consistency_inputs.csv"
SPEED_REFERENCE = "mach_speed_consistency.csv"
ACCELERATION_REFERENCE = "mach_speed_acceleration_ranges.csv"
OUTPUT = "mach_speed_independent_check.csv"
TOLERANCE = 1e-12
MACH_BY_BIN = {
    "subsonic_reference": (0.85, 900.0),
    "Concorde_historical": (2.0, 2160.0),
    "Mach_3_conceptual_bin": (3.0, 3240.0),
    "Mach_5_conceptual_bin": (5.0, 5400.0),
}


def read_inputs(path=INPUT):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def sound_speed(values, gamma, temperature):
    return math.sqrt(gamma * values["specific_gas_constant"] * temperature) * 3.6


def compare():
    values = read_inputs()
    results = []
    for reference in read_rows(SPEED_REFERENCE):
        mach, nominal = MACH_BY_BIN[reference["speed_bin"]]
        gamma = float(reference["gamma"])
        temperature = float(reference["static_temperature_K"])
        derived = mach * sound_speed(values, gamma, temperature)
        delta = derived - float(reference["derived_speed_kmh"])
        results.append(
            {
                "table": "speed",
                "row_key": f"{reference['speed_bin']}|{gamma}|{temperature}",
                "max_absolute_delta": abs(delta),
                "pass": abs(delta) <= TOLERANCE,
            }
        )
    for reference in read_rows(ACCELERATION_REFERENCE):
        mach, nominal = MACH_BY_BIN[reference["speed_bin"]]
        speeds = [
            mach * sound_speed(values, gamma, temperature)
            for gamma in (values["gamma_low"], values["gamma_high"])
            for temperature in (values["static_temperature_low"], values["static_temperature_high"])
        ]
        speed_low, speed_high = min(speeds), max(speeds)
        acceleration = float(reference["acceleration_fraction_g"]) * values["standard_gravity"]
        distance_m = values["reference_distance_km"] * 1000.0
        low_fraction = (speed_low / 3.6) ** 2 / acceleration / distance_m
        high_fraction = (speed_high / 3.6) ** 2 / acceleration / distance_m
        deltas = [
            speed_low - float(reference["derived_speed_low_kmh"]),
            speed_high - float(reference["derived_speed_high_kmh"]),
            low_fraction - float(reference["accel_decel_distance_fraction_low"]),
            high_fraction - float(reference["accel_decel_distance_fraction_high"]),
        ]
        max_delta = max(abs(delta) for delta in deltas)
        results.append(
            {
                "table": "acceleration",
                "row_key": f"{reference['speed_bin']}|{reference['acceleration_fraction_g']}",
                "max_absolute_delta": max_delta,
                "pass": max_delta <= TOLERANCE,
            }
        )
    return results


def run():
    rows = compare()
    for row in rows:
        print(f"{row['table']} {row['row_key']} max_absolute_delta={row['max_absolute_delta']:.3e} pass={row['pass']}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

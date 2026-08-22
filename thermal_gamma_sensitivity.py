#!/usr/bin/env python3
"""Bounded ideal total-temperature sensitivity to the gamma assumption.

This is an analytical robustness check around the existing thermal screen. It
varies the calorically-perfect-air parameter only; it is not a wall-temperature,
heat-flux, material, geometry, cooling, trajectory, or operating model.
"""
import csv

from physics_envelope import MACH_BINS, total_temperature_ratio

INPUT = "thermal_inputs.csv"
OUTPUT = "thermal_gamma_sensitivity.csv"
GAMMA_SCENARIOS = (1.30, 1.40)


def load_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    values = {row["key"]: float(row["value"]) for row in rows}
    required = {"static_temperature_low", "static_temperature_high", "gamma"}
    if required - values.keys():
        raise ValueError("thermal inputs missing required keys")
    if values["static_temperature_low"] >= values["static_temperature_high"]:
        raise ValueError("temperature interval is not increasing")
    if any(gamma <= 1.0 for gamma in GAMMA_SCENARIOS):
        raise ValueError("gamma scenarios must exceed one")
    return values


def calculate(values=None):
    values = load_inputs() if values is None else values
    rows = []
    for gamma in GAMMA_SCENARIOS:
        for mach in MACH_BINS:
            ratio = total_temperature_ratio(mach, gamma)
            rows.append(
                {
                    "gamma_scenario": gamma,
                    "mach_bin": mach,
                    "ideal_total_to_static_temperature_ratio": ratio,
                    "ideal_total_temperature_low_K": ratio * values["static_temperature_low"],
                    "ideal_total_temperature_high_K": ratio * values["static_temperature_high"],
                }
            )
    return rows


def run():
    rows = calculate()
    for row in rows:
        print(
            f"gamma={row['gamma_scenario']:.2f} Mach {row['mach_bin']:.2f}: "
            f"ideal T0 interval "
            f"{row['ideal_total_temperature_low_K']:.1f}–"
            f"{row['ideal_total_temperature_high_K']:.1f} K"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

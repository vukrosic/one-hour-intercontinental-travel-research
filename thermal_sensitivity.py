#!/usr/bin/env python3
"""Bounded ideal total-temperature sensitivity by Mach bin.

The result is a thermodynamic screening interval, not wall temperature, heat
flux, material selection, vehicle analysis, or operating guidance.
"""
import csv

from physics_envelope import MACH_BINS, total_temperature_ratio

INPUT = "thermal_inputs.csv"
OUTPUT = "thermal_sensitivity.csv"


def load_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"key", "value", "unit", "source_id", "role", "limitation"}
    if not rows or required - set(rows[0]):
        raise ValueError("invalid thermal input table")
    values = {}
    for row in rows:
        if not all(row[field].strip() for field in required):
            raise ValueError(f"blank evidence field for {row.get('key', '<unknown>')}")
        if row["key"] in values:
            raise ValueError(f"duplicate key: {row['key']}")
        values[row["key"]] = float(row["value"])
    if values["static_temperature_low"] >= values["static_temperature_high"]:
        raise ValueError("temperature interval is not increasing")
    return values


def calculate(values):
    rows = []
    for mach in MACH_BINS:
        ratio = total_temperature_ratio(mach, values["gamma"])
        rows.append(
            {
                "mach_bin": mach,
                "ideal_total_to_static_temperature_ratio": ratio,
                "ideal_total_temperature_low_K": ratio * values["static_temperature_low"],
                "ideal_total_temperature_high_K": ratio * values["static_temperature_high"],
            }
        )
    return rows


def run():
    rows = calculate(load_inputs())
    for row in rows:
        print(
            f"Mach {row['mach_bin']:.2f}: ideal T0 interval "
            f"{row['ideal_total_temperature_low_K']:.1f}–{row['ideal_total_temperature_high_K']:.1f} K"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

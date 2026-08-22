#!/usr/bin/env python3
"""Bounded airborne-time context for current civilian Mach references.

The fixed distance is a mathematical yardstick inherited from the archived
screen. This is speed-only arithmetic, not a route, schedule, trajectory, or
operations model.
"""
import csv
import math

SPEED_INPUT = "current_civilian_speed_close_read.csv"
CONSISTENCY_INPUT = "mach_speed_consistency_inputs.csv"
OUTPUT = "current_speed_time_context.csv"
SUMMARY_OUTPUT = "current_speed_time_context_summary.csv"


def read_key_values(path):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def load_rows(path=SPEED_INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"entry_id", "aircraft_class", "reference_speed_mach"}
    if not rows or required - set(rows[0]):
        raise ValueError("invalid current speed table")
    result = []
    for row in rows:
        mach = float(row["reference_speed_mach"])
        if not 0 < mach < 1:
            raise ValueError(f"expected subsonic current reference: {row['entry_id']}")
        result.append(
            {
                "reference_id": row["entry_id"],
                "reference_label": row["aircraft_class"],
                "mach": mach,
            }
        )
    result.append(
        {
            "reference_id": "MACH2_HISTORICAL",
            "reference_label": "Mach 2 historical service class",
            "mach": 2.0,
        }
    )
    return result


def sound_speed_kmh(values, gamma, temperature):
    return math.sqrt(gamma * values["specific_gas_constant"] * temperature) * 3.6


def calculate(values=None, rows=None):
    values = read_key_values(CONSISTENCY_INPUT) if values is None else values
    rows = load_rows() if rows is None else rows
    sound_speeds = [
        sound_speed_kmh(values, gamma, temperature)
        for gamma in (values["gamma_low"], values["gamma_high"])
        for temperature in (values["static_temperature_low"], values["static_temperature_high"])
    ]
    sound_low = min(sound_speeds)
    sound_high = max(sound_speeds)
    distance = values["reference_distance_km"]
    airline_mach = next(row["mach"] for row in rows if row["reference_id"] == "SPEED-001")
    output = []
    for row in rows:
        speed_low = row["mach"] * sound_low
        speed_high = row["mach"] * sound_high
        output.append(
            {
                **row,
                "derived_speed_low_kmh": speed_low,
                "derived_speed_high_kmh": speed_high,
                "airborne_time_high_minutes": distance / speed_low * 60.0,
                "airborne_time_low_minutes": distance / speed_high * 60.0,
                "speed_only_time_saving_vs_airline_percent": (1.0 - airline_mach / row["mach"]) * 100.0,
            }
        )
    return output


def summarize(rows):
    service_rows = [row for row in rows if row["reference_id"] != "MACH2_HISTORICAL"]
    mach2 = next(row for row in rows if row["reference_id"] == "MACH2_HISTORICAL")
    return {
        "current_speed_time_context_rows": len(rows),
        "current_reference_rows": len(service_rows),
        "mach2_comparison_rows": 1,
        "airline_reference_saving_percent": next(
            row["speed_only_time_saving_vs_airline_percent"]
            for row in rows
            if row["reference_id"] == "SPEED-001"
        ),
        "certified_business_reference_saving_percent": next(
            row["speed_only_time_saving_vs_airline_percent"]
            for row in rows
            if row["reference_id"] == "SPEED-002"
        ),
        "marketed_high_subsonic_reference_saving_percent": next(
            row["speed_only_time_saving_vs_airline_percent"]
            for row in rows
            if row["reference_id"] == "SPEED-003"
        ),
        "mach2_speed_only_saving_percent": mach2["speed_only_time_saving_vs_airline_percent"],
    }


def run():
    rows = calculate()
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    summary = summarize(rows)
    for key, value in summary.items():
        print(f"{key}={value}")
    with open(SUMMARY_OUTPUT, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerows(summary.items())


if __name__ == "__main__":
    run()

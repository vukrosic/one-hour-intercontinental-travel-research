#!/usr/bin/env python3
"""Compute fixed-distance time context by explicitly stated speed basis.

Top/max rows are retained as labeled arithmetic context only. Explicit cruise
rows are the more relevant basis for repeatable passenger-service comparisons.
No route, trajectory, operating procedure, or aircraft design is inferred.
"""
import csv
import math

EVIDENCE_INPUT = "current_speed_evidence_basis.csv"
CONSISTENCY_INPUT = "mach_speed_consistency_inputs.csv"
OUTPUT = "current_speed_basis_time_context.csv"
SUMMARY_OUTPUT = "current_speed_basis_time_context_summary.csv"
MISSING = "not_reported"


def read_key_values(path):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def optional(value):
    return None if value == MISSING else float(value)


def load_rows(path=EVIDENCE_INPUT):
    with open(path, newline="") as f:
        source_rows = list(csv.DictReader(f))
    result = []
    for row in source_rows:
        bases = (
            ("top_or_max", "top_or_max_mach", "top/max arithmetic only"),
            ("explicit_high_speed_cruise", "explicit_high_speed_cruise_mach", "explicit cruise wording"),
            (
                "explicit_long_range_or_typical_cruise",
                "explicit_long_range_or_typical_cruise_mach",
                "explicit cruise wording",
            ),
        )
        for basis, field, interpretation in bases:
            mach = optional(row[field])
            if mach is not None:
                result.append(
                    {
                        "entry_id": row["entry_id"],
                        "aircraft_class": row["aircraft_class"],
                        "speed_basis": basis,
                        "basis_interpretation": interpretation,
                        "mach": mach,
                    }
                )
    if not result:
        raise ValueError("no speed-basis rows")
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
    airline_mach = 0.85
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
    top = [row for row in rows if row["speed_basis"] == "top_or_max"]
    cruise = [row for row in rows if row["speed_basis"] != "top_or_max"]
    g700_top = next(row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "top_or_max")
    g700_high = next(
        row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "explicit_high_speed_cruise"
    )
    return {
        "current_speed_basis_time_context_rows": len(rows),
        "top_or_max_basis_rows": len(top),
        "explicit_cruise_basis_rows": len(cruise),
        "highest_top_or_max_mach": max(row["mach"] for row in top),
        "highest_explicit_cruise_mach": max(row["mach"] for row in cruise),
        "highest_explicit_cruise_saving_percent": max(
            row["speed_only_time_saving_vs_airline_percent"] for row in cruise
        ),
        "g700_top_or_max_saving_percent": g700_top["speed_only_time_saving_vs_airline_percent"],
        "g700_high_speed_cruise_saving_percent": g700_high["speed_only_time_saving_vs_airline_percent"],
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

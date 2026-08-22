#!/usr/bin/env python3
"""Independent reproduction of acceleration-adjusted time comparisons."""
import csv

INPUT = "acceleration_sensitivity.csv"
REFERENCE_OUTPUT = "effective_time_sensitivity.csv"
OUTPUT = "effective_time_independent_check.csv"
TOLERANCE = 1e-12


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(acceleration_rows, reference_row):
    acceleration = float(reference_row["acceleration_fraction_g"])
    group = [
        row
        for row in acceleration_rows
        if abs(float(row["acceleration_fraction_g"]) - acceleration) <= TOLERANCE
    ]
    reference = next(row for row in group if row["speed_bin"] == "subsonic_reference")
    reference_cruise = float(reference["cruise_only_time_s"])
    reference_total = float(reference["total_idealized_time_s"])
    row = next(
        row
        for row in group
        if row["speed_bin"] == reference_row["speed_bin"]
        and abs(float(row["speed_kmh"]) - float(reference_row["speed_kmh"])) <= TOLERANCE
    )
    cruise = float(row["cruise_only_time_s"])
    total = float(row["total_idealized_time_s"])
    speed_ratio = cruise / reference_cruise
    adjusted_ratio = total / reference_total
    return {
        "independent_speed_only_ratio": speed_ratio,
        "independent_adjusted_ratio": adjusted_ratio,
        "independent_speed_only_saved": 1.0 - speed_ratio,
        "independent_adjusted_saved": 1.0 - adjusted_ratio,
        "independent_saved_lost": adjusted_ratio - speed_ratio,
        "independent_overhead": float(row["acceleration_time_overhead_fraction"]),
    }


def compare():
    acceleration_rows = read_rows(INPUT)
    reference_rows = read_rows(REFERENCE_OUTPUT)
    results = []
    for reference in reference_rows:
        independent = recompute(acceleration_rows, reference)
        deltas = {
            "speed_ratio": independent["independent_speed_only_ratio"]
            - float(reference["speed_only_time_ratio_vs_subsonic"]),
            "adjusted_ratio": independent["independent_adjusted_ratio"]
            - float(reference["acceleration_adjusted_time_ratio_vs_subsonic"]),
            "speed_saved": independent["independent_speed_only_saved"]
            - float(reference["speed_only_saved_fraction_vs_subsonic"]),
            "adjusted_saved": independent["independent_adjusted_saved"]
            - float(reference["acceleration_adjusted_saved_fraction_vs_subsonic"]),
            "saved_lost": independent["independent_saved_lost"]
            - float(reference["saved_fraction_lost_to_acceleration"]),
            "overhead": independent["independent_overhead"]
            - float(reference["candidate_acceleration_overhead_fraction"]),
        }
        max_delta = max(abs(delta) for delta in deltas.values())
        results.append(
            {
                "speed_bin": reference["speed_bin"],
                "acceleration_fraction_g": reference["acceleration_fraction_g"],
                **independent,
                "max_absolute_delta": max_delta,
                "pass": max_delta <= TOLERANCE,
            }
        )
    return results


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

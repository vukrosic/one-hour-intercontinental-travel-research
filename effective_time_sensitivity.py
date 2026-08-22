#!/usr/bin/env python3
"""Compare speed-only and acceleration-adjusted airborne-time savings.

This consumes the committed abstract acceleration table. It is a derived
kinematic comparison, not a flight profile, route, trajectory, or operation.
"""
import csv

INPUT = "acceleration_sensitivity.csv"
OUTPUT = "effective_time_sensitivity.csv"


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required = {
        "speed_bin",
        "speed_kmh",
        "acceleration_fraction_g",
        "cruise_only_time_s",
        "total_idealized_time_s",
        "acceleration_time_overhead_fraction",
    }
    if not rows or required - set(rows[0]):
        raise ValueError("invalid acceleration sensitivity table")
    return rows


def calculate(rows=None):
    rows = load_rows() if rows is None else rows
    by_acceleration = {}
    for row in rows:
        acceleration = float(row["acceleration_fraction_g"])
        by_acceleration.setdefault(acceleration, []).append(row)
    result = []
    for acceleration, group in sorted(by_acceleration.items()):
        references = [row for row in group if row["speed_bin"] == "subsonic_reference"]
        if len(references) != 1:
            raise ValueError(f"expected one subsonic reference at {acceleration}g")
        reference = references[0]
        reference_cruise = float(reference["cruise_only_time_s"])
        reference_total = float(reference["total_idealized_time_s"])
        for row in sorted(group, key=lambda item: float(item["speed_kmh"])):
            cruise_time = float(row["cruise_only_time_s"])
            total_time = float(row["total_idealized_time_s"])
            speed_only_ratio = cruise_time / reference_cruise
            adjusted_ratio = total_time / reference_total
            result.append(
                {
                    "speed_bin": row["speed_bin"],
                    "speed_kmh": float(row["speed_kmh"]),
                    "acceleration_fraction_g": acceleration,
                    "speed_only_time_ratio_vs_subsonic": speed_only_ratio,
                    "acceleration_adjusted_time_ratio_vs_subsonic": adjusted_ratio,
                    "speed_only_saved_fraction_vs_subsonic": 1.0 - speed_only_ratio,
                    "acceleration_adjusted_saved_fraction_vs_subsonic": 1.0 - adjusted_ratio,
                    "saved_fraction_lost_to_acceleration": adjusted_ratio - speed_only_ratio,
                    "candidate_acceleration_overhead_fraction": float(
                        row["acceleration_time_overhead_fraction"]
                    ),
                }
            )
    return result


def run():
    rows = calculate()
    for row in rows:
        print(
            f"{row['speed_bin']} a={row['acceleration_fraction_g']:.2f}g "
            f"adjusted_ratio={row['acceleration_adjusted_time_ratio_vs_subsonic']:.3f} "
            f"saved={row['acceleration_adjusted_saved_fraction_vs_subsonic']:.1%}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

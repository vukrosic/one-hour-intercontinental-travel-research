#!/usr/bin/env python3
"""Quantify the historical Mach 2 proxy's gap to the modern benchmark."""
import csv

INPUT = "energy_intensity_results.csv"
OUTPUT = "energy_gap_sensitivity.csv"


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("energy results table is empty")
    return rows


def calculate(rows=None):
    rows = load_rows() if rows is None else rows
    result = []
    for row in rows:
        ratio = float(row["energy_ratio_vs_modern_long_haul"])
        result.append(
            {
                "load_factor": float(row["load_factor"]),
                "historical_proxy_ratio": ratio,
                "historical_intensity_fraction_allowed_to_match": 1.0 / ratio,
                "required_reduction_fraction": 1.0 - 1.0 / ratio,
                "required_reduction_percent": (1.0 - 1.0 / ratio) * 100.0,
            }
        )
    return result


def run():
    rows = calculate()
    for row in rows:
        print(
            f"load_factor={row['load_factor']:.0%} "
            f"historical_ratio={row['historical_proxy_ratio']:.2f}x "
            f"required_reduction={row['required_reduction_percent']:.1f}%"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

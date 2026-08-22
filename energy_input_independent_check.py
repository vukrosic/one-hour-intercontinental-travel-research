#!/usr/bin/env python3
"""Independent arithmetic reproduction of the energy input stress table."""
import csv

INPUT = "energy_inputs.csv"
REFERENCE_OUTPUT = "energy_input_sensitivity.csv"
OUTPUT = "energy_input_independent_check.csv"
TOLERANCE = 1e-12


def read_inputs(path=INPUT):
    with open(path, newline="") as f:
        return {row["key"]: float(row["value"]) for row in csv.DictReader(f)}


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(values, row):
    fuel = values["concorde_fuel_l_per_hour"] * float(row["fuel_multiplier"])
    speed = values["concorde_speed_kmh"] * float(row["speed_multiplier"])
    seats = values["concorde_seat_capacity"] * float(row["seat_capacity_multiplier"])
    benchmark = values["long_haul_co2_kg_per_passenger_mile"] * float(
        row["modern_benchmark_multiplier"]
    )
    load_factor = float(row["load_factor"])
    # Alternate grouping: first form passenger miles per hour, then convert
    # the historical fuel liters to US gallons.
    passenger_miles_per_hour = seats * load_factor * speed / values["km_per_mile"]
    fuel_gallons_per_hour = fuel / values["liters_per_us_gallon"]
    historical_co2 = (
        fuel_gallons_per_hour / passenger_miles_per_hour * values["jet_co2_kg_per_us_gallon"]
    )
    ratio = historical_co2 / benchmark
    return ratio, (1.0 - 1.0 / ratio) * 100.0


def compare():
    values = read_inputs()
    rows = []
    for reference_row in read_reference():
        ratio, reduction = recompute(values, reference_row)
        reference_ratio = float(reference_row["historical_proxy_co2_ratio_vs_modern"])
        reference_reduction = float(reference_row["required_reduction_percent_to_match"])
        max_delta = max(abs(ratio - reference_ratio), abs(reduction - reference_reduction))
        rows.append(
            {
                "scenario": reference_row["scenario"],
                "load_factor": reference_row["load_factor"],
                "independent_ratio": ratio,
                "independent_reduction_percent": reduction,
                "reference_ratio": reference_row["historical_proxy_co2_ratio_vs_modern"],
                "reference_reduction_percent": reference_row["required_reduction_percent_to_match"],
                "max_absolute_delta": max_delta,
                "pass": max_delta <= TOLERANCE,
            }
        )
    return rows


def run():
    rows = compare()
    for row in rows:
        print(
            f"{row['scenario']} load_factor={float(row['load_factor']):.0%} "
            f"max_absolute_delta={row['max_absolute_delta']:.3e} pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

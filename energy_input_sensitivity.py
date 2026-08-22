#!/usr/bin/env python3
"""Stress-test the historical energy proxy against declared input perturbations.

The scenarios are deterministic +/-10% bookkeeping stresses, not statistical
uncertainty intervals and not technology or design targets. The model remains
an aggregate historical-versus-modern passenger-distance comparison.
"""
import csv

INPUT = "energy_inputs.csv"
OUTPUT = "energy_input_sensitivity.csv"
LOAD_FACTORS = (1.0, 0.8, 0.6)
PERTURBATION = 0.10


def load_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    values = {row["key"]: float(row["value"]) for row in rows}
    required = {
        "concorde_fuel_l_per_hour",
        "concorde_speed_kmh",
        "concorde_seat_capacity",
        "jet_co2_kg_per_us_gallon",
        "long_haul_co2_kg_per_passenger_mile",
        "km_per_mile",
    }
    if required - values.keys():
        raise ValueError("energy inputs missing required keys")
    if any(values[key] <= 0 for key in required):
        raise ValueError("energy inputs must be positive")
    return values


def scenario_definitions():
    """Return deterministic stress multipliers for the public proxy inputs."""
    return (
        ("baseline", 1.0, 1.0, 1.0, 1.0),
        ("fuel_minus_10pct", 1.0 - PERTURBATION, 1.0, 1.0, 1.0),
        ("fuel_plus_10pct", 1.0 + PERTURBATION, 1.0, 1.0, 1.0),
        ("speed_minus_10pct", 1.0, 1.0 - PERTURBATION, 1.0, 1.0),
        ("speed_plus_10pct", 1.0, 1.0 + PERTURBATION, 1.0, 1.0),
        ("seats_minus_10pct", 1.0, 1.0, 1.0 - PERTURBATION, 1.0),
        ("seats_plus_10pct", 1.0, 1.0, 1.0 + PERTURBATION, 1.0),
        ("benchmark_minus_10pct", 1.0, 1.0, 1.0, 1.0 - PERTURBATION),
        ("benchmark_plus_10pct", 1.0, 1.0, 1.0, 1.0 + PERTURBATION),
        (
            "all_favorable_10pct",
            1.0 - PERTURBATION,
            1.0 + PERTURBATION,
            1.0 + PERTURBATION,
            1.0 + PERTURBATION,
        ),
        (
            "all_adverse_10pct",
            1.0 + PERTURBATION,
            1.0 - PERTURBATION,
            1.0 - PERTURBATION,
            1.0 - PERTURBATION,
        ),
    )


def proxy_ratio(values, load_factor, fuel_multiplier, speed_multiplier, seats_multiplier, benchmark_multiplier):
    fuel_l_per_hour = values["concorde_fuel_l_per_hour"] * fuel_multiplier
    speed_kmh = values["concorde_speed_kmh"] * speed_multiplier
    seats = values["concorde_seat_capacity"] * seats_multiplier
    benchmark = values["long_haul_co2_kg_per_passenger_mile"] * benchmark_multiplier
    # Shared fuel conversion factors cancel in the ratio, but the expression
    # retains the published speed, seat, and passenger-distance units.
    historical_co2 = (
        fuel_l_per_hour
        * values["km_per_mile"]
        / speed_kmh
        / (seats * load_factor)
        * values["jet_co2_kg_per_us_gallon"]
        / values["liters_per_us_gallon"]
    )
    return historical_co2 / benchmark


def calculate(values=None):
    values = load_inputs() if values is None else values
    rows = []
    for scenario, fuel_m, speed_m, seats_m, benchmark_m in scenario_definitions():
        for load_factor in LOAD_FACTORS:
            ratio = proxy_ratio(values, load_factor, fuel_m, speed_m, seats_m, benchmark_m)
            rows.append(
                {
                    "scenario": scenario,
                    "load_factor": load_factor,
                    "fuel_multiplier": fuel_m,
                    "speed_multiplier": speed_m,
                    "seat_capacity_multiplier": seats_m,
                    "modern_benchmark_multiplier": benchmark_m,
                    "historical_proxy_co2_ratio_vs_modern": ratio,
                    "required_reduction_percent_to_match": (1.0 - 1.0 / ratio) * 100.0,
                }
            )
    return rows


def run():
    rows = calculate()
    for row in rows:
        print(
            f"{row['scenario']} load_factor={row['load_factor']:.0%} "
            f"ratio={row['historical_proxy_co2_ratio_vs_modern']:.3f}x "
            f"required_reduction={row['required_reduction_percent_to_match']:.1f}%"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

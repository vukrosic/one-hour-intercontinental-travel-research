#!/usr/bin/env python3
"""Independent algebraic cross-check of the historical energy proxy.

This intentionally does not import energy_intensity.py. It re-reads the pinned
CSV inputs, recomputes the proxy with an alternate grouping of unit
conversions, and compares the result with the published output table.
"""
import csv

INPUT = "energy_inputs.csv"
REFERENCE_OUTPUT = "energy_intensity_results.csv"
OUTPUT = "energy_independent_check.csv"
TOLERANCE = 1e-9


def read_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return {row["key"]: float(row["value"]) for row in rows}


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(values, load_factor):
    gallons_per_hour = values["concorde_fuel_l_per_hour"] / values["liters_per_us_gallon"]
    miles_per_hour = values["concorde_speed_kmh"] / values["km_per_mile"]
    occupied_seats = values["concorde_seat_capacity"] * load_factor
    passenger_miles_per_hour = occupied_seats * miles_per_hour
    fuel_gallons_per_passenger_mile = gallons_per_hour / passenger_miles_per_hour
    energy = fuel_gallons_per_passenger_mile * values["jet_heat_btu_per_us_gallon"]
    co2 = fuel_gallons_per_passenger_mile * values["jet_co2_kg_per_us_gallon"]
    modern_energy = (
        values["long_haul_co2_kg_per_passenger_mile"]
        / values["jet_co2_kg_per_us_gallon"]
        * values["jet_heat_btu_per_us_gallon"]
    )
    return {
        "load_factor": load_factor,
        "independent_energy_btu_per_passenger_mile": energy,
        "independent_co2_kg_per_passenger_mile": co2,
        "independent_modern_energy_btu_per_passenger_mile": modern_energy,
    }


def compare():
    values = read_inputs()
    reference = read_reference()
    rows = []
    for reference_row in reference:
        load_factor = float(reference_row["load_factor"])
        independent = recompute(values, load_factor)
        energy_delta = independent["independent_energy_btu_per_passenger_mile"] - float(
            reference_row["concorde_proxy_btu_per_passenger_mile"]
        )
        co2_delta = independent["independent_co2_kg_per_passenger_mile"] - float(
            reference_row["concorde_proxy_kg_co2_per_passenger_mile"]
        )
        modern_delta = independent["independent_modern_energy_btu_per_passenger_mile"] - float(
            reference_row["derived_modern_long_haul_btu_per_passenger_mile"]
        )
        passed = max(abs(energy_delta), abs(co2_delta), abs(modern_delta)) <= TOLERANCE
        rows.append(
            {
                "load_factor": load_factor,
                **independent,
                "reference_energy_btu_per_passenger_mile": reference_row[
                    "concorde_proxy_btu_per_passenger_mile"
                ],
                "reference_co2_kg_per_passenger_mile": reference_row[
                    "concorde_proxy_kg_co2_per_passenger_mile"
                ],
                "reference_modern_energy_btu_per_passenger_mile": reference_row[
                    "derived_modern_long_haul_btu_per_passenger_mile"
                ],
                "max_absolute_delta": max(abs(energy_delta), abs(co2_delta), abs(modern_delta)),
                "pass": passed,
            }
        )
    return rows


def run():
    rows = compare()
    for row in rows:
        print(
            f"load_factor={row['load_factor']:.0%} "
            f"max_absolute_delta={row['max_absolute_delta']:.3e} "
            f"pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

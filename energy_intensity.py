#!/usr/bin/env python3
"""Historical passenger energy-intensity proxy with load-factor sensitivity.

This is an aggregate comparison, not an aircraft design, mission model, fuel
system model, route analysis, or operating recommendation.
"""
import csv

INPUT = "energy_inputs.csv"
OUTPUT = "energy_intensity_results.csv"
LOAD_FACTORS = (1.0, 0.8, 0.6)


def load_inputs(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required_fields = {"key", "value", "unit", "source_id", "role", "limitation"}
    if not rows:
        raise ValueError("energy input table is empty")
    if required_fields - set(rows[0]):
        raise ValueError("energy input table is missing required fields")
    values = {}
    for row in rows:
        if not all(row[field].strip() for field in required_fields):
            raise ValueError(f"blank evidence field for {row.get('key', '<unknown>')}")
        if row["key"] in values:
            raise ValueError(f"duplicate key: {row['key']}")
        values[row["key"]] = float(row["value"])
    return values


def calculate(values, load_factors=LOAD_FACTORS):
    fuel_us_gal_h = values["concorde_fuel_l_per_hour"] / values["liters_per_us_gallon"]
    speed_mph = values["concorde_speed_kmh"] / values["km_per_mile"]
    modern_co2 = values["long_haul_co2_kg_per_passenger_mile"]
    modern_energy = modern_co2 / values["jet_co2_kg_per_us_gallon"] * values["jet_heat_btu_per_us_gallon"]
    rows = []
    for load_factor in load_factors:
        passengers = values["concorde_seat_capacity"] * load_factor
        passenger_miles_h = passengers * speed_mph
        fuel_gal_per_passenger_mile = fuel_us_gal_h / passenger_miles_h
        energy_btu_per_passenger_mile = fuel_gal_per_passenger_mile * values["jet_heat_btu_per_us_gallon"]
        co2_kg_per_passenger_mile = fuel_gal_per_passenger_mile * values["jet_co2_kg_per_us_gallon"]
        rows.append(
            {
                "load_factor": load_factor,
                "occupied_passengers": passengers,
                "concorde_proxy_btu_per_passenger_mile": energy_btu_per_passenger_mile,
                "concorde_proxy_kg_co2_per_passenger_mile": co2_kg_per_passenger_mile,
                "concorde_proxy_kg_co2_per_passenger_km": co2_kg_per_passenger_mile / values["km_per_mile"],
                "derived_modern_long_haul_btu_per_passenger_mile": modern_energy,
                "modern_long_haul_kg_co2_per_passenger_mile": modern_co2,
                "energy_ratio_vs_modern_long_haul": energy_btu_per_passenger_mile / modern_energy,
                "co2_ratio_vs_modern_long_haul": co2_kg_per_passenger_mile / modern_co2,
            }
        )
    return rows


def run():
    rows = calculate(load_inputs())
    for row in rows:
        print(
            f"load_factor={row['load_factor']:.0%} "
            f"energy={row['concorde_proxy_btu_per_passenger_mile']:.0f} Btu/pmi "
            f"CO2={row['concorde_proxy_kg_co2_per_passenger_mile']:.3f} kg/pmi "
            f"ratio={row['energy_ratio_vs_modern_long_haul']:.2f}x"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

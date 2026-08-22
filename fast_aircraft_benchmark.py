#!/usr/bin/env python3
"""Abstract speed-bin comparison for civilian travel research.

This is a public-data research aid, not an aircraft design or operations tool.
"""
import csv

DISTANCE_KM = 9492.6  # SFO-PEK lower-bound distance from phase 1 model

# Reference bins intentionally avoid naming a proposed aircraft or configuration.
SPEED_BINS = [
    ("subsonic_reference", 900.0, "commercial-jet-like"),
    ("Concorde_historical", 2160.0, "historical public benchmark"),
    ("Mach_3_conceptual_bin", 3240.0, "abstract comparison bin"),
    ("Mach_5_conceptual_bin", 5400.0, "abstract comparison bin"),
]
OVERHEAD_CONTEXT_MINUTES = [15.0, 20.0, 30.0]  # secondary context only; not a target

def run():
    rows = []
    for label, speed_kmh, basis in SPEED_BINS:
        airborne_min = DISTANCE_KM / speed_kmh * 60.0
        for overhead in OVERHEAD_CONTEXT_MINUTES:
            rows.append((label, basis, speed_kmh, airborne_min, overhead, airborne_min + overhead))
    print(f"distance_km={DISTANCE_KM:.1f}")
    for label, basis, speed, airborne, overhead, total in rows:
        print(f"{label:24s} airborne={airborne:6.1f} min | optional_overhead={overhead:4.0f} min | contextual_sum={total:6.1f} min")
    with open("fast_aircraft_benchmark.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["speed_bin", "basis", "reference_speed_kmh", "airborne_minutes", "abstract_overhead_context_minutes", "contextual_sum_minutes"])
        w.writerows(rows)

if __name__ == "__main__":
    run()

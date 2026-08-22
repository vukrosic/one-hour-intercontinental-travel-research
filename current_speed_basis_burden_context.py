#!/usr/bin/env python3
"""Apply the repository's dimensionless speed-burden proxies by evidence basis.

The kinetic-energy proxy scales as M^2 and the ideal total/static-temperature
proxy uses gamma=1.4. They are trend indicators, not fuel burn, heat flux,
materials, propulsion, or aircraft-performance predictions.
"""
import csv

INPUT = "current_speed_basis_time_context.csv"
OUTPUT = "current_speed_basis_burden_context.csv"
SUMMARY_OUTPUT = "current_speed_basis_burden_context_summary.csv"
REFERENCE_MACH = 0.85
GAMMA = 1.4


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"entry_id", "aircraft_class", "speed_basis", "basis_interpretation", "mach"}
    if not rows or required - set(rows[0]):
        raise ValueError("invalid speed-basis time context")
    return rows


def calculate(rows=None):
    rows = load_rows() if rows is None else rows
    result = []
    for row in rows:
        mach = float(row["mach"])
        result.append(
            {
                **row,
                "airborne_time_saved_fraction_vs_mach_0_85": 1.0 - REFERENCE_MACH / mach,
                "kinetic_energy_per_mass_proxy_vs_mach_0_85": (mach / REFERENCE_MACH) ** 2,
                "ideal_total_to_static_temperature_ratio": 1.0 + 0.5 * (GAMMA - 1.0) * mach**2,
            }
        )
    return result


def summarize(rows):
    top = [row for row in rows if row["speed_basis"] == "top_or_max"]
    cruise = [row for row in rows if row["speed_basis"] != "top_or_max"]
    g700_top = next(row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "top_or_max")
    g700_high = next(
        row for row in rows if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "explicit_high_speed_cruise"
    )
    return {
        "current_speed_basis_burden_context_rows": len(rows),
        "top_or_max_rows": len(top),
        "explicit_cruise_rows": len(cruise),
        "highest_top_or_max_ke_proxy": max(float(row["kinetic_energy_per_mass_proxy_vs_mach_0_85"]) for row in top),
        "highest_explicit_cruise_ke_proxy": max(
            float(row["kinetic_energy_per_mass_proxy_vs_mach_0_85"]) for row in cruise
        ),
        "highest_top_or_max_temperature_ratio": max(
            float(row["ideal_total_to_static_temperature_ratio"]) for row in top
        ),
        "highest_explicit_cruise_temperature_ratio": max(
            float(row["ideal_total_to_static_temperature_ratio"]) for row in cruise
        ),
        "g700_top_ke_proxy": float(g700_top["kinetic_energy_per_mass_proxy_vs_mach_0_85"]),
        "g700_high_cruise_ke_proxy": float(g700_high["kinetic_energy_per_mass_proxy_vs_mach_0_85"]),
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

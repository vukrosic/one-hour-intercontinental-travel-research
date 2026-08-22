#!/usr/bin/env python3
"""Dimensionless airborne-time benefit versus physics-burden comparison.

The outputs are trend indicators, not aircraft performance predictions. The
model contains no geometry, propulsion, material, route, or operating inputs.
"""
import csv

from physics_envelope import MACH_BINS, REFERENCE_MACH, normalized_kinetic_energy, total_temperature_ratio


def tradeoff_rows():
    result = []
    previous = None
    for mach in MACH_BINS:
        time_ratio = REFERENCE_MACH / mach
        saved_fraction = 1.0 - time_ratio
        ke_ratio = normalized_kinetic_energy(mach)
        temperature_ratio = total_temperature_ratio(mach)
        if previous is None:
            marginal_ke_efficiency = None
            marginal_thermal_efficiency = None
        else:
            delta_saved = saved_fraction - previous[2]
            marginal_ke_efficiency = delta_saved / (ke_ratio - previous[3])
            marginal_thermal_efficiency = delta_saved / (temperature_ratio - previous[4])
        row = (
            mach,
            time_ratio,
            saved_fraction,
            ke_ratio,
            temperature_ratio,
            marginal_ke_efficiency,
            marginal_thermal_efficiency,
        )
        result.append(row)
        previous = row
    return result


def run():
    data = tradeoff_rows()
    print("Dimensionless speed benefit versus burden")
    for row in data:
        mach, time_ratio, saved, ke_ratio, temp_ratio, ke_eff, thermal_eff = row
        ke_text = "n/a" if ke_eff is None else f"{ke_eff:.4f}"
        thermal_text = "n/a" if thermal_eff is None else f"{thermal_eff:.4f}"
        print(
            f"Mach {mach:>4.2f}: time={time_ratio:>5.3f}x, saved={saved:>5.1%}, "
            f"KE={ke_ratio:>6.2f}x, T0/T={temp_ratio:>5.3f}, "
            f"marginal_saved/KE={ke_text}, marginal_saved/dT={thermal_text}"
        )
    with open("speed_tradeoff.csv", "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(
            [
                "mach_bin",
                "airborne_time_vs_mach_0_85",
                "airborne_time_saved_fraction",
                "kinetic_energy_per_mass_vs_mach_0_85",
                "ideal_total_to_static_temperature_ratio",
                "marginal_time_saved_per_incremental_ke_proxy",
                "marginal_time_saved_per_incremental_temperature_ratio",
            ]
        )
        writer.writerows(data)


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Dimensionless speed-class physics envelope.

This model compares trends only. It does not represent an aircraft, material,
propulsion system, trajectory, or operating procedure.
"""
import csv

GAMMA = 1.4
REFERENCE_MACH = 0.85
MACH_BINS = [0.85, 1.0, 1.5, 2.0, 3.0, 5.0]

def total_temperature_ratio(mach, gamma=GAMMA):
    """Ideal-gas isentropic T_total/T_static relation."""
    return 1.0 + 0.5 * (gamma - 1.0) * mach * mach

def normalized_kinetic_energy(mach):
    """Kinetic-energy-per-mass ratio relative to the Mach 0.85 bin."""
    return (mach / REFERENCE_MACH) ** 2

def rows():
    return [
        (mach, total_temperature_ratio(mach), normalized_kinetic_energy(mach))
        for mach in MACH_BINS
    ]

def run():
    data = rows()
    print("Ideal-gas, dimensionless screening envelope (gamma=1.4)")
    for mach, t_ratio, ke_ratio in data:
        print(f"Mach {mach:>4.2f}: T_total/T_static={t_ratio:>5.3f}, KE_per_mass_vs_M0.85={ke_ratio:>6.2f}x")
    with open("physics_envelope.csv", "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["mach_bin", "ideal_total_to_static_temperature_ratio", "kinetic_energy_per_mass_vs_mach_0_85"])
        writer.writerows(data)

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Independent reproduction of the fixed-distance speed-tradeoff table."""
import csv

REFERENCE_OUTPUT = "speed_tradeoff.csv"
OUTPUT = "speed_tradeoff_independent_check.csv"
TOLERANCE = 1e-12


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def recompute(reference_rows):
    reference_mach = float(reference_rows[0]["mach_bin"])
    rows = []
    previous = None
    for reference_row in reference_rows:
        mach = float(reference_row["mach_bin"])
        time_ratio = reference_mach / mach
        saved_fraction = 1.0 - time_ratio
        ke_ratio = (mach / reference_mach) ** 2
        temperature_ratio = 1.0 + 0.2 * mach**2
        if previous is None:
            marginal_ke = None
            marginal_temperature = None
        else:
            delta_saved = saved_fraction - previous["saved_fraction"]
            marginal_ke = delta_saved / (ke_ratio - previous["ke_ratio"])
            marginal_temperature = delta_saved / (
                temperature_ratio - previous["temperature_ratio"]
            )
        rows.append(
            {
                "mach_bin": mach,
                "independent_time_ratio": time_ratio,
                "independent_saved_fraction": saved_fraction,
                "independent_ke_ratio": ke_ratio,
                "independent_temperature_ratio": temperature_ratio,
                "independent_marginal_ke": marginal_ke,
                "independent_marginal_temperature": marginal_temperature,
            }
        )
        previous = {
            "saved_fraction": saved_fraction,
            "ke_ratio": ke_ratio,
            "temperature_ratio": temperature_ratio,
        }
    return rows


def compare():
    reference = read_reference()
    independent = recompute(reference)
    rows = []
    for ref, calc in zip(reference, independent):
        fields = (
            ("time_ratio", calc["independent_time_ratio"], ref["airborne_time_vs_mach_0_85"]),
            ("saved_fraction", calc["independent_saved_fraction"], ref["airborne_time_saved_fraction"]),
            ("ke_ratio", calc["independent_ke_ratio"], ref["kinetic_energy_per_mass_vs_mach_0_85"]),
            (
                "temperature_ratio",
                calc["independent_temperature_ratio"],
                ref["ideal_total_to_static_temperature_ratio"],
            ),
        )
        deltas = [abs(value - float(reference_value)) for _, value, reference_value in fields]
        for field, value, reference_value in (
            ("marginal_ke", calc["independent_marginal_ke"], ref["marginal_time_saved_per_incremental_ke_proxy"]),
            (
                "marginal_temperature",
                calc["independent_marginal_temperature"],
                ref["marginal_time_saved_per_incremental_temperature_ratio"],
            ),
        ):
            if value is None and reference_value == "":
                continue
            deltas.append(abs(value - float(reference_value)))
        max_delta = max(deltas)
        rows.append(
            {
                "mach_bin": calc["mach_bin"],
                "max_absolute_delta": max_delta,
                "pass": max_delta <= TOLERANCE,
            }
        )
    return rows


def run():
    rows = compare()
    for row in rows:
        print(
            f"Mach {row['mach_bin']:.2f} "
            f"max_absolute_delta={row['max_absolute_delta']:.3e} "
            f"pass={row['pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

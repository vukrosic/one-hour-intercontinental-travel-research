#!/usr/bin/env python3
"""Independent arithmetic check for speed-basis burden context."""
import csv

INPUT = "current_speed_basis_time_context.csv"
REFERENCE_OUTPUT = "current_speed_basis_burden_context_summary.csv"
OUTPUT = "current_speed_basis_burden_context_independent_check.csv"
REFERENCE_MACH = 0.85
GAMMA = 1.4
TOLERANCE = 1e-12


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def ke_proxy(mach):
    return (mach / REFERENCE_MACH) ** 2


def temp_ratio(mach):
    return 1.0 + 0.5 * (GAMMA - 1.0) * mach**2


def independently_summarize(rows):
    enriched = [
        {"entry_id": row["entry_id"], "speed_basis": row["speed_basis"], "mach": float(row["mach"])}
        for row in rows
    ]
    top = [row for row in enriched if row["speed_basis"] == "top_or_max"]
    cruise = [row for row in enriched if row["speed_basis"] != "top_or_max"]
    g700_top = next(row for row in enriched if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "top_or_max")
    g700_high = next(
        row for row in enriched if row["entry_id"] == "SPEED-003" and row["speed_basis"] == "explicit_high_speed_cruise"
    )
    return {
        "current_speed_basis_burden_context_rows": len(enriched),
        "top_or_max_rows": len(top),
        "explicit_cruise_rows": len(cruise),
        "highest_top_or_max_ke_proxy": max(ke_proxy(row["mach"]) for row in top),
        "highest_explicit_cruise_ke_proxy": max(ke_proxy(row["mach"]) for row in cruise),
        "highest_top_or_max_temperature_ratio": max(temp_ratio(row["mach"]) for row in top),
        "highest_explicit_cruise_temperature_ratio": max(temp_ratio(row["mach"]) for row in cruise),
        "g700_top_ke_proxy": ke_proxy(g700_top["mach"]),
        "g700_high_cruise_ke_proxy": ke_proxy(g700_high["mach"]),
    }


def read_reference(path=REFERENCE_OUTPUT):
    values = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            value = row["value"]
            values[row["metric"]] = float(value) if "." in value else int(value)
    return values


def compare():
    independent = independently_summarize(read_rows())
    reference = read_reference()
    return [
        {
            "metric": metric,
            "independent_value": value,
            "reference_value": reference.get(metric),
            "absolute_delta": abs(value - reference.get(metric)),
            "pass": abs(value - reference.get(metric)) <= TOLERANCE,
        }
        for metric, value in independent.items()
    ]


def run():
    rows = compare()
    for row in rows:
        print(f"{row['metric']} delta={row['absolute_delta']:.3e} pass={row['pass']}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

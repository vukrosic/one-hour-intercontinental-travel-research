#!/usr/bin/env python3
"""Apply the existing ideal thermal screen to current civilian Mach references.

This is a bounded comparison only. It is not a heat-flux, materials, cabin,
trajectory, or serviceability model.
"""
import csv

from thermal_sensitivity import load_inputs

SPEED_INPUT = "current_civilian_speed_close_read.csv"
THERMAL_OUTPUT = "thermal_current_service_context.csv"
SUMMARY_OUTPUT = "thermal_current_service_context_summary.csv"
MACH2_REFERENCE = 2.0


def load_current_speeds(path=SPEED_INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"entry_id", "aircraft_class", "reference_speed_mach"}
    if not rows or required - set(rows[0]):
        raise ValueError("invalid current speed reference table")
    result = []
    for row in rows:
        speed = float(row["reference_speed_mach"])
        if not 0 < speed < 1:
            raise ValueError(f"current reference is not subsonic: {row['entry_id']}")
        result.append(
            {
                "reference_id": row["entry_id"],
                "reference_label": row["aircraft_class"],
                "mach": speed,
                "reference_scope": "current civilian reference",
            }
        )
    return result


def calculate_rows(thermal_values, current_speeds=None):
    gamma = thermal_values["gamma"]
    low = thermal_values["static_temperature_low"]
    high = thermal_values["static_temperature_high"]
    rows = list(current_speeds if current_speeds is not None else load_current_speeds())
    rows.append(
        {
            "reference_id": "MACH2_HISTORICAL",
            "reference_label": "Mach 2 historical service class",
            "mach": MACH2_REFERENCE,
            "reference_scope": "historical comparison",
        }
    )
    output = []
    for row in rows:
        ratio = 1.0 + 0.5 * (gamma - 1.0) * row["mach"] ** 2
        output.append(
            {
                **row,
                "ideal_total_to_static_temperature_ratio": ratio,
                "ideal_total_temperature_low_K": ratio * low,
                "ideal_total_temperature_high_K": ratio * high,
            }
        )
    return output


def summarize(rows):
    current = [row for row in rows if row["reference_scope"] == "current civilian reference"]
    historical = [row for row in rows if row["reference_id"] == "MACH2_HISTORICAL"]
    if len(historical) != 1 or not current:
        raise ValueError("expected current rows plus exactly one Mach 2 comparison")
    historical_low = historical[0]["ideal_total_temperature_low_K"]
    highest_current_high = max(row["ideal_total_temperature_high_K"] for row in current)
    return {
        "thermal_current_service_context_rows": len(rows),
        "current_reference_rows": len(current),
        "mach2_comparison_rows": len(historical),
        "mach2_lower_bound_K": historical_low,
        "highest_current_reference_upper_bound_K": highest_current_high,
        "mach2_lower_to_highest_current_upper_ratio": historical_low / highest_current_high,
        "mach2_lower_exceeds_highest_current_upper": int(historical_low > highest_current_high),
    }


def run():
    rows = calculate_rows(load_inputs())
    with open(THERMAL_OUTPUT, "w", newline="") as f:
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

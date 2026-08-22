#!/usr/bin/env python3
"""Summarize the non-scalar practicality matrix.

The matrix is a transparent evidence screen, not a weighted ranking model.
Each speed class is evaluated conjunctively across named gates.
"""
import csv
from collections import Counter

INPUT = "practicality_matrix.csv"
OUTPUT = "practicality_summary.csv"
REQUIRED_COLUMNS = {
    "speed_bin",
    "reference_mach",
    "basis",
    "historical_service",
    "time_benefit",
    "passenger_environment",
    "cabin_environment",
    "thermal_environment",
    "noise",
    "energy_climate",
    "economics",
    "airport_compatibility",
    "practical_status",
    "blocking_gates",
    "caveat",
}
GATE_COLUMNS = (
    "historical_service",
    "time_benefit",
    "passenger_environment",
    "cabin_environment",
    "thermal_environment",
    "noise",
    "energy_climate",
    "economics",
    "airport_compatibility",
)
ALLOWED_STATUSES = {
    "supported_reference",
    "benchmark_reference",
    "supported_historical",
    "arithmetic_reference",
    "arithmetic_supported",
    "supported_general",
    "bounded_proxy_only",
    "baseline_only",
    "unresolved",
    "unresolved_binding",
    "unresolved_no_service_anchor",
    "unresolved_high_proxy",
    "unresolved_no_empirical_anchor",
    "contradicted_vs_modern_benchmark",
    "adverse_historical",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid practicality matrix")
    for row in rows:
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{row.get('speed_bin', '<unknown>')} has blank {field}")
        for field in GATE_COLUMNS:
            if row[field] not in ALLOWED_STATUSES:
                raise ValueError(f"{row['speed_bin']} has unknown status {row[field]}")
    return rows


def summarize(rows):
    statuses = Counter(row["practical_status"] for row in rows)
    contradicted_cells = sum(
        row[field] == "contradicted_vs_modern_benchmark"
        for row in rows
        for field in GATE_COLUMNS
    )
    adverse_cells = sum(
        row[field] == "adverse_historical" for row in rows for field in GATE_COLUMNS
    )
    return {
        "speed_class_rows": len(rows),
        "current_practical_pass_rows": statuses["practical_pass"],
        "current_baseline_not_ranked_rows": statuses["current_baseline_not_ranked"],
        "historical_anchor_not_current_practical_pass_rows": statuses[
            "historical_anchor_not_current_practical_pass"
        ],
        "conceptual_unresolved_rows": statuses["conceptual_unresolved"],
        "contradicted_gate_cells": contradicted_cells,
        "adverse_historical_gate_cells": adverse_cells,
        "classes_with_no_service_anchor": sum(
            row["historical_service"] == "unresolved_no_service_anchor" for row in rows
        ),
    }


def run():
    summary = summarize(load_rows())
    for key, value in summary.items():
        print(f"{key}={value}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerows(summary.items())


if __name__ == "__main__":
    run()

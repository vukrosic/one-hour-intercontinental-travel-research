#!/usr/bin/env python3
"""Validate semantic consistency of the non-scalar practicality matrix."""
import csv

INPUT = "practicality_matrix.csv"
OUTPUT = "practicality_gate_check.csv"
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
BLOCKING_MARKERS = ("unresolved", "contradicted", "adverse")
CURRENT_REFERENCE_STATUSES = {"current_baseline_not_ranked", "current_business_reference_not_ranked"}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("practicality matrix is empty")
    return rows


def check_row(row):
    blocking = [
        field
        for field in GATE_COLUMNS
        if any(marker in row[field] for marker in BLOCKING_MARKERS)
    ]
    checks = {
        "practical_pass_has_no_blocking_gates": row["practical_status"] != "practical_pass"
        or not blocking,
        "non_pass_has_no_false_pass_label": row["practical_status"] != "practical_pass",
        "conceptual_bin_lacks_service_anchor": row["practical_status"] != "conceptual_unresolved"
        or row["historical_service"] == "unresolved_no_service_anchor",
        "nonbaseline_status_lists_blocking_gates": row["practical_status"]
        in CURRENT_REFERENCE_STATUSES
        or bool(row["blocking_gates"] and row["blocking_gates"] != "none"),
    }
    return {
        "speed_bin": row["speed_bin"],
        "practical_status": row["practical_status"],
        "blocking_gate_count": len(blocking),
        "blocking_gates_detected": ";".join(blocking) or "none",
        "semantic_checks_pass": all(checks.values()),
    }


def check(rows=None):
    source_rows = load_rows() if rows is None else rows
    return [check_row(row) for row in source_rows]


def run():
    rows = check()
    for row in rows:
        print(
            f"{row['speed_bin']} blocking={row['blocking_gate_count']} "
            f"semantic_checks_pass={row['semantic_checks_pass']}"
        )
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

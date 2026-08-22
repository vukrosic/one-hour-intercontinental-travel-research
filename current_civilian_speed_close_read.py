#!/usr/bin/env python3
"""Validate and summarize current civilian speed-reference evidence.

The table separates airline service, certified business-aviation service, and
manufacturer-only performance claims. It is not a design or operations model.
"""
import csv

INPUT = "current_civilian_speed_close_read.csv"
OUTPUT = "current_civilian_speed_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "aircraft_class",
    "civilian_scope",
    "service_state",
    "evidence_state",
    "reference_speed_mach",
    "speed_basis",
    "extracted_claim",
    "service_or_certification_evidence",
    "speed_frontier_pass",
    "what_it_supports",
    "what_it_does_not_support",
}
ALLOWED_SERVICE_STATES = {
    "current_airline_service",
    "current_certified_in_service",
    "current_marketed_product",
}
ALLOWED_EVIDENCE_STATES = {
    "service_and_manufacturer_record",
    "certified_service_record",
    "manufacturer_performance_claim",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid current civilian speed close-read table")
    ids = set()
    for row in rows:
        entry_id = row["entry_id"]
        if entry_id in ids:
            raise ValueError(f"duplicate entry_id: {entry_id}")
        ids.add(entry_id)
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {entry_id}")
        if row["service_state"] not in ALLOWED_SERVICE_STATES:
            raise ValueError(f"unknown service state: {entry_id}")
        if row["evidence_state"] not in ALLOWED_EVIDENCE_STATES:
            raise ValueError(f"unknown evidence state: {entry_id}")
        try:
            speed = float(row["reference_speed_mach"])
        except ValueError as exc:
            raise ValueError(f"invalid Mach value: {entry_id}") from exc
        if not 0 < speed < 1:
            raise ValueError(f"current subsonic speed must be between 0 and 1: {entry_id}")
        if row["speed_frontier_pass"] != "no":
            raise ValueError("speed close read cannot assert a practical pass")
        if row["service_state"] == "current_marketed_product" and row["evidence_state"] != "manufacturer_performance_claim":
            raise ValueError("marketed product must retain manufacturer-claim status")
    return rows


def summarize(rows):
    service_rows = [
        row for row in rows if row["service_state"] in {"current_airline_service", "current_certified_in_service"}
    ]
    speeds = [float(row["reference_speed_mach"]) for row in rows]
    service_speeds = [float(row["reference_speed_mach"]) for row in service_rows]
    return {
        "current_civilian_speed_close_read_rows": len(rows),
        "current_airline_service_rows": sum(row["service_state"] == "current_airline_service" for row in rows),
        "current_certified_business_aviation_rows": sum(
            row["service_state"] == "current_certified_in_service" for row in rows
        ),
        "manufacturer_only_rows": sum(row["evidence_state"] == "manufacturer_performance_claim" for row in rows),
        "service_anchored_rows": len(service_rows),
        "highest_published_subsonic_mach": max(speeds),
        "highest_service_anchored_mach": max(service_speeds),
        "speed_frontier_pass_rows": sum(row["speed_frontier_pass"] == "yes" for row in rows),
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

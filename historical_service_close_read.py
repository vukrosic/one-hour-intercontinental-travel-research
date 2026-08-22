#!/usr/bin/env python3
"""Validate and summarize the public historical passenger-service close read.

This is a historical evidence ledger, not an aircraft or operations model.
"""
import csv

INPUT = "historical_service_close_read.csv"
OUTPUT = "historical_service_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "aircraft_or_record",
    "service_state",
    "evidence_scope",
    "extracted_claim",
    "speed_class",
    "time_scope",
    "transferability",
    "historical_service_anchor",
    "current_practical_pass",
    "what_it_supports",
    "what_it_does_not_support",
}
ALLOWED_SERVICE_STATES = {
    "scheduled_passenger_service",
    "limited_airline_passenger_service",
    "research_only_follow_on",
}
ALLOWED_TRANSFERABILITY = {
    "high_for_historical_service",
    "low_for_service_inference",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid historical-service close-read table")
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
        if row["transferability"] not in ALLOWED_TRANSFERABILITY:
            raise ValueError(f"unknown transferability: {entry_id}")
        if row["historical_service_anchor"] not in {"yes", "no"}:
            raise ValueError(f"invalid anchor flag: {entry_id}")
        if row["current_practical_pass"] != "no":
            raise ValueError("historical close read cannot assert a current practical pass")
        expected_anchor = row["service_state"] != "research_only_follow_on"
        if (row["historical_service_anchor"] == "yes") != expected_anchor:
            raise ValueError(f"service-anchor semantics mismatch: {entry_id}")
    return rows


def summarize(rows):
    anchored_classes = {
        row["speed_class"]
        for row in rows
        if row["historical_service_anchor"] == "yes"
    }
    return {
        "historical_service_close_read_rows": len(rows),
        "direct_scheduled_service_rows": sum(
            row["service_state"] == "scheduled_passenger_service" for row in rows
        ),
        "limited_airline_service_rows": sum(
            row["service_state"] == "limited_airline_passenger_service" for row in rows
        ),
        "research_only_follow_on_rows": sum(
            row["service_state"] == "research_only_follow_on" for row in rows
        ),
        "historical_service_anchor_rows": sum(
            row["historical_service_anchor"] == "yes" for row in rows
        ),
        "historical_service_anchor_speed_classes": len(anchored_classes),
        "current_service_rows": sum(row["time_scope"] == "2026-current" for row in rows),
        "current_practical_pass_rows": sum(
            row["current_practical_pass"] == "yes" for row in rows
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

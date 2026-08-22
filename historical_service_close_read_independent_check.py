#!/usr/bin/env python3
"""Independent bookkeeping check for the historical-service close read."""
import csv

INPUT = "historical_service_close_read.csv"
REFERENCE_OUTPUT = "historical_service_close_read_summary.csv"
OUTPUT = "historical_service_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    anchors = {row["speed_class"] for row in rows if row["historical_service_anchor"] == "yes"}
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
        "historical_service_anchor_speed_classes": len(anchors),
        "current_service_rows": sum(row["time_scope"] == "2026-current" for row in rows),
        "current_practical_pass_rows": sum(row["current_practical_pass"] == "yes" for row in rows),
    }


def compare():
    independent = independently_summarize(read_rows())
    reference = read_reference()
    return [
        {
            "metric": metric,
            "independent_value": value,
            "reference_value": reference.get(metric),
            "pass": value == reference.get(metric),
        }
        for metric, value in independent.items()
    ]


def run():
    rows = compare()
    for row in rows:
        print(f"{row['metric']} independent={row['independent_value']} pass={row['pass']}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run()

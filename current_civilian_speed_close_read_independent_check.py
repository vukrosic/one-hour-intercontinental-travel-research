#!/usr/bin/env python3
"""Independent bookkeeping check for current civilian speed references."""
import csv

INPUT = "current_civilian_speed_close_read.csv"
REFERENCE_OUTPUT = "current_civilian_speed_close_read_summary.csv"
OUTPUT = "current_civilian_speed_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    values = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            value = row["value"]
            values[row["metric"]] = float(value) if "." in value else int(value)
    return values


def independently_summarize(rows):
    service_rows = [
        row for row in rows if row["service_state"] == "current_airline_service"
        or row["service_state"] == "current_certified_in_service"
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

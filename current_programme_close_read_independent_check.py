#!/usr/bin/env python3
"""Independent bookkeeping check for current programme evidence."""
import csv

INPUT = "current_programme_close_read.csv"
REFERENCE_OUTPUT = "current_programme_close_read_summary.csv"
OUTPUT = "current_programme_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    return {
        "current_programme_close_read_rows": len(rows),
        "research_demonstrator_rows": sum(row["program_class"] == "research_demonstrator" for row in rows),
        "experimental_test_authorization_rows": sum(
            row["program_class"] == "experimental_test_authorization" for row in rows
        ),
        "company_reported_future_airliner_rows": sum(
            row["program_class"] == "company_reported_future_airliner" for row in rows
        ),
        "proposed_regulatory_path_rows": sum(
            row["program_class"] == "proposed_regulatory_path" for row in rows
        ),
        "current_passenger_service_rows": sum(
            row["independent_service_evidence"] == "current_passenger_service" for row in rows
        ),
        "passenger_certification_evidence_rows": sum(
            "passenger certification" in row["certification_state"].lower()
            and "no passenger certification" not in row["certification_state"].lower()
            for row in rows
        ),
        "high_speed_practical_pass_rows": sum(row["high_speed_practical_pass"] == "yes" for row in rows),
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

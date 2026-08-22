#!/usr/bin/env python3
"""Validate and summarize current civilian high-speed programme evidence.

This ledger records programme maturity only; it is not a design or operations
model and it cannot award a practical-airliner pass.
"""
import csv

INPUT = "current_programme_close_read.csv"
OUTPUT = "current_programme_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "program",
    "program_class",
    "evidence_state",
    "public_claim",
    "independent_service_evidence",
    "certification_state",
    "high_speed_practical_pass",
    "what_it_supports",
    "what_it_does_not_support",
}
ALLOWED_PROGRAM_CLASSES = {
    "research_demonstrator",
    "experimental_test_authorization",
    "company_reported_future_airliner",
    "proposed_regulatory_path",
}
ALLOWED_EVIDENCE_STATES = {
    "active_research_evidence",
    "limited_experimental_authorization",
    "self_reported_programme",
    "proposed_rulemaking",
}
ALLOWED_SERVICE_EVIDENCE = {
    "none_research_aircraft",
    "none_experimental_test",
    "none_public_service_evidence",
    "none_rule_proposal",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid current-programme close-read table")
    ids = set()
    for row in rows:
        entry_id = row["entry_id"]
        if entry_id in ids:
            raise ValueError(f"duplicate entry_id: {entry_id}")
        ids.add(entry_id)
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {entry_id}")
        if row["program_class"] not in ALLOWED_PROGRAM_CLASSES:
            raise ValueError(f"unknown programme class: {entry_id}")
        if row["evidence_state"] not in ALLOWED_EVIDENCE_STATES:
            raise ValueError(f"unknown evidence state: {entry_id}")
        if row["independent_service_evidence"] not in ALLOWED_SERVICE_EVIDENCE:
            raise ValueError(f"unknown service-evidence state: {entry_id}")
        if row["high_speed_practical_pass"] != "no":
            raise ValueError("programme close read cannot assert a practical pass")
        if row["independent_service_evidence"].startswith("none_") is False:
            raise ValueError(f"service evidence must remain explicitly absent: {entry_id}")
    return rows


def summarize(rows):
    return {
        "current_programme_close_read_rows": len(rows),
        "research_demonstrator_rows": sum(
            row["program_class"] == "research_demonstrator" for row in rows
        ),
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
        "high_speed_practical_pass_rows": sum(
            row["high_speed_practical_pass"] == "yes" for row in rows
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

#!/usr/bin/env python3
"""Independent state-count check for the dated noise evidence table."""
import csv

INPUT = "noise_evidence.csv"
REFERENCE_OUTPUT = "noise_state_guard.csv"
OUTPUT = "noise_state_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    final_states = {"final_pass_threshold", "commercial_acceptance_demonstrated"}
    current_states = {"current_binding"}
    prospective_states = {
        "proposed_not_final",
        "adopted_future_applicability",
        "standards_in_development",
    }
    return {
        "noise_rows": len(rows),
        "current_binding_rows": sum(row["evidence_state"] in current_states for row in rows),
        "prospective_or_development_rows": sum(row["evidence_state"] in prospective_states for row in rows),
        "research_in_progress_rows": sum(
            row["evidence_state"] == "empirical_program_in_progress" for row in rows
        ),
        "unresolved_rows": sum(row["evidence_state"] == "unresolved" for row in rows),
        "certified_subsonic_aircraft_record_rows": sum(
            row["evidence_state"] == "certified_subsonic_aircraft_record" for row in rows
        ),
        "final_high_speed_pass_rows": sum(
            row["evidence_state"] in final_states and row["high_speed_practical_pass"] == "yes"
            for row in rows
        ),
        "semantic_error_count": sum(
            row["high_speed_practical_pass"] != "no"
            and row["evidence_state"] not in final_states
            for row in rows
        ),
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

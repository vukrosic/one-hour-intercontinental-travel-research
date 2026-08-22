#!/usr/bin/env python3
"""Enforce conservative semantics for dated noise evidence states."""
import csv

INPUT = "noise_evidence.csv"
OUTPUT = "noise_state_guard.csv"
REQUIRED_COLUMNS = {
    "gate_id",
    "domain",
    "jurisdiction",
    "evidence_state",
    "high_speed_specific",
    "threshold_value",
    "threshold_unit",
    "claim",
    "source_id",
    "accessed",
    "limitation",
    "high_speed_practical_pass",
}
NONBLANK_COLUMNS = REQUIRED_COLUMNS - {"threshold_value", "threshold_unit"}
ALLOWED_STATES = {
    "current_binding",
    "proposed_not_final",
    "adopted_future_applicability",
    "standards_in_development",
    "empirical_program_in_progress",
    "unresolved",
    "final_pass_threshold",
    "commercial_acceptance_demonstrated",
}
FINAL_PASS_STATES = {"final_pass_threshold", "commercial_acceptance_demonstrated"}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid noise evidence table")
    return rows


def semantic_errors(rows):
    errors = []
    ids = set()
    for row in rows:
        gate_id = row["gate_id"]
        if gate_id in ids:
            errors.append(f"duplicate gate_id: {gate_id}")
        ids.add(gate_id)
        for field in NONBLANK_COLUMNS:
            if not row[field].strip():
                errors.append(f"blank {field}: {gate_id}")
        state = row["evidence_state"]
        if state not in ALLOWED_STATES:
            errors.append(f"unknown evidence state: {gate_id}={state}")
        if row["high_speed_specific"] not in {"yes", "no"}:
            errors.append(f"invalid high_speed_specific: {gate_id}")
        if bool(row["threshold_value"].strip()) != bool(row["threshold_unit"].strip()):
            errors.append(f"threshold value/unit must be paired: {gate_id}")
        if state == "proposed_not_final" and not row["limitation"].lower().startswith("proposed rule"):
            errors.append(f"proposal limitation missing: {gate_id}")
        if state not in FINAL_PASS_STATES and row["high_speed_practical_pass"] == "yes":
            errors.append(f"non-final state marked pass: {gate_id}")
        if state in {"current_binding", "proposed_not_final", "adopted_future_applicability", "standards_in_development", "empirical_program_in_progress", "unresolved"} and row["high_speed_practical_pass"] != "no":
            errors.append(f"non-pass state must remain no: {gate_id}")
    return errors


def summarize(rows):
    errors = semantic_errors(rows)
    return {
        "noise_rows": len(rows),
        "current_binding_rows": sum(row["evidence_state"] == "current_binding" for row in rows),
        "prospective_or_development_rows": sum(
            row["evidence_state"] in {"proposed_not_final", "adopted_future_applicability", "standards_in_development"}
            for row in rows
        ),
        "research_in_progress_rows": sum(
            row["evidence_state"] == "empirical_program_in_progress" for row in rows
        ),
        "unresolved_rows": sum(row["evidence_state"] == "unresolved" for row in rows),
        "final_high_speed_pass_rows": sum(
            row["evidence_state"] in FINAL_PASS_STATES and row["high_speed_practical_pass"] == "yes"
            for row in rows
        ),
        "semantic_error_count": len(errors),
    }


def run():
    rows = load_rows()
    errors = semantic_errors(rows)
    for error in errors:
        print(f"ERROR {error}")
    summary = summarize(rows)
    for key, value in summary.items():
        print(f"{key}={value}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerows(summary.items())
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    run()

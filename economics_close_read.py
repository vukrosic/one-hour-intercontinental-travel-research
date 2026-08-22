#!/usr/bin/env python3
"""Validate and summarize the public historical economics close read."""
import csv

INPUT = "economics_close_read.csv"
OUTPUT = "economics_close_read_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "source_id",
    "evidence_context",
    "economic_measure",
    "time_scope",
    "direct_claim",
    "comparability",
    "economic_pass",
    "what_it_supports",
    "what_it_cannot_support",
}


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid economics close-read table")
    ids = set()
    for row in rows:
        if row["entry_id"] in ids:
            raise ValueError(f"duplicate entry_id: {row['entry_id']}")
        ids.add(row["entry_id"])
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {row['entry_id']}")
        if row["economic_pass"] != "no":
            raise ValueError("economics close read cannot assert a practical pass")
    return rows


def summarize(rows):
    return {
        "economics_close_read_rows": len(rows),
        "quantified_historical_rows": sum(
            "fuel per seat-mile" in row["economic_measure"] or "total operating cost" in row["economic_measure"]
            for row in rows
        ),
        "current_market_research_rows": sum("current research" in row["comparability"] for row in rows),
        "qualitative_synthesis_rows": sum("qualitative" in row["comparability"] for row in rows),
        "historical_adverse_rows": sum("adverse" in row["what_it_supports"] for row in rows),
        "current_empirical_business_case_rows": sum(
            row["economic_pass"] == "yes" for row in rows
        ),
        "economic_pass_rows": sum(row["economic_pass"] == "yes" for row in rows),
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

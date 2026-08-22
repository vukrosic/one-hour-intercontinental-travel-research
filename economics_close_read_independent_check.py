#!/usr/bin/env python3
"""Independent bookkeeping check for the economics close-read summary."""
import csv

INPUT = "economics_close_read.csv"
REFERENCE_OUTPUT = "economics_close_read_summary.csv"
OUTPUT = "economics_close_read_independent_check.csv"


def read_rows(path=INPUT):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def read_reference(path=REFERENCE_OUTPUT):
    with open(path, newline="") as f:
        return {row["metric"]: int(row["value"]) for row in csv.DictReader(f)}


def independently_summarize(rows):
    return {
        "economics_close_read_rows": len(rows),
        "quantified_historical_rows": sum(
            "fuel per seat-mile" in row["economic_measure"]
            or "total operating cost" in row["economic_measure"]
            for row in rows
        ),
        "current_market_research_rows": sum(
            row["time_scope"] == "current research programme page" for row in rows
        ),
        "qualitative_synthesis_rows": sum(
            row["comparability"].startswith("qualitative") for row in rows
        ),
        "historical_adverse_rows": sum(
            "adverse economics" in row["what_it_supports"] for row in rows
        ),
        "current_empirical_business_case_rows": sum(row["economic_pass"] == "yes" for row in rows),
        "economic_pass_rows": sum(row["economic_pass"] == "yes" for row in rows),
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

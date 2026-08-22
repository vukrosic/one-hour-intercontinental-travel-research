#!/usr/bin/env python3
"""Static integrity checks for the public source register.

These checks validate record hygiene, not the truth of external sources.
"""
import csv
from datetime import datetime

INPUT = "fast_aircraft_sources.csv"
OUTPUT = "source_integrity_summary.csv"
REQUIRED_COLUMNS = {"source_id", "source", "public_url", "claim_or_use", "accessed"}


def inspect(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid source register")
    ids = [row["source_id"] for row in rows]
    blank_fields = sum(
        not row[field].strip()
        for row in rows
        for field in REQUIRED_COLUMNS
    )
    invalid_urls = sum(
        not (row["public_url"].startswith("https://") or row["public_url"].startswith("http://"))
        for row in rows
    )
    invalid_dates = 0
    for row in rows:
        try:
            datetime.strptime(row["accessed"], "%Y-%m-%d")
        except ValueError:
            invalid_dates += 1
    return {
        "source_rows": len(rows),
        "unique_source_ids": len(set(ids)),
        "duplicate_source_ids": len(ids) - len(set(ids)),
        "blank_required_fields": blank_fields,
        "invalid_urls": invalid_urls,
        "invalid_access_dates": invalid_dates,
        "pass": int(
            len(ids) == len(set(ids))
            and blank_fields == 0
            and invalid_urls == 0
            and invalid_dates == 0
        ),
    }


def run():
    summary = inspect()
    for key, value in summary.items():
        print(f"{key}={value}")
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerows(summary.items())


if __name__ == "__main__":
    run()

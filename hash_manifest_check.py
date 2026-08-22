#!/usr/bin/env python3
"""Validate the metadata-only hash manifest for refreshed public pages."""
import csv
import re
from datetime import datetime

INPUT = "source_document_hashes.csv"
SOURCE_REGISTER = "fast_aircraft_sources.csv"
OUTPUT = "hash_manifest_summary.csv"
REQUIRED_COLUMNS = {
    "source_id",
    "public_url",
    "retrieved",
    "bytes",
    "sha256",
    "retrieval_mode",
    "scope_note",
}


def load_source_ids(path=SOURCE_REGISTER):
    with open(path, newline="") as f:
        return {row["source_id"] for row in csv.DictReader(f)}


def inspect(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid source hash manifest")
    source_ids = load_source_ids()
    missing_register_ids = sum(row["source_id"] not in source_ids for row in rows)
    duplicate_ids = len(rows) - len({row["source_id"] for row in rows})
    invalid_dates = 0
    invalid_hashes = 0
    invalid_bytes = 0
    invalid_urls = 0
    for row in rows:
        try:
            datetime.strptime(row["retrieved"], "%Y-%m-%d")
        except ValueError:
            invalid_dates += 1
        if not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            invalid_hashes += 1
        if int(row["bytes"]) <= 0:
            invalid_bytes += 1
        if not row["public_url"].startswith("https://"):
            invalid_urls += 1
    return {
        "hash_rows": len(rows),
        "missing_source_register_ids": missing_register_ids,
        "duplicate_source_ids": duplicate_ids,
        "invalid_dates": invalid_dates,
        "invalid_sha256_values": invalid_hashes,
        "nonpositive_byte_counts": invalid_bytes,
        "invalid_urls": invalid_urls,
        "pass": int(
            missing_register_ids == 0
            and duplicate_ids == 0
            and invalid_dates == 0
            and invalid_hashes == 0
            and invalid_bytes == 0
            and invalid_urls == 0
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

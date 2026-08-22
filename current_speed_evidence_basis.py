#!/usr/bin/env python3
"""Summarize top-speed versus explicit-cruise evidence for current references.

This is a source-role and wording guard. It does not infer a recommended speed,
route, trajectory, aircraft design, or operating procedure.
"""
import csv

INPUT = "current_speed_evidence_basis.csv"
OUTPUT = "current_speed_evidence_basis_summary.csv"
REQUIRED_COLUMNS = {
    "entry_id",
    "aircraft_class",
    "service_state",
    "top_or_max_mach",
    "explicit_high_speed_cruise_mach",
    "explicit_long_range_or_typical_cruise_mach",
    "speed_source_id",
    "interpretation",
}
MISSING = "not_reported"


def parse_optional(value, entry_id, field):
    if value == MISSING:
        return None
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field} for {entry_id}") from exc
    if not 0 < number < 1:
        raise ValueError(f"Mach value out of range for {entry_id}: {field}")
    return number


def load_rows(path=INPUT):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or REQUIRED_COLUMNS - set(rows[0]):
        raise ValueError("invalid current speed evidence basis table")
    ids = set()
    for row in rows:
        if row["entry_id"] in ids:
            raise ValueError(f"duplicate entry_id: {row['entry_id']}")
        ids.add(row["entry_id"])
        for field in REQUIRED_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"blank {field} for {row['entry_id']}")
        for field in (
            "top_or_max_mach",
            "explicit_high_speed_cruise_mach",
            "explicit_long_range_or_typical_cruise_mach",
        ):
            parse_optional(row[field], row["entry_id"], field)
    return rows


def summarize(rows):
    parsed = []
    for row in rows:
        top = parse_optional(row["top_or_max_mach"], row["entry_id"], "top_or_max_mach")
        high = parse_optional(
            row["explicit_high_speed_cruise_mach"], row["entry_id"], "explicit_high_speed_cruise_mach"
        )
        long_range = parse_optional(
            row["explicit_long_range_or_typical_cruise_mach"],
            row["entry_id"],
            "explicit_long_range_or_typical_cruise_mach",
        )
        parsed.append((top, high, long_range))
    gaps = [top - high for top, high, _ in parsed if top is not None and high is not None]
    top_values = [top for top, _, _ in parsed if top is not None]
    cruise_values = [value for _, high, long_range in parsed for value in (high, long_range) if value is not None]
    return {
        "current_speed_evidence_basis_rows": len(rows),
        "rows_with_top_or_max_speed": sum(top is not None for top, _, _ in parsed),
        "rows_with_explicit_high_speed_cruise": sum(high is not None for _, high, _ in parsed),
        "rows_with_explicit_long_range_or_typical_cruise": sum(long_range is not None for _, _, long_range in parsed),
        "rows_with_top_and_high_speed_cruise": len(gaps),
        "highest_top_or_max_mach": max(top_values),
        "highest_explicit_cruise_mach": max(cruise_values),
        "largest_top_minus_high_speed_cruise_gap": max(gaps),
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

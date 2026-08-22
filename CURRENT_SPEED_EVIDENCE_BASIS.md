# Current speed evidence basis

## Question

Which current civilian reference records provide a top or maximum speed, and
which provide an explicitly named cruise value?

This is a source-wording check. It prevents a top-speed or maximum-operating
number from being silently treated as a repeatable high-speed cruise value.
It does not recommend an operating speed and does not infer a design,
trajectory, route, or schedule.

## Result

| Reference | Top/max Mach in selected record | Explicit high-speed cruise | Explicit long-range/typical cruise | Conservative reading |
|---|---:|---:|---:|---|
| Boeing 787 | not reported | not reported | 0.850 | Airline record anchors an explicit cruise reference, not a top-speed claim. |
| Global 7500 | 0.925 | not reported | 0.850 | The selected EPD supplies a top-speed record and a cruise mission assumption; high-speed cruise is not promoted without a selected source. |
| Gulfstream G700 | 0.935 | 0.900 | 0.850 | One product record explicitly separates maximum operating Mach, high-speed cruise, and long-range cruise. |
| Global 8000 | 0.950 | not reported | not reported | The selected certification announcement supplies a top-speed record; a cruise value remains an evidence gap. |

The structured table is [`current_speed_evidence_basis.csv`](current_speed_evidence_basis.csv).
The summary reports three rows with top/max values, three with explicit cruise
values, one with both a top/max and explicit high-speed-cruise value, a highest
top/max value of Mach 0.95, and a highest explicit cruise value of Mach 0.90.
The only directly observed top-to-high-speed-cruise gap in this selected table
is 0.035 Mach for the G700; this is not a general aircraft rule.

## Reproducibility

```text
python3 current_speed_evidence_basis.py
python3 current_speed_evidence_basis_independent_check.py
```

The independent implementation reproduces all eight summary metrics within
`1e-12`.

## Limits and next use

- “Not reported” means not present in the selected public record, not that the
  aircraft has no such value.
- A top speed, maximum operating Mach, high-speed cruise, and long-range cruise
  are different evidence roles; they cannot be substituted without a source.
- The table does not model winds, climb/descent, acceleration, fuel burn,
  noise, passenger comfort, or airport constraints.
- Next use: time and energy comparisons should label whether they use a top/max
  value or an explicit cruise value, and should prefer the latter when the
  research question is repeatable passenger service.

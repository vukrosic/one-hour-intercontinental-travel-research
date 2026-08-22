# Speed-basis time context

## Question

How much does the fixed-distance time screen change when it uses an explicitly
named cruise value instead of a top or maximum-speed value?

The model reuses the repository's fixed 9,492.6 km mathematical yardstick and
ideal sound-speed bracket. It is a labeled arithmetic comparison, not a route,
trajectory, schedule, or operating recommendation.

## Result

| Basis group | Rows | Highest Mach in group | Highest speed-only saving vs Mach 0.85 |
|---|---:|---:|---:|
| Top/max arithmetic rows | 3 | 0.950 | 10.5% |
| Explicit cruise wording rows | 4 | 0.900 | 5.6% |

The G700 is the only selected current row with both a top/max and explicit
high-speed-cruise value: Mach 0.935 gives a 9.1% speed-only saving in this
screen, while Mach 0.90 gives 5.6%. The Global 8000's Mach 0.95 result is
therefore a top-speed arithmetic context only; its selected public record does
not supply a cruise value for this table.

## Reproducibility

```text
python3 current_speed_basis_time_context.py
python3 current_speed_basis_time_context_independent_check.py
```

The first command writes
[`current_speed_basis_time_context.csv`](current_speed_basis_time_context.csv)
and its summary. The independent implementation reproduces all eight summary
metrics within `1e-12`.

## Limits

- The speed intervals inherit the ideal sound-speed bracket and fixed
  mathematical distance from the existing context model.
- The comparison does not model wind, routing, acceleration, climb/descent,
  fuel burn, passenger load, noise, airport access, or dispatch reliability.
- Top/max values are not silently treated as repeatable cruise values.
- Missing cruise values remain missing; no value is inferred from a competitor,
  a brochure, or a conceptual assumption.
- The companion [`CURRENT_SPEED_BASIS_BURDEN_CONTEXT.md`](CURRENT_SPEED_BASIS_BURDEN_CONTEXT.md)
  applies the repository's dimensionless kinetic and ideal-thermal proxies to
  the same rows, with the same evidence-basis labels.

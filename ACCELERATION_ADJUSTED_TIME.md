# Acceleration-adjusted airborne-time sensitivity

## Question

How much does an explicit symmetric acceleration/deceleration time budget
reduce the apparent speed-only airborne-time saving?

This artifact derives a second-order comparison from the committed
[`acceleration_sensitivity.csv`](acceleration_sensitivity.csv) table. The common
9,492.6 km distance is retained only as the repository's fixed mathematical
yardstick. It is not a route, trajectory, or operating recommendation.

## Method

For each speed class and declared acceleration fraction, the script compares:

```text
speed-only ratio = cruise-only time / subsonic-reference cruise-only time
adjusted ratio   = idealized total time / subsonic-reference idealized total time
saved fraction   = 1 - ratio
```

The difference between the adjusted and speed-only ratios is recorded as the
fraction of the speed-only saving lost to the abstract acceleration phases. The
model contains no comfort threshold, trajectory, geometry, control law, route,
or operating procedure.

Run:

```text
python3 effective_time_sensitivity.py
python3 effective_time_independent_check.py
```

The first command writes [`effective_time_sensitivity.csv`](effective_time_sensitivity.csv).
The second independently recomputes all 12 rows and writes
[`effective_time_independent_check.csv`](effective_time_independent_check.csv).

## Result

| Speed class | Speed-only saving | Adjusted saving at 0.05g | Saving lost | Adjusted saving at 0.20g | Saving lost |
|---|---:|---:|---:|---:|---:|
| Concorde historical | 58.3% | 55.7% | 2.6 percentage points | 57.7% | 0.7 percentage points |
| Mach 3 conceptual | 72.2% | 67.8% | 4.4 percentage points | 71.1% | 1.1 percentage points |
| Mach 5 conceptual | 83.3% | 75.6% | 7.7 percentage points | 81.4% | 2.0 percentage points |

Under every tested acceleration fraction, all faster bins remain faster than
the subsonic reference in this kinematic screen. However, the speed-only model
overstates the saving, especially for the higher-speed bins at the lower
declared acceleration fraction. The independent reproduction matches all 12
rows within `1e-12`.

## Interpretation and limits

- This is a time-accounting result, not evidence that any speed class is
  passenger-safe, certifiable, affordable, quiet, or airport-compatible.
- The acceleration fractions are declared sensitivity inputs, not comfort or
  injury limits. No human-factors inference is made.
- Real aircraft do not follow constant-acceleration phases in a fixed uniform
  environment; the result is a falsifiable algebraic baseline only.
- No practicality status changes follow. The next useful test is to compare
  the abstract time savings with transferable passenger ride-quality evidence,
  without turning a kinematic assumption into a design requirement.

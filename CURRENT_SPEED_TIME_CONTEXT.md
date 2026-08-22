# Current speed/time context

## Question

How much airborne-time reduction does the current civilian subsonic speed
frontier provide in the repository's fixed-distance arithmetic screen, and how
does that compare with Mach 2?

The model uses the existing 9,492.6 km fixed mathematical yardstick and the
ideal speed-of-sound interval from `MACH_SPEED_CONSISTENCY.md`. It is not a
route, schedule, trajectory, climb profile, or operating model.

## Result

| Reference | Mach | Speed interval (km/h) | Airborne-time interval (min) | Speed-only saving vs Mach 0.85 |
|---|---:|---:|---:|---:|
| Airline-service baseline | 0.850 | 870–971 | 587–655 | 0.0% |
| Certified business-aviation reference: Global 7500 | 0.925 | 947–1,057 | 537–602 | 8.1% |
| Certified business-aviation reference: G700 | 0.935 | 957–1,068 | 535–595 | 9.1% |
| Historical Mach 2 service class | 2.000 | 2,047–2,284 | 250–279 | 57.5% |

The speed-only arithmetic shows why the repository should distinguish current
airline and business-aviation baselines: moving from Mach 0.85 to the certified
Global 7500 or G700 references yields single-digit percentage airborne-time
savings in this screen, while the historical Mach 2 class yields 57.5%. These
are ratios at fixed Mach and a common ideal sound-speed bracket, not promises
about actual flights.

## Reproducibility

```text
python3 current_speed_time_context.py
python3 current_speed_time_context_independent_check.py
```

The first command writes
[`current_speed_time_context.csv`](current_speed_time_context.csv) and
[`current_speed_time_context_summary.csv`](current_speed_time_context_summary.csv).
The independent implementation writes
[`current_speed_time_context_independent_check.csv`](current_speed_time_context_independent_check.csv)
and reproduces all seven summary metrics within `1e-12`.

## Interpretation and limits

- The time intervals inherit the ideal-gas sound-speed bracket, not observed
  winds, routing, climb/descent, acceleration, or airport timing.
- The 9,492.6 km value is retained only as a common mathematical yardstick from
  the archived screen; it is not a route recommendation.
- The G700 row is now service- and certification-anchored, but its Mach 0.935
  value is still a maximum-operating reference rather than a normal-cruise or
  airline-capacity claim.
- No one-hour target, route, vehicle, operational procedure, or design is
  inferred.
- This result does not change practicality status. It only clarifies the
  speed-only benefit available within current subsonic civilian aviation.

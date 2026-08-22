# Thermal context for current civilian speed references

## Question

How does the repository's ideal total-temperature screen compare the current
subsonic civilian references with the historical Mach 2 service class?

This is a deliberately narrow extension of `THERMAL_ENVELOPE.md`. It reuses
the frozen standard-atmosphere static-temperature interval and `gamma = 1.4`,
then adds the current reference speeds from
`CURRENT_CIVILIAN_SPEED_CLOSE_READ.md`.

## Result

| Reference | Mach | Ideal total-temperature interval |
|---|---:|---:|
| Airline-service baseline | 0.850 | 248.0–286.5 K |
| Certified business-aviation reference: Global 7500 | 0.925 | 253.7–293.1 K |
| Certified business-aviation reference: G700 | 0.935 | 254.4–293.9 K |
| Historical Mach 2 service class | 2.000 | 390.0–450.6 K |

The Mach 2 lower bound is above the highest current-reference upper bound in
this ideal screen: 390.0 K versus 294.1 K, a ratio of about 1.326. This is a
dimensioned ordering result, not a claim that any listed aircraft reaches the
ideal interval as a wall or cabin temperature.

## Reproducibility

```text
python3 thermal_current_service_context.py
python3 thermal_current_service_context_independent_check.py
```

The first command writes
[`thermal_current_service_context.csv`](thermal_current_service_context.csv)
and [`thermal_current_service_context_summary.csv`](thermal_current_service_context_summary.csv).
The independent implementation writes
[`thermal_current_service_context_independent_check.csv`](thermal_current_service_context_independent_check.csv)
and reproduces all seven summary metrics within `1e-12`.

## Interpretation and limits

- The relation is the ideal calorically-perfect-gas total/static temperature
  proxy already used by the repository; it does not model heat flux, duration,
  recovery factor, wall temperature, cabin temperature, materials, cooling, or
  serviceability.
- The current Mach 0.925 and 0.935 values are both certified in-service
  business-aviation references, but they remain distinct aircraft records and
  neither is interchangeable with an airline-capacity benchmark.
- “Higher than” here means higher within the frozen ideal proxy interval, not
  hotter aircraft hardware or a safety threshold.
- No vehicle, trajectory, altitude, route, construction, or operational
  guidance is inferred.

## Gate effect

The result adds context to the thermal gate but does not change its status.
Mach 2 remains a historical service anchor with unresolved system-level
thermal evidence; faster conceptual bins remain unresolved as well.

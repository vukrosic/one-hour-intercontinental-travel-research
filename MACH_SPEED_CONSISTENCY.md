# Mach-to-speed consistency audit

## Question

Are the repository's nominal km/h acceleration bins compatible with the Mach
classes and static-temperature sensitivity used by the thermal screen?

This is a unit and assumption audit. It uses the ideal-air speed-of-sound
relation

```text
a = sqrt(gamma * R * T)
speed = Mach * a
```

with the existing static-temperature interval (216.65–250.35 K), the existing
gamma sensitivity (1.30–1.40), and `R = 287.05 J/(kg K)`. It does not describe a
vehicle, altitude, trajectory, route, engine, or operating procedure.

## Reproducible method

Run:

```text
python3 mach_speed_consistency.py
python3 mach_speed_independent_check.py
```

The first command writes [`mach_speed_consistency.csv`](mach_speed_consistency.csv)
and [`mach_speed_acceleration_ranges.csv`](mach_speed_acceleration_ranges.csv).
The second independently recomputes all 16 speed rows and 12 derived
acceleration rows, writing [`mach_speed_independent_check.csv`](mach_speed_independent_check.csv).

The acceleration-distance fraction is the same abstract quantity used in the
existing kinematic screen:

```text
phase-distance fraction = speed^2 / (acceleration * fixed-distance yardstick)
```

The fixed 9,492.6 km value remains only a common mathematical yardstick inherited
from the archived baseline.

## Result

| Class | Mach | Derived speed interval (km/h) | Nominal bin (km/h) | Nominal inside interval? |
|---|---:|---:|---:|---|
| Subsonic reference | 0.85 | 870–971 | 900 | yes |
| Concorde historical | 2.0 | 2,047–2,284 | 2,160 | yes |
| Mach 3 conceptual | 3.0 | 3,071–3,426 | 3,240 | yes |
| Mach 5 conceptual | 5.0 | 5,118–5,709 | 5,400 | yes |

The nominal km/h bins are therefore internally compatible with the declared
Mach/temperature bracket. The uncertainty matters more for acceleration phase
distance: at 0.05g, the Mach 5 class spans roughly 43.4–54.0% of the fixed
yardstick, compared with 6.9–8.6% for Mach 2. All tested rows remain in the
accelerate–cruise–decelerate regime under this abstract screen.

## Interpretation and limits

- This resolves a bookkeeping inconsistency risk, not a feasibility gate.
- The ideal-air relation is not a high-temperature real-gas or aircraft-flow
  model; the gamma and temperature ranges are declared analytical sensitivities.
- Phase-distance fractions are not passenger comfort limits or recommended
  acceleration profiles.
- No practicality status changes follow. Thermal, passenger, noise, energy,
  economics, and airport gates remain conjunctive evidence requirements.

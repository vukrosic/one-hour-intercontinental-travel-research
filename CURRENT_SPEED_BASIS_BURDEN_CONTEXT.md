# Speed-basis burden context

## Question

Within the current evidence-basis rows, how do the simple (M^2) kinetic
energy-per-mass proxy and ideal total/static-temperature proxy differ between
top/max values and explicit cruise values?

These are dimensionless screening relations already used elsewhere in the
repository. They are not fuel burn, thrust, heat flux, wall temperature,
materials, propulsion, or aircraft-performance predictions.

## Result

| Basis group | Rows | Highest kinetic-energy-per-mass proxy vs M0.85 | Highest ideal total/static-temperature ratio |
|---|---:|---:|---:|
| Top/max arithmetic rows | 3 | 1.249x | 1.1805 |
| Explicit cruise wording rows | 4 | 1.121x | 1.1620 |

For the G700, the top/max Mach 0.935 row has a kinetic-energy-per-mass proxy
of about 1.21x the Mach 0.85 reference, while the explicitly named Mach 0.90
high-speed-cruise row is about 1.12x. The difference is a mathematical
consequence of the speed basis, not a claim about fuel use or a recommended
operating point.

## Reproducibility

```text
python3 current_speed_basis_burden_context.py
python3 current_speed_basis_burden_context_independent_check.py
```

The independent implementation reproduces all nine summary metrics within
`1e-12`.

## Limits

- Kinetic energy per unit mass is only proportional to (V^2); it is not the
  aircraft's drag power, fuel burn, or lifecycle energy.
- The ideal temperature relation assumes a calorically perfect gas with
  gamma=1.4 and does not model heat flux, duration, wall temperature, or
  cooling.
- The evidence-basis table's missing cruise values remain missing.
- No candidate design, propulsion recipe, construction instruction, route, or
  operating procedure is inferred.

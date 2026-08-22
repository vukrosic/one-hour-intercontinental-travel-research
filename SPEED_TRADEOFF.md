# Dimensionless speed-benefit tradeoff

## Question

How quickly does airborne-time benefit saturate as high-level thermal and kinetic-energy burdens rise with Mach number?

## Method

The comparison uses the same frozen Mach bins as `physics_envelope.py`. For a fixed distance and a common reference speed of Mach 0.85:

```text
airborne_time_ratio = 0.85 / Mach
airborne_time_saved_fraction = 1 - airborne_time_ratio
kinetic_energy_per_mass_ratio = (Mach / 0.85)^2
ideal_total_temperature_ratio = 1 + 0.2 Mach^2
```

The final two columns in `speed_tradeoff.csv` report the incremental time-saving fraction divided by the incremental kinetic-energy proxy and by the incremental total/static-temperature ratio relative to the previous speed bin. These are dimensionless screening metrics. They are not fuel burn, wall temperature, heat flux, cost, or vehicle performance.

## Result

| Mach bin | Airborne time vs M0.85 | Time saved | KE/mass proxy | Ideal total/static temperature | Marginal time saved per incremental KE proxy |
|---:|---:|---:|---:|---:|---:|
| 0.85 | 1.000 | 0.0% | 1.00x | 1.144 | n/a |
| 1.00 | 0.850 | 15.0% | 1.38x | 1.200 | 0.390 |
| 1.50 | 0.567 | 43.3% | 3.11x | 1.450 | 0.164 |
| 2.00 | 0.425 | 57.5% | 5.54x | 1.800 | 0.058 |
| 3.00 | 0.283 | 71.7% | 12.46x | 2.800 | 0.020 |
| 5.00 | 0.170 | 83.0% | 34.60x | 6.000 | 0.005 |

The marginal time saved per incremental kinetic-energy proxy falls by roughly 76 times from the M0.85→M1 step to the M3→M5 step. This is a robust mathematical diminishing-return result inside this deliberately narrow model.

## Interpretation

The comparison strengthens a negative constraint: higher speed always reduces airborne time, but the incremental time benefit shrinks while idealized thermal and kinetic-energy burdens grow quadratically. It does **not** identify an optimum Mach number because real practicality also depends on aerodynamics, propulsion efficiency, noise, passenger environment, emissions, utilization, reliability, and economics. No arbitrary weights are combined into a single score.

## Verification checkpoint

`speed_tradeoff_independent_check.py` independently reproduces all six rows within `1e-12`, including the marginal diminishing-return columns. This verifies the arithmetic trend only; it does not validate the physical proxies or any aircraft performance claim.

## Limitations

- Fixed-distance cruise arithmetic omits acceleration, climb, descent, winds, routing, and reserves.
- Kinetic energy is not fuel burn or lifecycle energy.
- Total temperature is not wall temperature or heat flux.
- The ideal-gas relation is a screening approximation and becomes progressively less representative at extreme conditions.
- The speed bins are conceptual comparisons, not aircraft specifications.

## Next hypothesis

If public passenger-service evidence is required, Mach 2 remains the upper demonstrated anchor. A speed class above Mach 2 should not be called practical unless empirical noise, energy/economic, passenger-environment, and thermal evidence compensates for the sharply weaker marginal time benefit shown here.

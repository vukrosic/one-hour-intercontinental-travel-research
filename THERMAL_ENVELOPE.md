# Bounded ideal thermal sensitivity

## Question

How does the ideal total-temperature screening interval change across the project’s abstract Mach bins under a public standard-atmosphere temperature range?

## Method

NASA’s standard-atmosphere table gives 216.65 K through part of the lower stratosphere and 250.35 K at another tabulated high-altitude point. The model uses these values only as a generic static-temperature sensitivity interval; it does not select an altitude, route, or flight condition.

For calorically perfect air with `gamma = 1.4`:

```text
T_total / T_static = 1 + 0.5 * (gamma - 1) * Mach^2
```

`thermal_inputs.csv` records the numerical inputs and limitations. `thermal_sensitivity.py` reproduces the interval for the same frozen Mach bins used elsewhere in the repository.

## Result

| Mach bin | Ideal total/static ratio | Ideal total-temperature interval |
|---:|---:|---:|
| 0.85 | 1.144 | 248.0–286.5 K |
| 1.00 | 1.200 | 260.0–300.4 K |
| 1.50 | 1.450 | 314.1–363.0 K |
| 2.00 | 1.800 | 390.0–450.6 K |
| 3.00 | 2.800 | 606.6–701.0 K |
| 5.00 | 6.000 | 1,299.9–1,502.1 K |

The Mach 3 lower bound is above the Mach 2 upper bound across this entire static-temperature interval. The ideal interval grows much faster than the airborne-time benefit.

## Interpretation

This makes the thermal burden concrete without designing a vehicle. Mach 2 already moves the ideal total-temperature proxy far above the ambient interval; Mach 3 and Mach 5 move into qualitatively different thermal regimes. The result strengthens the requirement for empirical thermal evidence before calling a speed class above Mach 2 practical.

## What this result is not

- It is not wall, skin, cabin, engine, or material temperature.
- It is not heat flux, heating duration, thermal stress, or cooling demand.
- It does not select an altitude, trajectory, atmosphere, material, geometry, thickness, or protection system.
- It does not show that any speed class is safe, unsafe, possible, or impossible.

## Limitations

- The calorically perfect-gas approximation becomes progressively weaker as temperature rises; the Mach 5 numbers are especially illustrative rather than predictive.
- Real-gas chemistry, viscous heating, radiative effects, heat transfer, and recovery factor are outside this model.
- The static-temperature interval is a sensitivity range from a standard atmosphere, not observed weather or an operating envelope.

## Gate conclusion

The thermal gate remains unresolved, but its high-level trend is now supported by both dimensionless and bounded-temperature calculations. Public empirical evidence would be required to connect these ideal total temperatures to passenger-aircraft serviceability. No material or vehicle inference is justified from this model.

## Verification checkpoint

`thermal_independent_check.py` independently re-derives the ideal relation and reproduces all six committed rows within `1e-12`. This validates arithmetic and frozen inputs only; it does not validate the calorically perfect-gas approximation or the application of the ideal proxy to an aircraft.

## Next hypothesis

The thermal step from Mach 2 to Mach 3 may be a stronger practical discriminator than the associated fixed-distance time saving. Testing that safely requires public empirical programme data or system-level environmental limits, not material selection or thermal-protection design.

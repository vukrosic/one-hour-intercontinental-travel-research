# Historical energy proxy: input stress test

## Question

Does the adverse historical Mach 2 energy comparison depend on one rounded
public input, or does it survive a declared bookkeeping stress?

This artifact stress-tests the existing aggregate Concorde-versus-modern
long-haul comparison. It is not a statistical confidence interval, a forecast,
a technology target, or a design requirement.

## Method

`energy_input_sensitivity.py` reuses the pinned values in
[`energy_inputs.csv`](energy_inputs.csv) and evaluates 11 deterministic
scenarios for each of the existing 100%, 80%, and 60% occupancy assumptions:

- baseline;
- one-factor ±10% changes to the historical fuel-use proxy, cruise-speed
  proxy, seat-capacity denominator, or modern long-haul benchmark; and
- an all-favorable and all-adverse ±10% combination.

The ±10% bracket is an explicit stress choice, not a source-derived uncertainty
estimate. The result is a passenger-distance direct-CO2 ratio only. It does not
model aircraft operations, lifecycle climate effects, cost, reliability, or any
future aircraft.

Run:

```text
python3 energy_input_sensitivity.py
python3 energy_input_independent_check.py
```

The first command writes [`energy_input_sensitivity.csv`](energy_input_sensitivity.csv).
The second independently recomputes all 33 rows and writes
[`energy_input_independent_check.csv`](energy_input_independent_check.csv).

## Result

| Occupancy | Baseline ratio | All-favorable ±10% stress | All-adverse ±10% stress |
|---:|---:|---:|---:|
| 100% | 3.017x | 2.040x | 4.553x |
| 80% | 3.772x | 2.550x | 5.691x |
| 60% | 5.029x | 3.401x | 7.588x |

The most favorable declared stress still leaves the historical proxy above the
modern aggregate at every occupancy level. At 100% occupancy it still implies
about a 51.0% direct-intensity reduction to match the benchmark. The independent
implementation reproduces all 33 rows with a maximum absolute difference below
`1e-12`.

## Interpretation and limits

- Within this deliberately bounded bookkeeping stress, the direction of the
  historical energy result does not flip.
- This does not prove that every future supersonic concept would exceed the
  benchmark; no future aircraft is modeled.
- The dominant limitations remain historical specification data versus a
  modern aggregate, occupancy comparability, and omission of non-CO2 climate
  effects.
- The energy gate therefore remains **contradicted for the historical Mach 2
  anchor relative to the selected benchmark**, while future speed classes remain
  unresolved rather than numerically ruled out.

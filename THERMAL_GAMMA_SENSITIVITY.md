# Ideal thermal screen: gamma sensitivity

## Question

Does the ordering of the bounded ideal total-temperature intervals depend on
freezing the ideal-gas parameter `gamma` at exactly 1.4?

This is a robustness check for the existing [thermal envelope](THERMAL_ENVELOPE.md),
not a vehicle or certification model. It varies only `gamma` across two declared
analytical scenarios, `1.30` and `1.40`, while retaining the existing generic
static-temperature interval of 216.65–250.35 K and Mach bins. The scenarios are
not a claim about the actual thermodynamic state of a passenger aircraft.

## Reproducible method

For each Mach bin and each `gamma` scenario, the script evaluates the ideal-gas
relation

```text
T0 / T = 1 + 0.5 * (gamma - 1) * M^2
```

and multiplies the ratio by the two static-temperature bounds. Run:

```text
python3 thermal_gamma_sensitivity.py
python3 thermal_gamma_independent_check.py
```

The first command writes [`thermal_gamma_sensitivity.csv`](thermal_gamma_sensitivity.csv).
The second command independently recomputes every row and writes
[`thermal_gamma_independent_check.csv`](thermal_gamma_independent_check.csv).
The committed inputs remain in [`thermal_inputs.csv`](thermal_inputs.csv), with
source IDs and limitations recorded there.

## Result

The Mach 3 lower bound remains above the Mach 2 upper bound in both scenarios:

| gamma | Mach 2 interval (K) | Mach 3 interval (K) | ordering |
|---:|---:|---:|---|
| 1.30 | 346.6–400.6 | 509.1–588.3 | separated |
| 1.40 | 390.0–450.6 | 606.6–701.0 | separated |

The qualitative ordering is therefore robust to this small analytical gamma
sensitivity. The independent check reproduces all 12 rows with a maximum
absolute difference of `0` in the committed decimal representation.

## Interpretation and limits

- This supports only the narrow statement that the idealized temperature ratio
  grows strongly with Mach under either declared gamma scenario.
- It does **not** predict wall temperature, heat flux, material behavior,
  cooling, structural life, cabin conditions, or passenger serviceability.
- The two gamma values are a deliberately small sensitivity bracket, not a
  validated high-temperature-air model. Real-gas effects, dissociation,
  boundary layers, and vehicle-specific flow are outside scope.
- No practicality status changes follow from this arithmetic result. Thermal,
  passenger, noise, energy, economics, and airport gates remain conjunctive
  evidence requirements.

The related Mach-to-speed bookkeeping audit is in
[MACH_SPEED_CONSISTENCY.md](MACH_SPEED_CONSISTENCY.md).

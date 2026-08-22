# Independent thermal-envelope reproduction

`thermal_independent_check.py` re-reads `thermal_inputs.csv` and the committed `thermal_sensitivity.csv` without importing either the primary thermal script or the shared physics helper. It independently evaluates the ideal total/static relation and compares the ratio and both temperature bounds for all six Mach bins.

Running `python3 thermal_independent_check.py` gives six passing rows at an absolute tolerance of `1e-12`. This verifies the arithmetic path and frozen inputs. It does not turn the ideal proxy into a wall-temperature, heat-flux, material, or vehicle prediction.

The calorically perfect-gas and standard-atmosphere limitations remain exactly as documented in [THERMAL_ENVELOPE.md](THERMAL_ENVELOPE.md). Empirical system-level thermal evidence is still required before any high-speed class can receive a practical pass.

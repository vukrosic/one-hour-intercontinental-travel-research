# Independent energy-gate reproduction

## Purpose

This checkpoint tests whether the historical Mach 2 energy comparison can be reproduced by a separate implementation. It is a verification artifact, not a new aircraft model.

## Method

`energy_independent_check.py` reads `energy_inputs.csv` and the committed `energy_intensity_results.csv`. It does not import `energy_intensity.py`. Instead it independently groups the same public inputs into gallons/hour, passenger-miles/hour, fuel per passenger-mile, and energy/CO2 per passenger-mile, then compares each result with an absolute tolerance of `1e-9` in the reported units.

## Result

Running `python3 energy_independent_check.py` gives three passing rows, one each for 100%, 80%, and 60% occupancy. The maximum absolute delta across energy, direct CO2, and the derived modern-energy benchmark is below `1e-9` for every row.

This confirms arithmetic and unit-conversion agreement with the existing energy proxy. It does **not** validate the public source measurements, the comparability of a historical cruise proxy with a modern aggregate, or any future aircraft performance.

## Scope and limitation

The check remains bounded to direct-combustion energy and CO2 per passenger-mile. It excludes lifecycle and non-CO2 climate effects, mission phases, maintenance, economics, and all physical design or propulsion questions. Independent reproduction of the thermal, noise, passenger, and airport gates remains open.

# Historical Mach 2 energy-gap sensitivity

## Question

How large is the direct energy-intensity reduction implied by the historical Mach 2 proxy if it were to match the selected modern long-haul benchmark?

## Method

`energy_gap_sensitivity.py` reads the committed ratios in `energy_intensity_results.csv` and calculates the allowed fraction and required reduction relative to the modern benchmark:

```text
allowed fraction = 1 / historical proxy ratio
required reduction = 1 - allowed fraction
```

This is an arithmetic restatement of the existing comparison. It does not forecast a future aircraft or identify a way to achieve the reduction.

## Result

| Occupancy assumption | Historical proxy ratio | Required direct-intensity reduction to match modern benchmark |
|---:|---:|---:|
| 100% | 3.02x | 66.9% |
| 80% | 3.77x | 73.5% |
| 60% | 5.03x | 80.1% |

Even the favorable full-occupancy case requires roughly a two-thirds reduction in direct passenger-distance energy relative to the historical proxy. Lower occupancy increases the gap.

## Boundary and limitations

- The calculation inherits the historical-specification-versus-modern-aggregate comparability limits in [ENERGY_ECONOMICS.md](ENERGY_ECONOMICS.md).
- “Required reduction” is a benchmark gap, not a technology target, design requirement, or propulsion recipe.
- Direct combustion energy and CO2 omit lifecycle and non-CO2 climate effects.
- No claim is extrapolated above Mach 2.

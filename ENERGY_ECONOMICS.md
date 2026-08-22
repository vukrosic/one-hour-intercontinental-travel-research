# Energy, climate, and historical economics gate

## Question

How does the only historical Mach 2 passenger-service anchor compare with a modern long-haul aggregate on direct fuel energy and CO2 per passenger-distance?

## Method

`energy_inputs.csv` records all numerical inputs, units, sources, roles, and limitations. `energy_intensity.py` combines:

- British Airways’ published Concorde fuel use (25,629 L/hour), cruise speed (2,160 km/hour), and 100-seat capacity;
- the Bureau of Transportation Statistics jet-fuel heat conversion (135,000 Btu/US gallon) and unit conversions;
- the U.S. Energy Information Administration direct-combustion jet-fuel factor (9.75 kg CO2/US gallon); and
- the U.S. EPA long-haul air-travel factor (0.163 kg CO2/passenger-mile, based on 2019 source data).

The modern long-haul energy comparison is derived from the EPA CO2 factor using the same EIA/BTS fuel factors. Concorde is evaluated at 100%, 80%, and 60% seat occupancy. No ticket price, aircraft purchase price, propulsion model, or route is used.

## Reproducible result

| Concorde occupancy assumption | Proxy energy (Btu/passenger-mile) | Direct CO2 (kg/passenger-mile) | Ratio versus modern long-haul aggregate |
|---:|---:|---:|---:|
| 100% | 6,810 | 0.492 | 3.02x |
| 80% | 8,513 | 0.615 | 3.77x |
| 60% | 11,350 | 0.820 | 5.03x |

The derived modern long-haul comparison is approximately 2,257 Btu/passenger-mile. Because both comparisons use the same fuel heat and direct-CO2 factors, their energy and direct-CO2 ratios are numerically equal.

## Interpretation

Even under the favorable 100%-occupied assumption, the public Concorde cruise proxy is roughly three times the modern long-haul aggregate energy and direct CO2 per passenger-mile. Lower occupancy worsens the result inversely. This supports a strong negative constraint: a speed class at or above Mach 2 needs a substantial efficiency improvement merely to approach current long-haul passenger energy intensity.

Historical NASA work independently described Concorde’s operating economics as uncompetitive and reported total operating cost around twice that of similar-technology subsonic transport. That historical comparison corroborates the direction of the energy result, but it is not a current business case.

## Limitations

- Concorde’s published hourly fuel use and cruise speed form a specification proxy, not observed gate-to-gate mission data.
- The modern EPA aggregate includes real-world operations and occupancy; the Concorde 100% case assumes every seat is occupied.
- The comparison mixes a historical aircraft fact sheet with a modern aggregate whose underlying travel data are from 2019.
- Direct combustion CO2 excludes fuel production and non-CO2 climate effects.
- Energy intensity is not total operating cost, fare, profitability, reliability, maintenance burden, or market demand.
- No result is extrapolated to a proposed aircraft above Mach 2.

## Gate conclusion

The energy gate is **contradicted for historical Concorde relative to the selected modern long-haul benchmark**. The economics gate remains unresolved for any future speed class, although historical evidence is adverse. A faster class cannot be labeled practical without public evidence that closes the energy-intensity gap under realistic occupancy.

## Next hypothesis

The practical frontier may lie near the lowest supersonic speed that produces meaningful time savings while avoiding the steep energy penalty of the Mach 2 historical anchor. Testing that hypothesis requires empirical data from civil supersonic demonstrators or transparent commercial studies; an abstract propulsion or vehicle design would not resolve it.

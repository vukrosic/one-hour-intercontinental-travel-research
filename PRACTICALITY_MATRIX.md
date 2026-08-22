# Cross-gate practicality matrix

## Purpose

This is the next bounded research artifact for the question **what is the fastest practical civilian passenger airplane?** It translates the repository's separate evidence gates into a transparent comparison of four abstract speed classes:

- a current commercial reference near Mach 0.85;
- the historical Mach 2 service anchor (sustained Concorde plus limited Tu-144 service); and
- Mach 3 and Mach 5 conceptual comparison bins.

The bins are not aircraft specifications. They do not imply a route, vehicle layout, propulsion system, material, trajectory, or operating procedure.

## Method

`practicality_matrix.csv` records one evidence state for each named gate. The states are copied from or conservatively derived from the existing benchmark, passenger, thermal, noise, energy/economics, and airport audits. `practicality_summary.py` validates the vocabulary and counts evidence states; it does not assign weights, optimize a design, or calculate a scalar practicality score.

`practicality_gate_check.py` adds a semantic guard: a future `practical_pass` row cannot contain unresolved, contradicted, or adverse gate states.

The screen is conjunctive: a class cannot receive a current `practical_pass` while any critical gate remains unresolved or contradicted. The `practical_status` labels therefore describe evidence maturity, not a universal physical impossibility result.

## Reproducible result

Running `python3 practicality_summary.py` yields:

```text
speed_class_rows=4
current_practical_pass_rows=0
current_baseline_not_ranked_rows=1
historical_anchor_not_current_practical_pass_rows=1
conceptual_unresolved_rows=2
contradicted_gate_cells=1
adverse_historical_gate_cells=1
classes_with_no_service_anchor=2
```

The current evidence hierarchy is therefore:

1. **Mach 0.85 reference:** a current-service baseline, not a claim that it is the fastest practical class.
2. **Mach 2:** the only class with direct historical passenger-service evidence (sustained Concorde and limited Tu-144 service), but not a current practicality pass because energy/climate is contradicted versus the selected modern benchmark and multiple gates remain unresolved or historically adverse.
3. **Mach 3 and Mach 5:** conceptual bins with arithmetic time benefit but no passenger-service anchor and no complete evidence across thermal, noise, energy, economics, or airport compatibility.

## Plain-language conclusion

The fastest practical civilian passenger airplane is **not yet identified** by public evidence in this repository. Mach 2 is the strongest historical anchor, not a recommendation. Speeds above Mach 2 currently have a larger evidence gap, while the time model shows diminishing returns as speed rises. A defensible answer requires closing the named gates with comparable public data; it cannot be obtained by extrapolating a faster number.

## Limitations and next hypothesis

- The matrix is an evidence-status screen, not a probability, cost, or utility model.
- “Current baseline” means present-day commercial reference evidence; it does not prove every airport, route, or aircraft configuration.
- The Mach 2 energy result is a bounded historical proxy, not a forecast for a future design.
- Thermal entries use idealized dimensionless and atmosphere sensitivity results only; no heat flux, wall temperature, materials, or protection system is inferred.
- The next useful experiment is an independent reproduction of one gate at a time, beginning with the Mach 2 energy comparison and then the thermal sensitivity, with pinned inputs and source dates.

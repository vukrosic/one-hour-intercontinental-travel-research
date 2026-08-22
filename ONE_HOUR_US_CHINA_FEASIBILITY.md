# One-hour U.S.–China passenger travel: bounded public-data feasibility study

## Scope and safety boundary

This is a civilian transport-science feasibility and simulation study. It does **not** specify a vehicle, propulsion system, trajectory, materials, manufacturing process, or operational procedure. Any numerical model is intentionally low-order and uses public, aggregate data only.

## Research question

Under explicit, civilian assumptions, is a scheduled one-hour door-to-door U.S.–China passenger journey physically and economically plausible, and which constraints dominate? The first milestone tests an even narrower claim: whether a one-hour **airborne cruise** can satisfy a transparent energy/heat/acceleration/noise screening model without requiring implausible parameter values.

## High-level bottlenecks

- **Time accounting:** airport access, security, boarding, climb/descent, routing, and arrival handling can consume much of a one-hour door-to-door target.
- **Aerothermal environment:** high-speed atmospheric flight creates heating and thermal-protection demands; we will use literature bounds, not vehicle design.
- **Energy and emissions:** compare order-of-magnitude specific energy to public aviation and electricity/fuel lifecycle factors.
- **Aerodynamics:** use published drag/lift efficiency ranges and sensitivity analysis, not geometry or optimization of a craft.
- **Passenger acceleration:** screen peak and sustained acceleration against public human-factors limits and comfort guidance.
- **Noise and sonic boom:** treat community exposure as a constraint using published regulatory/research thresholds.
- **Cost and reliability:** compare energy, maintenance, infrastructure, and schedule-reliability ranges with public transport benchmarks.
- **Infrastructure and regulation:** identify airport, airspace, overflight, safety, and environmental approval dependencies at a descriptive level only.

## What is feasible with public sources and modest computing

We can reproduce a spreadsheet/Python model using route great-circle distance, time-budget equations, bounded speed/acceleration profiles, and literature-derived ranges for lift-to-drag ratio, thermal load proxies, specific energy, noise, and passenger limits. Monte Carlo or one-at-a-time sensitivity analysis is sufficient; no CFD, proprietary data, or hardware is required.

## First falsifiable experiment (v0.1)

### Hypothesis

For a representative U.S.–China city pair, a one-hour airborne segment is ruled out by at least one of four screening constraints across the majority of defensible public parameter ranges: (1) required average speed after climb/descent and routing margin, (2) energy per passenger, (3) thermal/heat-rate proxy, or (4) passenger acceleration/noise bounds.

### Frozen scenario and assumptions

1. Select one city pair only (default Los Angeles–Shanghai) and record airport coordinates and source.
2. Use great-circle distance as a lower bound; add a fixed routing margin (default 10%, sensitivity 0–25%).
3. Define “airborne one hour” separately from “door-to-door one hour”; do not mix them.
4. Reserve explicit climb/descent and schedule margins (default 10 minutes total), leaving 50 minutes for cruise in the screening case.
5. Represent passenger payload as a range per traveler (including seat, baggage, and allocated systems mass); do not choose a vehicle layout.
6. Evaluate speed, energy, and heat with broad literature ranges and report intervals, not point claims.
7. Treat any result as a screen, not a certification or design result.

### Reproducible calculations

For each sampled parameter set:

```text
route_km = great_circle_km * (1 + routing_margin)
cruise_time_h = 1 - climb_descent_minutes/60
required_mean_speed = route_km / cruise_time_h
specific_transport_energy = (g * route_km) / (L_over_D * payload_efficiency)
passenger_energy = specific_transport_energy * allocated_mass_per_passenger
```

The energy expression is an intentionally transparent lower-order transport-work proxy; it must be labeled as such and compared against a second, empirical benchmark from public aircraft energy/fuel data. A separate heat screen should use published stagnation/convective-heating correlations only as dimensionless or normalized proxies, avoiding geometry, material, or propulsion prescriptions.

### Pass/fail criteria

- **Speed:** report whether required mean speed lies inside the selected public reference envelope.
- **Energy:** report median and 5–95% interval versus commercial aviation and public high-speed-transport benchmarks.
- **Human factors:** fail the scenario if required acceleration profile exceeds the chosen public comfort/safety envelope.
- **Noise:** mark “unresolved/likely blocker” when no public evidence supports compliance for populated-route operation; do not infer a design fix.
- **Robustness:** the hypothesis is supported if ≥3 of 4 screens fail in ≥80% of Monte Carlo draws. Otherwise classify as inconclusive and tighten sources, not assumptions.

## Data and source plan

Use primary or authoritative public sources: Great-circle coordinates from government/geospatial datasets; FAA/ICAO and national aviation/environmental rules; NASA/ESA or peer-reviewed aerothermal and human-factors literature; EASA/FAA noise and sonic-boom research; publicly reported aircraft performance and energy data; World Bank/IEA lifecycle factors where relevant. Record URL/DOI, access date, units, extraction method, and uncertainty for every value.

## Reproducibility record

Store a plain-text assumptions table, source ledger, and script/notebook under a dedicated project folder. Pin software versions, random seed, and parameter ranges. Keep airborne and door-to-door outputs in separate columns. Preserve negative and inconclusive results. Every chart must show units, source, and sampled range.

## Constraints and non-goals

No detailed vehicle configuration, propulsion recipe, trajectory, thermal-protection design, construction method, weapons application, evasion tactic, or operational guidance. No claim of commercial, regulatory, or safety readiness follows from this screen. Public-data gaps are findings, not invitations to infer hidden engineering details.

## Next steps

1. Confirm the city pair and the operational definition (airborne vs door-to-door).
2. Build the source ledger and coordinate/distance calculation.
3. Implement the frozen v0.1 model with a fixed seed and unit tests for distance/time/energy equations.
4. Run a small 1,000-draw smoke test, inspect ranges, then expand only if calculations are correct.
5. Publish a methods note with assumptions, uncertainty, and failure modes before adding any new physics.

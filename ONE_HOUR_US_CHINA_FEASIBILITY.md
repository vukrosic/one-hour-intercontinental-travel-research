# One-hour U.S.–China passenger travel: bounded public-data feasibility study

> **Archive note (2026-08-22):** The door-to-door one-hour question is no longer the primary research objective. It is retained as a clearly labeled historical baseline. The active project question is now “what is the fastest practical civilian passenger airplane?” See `FAST_CIVILIAN_AIRCRAFT_RESEARCH_MAP.md`.

## Scope and safety boundary

This is a civilian transport-science feasibility and simulation study. It does **not** specify a vehicle, propulsion system, trajectory, materials, manufacturing process, or operational procedure. Any numerical model is intentionally low-order and uses public, aggregate data only.

## Research question

Under explicit, civilian assumptions, is a scheduled one-hour **door-to-door** San Francisco–Beijing passenger journey physically and economically plausible, and which constraints dominate? Airborne time is only one component of the total budget.

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

With realistic minimum airport-process and access times, the one-hour door-to-door target leaves too little airborne time for the San Francisco–Beijing distance across the majority of defensible public parameter ranges. This is a falsifiable screening claim, not a universal impossibility theorem.

### Frozen scenario and assumptions

1. Canonical city pair: San Francisco International (SFO) to Beijing Capital (PEK); coordinates are recorded in the script and must be replaced/verified against a cited public geospatial source.
2. Total target is exactly 60 minutes door-to-door. The budget is split into origin ground access, check-in/security, boarding, ground operations, ascent/descent, airborne segment, and arrival/egress.
3. Sample non-airborne components independently from explicit ranges: access 5–15 min, check-in/security 10–20, boarding 5–10, ground operations 3–8, ascent/descent 8–15, arrival/egress 5–15.
4. Use great-circle distance as a lower bound and add a routing margin (0–25%). Any negative airborne-time draw is an immediate failure.
5. Represent passenger payload as a range per traveler (including seat, baggage, and allocated systems mass); do not choose a vehicle layout.
6. Evaluate speed and energy with broad literature ranges and report intervals, not point claims. Heat, noise, and human factors remain separate evidence gates.
7. Treat every result as a screen, not a certification or design result.

### Reproducible calculations

For each sampled parameter set:

```text
non_airborne_min = access + checkin_security + boarding + ground_ops + ascent_descent + arrival_egress
airborne_time_h = (60 - non_airborne_min) / 60
route_km = great_circle_km * (1 + routing_margin)
required_mean_speed = route_km / airborne_time_h
specific_transport_energy = (g * route_km) / (L_over_D * payload_efficiency)
passenger_energy = specific_transport_energy * allocated_mass_per_passenger
```

The energy expression is an intentionally transparent lower-order transport-work proxy; it must be labeled as such and compared against a second, empirical benchmark from public aircraft energy/fuel data. A separate heat screen should use published stagnation/convective-heating correlations only as dimensionless or normalized proxies, avoiding geometry, material, or propulsion prescriptions.

### Pass/fail criteria

- **Time budget:** report median and 5–95% non-airborne time and the fraction of draws with positive airborne time.
- **Speed:** report whether required mean speed lies inside the selected public reference envelope; do not treat that envelope as a design target.
- **Energy:** report median and 5–95% interval versus commercial aviation and public high-speed-transport benchmarks.
- **Human factors:** fail the scenario if required acceleration profile exceeds the chosen public comfort/safety envelope.
- **Noise:** mark “unresolved/likely blocker” when no public evidence supports compliance for populated-route operation; do not infer a design fix.
- **Robustness:** the hypothesis is supported if ≥3 of 4 screens fail in ≥80% of Monte Carlo draws. Otherwise classify as inconclusive and tighten sources, not assumptions.

### v0.2 result (seed 20260822, 1,000 draws)

The SFO–PEK great-circle lower bound is approximately 9,493 km. Under the frozen process ranges, non-airborne time has p05/median/p95 of 49.9/59.3/68.9 minutes. Only 54.2% of draws leave any positive airborne time, and just 5.2% leave at least 10 minutes. Among positive-airborne draws, required mean speed has p05/median/p95 of approximately 53,937/139,520/1,635,895 km/h. The low-order transport-work proxy energy has p05/median/p95 of 1,719/3,266/6,920 MJ per passenger.

**Interpretation:** under these explicit assumptions, a 60-minute door-to-door SFO–PEK trip is not feasible as a robust public-data scenario. The dominant first-order result is the time budget, before heat, noise, passenger acceleration, infrastructure, or economics are considered. This does not prove that every conceivable transport architecture is impossible; it identifies which assumptions would have to change and which evidence gates must be tested next.

## Data and source plan

Use primary or authoritative public sources: Great-circle coordinates from government/geospatial datasets; FAA/ICAO and national aviation/environmental rules; NASA/ESA or peer-reviewed aerothermal and human-factors literature; EASA/FAA noise and sonic-boom research; publicly reported aircraft performance and energy data; World Bank/IEA lifecycle factors where relevant. Record URL/DOI, access date, units, extraction method, and uncertainty for every value.

## Reproducibility record

Store a plain-text assumptions table, source ledger, and script/notebook under a dedicated project folder. Pin software versions, random seed, and parameter ranges. Keep airborne and door-to-door outputs in separate columns. Preserve negative and inconclusive results. Every chart must show units, source, and sampled range.

## Constraints and non-goals

No detailed vehicle configuration, propulsion recipe, trajectory, thermal-protection design, construction method, weapons application, evasion tactic, or operational guidance. No claim of commercial, regulatory, or safety readiness follows from this screen. Public-data gaps are findings, not invitations to infer hidden engineering details.

## Next steps

1. Verify SFO/PEK coordinates and airport-process ranges against primary public sources.
2. Compare the time-budget screen with an empirical commercial-aviation baseline.
3. Add separately sourced heat, noise, and passenger-acceleration gates without introducing design details.
4. Preserve the negative/inconclusive result and update only through auditable commits.

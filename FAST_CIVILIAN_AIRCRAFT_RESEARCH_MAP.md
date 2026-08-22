# Fast civilian passenger aircraft: research map (primary phase)

## Scope

The primary question is: **what is the fastest practical civilian passenger airplane?** “Practical” means a speed class supported by credible evidence across passenger safety/comfort, thermal environment, noise, energy/economics, airport compatibility, and verification—not merely the highest speed in a paper study. The work uses public historical/commercial benchmarks and low-order comparisons. It is not a vehicle design study. It excludes geometry, dimensions, propulsion recipes, materials selection, trajectories, construction, certification procedures, and operational guidance.

## Benchmark anchors

- **Historical Mach 2 service:** British Airways documents Concorde's sustained passenger service at 1,350 mph (2,160 km/h, Mach 2), while NASA documents a separate, limited Tu-144 airline passenger service that ended after 102 flights. `HISTORICAL_SERVICE_CLOSE_READ.md` keeps the durable Concorde precedent separate from the limited Tu-144 record and from later research-only Tu-144LL flights. These are historical anchors, not templates to reproduce.
- **Current subsonic references:** `CURRENT_CIVILIAN_SPEED_CLOSE_READ.md` separates a Mach 0.85 airline-service baseline, a certified in-service Mach 0.925 business-aviation anchor, and a conditional Mach 0.935 manufacturer-only performance claim.
- **NASA X-59 / Quesst:** NASA describes X-59 as a research aircraft intended to collect community-response and acoustic data for future quiet-supersonic rules. It is evidence that noise acceptance is an unresolved verification gate, not evidence of commercial readiness.
- **Regulatory context:** FAA material records that civil supersonic flight over land in the United States has been prohibited since 1973, while current research may inform future rulemaking.

Sources are listed with retrieval dates and claim types in `fast_aircraft_sources.csv`.

The current programme-status close read in `CURRENT_PROGRAMME_CLOSE_READ.md`
keeps research demonstrators, experimental permissions, company-reported plans,
and proposed regulation separate from passenger service. It is a maturity audit,
not a design comparison.

## Bounded comparison model

`fast_aircraft_benchmark.py` compares abstract reference-speed classes (subsonic, Concorde-like supersonic, and faster conceptual bands) against a fixed intercontinental distance (the SFO–PEK great-circle lower bound used only as a common comparison yardstick). These are speed bins, not aircraft specifications. The primary output is airborne time at each speed. Optional non-airborne overhead values are retained only as a secondary practical-context sensitivity; there is no one-hour door-to-door target.

The model deliberately does not estimate lift, drag, heating, engine performance, structural loads, or noise. Those are separate evidence gates.

## Research gates

1. **Time and speed:** Does a public benchmark speed leave meaningful margin after non-airborne time? Report intervals, not a single promised journey time.
2. **Passenger safety and comfort:** Find public human-factors limits for sustained/peak acceleration, vibration, cabin pressure, evacuation, and thermal comfort. Distinguish comfort guidance from injury thresholds.
3. **Thermal environment:** Use normalized, literature-based heat-rate or wall-temperature proxies only. Do not infer materials, thicknesses, shapes, or thermal-protection recipes.
4. **Noise:** Compare takeoff/landing noise and sonic-boom evidence with public regulatory and community-response work. NASA Quesst is a measurement program, not a compliance result.
5. **Energy and economics:** Compare passenger-km energy and cost ranges with subsonic and historical supersonic data. Preserve uncertainty from load factor, fuel price, maintenance, and utilization.
6. **Airport compatibility:** Treat runway, gate, maintenance, emergency response, airspace, and overland-noise constraints as qualitative public-data checks; no operating procedure is proposed.
7. **Verification:** Every future claim needs a source, units, date, uncertainty, and an independent cross-check. A result is “inconclusive” when public evidence is missing.

## Current finding

Speed alone is not the research conclusion. `CURRENT_SPEED_TIME_CONTEXT.md` shows that the certified business-aviation reference saves only about 8.1% of speed-only airborne time versus the Mach 0.85 airline baseline, while the historical Mach 2 class saves 57.5% in the same arithmetic screen. A Mach 2-class cruise has the only direct passenger-service precedent in this ledger, while current programmes remain research, experimental-test, company-reported, or proposed-regulatory evidence. The current subsonic frontier also splits by service class: airline operations cluster near Mach 0.85, while certified business aviation reaches higher subsonic values. The fastest practical civilian aircraft is bounded by noise acceptance, energy per passenger, passenger comfort, airport compatibility, and certification evidence. Faster abstract speed bands are hypotheses to test, not recommendations. The next useful result is therefore a gate-by-gate evidence matrix, not a faster notional aircraft.

## Next bounded experiments

1. Validate the benchmark table against primary/authoritative sources and attach uncertainty ranges.
2. Build a passenger-comfort evidence table with separate comfort, operational, and injury thresholds.
3. Add a dimensionless thermal-load comparison from public literature, with no geometry or materials.
4. Reconcile energy/economics evidence from historical Concorde and modern commercial aviation.
5. Record which gates are supported, contradicted, or unresolved before any expanded model.

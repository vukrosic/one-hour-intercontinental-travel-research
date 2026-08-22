# Research log

## 2026-08-22 — Phase 1: archived one-hour travel screen

- Established a transparent SFO–PEK distance/time screen.
- Negative result: a 60-minute door-to-door requirement was dominated by non-airborne time assumptions.
- Direction changed: door-to-door time is no longer the research target.

## 2026-08-22 — Phase 2: fastest practical civilian passenger airplane

- Froze the primary question and non-actionable safety boundary.
- Added historical/reference speed bins and public source ledger.
- Demonstrated airborne-time arithmetic for a common intercontinental distance.
- Started gate-based feasibility: historical service, passenger comfort, cabin environment, thermal trend, noise, energy/climate, economics, airport compatibility, and independent verification.
- Added a dimensionless physics envelope using NASA’s ideal-gas total-temperature relation and normalized kinetic energy per unit mass.
- Negative/limiting result: increasing Mach produces nonlinear thermal and kinetic-energy burdens; time benefit alone cannot establish practicality.
- Next hypothesis: Mach 2 remains the highest evidence-backed passenger-service anchor, while higher speed classes will remain “unresolved” until multiple gates have public evidence.

## 2026-08-22 — Phase 3: marginal speed benefit versus burden

- Added a tested, dimensionless tradeoff model for fixed-distance airborne time, kinetic energy per mass, and ideal total/static temperature ratio.
- Result: airborne time falls as `1/M`, while both high-level burden proxies grow as `M^2` under the frozen assumptions.
- Negative/limiting result: marginal time saved per incremental kinetic-energy proxy declines from about 0.390 for M0.85→M1 to 0.005 for M3→M5, roughly a 76-fold reduction.
- Preserved the result without inventing a scalar “practicality score” or selecting an optimum Mach number.
- Next hypothesis: empirical noise, passenger-environment, and actual energy-intensity evidence—not speed arithmetic—will decide whether any class above the historical Mach 2 anchor is practical.

## 2026-08-22 — Phase 4: passenger environment evidence audit

- Added a structured passenger-environment evidence table with cabin pressure, ventilation, cruise buffet, ride-comfort research, and crashworthiness categories.
- Added a validator/summary script and tests that prevent emergency crash limits from being reused as comfort thresholds.
- Result: public transport-aircraft sources provide quantitative cabin requirements, but this pass found zero supported high-speed-specific passenger comfort thresholds.
- Negative/evidence-gap result: the passenger gate cannot yet verify practicality above Mach 2; general certification requirements are necessary but insufficient.
- Next hypothesis: aerospace-medicine and ride-quality literature may supply transferable thresholds, but their applicability must be demonstrated rather than assumed.

## 2026-08-22 — Phase 5: noise and sonic-boom evidence maturity

- Added a dated noise evidence table separating current rules, proposals, prospective standards, developing standards, and empirical programmes.
- Added a validator that prevents proposed policy or ongoing research from being counted as a final practicality pass.
- Result: the U.S. prohibition remains current while a July 2026 NPRM proposes a noise-based replacement; ICAO en-route certification and NASA community-response evidence are still developing.
- Negative/evidence-maturity result: zero audited rows demonstrate a final high-speed pass threshold or commercial community acceptance.
- Next hypothesis: noise remains a binding practicality gate above Mach 1 until final standards and community-response evidence mature.

## 2026-08-22 — Phase 6: energy intensity and historical economics

- Added a fully sourced input ledger and tested passenger-distance energy/CO2 comparison.
- Compared the historical Concorde public-spec cruise proxy at 100%, 80%, and 60% occupancy with an EPA modern long-haul aggregate using common EIA/BTS fuel factors.
- Result: Concorde proxy is approximately 3.02x the modern long-haul energy and direct CO2 intensity at full occupancy, 3.77x at 80%, and 5.03x at 60%.
- Negative result: the historical Mach 2 anchor fails the selected modern energy-intensity benchmark even under favorable occupancy.
- Historical NASA economics evidence points in the same adverse direction but does not establish a current business case.
- Next hypothesis: the practical frontier may favor a lower supersonic speed class if empirical evidence can show meaningful time savings without the Mach 2 energy penalty.

## 2026-08-22 — Phase 7: bounded ideal thermal sensitivity

- Added a sourced standard-atmosphere input ledger and tested ideal total-temperature interval model.
- Result: the Mach 2 interval is approximately 390–451 K, Mach 3 is 607–701 K, and Mach 5 is 1,300–1,502 K under the frozen 216.65–250.35 K static range.
- The Mach 3 lower bound exceeds the Mach 2 upper bound across the full sensitivity interval.
- Limiting result: thermal burden changes regime faster than fixed-distance time benefit, while empirical serviceability evidence remains absent.
- Preserved strict boundaries: no wall temperature, heat flux, material, geometry, cooling, altitude, or trajectory inference.
- Next hypothesis: the Mach 2→3 thermal step may be a stronger practicality discriminator than its time saving.

## 2026-08-22 — Phase 8: airport compatibility evidence audit

- Added a structured audit of FAA/ICAO airport-design frameworks, rescue readiness, prospective noise standards, and historical Concorde integration.
- Result: mature evaluation frameworks exist, but six of seven audited rows require candidate characteristics.
- Evidence-gap result: zero current generic high-speed compatibility passes; historical Mach 2 service is selective precedent only.
- Preserved the non-actionable boundary by excluding dimensions, runway calculations, loads, rescue indices, airport assessments, and procedures.
- Next hypothesis: airport compatibility should remain a conjunctive gate rather than a speed-only scalar constraint.

## 2026-08-22 — Phase 9: cross-gate practicality matrix

- Added `practicality_matrix.csv` and a validating summary script that compare four abstract speed classes without assigning a weighted practicality score.
- Result: zero current practical passes; Mach 0.85 is retained as a current-service reference, Mach 2 as a historical anchor with one contradicted and one adverse gate, and Mach 3/Mach 5 as unresolved conceptual bins.
- Reproducibility gate: 27 unit tests pass, including explicit checks that Mach 2 energy/climate is contradicted versus the selected modern benchmark and that both faster conceptual bins lack a service anchor.
- Limitation: the matrix inherits the evidence maturity and comparability limits of each underlying audit; it does not prove impossibility or rank designs.
- Next hypothesis: an independently reproduced Mach 2 energy comparison is the highest-value next check before adding more speed bins.

## 2026-08-22 — Phase 10: independent energy reproduction

- Added a second implementation that re-reads the pinned energy inputs and compares all three load-factor rows with the committed output.
- Result: all rows pass at an absolute tolerance of `1e-9`; the energy gate's arithmetic is independently reproduced.
- Verification boundary: source accuracy, historical-versus-modern comparability, and all non-energy gates remain open.
- Next hypothesis: independently reproduce the bounded thermal sensitivity before extending the speed envelope.

## 2026-08-22 — Phase 11: independent thermal reproduction

- Added a separate thermal check that re-reads the frozen atmosphere interval and Mach bins and compares ratio and temperature bounds with the committed output.
- Result: all six Mach rows pass at an absolute tolerance of `1e-12`.
- Verification boundary: the check validates arithmetic only; ideal-gas, standard-atmosphere, and system-level serviceability limitations remain unresolved.
- Next hypothesis: independently reproduce the fixed-distance speed-tradeoff model to test the diminishing-return result before adding new physics.

## 2026-08-22 — Phase 12: independent speed-tradeoff reproduction

- Added a separate implementation of the fixed-distance time, normalized kinetic-energy, ideal temperature, and marginal-benefit calculations.
- Result: all six Mach-bin rows pass at an absolute tolerance of `1e-12`; the diminishing-return trend is independently reproduced.
- Verification boundary: this remains a dimensionless arithmetic screen and does not validate aerodynamic, propulsion, thermal, noise, passenger, or economic proxies.
- Next hypothesis: independently reproduce the airport-compatibility summary and then add source-integrity checks to the verification gate.

## 2026-08-22 — Phase 13: airport and source-register verification

- Added a separate airport-summary implementation and a static source-register integrity checker.
- Result: all seven airport metrics match exactly; the source register has unique IDs, nonblank required fields, valid HTTP(S) URLs, and ISO access dates.
- Verification boundary: these checks validate bookkeeping and provenance hygiene, not the truth or current applicability of external claims.
- Next hypothesis: add source hashes where practical and independently replicate one passenger/noise evidence claim before changing any practical-status label.

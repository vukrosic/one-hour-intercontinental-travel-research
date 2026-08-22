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

## 2026-08-22 — Phase 15: direct-page claim replication

- Independently reread four primary public pages covering current restriction, prospective FAA policy, NASA Quesst research, and EASA cabin requirements.
- Result: all four claims are recorded with explicit “what remains unproven” fields; zero high-speed practical passes are asserted.
- Consequence: noise and passenger-environment gates remain unresolved; no speed-matrix status changes are justified.
- Next hypothesis: add document hashes where practical and keep dated regulatory refreshes separate from stable mathematical checks.

## 2026-08-22 — Phase 16: metadata-only document hashes

- Retrieved four refreshed primary pages and stored byte counts plus SHA-256 digests without copying the full documents into the public repository.
- Result: the hash manifest passes registration, URL, date, byte-count, and digest-format checks.
- Limitation: a digest is provenance metadata, not source truth, legal force, or proof of applicability; dynamic pages still require refresh.
- Next hypothesis: keep hashes as audit anchors while expanding independent public replication only where a source claim can be checked without speculative design assumptions.

## 2026-08-22 — Phase 17: abstract acceleration sensitivity

- Added a bounded kinematic screen for symmetric acceleration/deceleration across four speed classes and three declared acceleration fractions.
- Result: the model reports phase-distance and time-overhead sensitivity without assigning any comfort or certification threshold.
- Boundary preserved: no trajectory, geometry, route, control law, seat design, or operating procedure is generated.
- Next hypothesis: independently reproduce the acceleration table before using it to frame passenger-environment literature questions.

## 2026-08-22 — Phase 18: independent acceleration reproduction

- Added a separate implementation of the 12-row abstract acceleration sensitivity table.
- Result: all rows reproduce within `1e-12`, including the accelerate/cruise/decelerate regime labels.
- Verification boundary: this is arithmetic verification only; no comfort, certification, or operational inference is added.
- Next hypothesis: use the acceleration sensitivity as a literature-indexing aid, not as a substitute for passenger ride-quality evidence.

## 2026-08-22 — Phase 19: energy-gap sensitivity

- Added an arithmetic restatement of the historical Mach 2 energy comparison as a required-reduction gap to the modern benchmark.
- Result: the implied direct-intensity reduction is 66.9% at 100% occupancy, 73.5% at 80%, and 80.1% at 60%.
- Boundary preserved: these are benchmark gaps, not design targets or remedies.
- Next hypothesis: pair this negative constraint with comparable empirical civil-supersonic data before attempting any broader economics inference.

## 2026-08-22 — Phase 20: practicality semantic guard

- Added a validator that enforces the matrix's conjunctive semantics and prevents unresolved, contradicted, or adverse rows from being labeled a practical pass.
- Result: all four current speed-class rows pass the semantic checks; no status changes were made.
- Boundary preserved: this is editorial/reproducibility infrastructure, not a weighted ranking or a physical feasibility proof.
- Next hypothesis: keep the guard in the test suite as new evidence rows are added.

## 2026-08-22 — Phase 21: passenger/noise literature map

- Added a transferability-aware map of six public passenger-ride, cabin-noise, certification, and community-noise sources.
- Result: the map reports zero high-speed practical passes and keeps historical empirical studies, current research, and certification guidance in separate categories.
- Refinement: NASA's 2026 air-taxi study is recorded as recent empirical work, while Quesst remains research in progress; the distinction avoids overstating the status of either.
- Limitation: no source supplies a universal speed-specific acceleration, vibration, or noise threshold.
- Next hypothesis: close-read the highest-transferability entries before introducing any passenger-environment threshold into a model.

## 2026-08-22 — Phase 22: ideal thermal gamma sensitivity

- Added a bounded robustness check that varies the ideal-gas parameter from `gamma=1.30` to `1.40` while keeping the existing generic static-temperature interval and Mach bins.
- Result: the Mach 3 lower ideal total-temperature bound remains above the Mach 2 upper bound in both scenarios (509.1 K > 400.6 K at gamma 1.30; 606.6 K > 450.6 K at gamma 1.40).
- Independent reproduction matches all 12 rows within the committed decimal representation; no practical-status label changes follow.
- Limitation: gamma sensitivity does not model real-gas chemistry, boundary layers, wall temperature, heat flux, materials, cooling, or serviceability.
- Next hypothesis: use comparable empirical high-speed environmental data to test whether the robust ideal ordering has any system-level correlate; until then, keep thermal status unresolved.

## 2026-08-22 — Phase 23: historical energy input stress test

- Added a deterministic ±10% one-factor and all-factor stress test around the pinned historical fuel-use, speed, seat-capacity, and modern-benchmark inputs.
- Result: the all-favorable stress still leaves the historical proxy at 2.04x, 2.55x, and 3.40x the modern direct-CO2 benchmark at 100%, 80%, and 60% occupancy respectively.
- Independent reproduction matches all 33 rows within `1e-12`; the energy-gate status remains unchanged.
- Limitation: the bracket is not a statistical uncertainty interval and does not repair historical-versus-modern data comparability or represent a future aircraft.
- Next hypothesis: prioritize comparable empirical civil-supersonic energy data; otherwise preserve the historical contradiction and avoid extrapolating it into a universal impossibility claim.

## 2026-08-22 — Phase 24: acceleration-adjusted time savings

- Added a derived 12-row comparison of speed-only versus acceleration-adjusted airborne-time savings using the existing abstract kinematic table.
- Result: at 0.05g, the speed-only saving falls from 58.3% to 55.7% for the Mach 2 historical bin, from 72.2% to 67.8% for Mach 3, and from 83.3% to 75.6% for Mach 5; all faster bins remain faster than the subsonic reference in the screen.
- Independent reproduction matches all 12 rows within `1e-12`.
- Limitation: the result uses declared constant-acceleration sensitivity inputs and cannot establish comfort, certification, or operational feasibility.
- Next hypothesis: connect the time-savings arithmetic to transferable passenger ride-quality evidence without inventing a universal acceleration threshold.

## 2026-08-22 — Phase 25: passenger ride-quality close read

- Close-read six public NASA/FAA records and added `PASSENGER_RIDE_CLOSE_READ.md` plus a structured extraction table.
- Result: historical large-transport and simulator studies demonstrate frequency-, axis-, and multi-factor passenger-response methods, but the close read finds zero demonstrated speed-specific comfort thresholds and zero high-speed practical passes.
- Independent bookkeeping reproduces all seven summary metrics; two records expose frequency ranges and three explicitly describe multi-factor or combined-stimulus evidence.
- Limitation: study-specific curves, pilot buffeting guidance, and recent subsonic air-taxi work cannot be promoted to a universal faster-aircraft serviceability limit.
- Next hypothesis: seek a public study with a demonstrated high-speed passenger-context bridge; otherwise retain passenger comfort as unresolved.

## 2026-08-22 — Phase 26: Mach-to-speed consistency audit

- Added an ideal-air speed-of-sound audit connecting the existing Mach/temperature screen to the nominal km/h acceleration bins.
- Result: all four nominal bins lie inside the derived intervals (870–971 km/h at Mach 0.85, 2,047–2,284 at Mach 2, 3,071–3,426 at Mach 3, and 5,118–5,709 at Mach 5).
- Kinematic propagation result: at 0.05g the Mach 5 phase-distance fraction spans 43.4–54.0% of the fixed yardstick, versus 6.9–8.6% for Mach 2; all tested rows remain accelerate–cruise–decelerate.
- Independent reproduction matches all 28 rows within `1e-12`; no practicality status changes follow.
- Limitation: ideal speed of sound and phase fractions are bookkeeping sensitivities, not real-gas, aircraft-flow, passenger-comfort, or operating models.
- Next hypothesis: use the consistent bins to compare any future public empirical evidence without mixing Mach and fixed-speed assumptions.

## 2026-08-22 — Phase 27: economics evidence close read

- Close-read four public NASA records and added `ECONOMICS_CLOSE_READ.md` with a structured extraction and independent summary check.
- Result: NASA's 1988 historical comparison reports approximately three-times Concorde fuel per seat-mile and approximately twice total operating cost versus comparable-era subsonic transports; NASA's current market-study page shows economic viability remains under investigation.
- The close read records one quantified historical row, one current research-status row, one qualitative synthesis row, zero current empirical business-case rows, and zero economic practical passes.
- Limitation: historical operating-cost ratios and programme pages do not establish current fares, utilization, profitability, reliability, or a universal future penalty.
- Next hypothesis: only comparable modern public cost data could move the economics gate; until then retain adverse historical evidence and unresolved future status.

## 2026-08-22 — Phase 28: noise evidence state guard

- Refreshed the official FAA, NASA Quesst, and ICAO pages and formalized the existing noise evidence state vocabulary in `NOISE_STATE_GUARD.md`.
- Added an explicit `high_speed_practical_pass` field to `noise_evidence.csv`; current, proposed, future-applicability, developing, research, and unresolved rows are all forced to remain `no` unless a future final-pass state is explicitly demonstrated.
- Result: 1 current-binding row, 3 prospective/development rows, 1 research-in-progress row, 1 unresolved row, 0 final passes, and 0 semantic errors; the independent state-count check matches all seven metrics.
- Limitation: state validation is not a legal opinion, noise model, or community-acceptance result.
- Next hypothesis: retain noise as a temporally unstable binding gate until final standards and empirical community-response evidence are available.

## 2026-08-22 — Phase 29: cabin-environment requirement close read

- Close-read EASA CS-25.841 pressurisation, EASA CS-25.831/AMC 25.831 ventilation, FAA AC 25-7D buffet guidance, and EASA 16g seat-crashworthiness evidence.
- Result: the structured table separates 2 normal-operation requirement rows, 3 failure/emergency rows, and 1 partial qualitative row; it contains zero high-speed-specific rows and zero comfort/serviceability passes.
- Independent bookkeeping reproduces all 7 summary metrics; all evidence remains general transport-category context rather than a high-speed proof.
- Limitation: public requirements do not establish a complete cabin thermal, acoustic, pressure-transient, or passenger-acceptance demonstration for faster aircraft.
- Next hypothesis: keep cabin environment unresolved until comparable high-speed empirical evidence bridges the applicability gap.

## 2026-08-22 — Phase 30: airport compatibility close read

- Close-read FAA AC 150/5300-13B, FAA runway classification tools, FAA ARFF, ICAO Annex 14, historical Concorde precedent, and prospective ICAO environmental standards.
- Result: four current framework rows, one historical precedent, one prospective-standard row, five rows requiring candidate characteristics, and zero current generic high-speed passes.
- Independent bookkeeping reproduces all six summary metrics; no airport-specific calculation or physical specification was added.
- Limitation: framework existence cannot close a candidate- and aerodrome-specific compatibility gap.
- Next hypothesis: preserve airport compatibility as a conjunctive gate and avoid generating candidate characteristics to force a pass.

## 2026-08-22 — Phase 31: historical passenger-service anchor close read

- Audited the historical-service premise against British Airways' Concorde record and NASA's Tu-144 development-history fact sheet.
- Correction: Concorde was not the only first-generation supersonic transport to reach passenger service. NASA records a separate Tu-144 airline service that ended after 102 passenger flights; the later Tu-144LL programme was research-only.
- Added `HISTORICAL_SERVICE_CLOSE_READ.md` and a structured, independently checked evidence ledger. It records two historical service anchors in one speed class (Mach 2), one research-only follow-on row, zero current-service rows, and zero current practical passes.
- Limitation: historical service duration and scale are not current certification, market, passenger-acceptance, energy, noise, or airport evidence; no route, design, or operational detail is inferred.
- Next hypothesis: retain Mach 2 as the highest directly service-anchored speed class while looking for comparable public evidence before adding or promoting any faster class.

## 2026-08-22 — Phase 32: current civilian high-speed programme status

- Audited NASA X-59, the FAA's XB-1 special flight authorization, Boom's public XB-1/Overture announcement, and the FAA's current proposed-rule pathway.
- Result: the structured close read separates one active research demonstrator, one experimental test authorization, one company-reported future airliner programme, and one proposed regulatory path; it records zero independently verified current passenger-service rows, zero passenger-certification rows, and zero practical passes.
- Independent bookkeeping reproduces all eight summary metrics; the FAA source explicitly distinguishes a test authorization from airworthiness and other certification requirements.
- Limitation: company claims, research milestones, and proposed rules are not interchangeable evidence and do not establish future delivery, reliability, economics, or passenger acceptance.
- Next hypothesis: seek an independent certification or revenue-service record for any new civil high-speed programme before promoting it beyond the research/proposal evidence state.

## 2026-08-22 — Phase 14: dated regulatory and noise-evidence refresh

- Refreshed FAA, NASA Quesst, and EASA public pages and recorded four claims with separate current, prospective, research-in-progress, and general-requirement states.
- Result: the refresh reports zero high-speed practical passes; current FAA restriction context, future policy direction, and NASA community-response research are not interchangeable evidence.
- Limitation: web-page observations are not legal advice or final certification evidence and require rechecking before reuse.
- Next hypothesis: add source hashes where practical and independently replicate one passenger/noise evidence claim before changing any practical-status label.

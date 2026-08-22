# Evidence gates for “fastest practical”

Status vocabulary:

- **Supported:** public evidence is sufficient for a bounded comparison.
- **Contradicted:** public evidence conflicts with the candidate claim.
- **Unresolved:** evidence, threshold, or comparability is insufficient.
- **Not tested:** no reproducible check has been completed.

| Gate | Current status | Evidence available | What would falsify practicality | Next reproducible check |
|---|---|---|---|---|
| Historical passenger service | Supported through Mach 2 | British Airways documents Concorde cruise at Mach 2 and extensive certification testing | No credible commercial-service precedent at the speed class | Preserve Mach 2 as the demonstrated historical anchor |
| Airborne-time benefit | Supported as arithmetic with diminishing returns | Fixed-distance comparison shows shorter airborne time with increasing reference speed; `speed_tradeoff.py` quantifies declining marginal benefit | Benefit too small relative to uncertainty or non-speed constraints | Independently reproduce the fixed-distance calculation |
| Passenger acceleration/ride comfort | Unresolved; category boundaries documented | FAA cruise-buffet guidance and NASA comfort research do not establish a universal high-speed passenger threshold; emergency 16 g seat evidence is explicitly excluded | Public comfort/safety thresholds cannot be met across normal and off-normal conditions | Search aerospace-medicine and ride-quality literature for transferable thresholds |
| Cabin environment | General requirements supported; high-speed applicability unresolved | EASA CS-25 provides normal/failure cabin-pressure limits and a fresh-air minimum | No credible evidence for a habitable, certifiable cabin environment at the speed class | Compare speed-agnostic requirements with empirical high-speed cabin evidence |
| Thermal environment | Unresolved; dimensionless and bounded-temperature trends supported | NASA isentropic relation plus standard-atmosphere sensitivity gives ideal intervals of 390–451 K at Mach 2 and 607–701 K at Mach 3 | Public empirical evidence cannot connect the ideal proxy to passenger-aircraft serviceability | Seek system-level empirical environmental evidence; do not select materials or protection systems |
| Airport/community noise | Unresolved, currently binding in U.S. overland context, and temporally unstable | Current FAA prohibition, July 2026 NPRM, prospective ICAO standards, developing en-route scheme, and NASA Quesst are separated in `noise_evidence.csv` | No final high-speed pass threshold or demonstrated community acceptance | Refresh dated regulatory snapshot and track final-rule/community-data maturity |
| Energy and climate | Historical Mach 2 anchor contradicted versus selected modern long-haul benchmark | Concorde public-spec proxy is about 3.02x modern long-haul direct energy/CO2 at 100% occupancy and worsens at lower load factor | Passenger-distance energy remains materially above a declared benchmark under realistic occupancy | Seek empirical modern civil-supersonic energy data; do not extrapolate a design |
| Economics | Historical evidence adverse; future case unresolved | NASA historical work identifies operating economics as central and roughly twice similar-technology subsonic total operating cost | Required fare/utilization/load-factor range has no credible current market envelope | Reconstruct aggregate cost sensitivities only when public inputs are comparable |
| Airport compatibility | Not tested | Public certification/noise evidence implies integration constraints | Existing-airport compatibility cannot be shown at a high level | Qualitative checklist from public standards; no procedures |
| Independent verification | Not tested | Current models are internally reproducible but not independently replicated | Results cannot be reproduced from pinned assumptions and sources | Add tests, source hashes where possible, and an independent calculation |

## Current synthesis

Mach 2 is the fastest speed class in this repository with direct historical scheduled passenger-service evidence. Speeds above Mach 2 remain conceptual comparison bins, not practical candidates, until the thermal, noise, passenger, energy/economics, airport, and verification gates have credible public evidence. This is a status statement, not a claim that Mach 2 is optimal or that higher speeds are impossible.

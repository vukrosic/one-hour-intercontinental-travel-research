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
| Thermal environment | Unresolved; dimensionless trend supported | NASA isentropic-flow relation supports total/static temperature ratio scaling with Mach; tested envelope rises nonlinearly | Temperature/load proxies cross public serviceability evidence with no supported mitigation pathway | Compare normalized proxy with public empirical envelopes; do not select materials |
| Airport/community noise | Unresolved and likely binding | ICAO maintains aircraft-noise standards and is developing supersonic airport/en-route noise work; NASA Quesst is collecting community evidence | No path to current/future certification and public acceptability | Build a regulatory/source matrix by noise category |
| Energy and climate | Not tested | ICAO treats CO2, noise, and emissions as interdependent standards | Passenger-km energy or emissions remain outside a declared benchmark envelope | Add a public-data energy-intensity comparison with uncertainty |
| Economics | Unresolved | NASA historical work identifies operating economics as a central supersonic-transport constraint | Required fare/utilization/load-factor range has no credible market envelope | Reconstruct only aggregate historical comparisons |
| Airport compatibility | Not tested | Public certification/noise evidence implies integration constraints | Existing-airport compatibility cannot be shown at a high level | Qualitative checklist from public standards; no procedures |
| Independent verification | Not tested | Current models are internally reproducible but not independently replicated | Results cannot be reproduced from pinned assumptions and sources | Add tests, source hashes where possible, and an independent calculation |

## Current synthesis

Mach 2 is the fastest speed class in this repository with direct historical scheduled passenger-service evidence. Speeds above Mach 2 remain conceptual comparison bins, not practical candidates, until the thermal, noise, passenger, energy/economics, airport, and verification gates have credible public evidence. This is a status statement, not a claim that Mach 2 is optimal or that higher speeds are impossible.

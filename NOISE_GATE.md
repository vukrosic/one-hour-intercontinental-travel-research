# Noise and sonic-boom evidence gate

## Question

Does current public evidence support noise certification and community acceptability for a practical civilian passenger speed class above Mach 1?

## Method

`noise_evidence.csv` separates five evidence states that must not be conflated:

1. current binding rules;
2. proposed rules that are not final;
3. adopted standards with future applicability;
4. standards still in development; and
5. empirical research programmes still collecting evidence.

`noise_evidence_summary.py` validates the table and prevents a proposed threshold or ongoing programme from being counted as a final high-speed pass criterion.

## Current evidence snapshot (2026-08-22)

- FAA states that civil flight above Mach 1 over U.S. land remains prohibited except under special authorization.
- A July 2026 FAA proposed rule would replace the general speed-based prohibition with a performance-based interim en-route framework using a proposed 0.11 psf surface-overpressure limit. It is a proposal, not current permission or a final finding of community acceptance.
- ICAO has advanced landing-and-takeoff noise standards for future supersonic aircraft, while its CAEP/14 work programme continues development of an en-route sonic-boom certification scheme.
- NASA Quesst is conducting flight research before community surveys and future delivery of response data to regulators.

## Reproducible result

The current audit has six rows. It contains one current binding constraint, one proposal, one developing international en-route standard, one empirical programme in progress, one prospective landing/takeoff standards row, and one unresolved cabin-noise gap. It contains **zero final high-speed pass-threshold or demonstrated commercial-acceptance rows**.

## Conclusion

The noise gate is unresolved for practical civilian flight above Mach 1. It is also temporally unstable: the U.S. regulatory framework is actively changing. The existence of a proposed rule, an adopted future standard, or a successful research-aircraft flight cannot yet be treated as proof of routine passenger-aircraft acceptability.

This conclusion does not assert that acceptable supersonic noise is impossible. It says the required final regulatory and community evidence is not yet present in the audited public record.

## Limitations

- This audit is a dated regulatory/evidence snapshot and must be refreshed before relying on it later.
- It does not model sonic-boom generation, propagation, or mitigation.
- It does not propose compliance methods, aircraft shaping, routes, or operating procedures.
- Cabin noise, occupational exposure, airport-specific impacts, and international jurisdiction differences need separate passes.
- A proposed numerical limit is recorded only as public policy evidence, not as a design target.

## Next hypothesis

Noise is likely to remain a binding practicality gate above Mach 1 until final en-route standards and community-response evidence exist. The next safe analysis should quantify evidence maturity over time or audit actual passenger-kilometre energy intensity; it should not attempt to design a low-boom aircraft.

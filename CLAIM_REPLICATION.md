# Direct-page claim replication

## Purpose

This small audit independently rereads four primary public pages already listed in the source register. It records what each page directly supports and the practical claim it does **not** support. The goal is to prevent a current rule, a future policy direction, an active research programme, or a general cabin requirement from being promoted into a high-speed passenger-aircraft pass.

## Method and result

Each row in `claim_replication.csv` was checked by direct page reading on 2026-08-22. `claim_replication_summary.py` validates four unique claims, all using the same explicit method, and reports zero high-speed practical passes.

The replicated record is:

- FAA SFA page: current overland restriction and special-flight-authorization context.
- FAA Supersonic Flight overview: prospective noise-based policy direction, not a final rule.
- NASA Quesst mission page: planned community-response measurements, not commercial certification.
- EASA CS-25.841: general pressurised-cabin requirements, not high-speed serviceability.

## Limitations

- This is a dated direct-page reading, not a legal opinion, formal certification review, or automated source fetch.
- The page text can change; access dates and source URLs are part of the record.
- No row supplies a route, operating procedure, aircraft design, or compliance recipe.

## Consequence for the research question

The replication supports keeping the noise and passenger-environment gates unresolved. It does not justify changing any practical-status label in the speed matrix.

# Current civilian high-speed programme close read

## Question

Has any present-day civilian high-speed programme crossed the evidence
boundary from research or proposal into independently verifiable passenger
service?

The bounded answer is **no in this ledger**. NASA's X-59 is an active research
demonstrator. The FAA's XB-1 document is an experimental-test authorization
and explicitly says it does not establish airworthiness or other certification
requirements. Boom reports a future Overture airliner programme, but that is a
company claim rather than a passenger-service record. The FAA's current
supersonic pathway is still described through proposed and future rulemaking.

## Evidence states

| Record | Extracted claim | Evidence state |
|---|---|---|
| NASA X-59 / Quesst (`NASA_X59_SUPERSONIC_2026`) | NASA reports a 2026 supersonic flight milestone for the experimental X-59 and describes later community-response work to inform future standards. | Active research demonstrator; no passenger-service evidence. |
| FAA XB-1 authorization (`FAA_XB1_SFA_2024`) | The FAA authorization covers supersonic testing of the XB-1 experimental aircraft and says it does not establish airworthiness or other certification requirements. | Experimental test authorization; no passenger certification. |
| Boom Overture (`BOOM_XB1_2025`) | Boom reports that the XB-1 demonstrator informs its future Overture airliner programme and describes future commercial passenger ambitions. | Company-reported future airliner; no independent service record in this close read. |
| FAA regulatory path (`FAA_SUPERSONIC_OVERVIEW`) | The FAA describes an initial proposed rule and a future noise-threshold rule as steps toward commercial supersonic flight. | Proposed regulatory path; not a final rule or service approval. |

The structured extraction is in
[`current_programme_close_read.csv`](current_programme_close_read.csv).
It contains one row in each of four evidence states, zero independently
verified current passenger-service rows, zero passenger-certification rows, and
zero high-speed practical passes.

## Reproducibility

```text
python3 current_programme_close_read.py
python3 current_programme_close_read_independent_check.py
```

The first command writes
[`current_programme_close_read_summary.csv`](current_programme_close_read_summary.csv).
The independent implementation writes
[`current_programme_close_read_independent_check.csv`](current_programme_close_read_independent_check.csv)
and reproduces all eight summary metrics.

## Interpretation and limits

- A flying demonstrator is meaningful evidence of a test programme, not of
  passenger-airliner certification, economics, or service reliability.
- A special flight authorization is a bounded research permission, not a
  blanket operating approval and not an airworthiness certificate.
- Company-reported orders, ambitions, or technology milestones are retained as
  programme evidence but are not promoted to independent passenger service.
- Proposed rules and policy pages describe a pathway, not a final legal or
  technical pass.
- This close read intentionally omits vehicle specifications, propulsion
  recipes, construction, routes, and operational guidance.
- No practicality-matrix status changes follow. Mach 2 remains the only
  directly service-anchored speed class; present-day programmes remain
  research/proposal evidence until independently verified passenger service
  and certification records appear.

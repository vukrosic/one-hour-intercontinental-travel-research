# Cabin-environment requirement close read

## Question

What do public transport-aircraft cabin requirements establish, and what
remains unproven for a faster civilian passenger aircraft?

The close read separates normal-operation requirements, probable-failure
requirements, qualitative ride guidance, and emergency crashworthiness. The
result is **zero high-speed-specific serviceability passes**.

## Extracted evidence

| Record | Requirement or criterion | What it supports | What remains unproven |
|---|---|---|---|
| EASA CS-25.841 normal | Cabin pressure altitude no more than 8,000 ft under normal conditions. | A general occupied-cabin certification requirement. | High-speed cabin feasibility or passenger comfort. |
| EASA CS-25.841 failure | No more than 15,000 ft after a reasonably probable pressurisation failure when certification above 25,000 ft is requested. | A failure-case safety requirement. | Normal-operation comfort or a complete high-speed cabin demonstration. |
| EASA CS-25.831 normal | At least 0.25 kg fresh air/minute/occupant plus reasonable passenger-comfort language. | A ventilation and air-quality baseline. | Thermal, acoustic, pressure-transient, and high-speed serviceability evidence. |
| EASA AMC 25.831 failure | Guidance of at least 0.18 kg/minute/person for periods over five minutes under probable failure conditions, subject to air quality. | Failure-case ventilation context. | A normal comfort threshold or high-speed pass. |
| FAA AC 25-7D | No perceptible cruise buffeting; any acceleration proxy must correlate with pilot assessment. | A transport-category certification-evidence category. | A universal passenger acceleration or high-speed cabin threshold. |
| EASA 16g seat opinion | Dynamic seat testing in survivable emergency-landing context. | Emergency injury-protection evidence. | Normal-flight comfort, ride quality, or cabin serviceability. |

The structured extraction is in [`cabin_environment_close_read.csv`](cabin_environment_close_read.csv).
It contains two normal-operation requirement rows, three failure/emergency rows,
one partial qualitative row, zero high-speed-specific rows, and zero comfort or
serviceability passes.

## Reproducibility

```text
python3 cabin_environment_close_read.py
python3 cabin_environment_independent_check.py
```

The first command writes [`cabin_environment_close_read_summary.csv`](cabin_environment_close_read_summary.csv).
The independent bookkeeping implementation writes
[`cabin_environment_independent_check.csv`](cabin_environment_independent_check.csv)
and reproduces all seven summary metrics.

## Interpretation and limits

- General transport requirements are necessary evidence categories, not proof
  that an unspecified high-speed aircraft can satisfy them.
- Failure and emergency rows must not be reused as normal passenger-comfort
  limits.
- The close read does not select a cabin design, pressure system, insulation,
  material, operating procedure, or emergency procedure.
- The cabin-environment gate remains unresolved above the historical Mach 2
  anchor; no practicality-matrix status changes follow.

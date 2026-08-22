# Current civilian speed-reference close read

## Question

What should the repository use as the current subsonic reference when it
separates airline service from business aviation?

The bounded answer is not one universal number. Boeing's 787 provides a
current airline-service reference at Mach 0.85. Bombardier's Global 7500
provides a higher, certified in-service business-aviation reference at Mach
0.925. Gulfstream's current G700 page publishes Mach 0.935 maximum operating
Mach, but that page alone is a manufacturer performance claim rather than an
independent certification/service record. The repository should therefore keep
the airline baseline at Mach 0.85, add a certified business-aviation anchor at
Mach 0.925, and retain Mach 0.935 as a conditional marketed upper reference.

## Primary evidence

| Record | Extracted claim | Evidence state |
|---|---|---|
| Boeing 787 (`BOEING_787_2026` + `Boeing_787_SPEED_2024`) | Boeing's current fleet page supports the service context, while a separate airport-characteristics record publishes Mach 0.85 as the commercial-transport cruise reference. | Current airline-service baseline with explicit split provenance. |
| Bombardier Global 7500 (`BOMBARDIER_GLOBAL7500_EPD` + `TCCA_G7500_2025`) | Bombardier's public environmental declaration supplies the 0.925 Mach top-speed record, while Transport Canada's 2025 operational-evaluation report identifies the Global 7500 / BD-700-2A12 type certificate A-177. | Current certified business-aviation anchor with separate regulator provenance. |
| Gulfstream G700 (`GULFSTREAM_G700_2026`) | Gulfstream's current product page lists Mach 0.935 maximum operating Mach and Mach 0.90 high-speed cruise. | Manufacturer-only performance claim; service/certification not independently verified in this close read. |

The structured extraction is in
[`current_civilian_speed_close_read.csv`](current_civilian_speed_close_read.csv).
It records one airline-service row, one certified business-aviation row, one
manufacturer-only row, a highest published subsonic Mach of 0.935, a highest
service-anchored Mach of 0.925, and zero speed-frontier practical passes.

## Reproducibility

```text
python3 current_civilian_speed_close_read.py
python3 current_civilian_speed_close_read_independent_check.py
```

The first command writes
[`current_civilian_speed_close_read_summary.csv`](current_civilian_speed_close_read_summary.csv).
The independent implementation writes
[`current_civilian_speed_close_read_independent_check.csv`](current_civilian_speed_close_read_independent_check.csv)
and reproduces all eight summary metrics.

## Interpretation and limits

- “Maximum operating Mach” and “top speed” are not identical to normal cruise
  speed, passenger comfort, economics, or route capability.
- Business-aviation service is a valid civilian passenger reference but is not
  interchangeable with a high-capacity airline benchmark.
- Manufacturer product pages are retained as claims with explicit evidence
  status; they are not silently promoted to independent certification or
  service evidence.
- The close read does not rank aircraft, infer a universal fastest practical
  airplane, or add a design/operations model.
- No practicality-matrix status changes follow. This phase refines the current
  subsonic references while the supersonic Mach 2 anchor and unresolved gates
  remain unchanged.

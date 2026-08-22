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
| Boeing 787 (`BOEING_787_2026`) | Boeing describes an operating passenger fleet and publishes Mach 0.85 as a commercial-transport cruise reference. | Current airline-service baseline. |
| Bombardier Global 7500 (`BOMBARDIER_GLOBAL7500_EPD`) | Bombardier's public environmental declaration lists a type certificate, 2018 certification and entry into service, and a 0.925 Mach top speed. | Current certified business-aviation anchor. |
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

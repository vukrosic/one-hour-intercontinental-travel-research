# Current civilian speed-reference close read

## Question

What should the repository use as the current subsonic reference when it
separates airline service from business aviation?

The bounded answer is not one universal number. Boeing's 787 provides a
current airline-service reference at Mach 0.85. Bombardier's Global 7500
provides a higher, certified in-service business-aviation reference at Mach
0.925. The Gulfstream G700 record now has the same evidence separation: its
Mach 0.935 maximum-operating figure comes from the Gulfstream performance
record, while FAA/EASA type-certificate records and Qatar Executive's delivery
and charter-service record support a current certified in-service status. A
newer refresh also finds Bombardier's Global 8000: EASA type-certificate data,
Bombardier's certification announcements, and a first-delivery record support a
current certified in-service Mach 0.95 reference. The repository should
therefore keep Mach 0.85 as the airline baseline and retain Mach 0.925, Mach
0.935, and Mach 0.95 as distinct certified business-aviation references,
without treating any of them as a universal airline or practicality winner.

## Primary evidence

| Record | Extracted claim | Evidence state |
|---|---|---|
| Boeing 787 (`BOEING_787_2026` + `Boeing_787_SPEED_2024`) | Boeing's current fleet page supports the service context, while a separate airport-characteristics record publishes Mach 0.85 as the commercial-transport cruise reference. | Current airline-service baseline with explicit split provenance. |
| Bombardier Global 7500 (`BOMBARDIER_GLOBAL7500_EPD` + `TCCA_G7500_2025`) | Bombardier's public environmental declaration supplies the 0.925 Mach top-speed record, while Transport Canada's 2025 operational-evaluation report identifies the Global 7500 / BD-700-2A12 type certificate A-177. | Current certified business-aviation anchor with separate regulator provenance. |
| Gulfstream G700 (`QATAR_EXECUTIVE_G700_SERVICE_2024` + `GULFSTREAM_G700_2026` + `FAA_G700_TCDS_2025`) | The performance record lists Mach 0.935 maximum operating Mach and Mach 0.90 high-speed cruise; FAA/EASA records support certification and Qatar Executive records delivery and planned charter service. | Current certified in-service business-aviation reference, with performance, certification, and service roles kept separate. |
| Bombardier Global 8000 (`BOMBARDIER_GLOBAL8000_SERVICE_2026` + `BOMBARDIER_GLOBAL8000_SPEED_2026` + `EASA_GLOBAL8000_TCDS_2026`) | Bombardier's public record lists Mach 0.95 top speed; EASA's TCDS identifies the Global 8000 designation, while Bombardier records certification and first delivery. | Current certified in-service business-aviation reference; top speed is not normal cruise or an airline-capacity claim. |

The structured extraction is in
[`current_civilian_speed_close_read.csv`](current_civilian_speed_close_read.csv).
It records one airline-service row, three certified in-service business-aviation
rows, a highest published and service-anchored subsonic Mach of 0.95, and zero
speed-frontier practical passes.

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
- Manufacturer product pages remain the performance source for the G700 Mach
  value; the separate regulator and operator records are what support its
  certification/service state.
- The close read does not rank aircraft, infer a universal fastest practical
  airplane, or add a design/operations model.
- No practicality-matrix status changes follow. This phase adds the Global 8000
  as a newer certified in-service reference above the G700, while the
  supersonic Mach 2 anchor and unresolved gates remain unchanged.

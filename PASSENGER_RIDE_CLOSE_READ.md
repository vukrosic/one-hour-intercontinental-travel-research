# Passenger ride-quality close read

## Scope

This checkpoint close-reads six public records already indexed in the
repository's passenger/noise map. It asks a narrow question: do the records
provide a transferable, speed-specific passenger comfort threshold for a faster
civilian passenger airplane?

The answer is **no**. The records show that passenger response can be measured
and modelled, but their contexts, variables, and criteria do not constitute a
current high-speed serviceability or certification pass.

## Extracted evidence

| Record | What is measured or described | Transferability conclusion |
|---|---|---|
| NASA 1972 large-transport study (`NASA_RIDE_QUALITY_SUPERSONIC_1973`) | Passenger reaction to vertical and lateral vibration in a 0.20–7.0 Hz study; reported sensitivity varies with frequency and axis. | Relevant historical transport context, but no universal current high-speed threshold. |
| NASA 1975 vibration simulator (`NASA_VIBRATION_COMFORT_1976`) | Three-degree-of-freedom, multi-frequency/multi-axis simulator work with equal-discomfort curves from 1–30 Hz. | Supplies a measurement method and frequency dependence, not a serviceability limit. |
| NASA transport-aircraft ride-quality study (`NASA_RIDE_QUALITY_TRANSPORT_1979`) | Quantitative relationships include motion, noise, temperature, pressure, and seating. | Supports multi-factor analysis; does not validate a faster-aircraft threshold. |
| NASA interior-noise/vibration study (`NASA_NOISE_VIBRATION_1979`) | Combined cabin noise and multi-axis vibration response in a helicopter context. | Demonstrates interaction effects, but transfer to supersonic transport is low. |
| FAA AC 25-7D (`FAA_AC25_7D`) | Transport-category cruise-buffeting guidance, including pilot-assessment correlation. | Certification context only; not a passenger comfort threshold. |
| NASA 2026 air-taxi study (`NASA_RIDE_COMFORT_2026`) | Recent empirical work on passenger response to large and sudden motion profiles. | Useful current method, but subsonic air-taxi context and no high-speed threshold. |

The structured extraction is in [`passenger_ride_close_read.csv`](passenger_ride_close_read.csv).
Its summary reports six close reads, two explicit frequency-range records, three
multi-factor records, five medium/low-transferability records, zero demonstrated
speed-specific thresholds, and zero high-speed practical passes.

## Reproducibility

```text
python3 passenger_ride_close_read.py
python3 passenger_ride_close_read_independent_check.py
```

The first command writes [`passenger_ride_close_read_summary.csv`](passenger_ride_close_read_summary.csv).
The independent bookkeeping implementation writes
[`passenger_ride_close_read_independent_check.csv`](passenger_ride_close_read_independent_check.csv)
and reproduces all seven summary metrics.

## Boundaries

- Frequency ranges and study descriptions are evidence metadata, not proposed
  operating limits.
- “Study-specific” and “model-specific” criteria are not universal passenger
  acceptance thresholds.
- No acceleration, vibration, noise, seating, cabin, or control-system design
  is inferred.
- No practicality status changes follow. The passenger-environment gate remains
  unresolved above the historical Mach 2 anchor.

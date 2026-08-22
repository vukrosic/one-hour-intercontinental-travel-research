# Historical passenger-service close read

## Question

What direct public evidence exists for civilian passenger service at the upper
end of the repository's speed comparison?

The bounded answer is that the Mach 2 class has two distinct first-generation
airline-passenger precedents, but they are not equivalent. British Airways
documents Concorde as a large, long-lived supersonic service. NASA documents a
much shorter Tu-144 passenger service that ended after 102 passenger flights.
The later Tu-144LL programme was research-only and must not be counted as a
passenger-service anchor. No row establishes a current practical pass.

## Primary evidence

| Record | Extracted claim | Evidence state |
|---|---|---|
| British Airways Concorde history (`BA_CONCORDE`) | Just under 50,000 flights and more than 2.5 million passengers were flown supersonically; cruise was listed at 1,350 mph / 2,160 km/h / Mach 2; service ended in October 2003. | Sustained historical scheduled-service evidence; not current. |
| NASA Tu-144 history (`NASA_TU144_HISTORY_2002`) | NASA calls Tu-144 one of only two first-generation SSTs to enter production and commercial service; passenger service began in 1977 and ended in 1978 after 102 passenger flights. | Limited historical airline-passenger evidence; not a durable practical pass. |
| NASA Tu-144LL history (`NASA_TU144_HISTORY_2002`) | The later Tu-144LL was a modified former jetliner used as a flying laboratory in a 1996–1999 research programme. | Research-only evidence; excluded from passenger-service counts. |

The structured extraction is in
[`historical_service_close_read.csv`](historical_service_close_read.csv).
It records two historical service anchors in one speed class (Mach 2), one
research-only follow-on record, zero current-service rows, and zero current
practical passes.

## Reproducibility

```text
python3 historical_service_close_read.py
python3 historical_service_close_read_independent_check.py
```

The first command writes
[`historical_service_close_read_summary.csv`](historical_service_close_read_summary.csv).
The independent implementation writes
[`historical_service_close_read_independent_check.csv`](historical_service_close_read_independent_check.csv)
and reproduces all eight summary metrics.

## Interpretation and limits

- The evidence changes the wording from “Concorde was the only service
  precedent” to “Mach 2 is the only speed class with direct historical
  passenger-service precedent in this ledger.”
- Concorde's scale and duration are stronger practical evidence than the
  Tu-144's limited service, but neither establishes present-day feasibility.
- A service record does not close the passenger-comfort, thermal, noise,
  energy, economics, airport, or certification gates.
- The close read deliberately omits route planning, aircraft specifications,
  propulsion details, construction, and operational guidance.
- The historical-service gate remains supported through Mach 2 only; Mach 3
  and Mach 5 remain conceptual bins without a direct passenger-service anchor.

# Passenger environment and comfort evidence gate

## Question

Do public transport-aircraft rules and studies provide thresholds sufficient to judge passenger safety and comfort for speed classes above the historical Mach 2 passenger-service anchor?

## Method

`passenger_environment.csv` separates:

- normal-operation cabin requirements;
- failure and emergency safety requirements;
- qualitative cruise ride criteria;
- passenger-comfort research; and
- evidence that is specific to high-speed passenger flight.

`passenger_evidence_summary.py` validates required fields, summarizes coverage, and explicitly prevents an emergency crashworthiness acceleration from being counted as a normal-flight comfort threshold.

## Evidence found

1. EASA CS 25.841 gives quantitative cabin-pressure-altitude requirements: no more than 8,000 ft under normal conditions and no more than 15,000 ft after a reasonably probable pressurisation failure when certification above 25,000 ft is requested.
2. EASA CS 25.831 requires at least 0.25 kg of fresh air per minute per occupant during normal operations and uses “reasonable passenger comfort” language.
3. FAA AC 25-7D says no perceptible buffeting is permitted in cruise configuration. It notes that approximately ±0.05 g has been used in some buffet-onset evaluations, but explicitly says the appropriate value varies and must be correlated with pilot assessment.
4. NASA describes passenger ride-comfort thresholds as an active empirical research topic.
5. The 16 g dynamic-seat test belongs to emergency crashworthiness. It is not evidence for acceptable normal-flight acceleration.

## Reproducible result

The current table contains six evidence rows: three supported normal/failure cabin requirements, one partial qualitative cruise-buffet criterion, one unresolved passenger-comfort research row, and one emergency safety value explicitly excluded from comfort reasoning. It contains **zero supported high-speed-specific passenger comfort thresholds**.

## Conclusion

The passenger-environment gate is not failed, but it is unresolved above Mach 2. Existing public rules provide important cabin pressure, ventilation, and cruise-buffet constraints, yet they do not supply a single transferable acceleration/ride-quality threshold that proves passenger comfort for a faster civilian aircraft. Treating crashworthiness values as comfort limits would be a category error.

## Limitations

- This pass does not exhaust aerospace medicine, ISO ride-quality, decompression, vibration-frequency, noise-in-cabin, or accessibility literature.
- Requirements are not the same as observed passenger acceptance.
- Most sources are speed-agnostic; applicability to a faster speed class must be demonstrated, not assumed.
- No cabin design, pressure-system design, or operating procedure is inferred.

## Next hypothesis

A practical speed class above Mach 2 would need empirical ride-quality and cabin-environment evidence specific enough to bridge the gap between general certification requirements and actual passenger acceptance. The next passenger-focused pass should test whether aerospace-medicine and ride-quality literature supplies such transferable evidence.

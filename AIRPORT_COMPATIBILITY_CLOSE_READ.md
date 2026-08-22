# Airport-compatibility close read

## Question

What does public airport evidence establish about integrating a faster civilian
passenger airplane with existing civil-airport systems?

The close read finds that public frameworks exist, but their application is
candidate- and aerodrome-specific. Historical Concorde service is selective
precedent. No source supplies a current generic high-speed compatibility pass.

## Extracted evidence

| Record | Evidence | Boundary |
|---|---|---|
| FAA AC 150/5300-13B | Active standards and recommendations cover geometric layout and engineering design of civil-airport facilities. | Applying them requires aircraft and airport characteristics; the repository does not calculate them. |
| FAA runway design matrix | Current tool aligns with AC 150/5300-13B and uses aircraft approach/design classifications. | A speed class alone is not an aircraft classification or a compatibility result. |
| ICAO Annex 14 | Reference-code logic organizes aerodrome specifications; more-demanding future aircraft are left to appropriate authorities at each aerodrome. | This explicitly prevents a universal “future speed class passes existing airports” inference. |
| FAA ARFF | Part 139 airports must provide ARFF during applicable air-carrier operations and use index determinations. | Emergency-response compatibility depends on candidate and airport evidence. |
| Concorde history | Scheduled passenger service demonstrates selective historical airport integration through 2003. | Historical precedent is not current or universal compatibility. |
| ICAO 2026 standards | Prospective environmental standards include next-generation supersonic aircraft with future applicability. | A future environmental standard is not a specific aircraft-airport approval. |

The structured extraction is in [`airport_compatibility_close_read.csv`](airport_compatibility_close_read.csv).
It contains four current framework rows, one historical precedent, one
prospective-standard row, five rows requiring candidate characteristics, and zero
current generic high-speed passes.

## Reproducibility

```text
python3 airport_compatibility_close_read.py
python3 airport_compatibility_close_read_independent_check.py
```

The first command writes [`airport_compatibility_close_read_summary.csv`](airport_compatibility_close_read_summary.csv).
The independent implementation writes
[`airport_compatibility_close_read_independent_check.csv`](airport_compatibility_close_read_independent_check.csv)
and reproduces all six metrics.

## Limits

- No airport, runway, taxiway, pavement, gate, rescue, noise-contour, or
  airspace assessment is performed.
- No dimensions, loads, procedures, or infrastructure modifications are
  inferred.
- Framework existence is not compatibility proof.
- The airport gate remains unresolved for future speed classes; no
  practicality-matrix status changes follow.

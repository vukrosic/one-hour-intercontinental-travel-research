# Airport compatibility evidence gate

## Question

Does public evidence show that a civilian passenger airplane faster than the historical Mach 2 anchor can integrate with existing major-airport infrastructure?

## Method

`airport_compatibility.csv` audits high-level evidence across:

- runway, taxiway, and apron design frameworks;
- aerodrome reference classification;
- rescue and firefighting readiness;
- airport noise standards;
- historical scheduled-service precedent; and
- generic future high-speed compatibility.

The audit records whether each determination requires candidate aircraft characteristics. It intentionally does not calculate or propose dimensions, pavement loads, runway requirements, rescue indices, gate layouts, or procedures.

## Evidence found

- FAA AC 150/5300-13B provides current standards and recommendations for civil-airport runway, taxiway, apron, and related geometric design. Its reference system uses aircraft categories and design groups.
- ICAO Annex 14 uses an aerodrome reference-code system and explicitly notes that more demanding future aircraft may require evaluation by appropriate authorities at particular aerodromes.
- FAA Part 139 airports must provide aircraft rescue and firefighting services during applicable air-carrier operations.
- ICAO has adopted prospective environmental standards that include next-generation supersonic aircraft.
- Concorde’s scheduled service is historical evidence that a Mach 2 passenger aircraft could be integrated at selected major civil airports.

## Reproducible result

The audit contains seven rows: four established compatibility frameworks, one historical-service precedent, one prospective standard, and one explicit evidence gap. Six rows require candidate characteristics. It contains **zero current generic high-speed compatibility passes**.

The source close read in [AIRPORT_COMPATIBILITY_CLOSE_READ.md](AIRPORT_COMPATIBILITY_CLOSE_READ.md)
rechecks four framework records, one historical precedent, and one prospective
standard. It independently reports five rows requiring candidate characteristics
and zero generic high-speed passes.

## Conclusion

Airport compatibility is unresolved for any future speed class above Mach 2. The standards framework exists, but speed alone is insufficient to evaluate compatibility. Historical Concorde service proves selective integration was possible; it does not prove that an unspecified faster aircraft would be compatible with existing airports today.

This is an important boundary result: the evidence gap cannot be closed responsibly without candidate and airport characteristics, and this repository will not generate a physical aircraft design to fill it.

## Limitations

- This audit does not assess individual airports.
- It does not calculate runway length, pavement strength, geometry, rescue index, gate clearance, jet effects, or noise contours.
- Historical operations occurred under different fleets, standards, economics, and community expectations.
- Published frameworks can establish evaluation categories without proving compatibility.

## Next hypothesis

Airport compatibility is unlikely to set a universal maximum speed by itself. Instead, it acts as a conjunctive practicality gate: a candidate speed class remains unverified unless credible public evidence demonstrates compatibility across geometry, loads, emergency response, and noise without bespoke infrastructure assumptions.

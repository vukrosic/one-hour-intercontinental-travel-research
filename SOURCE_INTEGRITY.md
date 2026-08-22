# Public-source register integrity

`source_integrity_check.py` performs static hygiene checks on `fast_aircraft_sources.csv`: required fields are nonblank, source IDs are unique, URLs use HTTP(S), and retrieval dates use ISO `YYYY-MM-DD` format. It does not fetch URLs, certify source accuracy, or replace independent reading of the underlying documents.

The current register passes all checks. This is a provenance-quality gate, not evidence that every external claim is correct or current; dated regulatory and research claims still require refresh before reuse.

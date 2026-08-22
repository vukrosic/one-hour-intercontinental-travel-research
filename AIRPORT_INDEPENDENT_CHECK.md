# Independent airport-summary reproduction

`airport_compatibility_independent_check.py` re-reads `airport_compatibility.csv`, recomputes each summary count with a separate implementation, and compares the result with `airport_compatibility_summary.csv`. It does not import the primary airport-summary script and does not evaluate any airport, runway, gate, rescue, load, or operating procedure.

All seven summary metrics match exactly. This verifies the audit bookkeeping only. It cannot establish that a source claim is true, that a standard applies to a particular airport, or that any unspecified high-speed aircraft is compatible.

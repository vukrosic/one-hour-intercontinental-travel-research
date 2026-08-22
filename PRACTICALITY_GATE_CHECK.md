# Practicality-matrix semantic check

`practicality_gate_check.py` validates the matrix's conjunctive interpretation. It detects unresolved, contradicted, or adverse gate states; rejects a `practical_pass` label when any such blocker exists; requires conceptual bins to lack a service anchor; and requires non-baseline rows to list their blocking gates.

The current five rows all pass the semantic checks. The Mach 0.85 airline and Mach 0.925 business-aviation rows are explicitly non-ranked reference classes. This is a guard against editorial drift, not a new physical result or a weighted practicality score.

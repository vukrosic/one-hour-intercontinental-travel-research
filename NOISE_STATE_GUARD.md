# Noise evidence state guard

## Purpose

Noise evidence changes over time and mixes different kinds of claims: current
restrictions, proposed rules, future-applicability standards, standards work,
research programmes, and unresolved gaps. This guard makes those distinctions
executable.

`noise_state_guard.py` validates the committed
[`noise_evidence.csv`](noise_evidence.csv) table and rejects a row that marks a
proposal, future standard, developing standard, research programme, current
binding restriction, or unresolved gap as a high-speed practical pass. It also
requires threshold value and unit fields to be paired when a public threshold is
recorded. A proposed threshold remains evidence about a proposal, not a design
target or permission.

## Current snapshot

The table contains:

- 1 current binding restriction;
- 3 prospective/development rows;
- 1 empirical community-research row;
- 1 unresolved cabin-noise row; and
- 0 final high-speed pass thresholds.

The current FAA page still describes the U.S. overland restriction and special
flight-authorisation context. The FAA overview describes a prospective
noise-based policy direction, while NASA Quesst describes future community
response data intended to inform acceptable-noise thresholds. These states are
kept separate in the table.

## Reproducibility

```text
python3 noise_state_guard.py
python3 noise_state_independent_check.py
```

The guard writes [`noise_state_guard.csv`](noise_state_guard.csv). The
independent state-count implementation writes
[`noise_state_independent_check.csv`](noise_state_independent_check.csv) and
reproduces all seven metrics. The full unit suite tests both valid rows and
deliberately invalid proposal/research-pass mutations.

## Limits

- A state guard verifies bookkeeping semantics, not legal applicability or
  community acceptance.
- It does not model sonic-boom generation, propagation, mitigation, airport
  noise, or cabin acoustics.
- It does not infer routes, operating procedures, shaping, or compliance
  methods.
- The noise gate remains unresolved for practical civilian service above Mach 1
  until final standards and empirical community-response evidence exist.

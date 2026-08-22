# Abstract acceleration and ride-time sensitivity

## Question

How much of a fixed intercontinental distance would an abstract speed class consume in symmetric acceleration and deceleration phases, under declared acceleration fractions?

## Method

`acceleration_scenarios.csv` compares four speed classes at 0.05g, 0.10g, and 0.20g. The common distance is 9,492.6 km, inherited only as a mathematical yardstick from the archived SFO–PEK screen. For a symmetric constant-acceleration thought experiment:

```text
phase time = speed / acceleration
accel+decel distance = speed^2 / acceleration
```

If the phase distance fits inside the yardstick, the script reports an abstract accelerate–cruise–decelerate total. If it does not, it reports a no-cruise lower-bound regime. This is a kinematic sensitivity, not a flight profile.

## Safety boundary

The acceleration fractions are not passenger-comfort limits, certification limits, or recommendations. No human tolerance, seat design, vehicle geometry, trajectory, control law, route, or operating procedure is inferred. The model only shows how a declared acceleration assumption changes time and distance algebraically.

## Result

Run `python3 acceleration_sensitivity.py` to regenerate `acceleration_sensitivity.csv`. The output exposes, for each speed/acceleration pair, phase time, phase-distance fraction, idealized cruise time, and acceleration-overhead fraction. It is intended to be read alongside the unresolved passenger-environment gate, not used to close it.

## Limitations and next hypothesis

- Real aircraft accelerate through changing atmosphere and aerodynamic states; this model does not.
- The fixed distance is a comparison yardstick, not a route or operating authorization.
- Passenger comfort, vibration, emergency cases, and certification are entirely outside scope.
- The next safe check is an independent algebraic reproduction of this table before any interpretation is extended.

The independent arithmetic reproduction is recorded in [ACCELERATION_INDEPENDENT_CHECK.md](ACCELERATION_INDEPENDENT_CHECK.md). The derived comparison of speed-only versus acceleration-adjusted time savings is in [ACCELERATION_ADJUSTED_TIME.md](ACCELERATION_ADJUSTED_TIME.md). The Mach-to-speed consistency audit is in [MACH_SPEED_CONSISTENCY.md](MACH_SPEED_CONSISTENCY.md).

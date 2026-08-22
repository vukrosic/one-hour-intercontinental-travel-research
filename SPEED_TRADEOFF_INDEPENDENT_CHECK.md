# Independent speed-tradeoff reproduction

`speed_tradeoff_independent_check.py` re-reads the committed `speed_tradeoff.csv` and independently recomputes the fixed-distance time ratio, saved fraction, normalized kinetic-energy proxy, ideal temperature ratio, and marginal ratios. It does not import `speed_tradeoff.py` or `physics_envelope.py`.

Running `python3 speed_tradeoff_independent_check.py` gives six passing rows at an absolute tolerance of `1e-12`. This verifies the diminishing-return arithmetic in the frozen dimensionless model. It does not turn the kinetic-energy proxy into fuel burn, aerodynamic drag, heat flux, noise, or economic cost.

The model's fixed-distance and common-reference assumptions remain documented in [SPEED_TRADEOFF.md](SPEED_TRADEOFF.md). The result is a mathematical screening trend, not an aircraft recommendation.

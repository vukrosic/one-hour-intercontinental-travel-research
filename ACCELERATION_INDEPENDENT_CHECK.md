# Independent acceleration-sensitivity reproduction

`acceleration_independent_check.py` re-reads the frozen acceleration inputs and committed sensitivity table, then independently recomputes every numeric output and profile regime. It does not import `acceleration_sensitivity.py`.

All 12 speed/acceleration rows reproduce within `1e-12`, with matching profile labels. This verifies the kinematic bookkeeping only. It does not validate any acceleration value as comfortable, safe, certifiable, or operationally achievable.

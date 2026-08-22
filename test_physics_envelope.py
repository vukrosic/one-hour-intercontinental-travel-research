import unittest

from physics_envelope import normalized_kinetic_energy, total_temperature_ratio


class PhysicsEnvelopeTests(unittest.TestCase):
    def test_reference_energy_ratio_is_one(self):
        self.assertAlmostEqual(normalized_kinetic_energy(0.85), 1.0)

    def test_total_temperature_ratio_at_mach_two(self):
        self.assertAlmostEqual(total_temperature_ratio(2.0), 1.8)

    def test_both_proxies_increase_with_mach(self):
        self.assertLess(total_temperature_ratio(2.0), total_temperature_ratio(3.0))
        self.assertLess(normalized_kinetic_energy(2.0), normalized_kinetic_energy(3.0))


if __name__ == "__main__":
    unittest.main()

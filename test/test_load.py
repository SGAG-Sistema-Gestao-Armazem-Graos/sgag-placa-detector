import unittest

from manager.load import Load


class TestLoad(unittest.TestCase):
    def test_weight_difference_positive(self):
        load = Load(load_id=1, initial_total_weight=1000.0, final_total_weight=950.0)
        self.assertEqual(load.weight_difference(), 50.0)

    def test_weight_difference_zero(self):
        load = Load(load_id=2, initial_total_weight=500.0, final_total_weight=500.0)
        self.assertEqual(load.weight_difference(), 0.0)

    def test_weight_difference_negative(self):
        load = Load(load_id=3, initial_total_weight=800.0, final_total_weight=850.0)
        self.assertEqual(load.weight_difference(), -50.0)

    def test_string_representation(self):
        load = Load(load_id=4, initial_total_weight=1000.0, final_total_weight=980.0)
        expected_str = "Load(ID: 4, Initial Weight: 1000.0, Final Weight: 980.0)"
        self.assertEqual(str(load), expected_str)

if __name__ == "__main__":
    unittest.main()

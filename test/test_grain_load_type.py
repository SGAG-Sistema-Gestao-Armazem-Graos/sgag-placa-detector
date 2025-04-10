import unittest

from manager.grain_load_type import GrainLoadType


class TestGrainLoadType(unittest.TestCase):

    def setUp(self):
        self.obj = GrainLoadType(
            grain_load_type_id=1,
            grain_type_id=2,
            load_id=10,
            grain_moisture=13,
            initial_weight=1000.0,
            final_weight=950.0
        )

    def test_attributes(self):
        self.assertEqual(self.obj.grain_type_id, 2)
        self.assertEqual(self.obj.grain_moisture, 13)

    def test_lost_weight(self):
        self.assertAlmostEqual(self.obj.lost_weight(), 50.0)

    def test_str_output(self):
        self.assertIn("Type: 2", str(self.obj))
        self.assertIn("Moisture: 13%", str(self.obj))

if __name__ == "__main__":
    unittest.main()

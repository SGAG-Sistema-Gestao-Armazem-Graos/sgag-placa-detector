import unittest

from manager.grain_type import GrainType


class TestGrainType(unittest.TestCase):

    def setUp(self):
        self.grain = GrainType(
            grain_type_id=1,
            name="Soybean",
            ideal_moisture=13,
            observations="Harvested in early fall"
        )

    def test_attributes(self):
        self.assertEqual(self.grain.grain_type_id, 1)
        self.assertEqual(self.grain.name, "Soybean")
        self.assertEqual(self.grain.ideal_moisture, 13)
        self.assertEqual(self.grain.observations, "Harvested in early fall")

    def test_str_representation(self):
        expected = "GrainType(ID: 1, Name: Soybean, Ideal Moisture: 13%, Observations: Harvested in early fall)"
        self.assertEqual(str(self.grain), expected)


if __name__ == "__main__":
    unittest.main()
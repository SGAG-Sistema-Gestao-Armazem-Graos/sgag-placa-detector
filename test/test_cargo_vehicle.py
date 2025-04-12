import unittest
from datetime import datetime

from manager.cargo_vehicle import CargoVehicle


class TestCargoVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = CargoVehicle(
            vehicle_id=1,
            vehicle_type_id=101,
            brand="Volvo",
            vehicle_description="Caminhão pesado com baú",
            plate="ABC1234",
            chassis="9BWZZZ377VT004251",
            model_year=datetime.now().year,
            manufacture_year=datetime.now().year - 1,
            cargo_capacity=12.5
        )

    def test_str_representation(self):
        result = str(self.vehicle)
        self.assertIn("CargoVehicle", result)
        self.assertIn("Volvo", result)
        self.assertIn("ABC1234", result)

    def test_is_new_model_true(self):
        self.assertTrue(self.vehicle.is_new_model())

    def test_is_new_model_false(self):
        self.vehicle.model_year = 2020
        self.assertFalse(self.vehicle.is_new_model())

    def test_capacity_over_threshold_true(self):
        self.assertTrue(self.vehicle.is_capacity_over(10.0))

    def test_capacity_over_threshold_false(self):
        self.assertFalse(self.vehicle.is_capacity_over(20.0))

if __name__ == '__main__':
    unittest.main()

import unittest
from manager.cargo_vehicle_type import CargoVehicleType

class TestCargoVehicleType(unittest.TestCase):
    
    def test_str_representation(self):
        truck = CargoVehicleType(1, "Test Truck", "CIDADE")
        expected = "CargoVehicleType(ID: 1, Description: Test Truck, Route Recommendation: CIDADE)"
        self.assertEqual(str(truck), expected)

    def test_is_urban_route_true(self):
        truck = CargoVehicleType(2, "Small Urban Truck", "CIDADE")
        self.assertTrue(truck.is_urban_route())
        self.assertFalse(truck.is_highway_route())
        self.assertFalse(truck.is_mixed_route())

    def test_is_highway_route_true(self):
        truck = CargoVehicleType(3, "Long Distance Truck", "RODOVIARIO")
        self.assertTrue(truck.is_highway_route())
        self.assertFalse(truck.is_urban_route())
        self.assertFalse(truck.is_mixed_route())

    def test_is_mixed_route_true(self):
        truck = CargoVehicleType(4, "Versatile Truck", "MISTO")
        self.assertTrue(truck.is_mixed_route())
        self.assertFalse(truck.is_urban_route())
        self.assertFalse(truck.is_highway_route())

    def test_case_insensitive_route(self):
        truck = CargoVehicleType(5, "Test Truck", "RODOVIARIO")
        self.assertTrue(truck.is_highway_route())

if __name__ == '__main__':
    unittest.main()

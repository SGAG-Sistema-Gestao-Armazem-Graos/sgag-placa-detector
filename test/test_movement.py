from datetime import datetime
import unittest

from manager.movement import Movement


class TestMovement(unittest.TestCase):
    def setUp(self):
        self.movement = Movement(
            movement_id=1,
            vehicle_id=10,
            driver_id=20,
            cargo_id=30,
            origin_location_id=100,
            destination_location_id=200,
            trip_status="PLANNED",
            start_datetime=datetime(2025, 4, 10, 9, 0, 0),
            end_datetime=None,
            observations="First trip"
        )

    def test_attributes_assignment(self):
        self.assertEqual(self.movement.movement_id, 1)
        self.assertEqual(self.movement.vehicle_id, 10)
        self.assertEqual(self.movement.driver_id, 20)
        self.assertEqual(self.movement.trip_status, "PLANNED")
        self.assertIsNone(self.movement.end_datetime)

    def test_str_representation(self):
        output = str(self.movement)
        self.assertIn("Movement(ID: 1", output)
        self.assertIn("Vehicle ID: 10", output)
        self.assertIn("Notes: First trip", output)


if __name__ == "__main__":
    unittest.main()
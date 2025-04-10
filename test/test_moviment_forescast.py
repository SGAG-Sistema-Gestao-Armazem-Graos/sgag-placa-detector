import unittest

from manager.movement_forecast import MovementForecast


class TestMovementForecast(unittest.TestCase):
    def setUp(self):
        self.forecast = MovementForecast(1, 100, 200)

    def test_attributes(self):
        self.assertEqual(self.forecast.movement_forecast_id, 1)
        self.assertEqual(self.forecast.movement_id, 100)
        self.assertEqual(self.forecast.climate_forecast_id, 200)

    def test_str_representation(self):
        expected_str = "MovementForecast(ID: 1, Movement ID: 100, Climate Forecast ID: 200)"
        self.assertEqual(str(self.forecast), expected_str)


if __name__ == "__main__":
    unittest.main()
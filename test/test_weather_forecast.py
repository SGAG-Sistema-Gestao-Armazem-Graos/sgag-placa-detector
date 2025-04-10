import unittest
from datetime import datetime

from manager.weather_forecast import WeatherForecast


class TestWeatherForecast(unittest.TestCase):

    def setUp(self):
        self.forecast = WeatherForecast(
            forecast_id=1,
            timestamp=datetime(2025, 4, 9, 15, 0),
            region="Amazon Rainforest",
            temperature=38,
            humidity=18
        )

    def test_str_representation(self):
        result = str(self.forecast)
        self.assertIn("Amazon Rainforest", result)
        self.assertIn("38°C", result)
        self.assertIn("18%", result)

    def test_is_heat_alert_true(self):
        self.assertTrue(self.forecast.is_heat_alert(), "Should trigger heat alert for temperature >= 35")

    def test_is_heat_alert_false(self):
        forecast = WeatherForecast(2, datetime.now(), "South Pole", 10, 80)
        self.assertFalse(forecast.is_heat_alert(), "Should not trigger heat alert for temperature < 35")

    def test_is_low_humidity_alert_true(self):
        self.assertTrue(self.forecast.is_low_humidity_alert(), "Should trigger low humidity alert for humidity <= 20")

    def test_is_low_humidity_alert_false(self):
        forecast = WeatherForecast(3, datetime.now(), "Coastal City", 28, 55)
        self.assertFalse(forecast.is_low_humidity_alert(), "Should not trigger low humidity alert for humidity > 20")

if __name__ == '__main__':
    unittest.main()

from datetime import datetime

class WeatherForecast:
    """
    Represents a weather forecast for a given date, time, and region.

    Attributes:
        forecast_id (int): Unique identifier of the forecast.
        timestamp (datetime): Date and time of the forecast.
        region (str): Name of the forecast region.
        temperature (int): Forecasted temperature in Celsius.
        humidity (int): Relative humidity percentage.
    """

    def __init__(self, forecast_id: int, timestamp: datetime, region: str, temperature: int, humidity: int):
        self.forecast_id = forecast_id
        self.timestamp = timestamp
        self.region = region
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):
        return (
            f"WeatherForecast(ID: {self.forecast_id}, Region: {self.region}, "
            f"Timestamp: {self.timestamp}, Temp: {self.temperature}°C, Humidity: {self.humidity}%)"
        )

    def is_heat_alert(self, temp_threshold=35):
        """Returns True if temperature exceeds the heat alert threshold."""
        return self.temperature >= temp_threshold

    def is_low_humidity_alert(self, humidity_threshold=20):
        """Returns True if humidity is below the low humidity threshold."""
        return self.humidity <= humidity_threshold


# Quick test
#if __name__ == "__main__":
#    forecast = WeatherForecast(
#        forecast_id=1,
#        timestamp=datetime(2025, 4, 10, 15, 30),
#        region="Midwest",
#        temperature=38,
#        humidity=18
#    )

#    print(forecast)
#    print("Heat alert?", forecast.is_heat_alert())
#    print("Low humidity alert?", forecast.is_low_humidity_alert())

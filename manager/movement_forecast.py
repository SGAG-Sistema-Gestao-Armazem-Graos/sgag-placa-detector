class MovementForecast:
    """
    Represents the association between a movement and a weather forecast.

    Attributes:
        movement_forecast_id (int): Unique identifier for the movement-forecast relationship (primary key).
        movement_id (int): Identifier for the movement (foreign key).
        climate_forecast_id (int): Identifier for the climate forecast (foreign key).
    """

    def __init__(self, movement_forecast_id: int, movement_id: int, climate_forecast_id: int):
        """
        Initializes a new instance of the MovementForecast class.

        Args:
            movement_forecast_id (int): Unique ID for this association.
            movement_id (int): ID of the movement.
            climate_forecast_id (int): ID of the climate forecast.
        """
        self.movement_forecast_id = movement_forecast_id
        self.movement_id = movement_id
        self.climate_forecast_id = climate_forecast_id

    def __str__(self):
        """
        Returns a readable string representation of the object.

        Returns:
            str: A string with the object's information.
        """
        return (
            f"MovementForecast("
            f"ID: {self.movement_forecast_id}, "
            f"Movement ID: {self.movement_id}, "
            f"Climate Forecast ID: {self.climate_forecast_id})"
        )


class MovementForecast:
    """
    Represents the association between a movement and a weather forecast.

    Attributes:
        movement_forecast_id (int): Unique identifier for the movement-forecast relationship (primary key).
        movement_id (int): Identifier for the movement (foreign key).
        climate_forecast_id (int): Identifier for the climate forecast (foreign key).
    """

    def __init__(self, movement_forecast_id: int, movement_id: int, climate_forecast_id: int):
        """
        Initializes a new instance of the MovementForecast class.

        Args:
            movement_forecast_id (int): Unique ID for this association.
            movement_id (int): ID of the movement.
            climate_forecast_id (int): ID of the climate forecast.
        """
        self.movement_forecast_id = movement_forecast_id
        self.movement_id = movement_id
        self.climate_forecast_id = climate_forecast_id

    def __str__(self):
        """
        Returns a readable string representation of the object.

        Returns:
            str: A string with the object's information.
        """
        return (
            f"MovementForecast("
            f"ID: {self.movement_forecast_id}, "
            f"Movement ID: {self.movement_id}, "
            f"Climate Forecast ID: {self.climate_forecast_id})"
        )


# Test block
#if __name__ == "__main__":
#    forecast = MovementForecast(1, 101, 202)
#    print(forecast)

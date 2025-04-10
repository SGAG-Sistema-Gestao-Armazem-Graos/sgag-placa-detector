from datetime import datetime
from typing import Optional


class Movement:
    """
    Represents a transportation movement.

    Attributes:
        movement_id (int): Unique identifier for the movement.
        vehicle_id (int): ID of the vehicle used.
        driver_id (int): ID of the driver responsible.
        cargo_id (int): ID of the cargo being transported.
        origin_location_id (int): ID of the origin location.
        destination_location_id (int): ID of the destination location.
        trip_status (str): Status of the trip (e.g., 'PLANNED', 'IN_PROGRESS', 'COMPLETED').
        start_datetime (datetime): Start date and time of the trip.
        end_datetime (datetime): End date and time of the trip.
        observations (str): Additional notes or observations (optional).
    """

    def __init__(
        self,
        movement_id: int,
        vehicle_id: int,
        driver_id: int,
        cargo_id: int,
        origin_location_id: int,
        destination_location_id: int,
        trip_status: str,
        start_datetime: datetime,
        end_datetime: Optional[datetime] = None,
        observations: Optional[str] = None
    ):
        self.movement_id = movement_id
        self.vehicle_id = vehicle_id
        self.driver_id = driver_id
        self.cargo_id = cargo_id
        self.origin_location_id = origin_location_id
        self.destination_location_id = destination_location_id
        self.trip_status = trip_status
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.observations = observations

    def __str__(self):
        return (
            f"Movement("
            f"ID: {self.movement_id}, Vehicle ID: {self.vehicle_id}, Driver ID: {self.driver_id}, "
            f"Cargo ID: {self.cargo_id}, From: {self.origin_location_id} To: {self.destination_location_id}, "
            f"Status: {self.trip_status}, Start: {self.start_datetime}, "
            f"End: {self.end_datetime}, Notes: {self.observations})"
        )

# test class
#if __name__ == "__main__":
#    from datetime import datetime

    # Example instantiation
#    movement = Movement(
#        movement_id=1,
#        vehicle_id=101,
#        driver_id=202,
#        cargo_id=303,
#        origin_location_id=1,
#        destination_location_id=2,
#        trip_status="IN_PROGRESS",
#        start_datetime=datetime(2025, 4, 10, 9, 0, 0),
#        observations="No issues reported so far."
#    )

#    print(movement)

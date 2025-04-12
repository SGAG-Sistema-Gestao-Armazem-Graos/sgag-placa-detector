

from manager.cargo_vehicle_type import CargoVehicleType


class CargoVehicle:
    """
    Represents a cargo vehicle with its attributes such as model, type, and capacity.

    Attributes:
        vehicle_id (int): Unique identifier for the cargo vehicle.
        vehicle_type_id (int): Identifier referencing the vehicle type.
        brand (str): Brand of the vehicle.
        vehicle_description (str): Description of the vehicle.
        plate (str): Vehicle license plate (format: ABC1234 or similar).
        chassis (str): Chassis number (up to 17 characters).
        model_year (int): Year model of the vehicle.
        manufacture_year (int): Year the vehicle was manufactured.
        cargo_capacity (float): Maximum cargo capacity in tons or kilograms.
    """

    def __init__(self,
                 vehicle_id: int,
                 vehicle_type_id: CargoVehicleType,
                 brand: str,
                 vehicle_description: str,
                 plate: str,
                 chassis: str,
                 model_year: int,
                 manufacture_year: int,
                 cargo_capacity: float):
        


        self.vehicle_id = vehicle_id
        self.vehicle_type_id = vehicle_type_id
        self.brand = brand
        self.vehicle_description = vehicle_description
        self.plate = plate
        self.chassis = chassis
        self.model_year = model_year
        self.manufacture_year = manufacture_year
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return (
            f"CargoVehicle("
            f"ID: {self.vehicle_id}, "
            f"TypeID: {self.vehicle_type_id}, "
            f"Brand: {self.brand}, "
            f"Description: {self.vehicle_description}, "
            f"Plate: {self.plate}, "
            f"Chassis: {self.chassis}, "
            f"Model Year: {self.model_year}, "
            f"Manufacture Year: {self.manufacture_year}, "
            f"Capacity: {self.cargo_capacity} tons)"
        )

    def is_new_model(self) -> bool:
        """Checks if model year is the current year."""
        from datetime import datetime
        return self.model_year == datetime.now().year

    def is_capacity_over(self, threshold: float) -> bool:
        """Returns True if cargo capacity is over the given threshold (in tons)."""
        return self.cargo_capacity > threshold

# if __name__ == "__main__":
#     from datetime import datetime

#    vehicle = CargoVehicle(
#        vehicle_id=1,
#        vehicle_type_id=101,
#        brand="Mercedes-Benz",
#        vehicle_description="Caminhão com capacidade para 15 toneladas",
#        plate="XYZ1234",
#        chassis="9BWZZZ377VT004251",
#        model_year=datetime.now().year,
#        manufacture_year=datetime.now().year - 1,
#        cargo_capacity=15.0
#    )

#    print(vehicle)
#    print("É modelo do ano?", vehicle.is_new_model())
#    print("Capacidade maior que 10 toneladas?", vehicle.is_capacity_over(10))
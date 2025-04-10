class CargoVehicleType:
    """
    Represents a type of cargo vehicle and its recommended route.

    Attributes:
        vehicle_type_id (int): Unique identifier for the cargo vehicle type.
        description (str): Description of the cargo vehicle type.
        route_recommendation (str): Recommended route type ('URBAN', 'HIGHWAY', or 'MIXED').
    """

    def __init__(self, 
                 vehicle_type_id: int, 
                 description: str, 
                 route_recommendation: str,
                 ):
        """
        Initializes a new instance of the CargoVehicleType class.

        Args:
            vehicle_type_id (int): The ID of the cargo vehicle type.
            description (str): The description of the cargo vehicle type.
            route_recommendation (str): The recommended route ('URBAN', 'HIGHWAY', or 'MIXED').
        """
        self.vehicle_type_id = vehicle_type_id
        self.description = description
        self.route_recommendation = route_recommendation

    def __str__(self):
        """
        Returns a readable string representation of the object.

        Returns:
            str: A string with the object's information.
        """
        return (
            f"CargoVehicleType("
            f"ID: {self.vehicle_type_id}, "
            f"Description: {self.description}, "
            f"Route Recommendation: {self.route_recommendation})"
        )

    def is_urban_route(self) -> bool:
        """
        Checks if the recommended route is urban.

        Returns:
            bool: True if route is 'CIDADE', False otherwise.
        """
        return self.route_recommendation.upper() == 'CIDADE'

    def is_highway_route(self) -> bool:
        """
        Checks if the recommended route is highway.

        Returns:
            bool: True if route is 'RODOVIARIO', False otherwise.
        """
        return self.route_recommendation.upper() == 'RODOVIARIO'

    def is_mixed_route(self) -> bool:
        """
        Checks if the recommended route is mixed.

        Returns:
            bool: True if route is 'MISTO', False otherwise.
        """
        return self.route_recommendation.upper() == 'MISTO'
    

#  Executa esse código de teste apenas se este arquivo for executado diretamente
# if __name__ == "__main__":
#     truck = CargoVehicleType(1, "Three-Axle Truck", "MISTO")
#     print(truck.route_recommendation)

#    if truck.is_highway_route():
#        print("This vehicle is suitable for highway routes.")

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

    def get_vehicle_type_id(self) -> int:
        """
        Returns the vehicle type ID.

        Returns:
            int: The vehicle type ID.
        """
        return self.vehicle_type_id

    def get_description(self) -> str:
        """
        Returns the description of the cargo vehicle type.

        Returns:
            str: The description of the cargo vehicle type.
        """
        return self.description

    def get_route_recommendation(self) -> str:
        """
        Returns the recommended route for the vehicle.

        Returns:
            str: The recommended route ('URBAN', 'HIGHWAY', or 'MIXED').
        """
        return self.route_recommendation

    def __str__(self):
        """
        Returns a readable string representation of the object, including all attributes.

        Returns:
            str: A string with the object's information.
        """
        return (
            f"CargoVehicleType(\n"
            f"  ID: {self.vehicle_type_id}\n"
            f"  Description: {self.description}\n"
            f"  Route Recommendation: {self.route_recommendation}\n"
            f")"
        )

    def is_urban_route(self) -> bool:
        """
        Checks if the recommended route is urban.

        Returns:
            bool: True if route is 'URBAN', False otherwise.
        """
        return self.route_recommendation.upper() == 'URBAN'

    def is_highway_route(self) -> bool:
        """
        Checks if the recommended route is highway.

        Returns:
            bool: True if route is 'HIGHWAY', False otherwise.
        """
        return self.route_recommendation.upper() == 'HIGHWAY'

    def is_mixed_route(self) -> bool:
        """
        Checks if the recommended route is mixed.

        Returns:
            bool: True if route is 'MIXED', False otherwise.
        """
        return self.route_recommendation.upper() == 'MIXED'


# Testando a classe
#if __name__ == "__main__":
    # Criando um veículo de carga do tipo caminhão de três eixos
#    truck = CargoVehicleType(1, "Three-Axle Truck", "MIXED")
    
    # Retornando cada atributo individualmente
#    print(f"Vehicle Type ID: {truck.get_vehicle_type_id()}")
#    print(f"Description: {truck.get_description()}")
#    print(f"Route Recommendation: {truck.get_route_recommendation()}")

    # Verificando a recomendação de rota
#    if truck.is_highway_route():
#        print("This vehicle is suitable for highway routes.")
#    elif truck.is_urban_route():
#        print("This vehicle is suitable for urban routes.")
#    elif truck.is_mixed_route():
#        print("This vehicle is suitable for mixed routes.")

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Optional

from manager.cargo_vehicle_type import CargoVehicleType

class CargoVehicleTypeCRUD:
    """
    Classe para realizar operações CRUD sobre objetos CargoVehicleType.
    """

    def __init__(self):
        self._vehicle_types: List[CargoVehicleType] = []

    def create(self, vehicle_type: CargoVehicleType) -> None:
        """
        Adiciona um novo tipo de veículo à lista.
        """
        self._vehicle_types.append(vehicle_type)

    def read_all(self) -> List[CargoVehicleType]:
        """
        Retorna todos os tipos de veículos cadastrados.
        """
        return self._vehicle_types

    def read_by_id(self, vehicle_type_id: int) -> Optional[CargoVehicleType]:
        """
        Retorna um tipo de veículo com base no ID.
        """
        for vehicle in self._vehicle_types:
            if vehicle.get_vehicle_type_id() == vehicle_type_id:
                return vehicle
        return None

    def update(self, vehicle_type_id: int, 
               new_description: Optional[str] = None, 
               new_route: Optional[str] = None) -> bool:
        """
        Atualiza o tipo de veículo com base no ID.
        """
        vehicle = self.read_by_id(vehicle_type_id)
        if vehicle:
            if new_description is not None:
                vehicle.description = new_description
            if new_route is not None:
                vehicle.route_recommendation = new_route
            return True
        return False

    def delete(self, vehicle_type_id: int) -> bool:
        """
        Remove um tipo de veículo com base no ID.
        """
        vehicle = self.read_by_id(vehicle_type_id)
        if vehicle:
            self._vehicle_types.remove(vehicle)
            return True
        return False


# Testando o CRUD
# if __name__ == "__main__":
#     crud = CargoVehicleTypeCRUD()

    # Criar novos veículos
#    v1 = CargoVehicleType(1, "Three-Axle Truck", "MIXED")
#    v2 = CargoVehicleType(2, "Delivery Van", "URBAN")
#    v3 = CargoVehicleType(3, "Long Haul Truck", "HIGHWAY")

    # Adicionar ao CRUD
#    crud.create(v1)
#    crud.create(v2)
#    crud.create(v3)

    # Listar todos
#    print("Todos os veículos:")
#    for v in crud.read_all():
#        print(v)

    # Buscar por ID
#    print("\nBuscar veículo ID 2:")
#    print(crud.read_by_id(2))

    # Atualizar
#    print("\nAtualizando veículo ID 1:")
#    crud.update(1, new_description="Updated Truck", new_route="URBAN")
#    print(crud.read_by_id(1))

    # Deletar
#    print("\nDeletando veículo ID 3:")
#    crud.delete(3)
#    print("Todos os veículos após deleção:")
#    for v in crud.read_all():
#        print(v)
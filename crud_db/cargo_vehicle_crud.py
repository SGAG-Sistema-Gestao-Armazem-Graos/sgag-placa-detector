import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

from manager.cargo_vehicle import CargoVehicle
from manager.cargo_vehicle_type import CargoVehicleType


class CargoVehicleCRUD:

    """
    Classe responsável pelas operações CRUD (Criar, Ler, Atualizar, Excluir) em veículos de carga.

    Atributos:
        vehicles (list): Lista que armazena os veículos cadastrados no sistema.
    """

    def __init__(self):
        """
        Inicializa a classe CargoVehicleCRUD com uma lista vazia de veículos.
        """
        self.vehicles = []

    def create_vehicle(self, vehicle: CargoVehicle):
        """
        Cria um novo veículo e o adiciona à lista de veículos.

        Parâmetros:
            vehicle (CargoVehicle): Instância da classe CargoVehicle contendo as informações do veículo a ser criado.
        
        Exemplo:
            v = CargoVehicle(vehicle_id=1, vehicle_type_id=100, brand="Volkswagen", ...)
            manager.create_vehicle(v)
        """
        self.vehicles.append(vehicle)
        print(f"✅ Veículo com ID {vehicle.vehicle_id} criado com sucesso.")

    def read_vehicles(self):
        """
        Exibe todos os veículos cadastrados no sistema.

        Se não houver veículos cadastrados, exibe uma mensagem informando que não há veículos.

        Exemplo:
            manager.read_vehicles()
        """
        if not self.vehicles:
            print("🚫 Nenhum veículo cadastrado.")
            return
        for vehicle in self.vehicles:
            print(vehicle)

    def update_vehicle(self, vehicle_id: int, **kwargs):
        """
        Atualiza os atributos de um veículo existente com base no ID.

        Parâmetros:
            vehicle_id (int): ID do veículo a ser atualizado.
            **kwargs: Parâmetros chave-valor que indicam o atributo a ser atualizado e o novo valor.
        
        Exemplo:
            manager.update_vehicle(1, brand="Iveco", cargo_capacity=10.0)
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                for key, value in kwargs.items():
                    if hasattr(vehicle, key):
                        setattr(vehicle, key, value)
                        print(f"🔄 Atributo '{key}' atualizado para '{value}' no veículo {vehicle_id}.")
                    else:
                        print(f"⚠️ Atributo '{key}' não encontrado.")
                return
        print(f"🚫 Veículo com ID {vehicle_id} não encontrado.")

    def delete_vehicle(self, vehicle_id: int):
        """
        Exclui um veículo com base no ID fornecido.

        Parâmetros:
            vehicle_id (int): ID do veículo a ser excluído.

        Exemplo:
            manager.delete_vehicle(1)
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                print(f"🗑️ Veículo com ID {vehicle_id} removido com sucesso.")
                return
        print(f"🚫 Veículo com ID {vehicle_id} não encontrado.")

# Testando a funcionalidade
#if __name__ == "__main__":

    # Criando o gerenciador de veículos
#    manager = CargoVehicleCRUD()

    # Criando um veículo para testar
#    v1 = CargoVehicle(
#        vehicle_id=1,
#        vehicle_type_id= CargoVehicleType(vehicle_type_id= 1, description= "Graneleiro", route_recommendation= "URBAN"),
#        brand="Volkswagen",
#        vehicle_description="Caminhão de carga leve",
#        plate="JKL5678",
#        chassis="ABCDEF12345678901",
#        model_year=datetime.now().year,
#        manufacture_year=datetime.now().year - 1,
#        cargo_capacity=8.5
#    )

    # Testando a criação de um veículo
#    manager.create_vehicle(v1)
    
    # Testando a leitura dos veículos cadastrados
#    manager.read_vehicles()
    
    # Testando a atualização do veículo
#    manager.update_vehicle(1, brand="Iveco", cargo_capacity=10.0)
    
    # Testando a leitura novamente após a atualização
#    manager.read_vehicles()
    
    # Testando a exclusão do veículo
#    manager.delete_vehicle(1)
    
    # Testando a leitura após a exclusão
#    manager.read_vehicles()

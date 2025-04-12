import sys
import os
from datetime import datetime
from display.display_cargo_vehicle_type import DisplayCargoVehicleType

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud_db.cargo_vehicle_crud import CargoVehicleCRUD
from manager.cargo_vehicle import CargoVehicle

class DisplayCargoVehicleMenu:
    """
    Classe responsável por exibir o menu de operações de veículos de carga, permitindo criar, ler,
    atualizar e excluir veículos. Cada operação interage com a classe CargoVehicleCRUD para manipular
    os dados dos veículos no banco de dados.

    Atributos:
        manager (CargoVehicleCRUD): Instância da classe responsável pelas operações CRUD dos veículos.
    """
    
    def __init__(self):
        """
        Inicializa a classe DisplayCargoVehicleMenu, configurando o gerenciador de veículos (CargoVehicleCRUD).
        """
        self.manager = CargoVehicleCRUD()

    def create_vehicle(self):
        """
        Solicita ao usuário as informações de um veículo e cria um novo veículo no sistema.
        """
        try:
            vehicle_id = int(input("Digite o ID do veículo: "))
            vehicle_type_display = DisplayCargoVehicleType()  # Instancia a classe para exibir tipos de veículos
            vehicle_type_id = vehicle_type_display

            brand = input("Digite a marca do veículo: ")
            description = input("Digite a descrição do veículo: ")
            plate = input("Digite a placa do veículo: ")
            chassis = input("Digite o chassis do veículo: ")
            model_year = int(input("Digite o ano do modelo: "))
            manufacture_year = int(input("Digite o ano de fabricação: "))
            cargo_capacity = float(input("Digite a capacidade de carga: "))
            
            # Criação do objeto CargoVehicle
            vehicle = CargoVehicle(
                vehicle_id=vehicle_id,
                vehicle_type_id=vehicle_type_id,
                brand=brand,
                vehicle_description=description,
                plate=plate,
                chassis=chassis,
                model_year=model_year,
                manufacture_year=manufacture_year,
                cargo_capacity=cargo_capacity
            )
            
            self.manager.create_vehicle(vehicle)
            print("Veículo criado com sucesso!")
        except ValueError as e:
            print(f"Erro ao criar o veículo: {e}. Verifique os dados e tente novamente.")

    def read_vehicles(self):
        """
        Exibe a lista de veículos cadastrados no sistema.
        """
        self.manager.read_vehicles()

    def update_vehicle(self):
        """
        Solicita ao usuário um veículo existente para ser atualizado.
        """
        try:
            vehicle_id = int(input("Digite o ID do veículo a ser atualizado: "))
            key = input("Digite o atributo que deseja atualizar (ex: brand, cargo_capacity): ")
            value = input(f"Digite o novo valor para o atributo '{key}': ")

            if key == "cargo_capacity":
                value = float(value)
            
            # Chama o CRUD para atualizar
            self.manager.update_vehicle(vehicle_id, **{key: value})
            print("Veículo atualizado com sucesso!")
        except ValueError as e:
            print(f"Erro ao atualizar o veículo: {e}. Verifique os dados e tente novamente.")

    def delete_vehicle(self):
        """
        Solicita ao usuário o ID de um veículo para ser excluído.
        """
        try:
            vehicle_id = int(input("Digite o ID do veículo a ser excluído: "))
            self.manager.delete_vehicle(vehicle_id)
            print("Veículo excluído com sucesso!")
        except ValueError as e:
            print(f"Erro ao excluir o veículo: {e}. Verifique os dados e tente novamente.")

    def show_menu(self):
        """
        Exibe o menu de opções de operações para o usuário interagir.
        """
        while True:
            print("\n--- Menu de Opções ---")
            print("1. Criar veículo")
            print("2. Ler veículos")
            print("3. Atualizar veículo")
            print("4. Excluir veículo")
            print("5. Sair")
            
            try:
                choice = int(input("Escolha uma opção: "))
            except ValueError:
                print("⚠️ Por favor, insira um número válido.")
                continue
            
            if choice == 1:
                self.create_vehicle()
            
            elif choice == 2:
                self.read_vehicles()
            
            elif choice == 3:
                self.update_vehicle()
            
            elif choice == 4:
                self.delete_vehicle()
            
            elif choice == 5:
                print("Saindo do sistema...")
                break
            
            else:
                print("⚠️ Opção inválida, por favor escolha uma opção de 1 a 5.")

# if __name__ == "__main__":
#     menu = DisplayCargoVehicleMenu()
#     menu.show_menu()

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manager.cargo_vehicle_type import CargoVehicleType
from crud_db.cargo_vehicle_type_CRUD import CargoVehicleTypeCRUD  # ajuste conforme seu caminho

def DisplayCargoVehicleType():
    crud = CargoVehicleTypeCRUD()

    while True:
        print("\n--- Menu de Tipos de Veículos de Carga ---")
        print("1. Cadastrar novo tipo de veículo")
        print("2. Listar todos os tipos de veículos")
        print("3. Buscar tipo de veículo por ID")
        print("4. Atualizar tipo de veículo")
        print("5. Deletar tipo de veículo")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                id_ = int(input("ID do tipo de veículo: "))
                descricao = input("Descrição: ")
                rota = input("Recomendação de rota (URBAN / HIGHWAY / MIXED): ").upper()
                novo_tipo = CargoVehicleType(id_, descricao, rota)
                crud.create(novo_tipo)
                print("Tipo de veículo cadastrado com sucesso.")
            except Exception as e:
                print(f"Erro ao cadastrar: {e}")

        elif escolha == "2":
            print("\n--- Lista de Tipos de Veículos ---")
            for tipo in crud.read_all():
                print(tipo)

        elif escolha == "3":
            try:
                id_ = int(input("ID do tipo de veículo a buscar: "))
                tipo = crud.read_by_id(id_)
                if tipo:
                    print(tipo)
                else:
                    print("Tipo de veículo não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif escolha == "4":
            try:
                id_ = int(input("ID do tipo de veículo a atualizar: "))
                nova_desc = input("Nova descrição (ou deixe em branco para manter): ")
                nova_rota = input("Nova rota (URBAN / HIGHWAY / MIXED) (ou deixe em branco): ").upper()
                updated = crud.update(id_, 
                                      new_description=nova_desc if nova_desc else None, 
                                      new_route=nova_rota if nova_rota else None)
                if updated:
                    print("Tipo de veículo atualizado.")
                else:
                    print("Tipo de veículo não encontrado.")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "5":
            try:
                id_ = int(input("ID do tipo de veículo a deletar: "))
                if crud.delete(id_):
                    print("Deletado com sucesso.")
                else:
                    print("Tipo de veículo não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# if __name__ == "__main__":
#     DisplayCargoVehicleType()

from detector import detect_plate
from driver_manager import register_driver, list_drivers

def main():
    print("Reconhecimento de Placas - Sistema Iniciado")
    while True:
        print("\n1. Detectar placa\n2. Cadastrar motorista\n3. Listar motoristas\n4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            detect_plate()
        elif escolha == "2":
            name = input("Nome do motorista: ")
            plate = input("Placa do veículo: ")
            register_driver(name, plate)
        elif escolha == "3":
            list_drivers()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

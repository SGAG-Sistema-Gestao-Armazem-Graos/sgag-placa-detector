from driver import Driver

drivers = []

def register_driver(name, plate):
    driver = Driver(name=name, plate=plate)
    drivers.append(driver)
    print(f"Motorista {name} com placa {plate} registrado com sucesso.")

def list_drivers():
    print("\n--- Lista de Motoristas ---")
    if not drivers:
        print("Nenhum motorista cadastrado.")
    for d in drivers:
        print(f"Nome: {d.name}, Placa: {d.plate}")

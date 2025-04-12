import json
from datetime import date
from typing import List, Optional
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manager.storage_location import StorageLocation

class StorageLocationCRUD:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def _load_data(self) -> List[StorageLocation]:
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
            return [StorageLocation(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, locations: List[StorageLocation]) -> None:
        with open(self.file_name, "w") as f:
            json.dump([loc.__dict__ for loc in locations], f, default=str, indent=4)

    def create(self, location: StorageLocation) -> None:
        locations = self._load_data()
        locations.append(location)
        self._save_data(locations)

    def read_all(self) -> List[StorageLocation]:
        return self._load_data()

    def read_by_id(self, location_id: int) -> Optional[StorageLocation]:
        locations = self._load_data()
        for loc in locations:
            if loc.location_id == location_id:
                return loc
        return None

    def update(self, location_id: int, updated_data: dict) -> bool:
        locations = self._load_data()
        for loc in locations:
            if loc.location_id == location_id:
                for key, value in updated_data.items():
                    setattr(loc, key, value)
                self._save_data(locations)
                return True
        return False

    def delete(self, location_id: int) -> bool:
        locations = self._load_data()
        for loc in locations:
            if loc.location_id == location_id:
                locations.remove(loc)
                self._save_data(locations)
                return True
        return False


# Exemplo de uso no bloco `if __name__ == "__main__":`
if __name__ == "__main__":
    # Inicializar CRUD
    storage_crud = StorageLocationCRUD("storage_locations.json")

    # Criando um novo local de armazenamento
    new_location = StorageLocation(
        location_id=1,
        location_type_id=5,
        location_type="WAREHOUSE",
        name="Armazém Central",
        address="Av. dos Transportes, 1234",
        storage_capacity=10000.50,
        last_inspection=date(2024, 10, 1),
        notes="Próxima inspeção recomendada em breve"
    )
    
    # Adicionando novo local
    storage_crud.create(new_location)

    # Lendo todos os locais
    all_locations = storage_crud.read_all()
    print("Todos os locais de armazenamento:")
    for location in all_locations:
        print(location)

    # Lendo um local específico por ID
    location = storage_crud.read_by_id(1)
    if location:
        print(f"Local encontrado: {location}")
    else:
        print("Local não encontrado.")

    # Atualizando um local
    updated_data = {
        "name": "Novo Armazém Central",
        "address": "Rua dos Armazéns, 5678",
        "storage_capacity": 12000.0
    }
    storage_crud.update(1, updated_data)

    # Lendo o local atualizado
    updated_location = storage_crud.read_by_id(1)
    print(f"Local atualizado: {updated_location}")

    # Deletando um local
    storage_crud.delete(1)
    print("Local deletado.")

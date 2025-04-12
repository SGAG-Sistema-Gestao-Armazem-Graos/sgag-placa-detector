import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manager.grain_type import GrainType



class GrainTypeCRUD:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def _load_data(self):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_data(self, data):
        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)

    def create(self, grain_type: GrainType):
        data = self._load_data()
        entry = {
            "grain_type_id": grain_type.get_grain_type_id(),
            "name": grain_type.get_name(),
            "ideal_moisture": grain_type.get_ideal_moisture(),
            "observations": grain_type.get_observations()
        }
        data.append(entry)
        self._save_data(data)

    def read_all(self):
        data = self._load_data()
        return [GrainType(**item) for item in data]

    def update(self, grain_type_id: int, new_data: dict):
        data = self._load_data()
        updated = False
        for item in data:
            if item["grain_type_id"] == grain_type_id:
                item.update(new_data)
                updated = True
                break
        if updated:
            self._save_data(data)

    def delete(self, grain_type_id: int):
        data = self._load_data()
        data = [item for item in data if item["grain_type_id"] != grain_type_id]
        self._save_data(data)


if __name__ == "__main__":
    crud = GrainTypeCRUD("grain_types.json")

    # Criar e salvar
    grain = GrainType(1, "Milho", 14, "Grão comum em safras de verão")
    crud.create(grain)

    # Ler todos
    print("Todos os registros:")
    for g in crud.read_all():
        print(g)

    # Atualizar
    crud.update(1, {"ideal_moisture": 13})

    # Deletar
    crud.delete(1)

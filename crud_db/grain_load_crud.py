import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json

from manager.grain_load_type import GrainLoadType


class GrainLoadCRUD:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def _load_data(self) -> list:
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def _save_data(self, data: list):
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def create(self, grain_load: GrainLoadType):
        data = self._load_data()
        item = {
            "grain_load_type_id": grain_load.get_grain_load_type_id(),
            "grain_type_id": grain_load.get_grain_type_id(),
            "load_id": grain_load.get_load_id(),
            "grain_moisture": grain_load.get_grain_moisture(),
            "initial_weight": grain_load.get_initial_weight(),
            "final_weight": grain_load.get_final_weight(),
        }
        data.append(item)
        self._save_data(data)

    def read_all(self) -> list:
        data = self._load_data()
        return [GrainLoadType(**item) for item in data]

    def update(self, grain_load_type_id: int, updated_data: dict):
        data = self._load_data()
        for item in data:
            if item["grain_load_type_id"] == grain_load_type_id:
                item.update(updated_data)
                break
        self._save_data(data)

    def delete(self, grain_load_type_id: int):
        data = self._load_data()
        data = [item for item in data if item["grain_load_type_id"] != grain_load_type_id]
        self._save_data(data)

# if __name__ == "__main__":
#     crud = GrainLoadCRUD('grain_loads.json')

#     # Criando e salvando
#     sample = GrainLoadType(1, 3, 2, 14, 500.0, 480.5)
#     crud.create(sample)

#     # Lendo todos
#     entries = crud.read_all()
#     for entry in entries:
#         print(entry)

#     # Atualizando
#     crud.update(1, {"final_weight": 475.0})

#     # Deletando
#     crud.delete(1)

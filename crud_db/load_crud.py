import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manager.load import Load



class LoadCRUD:
    def __init__(self, filename: str):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _load_data(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def create(self, load: Load):
        data = self._load_data()
        data.append({
            "load_id": load.get_load_id(),
            "initial_total_weight": load.get_initial_total_weight(),
            "final_total_weight": load.get_final_total_weight()
        })
        self._save_data(data)

    def read_all(self):
        data = self._load_data()
        return [Load(item["load_id"], item["initial_total_weight"], item["final_total_weight"]) for item in data]

    def update(self, load_id: int, updated_fields: dict):
        data = self._load_data()
        updated = False
        for item in data:
            if item["load_id"] == load_id:
                item.update(updated_fields)
                updated = True
                break
        if updated:
            self._save_data(data)
        else:
            raise ValueError("Load ID not found.")

    def delete(self, load_id: int):
        data = self._load_data()
        new_data = [item for item in data if item["load_id"] != load_id]
        if len(new_data) == len(data):
            raise ValueError("Load ID not found.")
        self._save_data(new_data)


if __name__ == "__main__":
    crud = LoadCRUD("loads.json")

    # Criar e salvar
    load = Load(load_id=1, initial_total_weight=1000.0, final_total_weight=950.5)
    crud.create(load)

    # Ler todos
    print("=== Cargas salvas ===")
    for l in crud.read_all():
        print(l)

    # Atualizar
    crud.update(1, {"final_total_weight": 940.0})

    # Ler novamente para ver mudança
    print("=== Após atualização ===")
    for l in crud.read_all():
        print(l)

    # Deletar
    crud.delete(1)

    # Confirmar remoção
    print("=== Após exclusão ===")
    for l in crud.read_all():
        print(l)

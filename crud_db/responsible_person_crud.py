import json
from typing import List
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manager.responsible_person import ResponsiblePerson

class ResponsiblePersonCRUD:
    """
    CRUD operations for ResponsiblePerson.

    This class handles creating, reading, updating, and deleting ResponsiblePerson
    objects from a JSON file.

    Attributes:
        file_name (str): Name of the file where data is stored.
    """

    def __init__(self, file_name: str):
        self.file_name = file_name

    def _read_data(self) -> List[dict]:
        """Reads data from the JSON file."""
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_data(self, data: List[dict]):
        """Writes data to the JSON file."""
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def create(self, responsible_person: ResponsiblePerson):
        """Creates a new ResponsiblePerson entry."""
        data = self._read_data()
        data.append({
            "responsible_id": responsible_person.get_responsible_id(),
            "location_id": responsible_person.get_location_id(),
            "name": responsible_person.get_name(),
            "phone": responsible_person.get_phone(),
            "email": responsible_person.get_email()
        })
        self._write_data(data)

    def read_all(self) -> List[ResponsiblePerson]:
        """Reads all ResponsiblePerson entries."""
        data = self._read_data()
        return [
            ResponsiblePerson(
                responsible_id=entry["responsible_id"],
                location_id=entry["location_id"],
                name=entry["name"],
                phone=entry["phone"],
                email=entry["email"]
            ) for entry in data
        ]

    def update(self, responsible_id: int, updated_data: dict):
        """Updates a ResponsiblePerson entry by responsible_id."""
        data = self._read_data()
        for entry in data:
            if entry["responsible_id"] == responsible_id:
                entry.update(updated_data)
                break
        self._write_data(data)

    def delete(self, responsible_id: int):
        """Deletes a ResponsiblePerson entry by responsible_id."""
        data = self._read_data()
        data = [entry for entry in data if entry["responsible_id"] != responsible_id]
        self._write_data(data)

# Exemplo de uso no bloco `if __name__ == "__main__":`

if __name__ == "__main__":
    # Criação de uma instância CRUD
    crud = ResponsiblePersonCRUD('responsible_persons.json')

    # Criando um novo responsável
    responsible = ResponsiblePerson(
        responsible_id=1,
        location_id=101,
        name="Carlos Silva",
        phone="(62)91234-5678",
        email="carlos.silva@email.com"
    )
    crud.create(responsible)

    # Lendo todos os responsáveis
    print("Lista de responsáveis:")
    for resp in crud.read_all():
        print(resp)

    # Atualizando um responsável
    crud.update(1, {"phone": "(62)98765-4321"})  # Atualizando o telefone

    # Deletando um responsável
    crud.delete(1)

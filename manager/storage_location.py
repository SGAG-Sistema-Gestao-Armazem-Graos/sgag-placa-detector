from datetime import date
from typing import Optional

class StorageLocation:
    """
    Represents a storage location with its type, capacity, and inspection information.

    Attributes:
        location_id (int): Unique identifier for the location.
        location_type_id (int): Foreign key to location type.
        location_type (str): Type of the location (e.g., 'WAREHOUSE', 'DEPOT', etc.).
        name (str): Name of the storage location.
        address (str): Address of the storage location.
        storage_capacity (float): Storage capacity in cubic meters or kilograms.
        last_inspection (date): Date of the last inspection.
        notes (str): Additional notes or comments about the location.
    """

    def __init__(self,
                 location_id: int,
                 location_type_id: int,
                 location_type: str,
                 name: str,
                 address: str,
                 storage_capacity: float,
                 last_inspection: Optional[date],
                 notes: Optional[str] = ""):
        self.location_id = location_id
        self.location_type_id = location_type_id
        self.location_type = location_type
        self.name = name
        self.address = address
        self.storage_capacity = storage_capacity
        self.last_inspection = last_inspection
        self.notes = notes

    def __str__(self):
        return (
            f"StorageLocation("
            f"ID: {self.location_id}, "
            f"Type: {self.location_type}, "
            f"Name: {self.name}, "
            f"Address: {self.address}, "
            f"Capacity: {self.storage_capacity}, "
            f"Last Inspection: {self.last_inspection}, "
            f"Notes: {self.notes})"
        )

    def needs_inspection(self, threshold_days: int = 180) -> bool:
        """
        Determines whether a new inspection is needed based on the number of days since the last one.

        Args:
            threshold_days (int): Number of days before another inspection is required.

        Returns:
            bool: True if a new inspection is needed, False otherwise.
        """
        if not self.last_inspection:
            return True
        delta = (date.today() - self.last_inspection).days
        return delta > threshold_days

    # Getters for all attributes
    def get_location_id(self):
        return self.location_id

    def get_location_type_id(self):
        return self.location_type_id

    def get_location_type(self):
        return self.location_type

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_storage_capacity(self):
        return self.storage_capacity

    def get_last_inspection(self):
        return self.last_inspection

    def get_notes(self):
        return self.notes

# Exemplo de uso no bloco `if __name__ == "__main__":`

if __name__ == "__main__":
    from datetime import datetime

    location = StorageLocation(
        location_id=1,
        location_type_id=5,
        location_type="WAREHOUSE",
        name="Armazém Central",
        address="Av. dos Transportes, 1234",
        storage_capacity=10000.50,
        last_inspection=date(2024, 10, 1),
        notes="Próxima inspeção recomendada em breve"
    )

    print(location)
    print("Precisa de nova inspeção?", location.needs_inspection())

    # Usando os getters
    print(f"ID do local de armazenamento: {location.get_location_id()}")
    print(f"Tipo do local de armazenamento: {location.get_location_type()}")
    print(f"Nome: {location.get_name()}")
    print(f"Endereço: {location.get_address()}")
    print(f"Capacidade de armazenamento: {location.get_storage_capacity()} m³")
    print(f"Última inspeção: {location.get_last_inspection()}")
    print(f"Notas: {location.get_notes()}")
    
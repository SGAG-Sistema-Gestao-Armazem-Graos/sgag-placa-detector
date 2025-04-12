from manager.storage_location import StorageLocation

class ResponsiblePerson:
    """
    Represents the person responsible for a storage location.

    Attributes:
        responsible_id (int): Unique identifier for the responsible person.
        location_id (int): ID referencing the associated storage location.
        name (str): Name of the responsible person.
        phone (str): Phone number (max 15 characters).
        email (str): Email address.
    """

    def __init__(self, 
                 responsible_id: int, 
                 location_id: StorageLocation, 
                 name: str, 
                 phone: str, 
                 email: str):
        self.responsible_id = responsible_id
        self.location_id = location_id
        self.name = name
        self.phone = phone
        self.email = email

    # Getters
    def get_responsible_id(self) -> int:
        return self.responsible_id

    def get_location_id(self) -> int:
        return self.location_id

    def get_name(self) -> str:
        return self.name

    def get_phone(self) -> str:
        return self.phone

    def get_email(self) -> str:
        return self.email

    # Other methods
    def has_valid_email(self) -> bool:
        """
        Checks if the email appears valid (basic check).
        
        Returns:
            bool: True if the email contains '@' and '.', otherwise False.
        """
        return '@' in self.email and '.' in self.email.split('@')[-1]

    def __str__(self):
        return (
            f"ResponsiblePerson("
            f"ID: {self.responsible_id}, "
            f"Location ID: {self.location_id}, "
            f"Name: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email})"
        )
    
# if __name__ == "__main__":
#     responsible = ResponsiblePerson(
#         responsible_id=1,
#         location_id=101,
#         name="Carlos Silva",
#         phone="(62)91234-5678",
#         email="carlos.silva@email.com"
#     )

#     print(responsible)
    
#     # Verificando se o email é válido
#     if responsible.has_valid_email():
#         print("Email válido.")
#     else:
#         print("Email inválido.")
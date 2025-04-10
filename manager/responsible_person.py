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
                 location_id: int, 
                 name: str, 
                 phone: str, 
                 email: str):
        self.responsible_id = responsible_id
        self.location_id = location_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (
            f"ResponsiblePerson("
            f"ID: {self.responsible_id}, "
            f"Location ID: {self.location_id}, "
            f"Name: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email})"
        )

    def has_valid_email(self) -> bool:
        """
        Checks if the email appears valid (basic check).
        
        Returns:
            bool: True if the email contains '@' and '.', otherwise False.
        """
        return '@' in self.email and '.' in self.email.split('@')[-1]

#if __name__ == "__main__":
#    responsible = ResponsiblePerson(
#        responsible_id=1,
#        location_id=101,
#        name="Carlos Silva",
#        phone="(62)91234-5678",
#        email="carlos.silva@email.com"
#    )

#    print(responsible)
#    
#    if responsible.has_valid_email():
#        print("Email válido.")
#    else:
#        print("Email inválido.")
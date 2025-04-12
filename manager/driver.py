from manager.driver_license import DriverLicense  # Importando a classe corretamente

class Driver:
    """
    Represents a driver with personal data and a linked driver's license.
    """

    def __init__(self, driver_id: int, name: str, cpf: str, driver_license: DriverLicense, phone: str, email: str):
        self._driver_id = driver_id
        self._name = name
        self._cpf = cpf
        self._driver_license = driver_license
        self._phone = phone
        self._email = email

    def __str__(self) -> str:
        return f"Driver({self._driver_id}): {self._name} - License: {self._driver_license.get_license_number()}"

    def is_valid_email(self) -> bool:
        return "@" in self._email and "." in self._email

    # Getters
    def get_driver_id(self) -> int:
        return self._driver_id

    def get_name(self) -> str:
        return self._name

    def get_cpf(self) -> str:
        return self._cpf

    def get_driver_license(self) -> DriverLicense:
        return self._driver_license

    def get_phone(self) -> str:
        return self._phone

    def get_email(self) -> str:
        return self._email

# from datetime import date
# from manager.driver_license import DriverLicense

# if __name__ == "__main__":
#     license = DriverLicense(
#         license_id=1,
#         driver_id=1,
#         license_number="12345678901",
#         category="B",
#         issue_date=date(2021, 1, 10),
#         expiry_date=date(2026, 1, 10),
#         is_valid=True,
#         notes="Condução de veículos leves"
#     )

#     driver = Driver(
#         driver_id=1,
#         name="Maria Oliveira",
#         cpf="11122233344",
#         driver_license=license,
#         phone="(62)91234-5678",
#         email="maria@example.com"
#     )

#     print(driver)
#     print("CNH válida?", "Sim" if not license.is_expired() else "Não")
#     print("Email válido?", "Sim" if driver.is_valid_email() else "Não")

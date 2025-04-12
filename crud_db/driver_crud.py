import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Optional
from manager.driver import Driver

class DriverCRUD:
    """
    Responsável por realizar operações CRUD com objetos da classe Driver.
    """

    def __init__(self):
        self._drivers: List[Driver] = []

    def create_driver(self, driver: Driver) -> None:
        """Adiciona um novo motorista à lista."""
        self._drivers.append(driver)

    def get_driver_by_id(self, driver_id: int) -> Optional[Driver]:
        """Retorna o motorista com o ID correspondente."""
        for driver in self._drivers:
            if driver.get_driver_id() == driver_id:
                return driver
        return None

    def update_driver_email(self, driver_id: int, new_email: str) -> bool:
        """Atualiza o e-mail do motorista com base no ID."""
        driver = self.get_driver_by_id(driver_id)
        if driver:
            driver._email = new_email  # Acesso direto por ser interno
            return True
        return False

    def delete_driver(self, driver_id: int) -> bool:
        """Remove um motorista com base no ID."""
        driver = self.get_driver_by_id(driver_id)
        if driver:
            self._drivers.remove(driver)
            return True
        return False

    def list_all_drivers(self) -> List[Driver]:
        """Retorna todos os motoristas cadastrados."""
        return self._drivers

from datetime import date
from manager.driver_license import DriverLicense
from manager.driver import Driver

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

#     manager = DriverCRUD()
#     manager.create_driver(driver)

#     print("👩‍💼 Motorista Criada:")
#     print(manager.get_driver_by_id(1))
#     print("Email válido?", "Sim" if driver.is_valid_email() else "Não")

#     print("\n🔄 Atualizando e-mail...")
#     manager.update_driver_email(1, "novoemail@maria.com")

#     print("\n📋 Lista de todos os motoristas:")
#     for d in manager.list_all_drivers():
#         print(d)

#     print("\n❌ Removendo motorista...")
#     manager.delete_driver(1)

#     print("\n📋 Lista final:")
#     print(manager.list_all_drivers())

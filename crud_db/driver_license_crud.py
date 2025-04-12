from datetime import date
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Optional

from manager.driver_license import DriverLicense



class DriverLicenseCRUD:
    """
    Class to handle CRUD operations for DriverLicense records.
    """
    def __init__(self):
        self.driver_licenses = {}

    def create(self, license: DriverLicense) -> None:
        if license.get_license_id() in self.driver_licenses:
            raise ValueError("License ID already exists.")
        self.driver_licenses[license.get_license_id()] = license
        print(f"License with ID {license.get_license_id()} created.")

    def read(self, license_id: int) -> Optional[DriverLicense]:
        return self.driver_licenses.get(license_id, None)

    def update(self, license_id: int, updated_license: DriverLicense) -> None:
        if license_id not in self.driver_licenses:
            raise ValueError(f"License with ID {license_id} not found.")
        self.driver_licenses[license_id] = updated_license
        print(f"License with ID {license_id} updated.")

    def delete(self, license_id: int) -> None:
        if license_id not in self.driver_licenses:
            raise ValueError(f"License with ID {license_id} not found.")
        del self.driver_licenses[license_id]
        print(f"License with ID {license_id} deleted.")

    def list_all(self) -> List[DriverLicense]:
        return list(self.driver_licenses.values())
    
    from datetime import date



# if __name__ == "__main__":
#     license1 = DriverLicense(
#         license_id=1,
#         driver_id=101,
#         license_number="12345678901",
#         category="D",
#         issue_date=date(2020, 5, 1),
#         expiry_date=date(2025, 5, 1),
#         is_valid=True,
#         notes="Profissional"
#     )

#     license2 = DriverLicense(
#         license_id=2,
#         driver_id=102,
#         license_number="98765432100",
#         category="B",
#         issue_date=date(2019, 6, 1),
#         expiry_date=date(2024, 6, 1),
#         is_valid=False,
#         notes="Uso pessoal"
#     )

#     crud = DriverLicenseCRUD()
#     crud.create(license1)
#     crud.create(license2)

#     print("\nTodas as CNHs:")
#     for lic in crud.list_all():
#         print(lic)

#     print("\nVerificando CNH com ID 1:")
#     print(crud.read(1))

#     print("\nAtualizando CNH com ID 1:")
#     updated = DriverLicense(
#         license_id=1,
#         driver_id=101,
#         license_number="12345678901",
#         category="D",
#         issue_date=date(2020, 5, 1),
#         expiry_date=date(2026, 5, 1),
#         is_valid=True,
#         notes="Renovada"
#     )
#     crud.update(1, updated)

#     print("\nRemovendo CNH com ID 2:")
#     crud.delete(2)

#     print("\nCNHs após remoção:")
#     for lic in crud.list_all():
#         print(lic)


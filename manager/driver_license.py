from datetime import date

class DriverLicense:
    """
    Represents a driver's license (CNH) record.
    """

    def __init__(self,
                 license_id: int,
                 driver_id: int,
                 license_number: str,
                 category: str,
                 issue_date: date,
                 expiry_date: date,
                 is_valid: bool,
                 notes: str = ""):
        self._license_id = license_id
        self._driver_id = driver_id
        self._license_number = license_number
        self._category = category
        self._issue_date = issue_date
        self._expiry_date = expiry_date
        self._is_valid = is_valid
        self._notes = notes

    def __str__(self):
        return (f"DriverLicense(ID: {self._license_id}, Driver: {self._driver_id}, "
                f"CNH: {self._license_number}, Category: {self._category}, "
                f"Issue: {self._issue_date}, Expiry: {self._expiry_date}, "
                f"Valid: {'Yes' if self._is_valid else 'No'}, Notes: {self._notes})")

    def is_expired(self, today: date = date.today()) -> bool:
        """
        Checks if the license is expired.

        Args:
            today (date): Current date to check against (default: today).

        Returns:
            bool: True if the license is expired, False otherwise.
        """
        return today > self._expiry_date

    # Getters
    def get_license_id(self):
        return self._license_id

    def get_driver_id(self):
        return self._driver_id

    def get_license_number(self):
        return self._license_number

    def get_category(self):
        return self._category

    def get_issue_date(self):
        return self._issue_date

    def get_expiry_date(self):
        return self._expiry_date

    def get_is_valid(self):
        return self._is_valid

    def get_notes(self):
        return self._notes


# # Manual test block
# if __name__ == "__main__":
#     license = DriverLicense(
#         license_id=1,
#         driver_id=101,
#         license_number="12345678901",
#         category="D",
#         issue_date=date(2020, 5, 1),
#         expiry_date=date(2025, 5, 1),
#         is_valid=True,
#         notes="Professional driver"
#     )

#     print(license)
#     print("Is the license expired?", "Yes" if license.is_expired() else "No")

#     # Testing the getters
#     # print("License ID:", license.get_license_id())
#     # print("Driver ID:", license.get_driver_id())
#     # print("License Number:", license.get_license_number())
#     # print("Category:", license.get_category())
#     # print("Issue Date:", license.get_issue_date())
#     # print("Expiry Date:", license.get_expiry_date())
#     # print("Is Valid:", license.get_is_valid())
#     # print("Notes:", license.get_notes())

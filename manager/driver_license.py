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
        self.license_id = license_id
        self.driver_id = driver_id
        self.license_number = license_number
        self.category = category
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.is_valid = is_valid
        self.notes = notes

    def __str__(self):
        return (f"DriverLicense(ID: {self.license_id}, Driver: {self.driver_id}, "
                f"CNH: {self.license_number}, Category: {self.category}, "
                f"Issue: {self.issue_date}, Expiry: {self.expiry_date}, "
                f"Valid: {'Yes' if self.is_valid else 'No'}, Notes: {self.notes})")

    def is_expired(self, today: date = date.today()) -> bool:
        """
        Checks if the license is expired.

        Args:
            today (date): Current date to check against (default: today).

        Returns:
            bool: True if the license is expired, False otherwise.
        """
        return today > self.expiry_date


# Manual test block
if __name__ == "__main__":
    license = DriverLicense(
        license_id=1,
        driver_id=101,
        license_number="12345678901",
        category="D",
        issue_date=date(2020, 5, 1),
        expiry_date=date(2025, 5, 1),
        is_valid=True,
        notes="Professional driver"
    )

    print(license)
    print("Is the license expired?", "Yes" if license.is_expired() else "No")

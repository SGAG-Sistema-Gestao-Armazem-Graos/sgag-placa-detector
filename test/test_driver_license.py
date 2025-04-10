import unittest
from datetime import date, timedelta

from manager.driver_license import DriverLicense


class TestDriverLicense(unittest.TestCase):

    def setUp(self):
        self.license = DriverLicense(
            license_id=1,
            driver_id=100,
            license_number="98765432100",
            category="B",
            issue_date=date(2020, 1, 1),
            expiry_date=date.today() + timedelta(days=30),
            is_valid=True,
            notes="Test license"
        )

    def test_license_str(self):
        self.assertIn("DriverLicense", str(self.license))
        self.assertIn("98765432100", str(self.license))

    def test_is_expired_false(self):
        self.assertFalse(self.license.is_expired())

    def test_is_expired_true(self):
        expired_license = DriverLicense(
            license_id=2,
            driver_id=101,
            license_number="12345678900",
            category="C",
            issue_date=date(2015, 1, 1),
            expiry_date=date.today() - timedelta(days=1),
            is_valid=False,
            notes="Expired license"
        )
        self.assertTrue(expired_license.is_expired())

if __name__ == '__main__':
    unittest.main()

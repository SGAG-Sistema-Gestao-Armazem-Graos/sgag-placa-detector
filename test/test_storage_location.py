import unittest
from datetime import date, timedelta

from manager.storage_location import StorageLocation



class TestStorageLocation(unittest.TestCase):

    def setUp(self):
        self.location = StorageLocation(
            location_id=1,
            location_type_id=10,
            location_type="WAREHOUSE",
            name="Depósito Central",
            address="Rua das Cargas, 1000",
            storage_capacity=5000.00,
            last_inspection=date.today() - timedelta(days=90),
            notes="Local limpo e organizado"
        )

    def test_str_representation(self):
        self.assertIn("Depósito Central", str(self.location))
        self.assertIn("WAREHOUSE", str(self.location))

    def test_needs_inspection_false(self):
        self.assertFalse(self.location.needs_inspection())

    def test_needs_inspection_true(self):
        self.location.last_inspection = date.today() - timedelta(days=200)
        self.assertTrue(self.location.needs_inspection())

    def test_needs_inspection_no_date(self):
        self.location.last_inspection = None
        self.assertTrue(self.location.needs_inspection())


if __name__ == "__main__":
    unittest.main()

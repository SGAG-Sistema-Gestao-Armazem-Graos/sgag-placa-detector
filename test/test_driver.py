import unittest

from manager.driver import Driver


class TestDriver(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(
            driver_id=1,
            name="Alice Smith",
            cpf="98765432100",
            driver_type="PERMANENT",
            phone="(11)12345-6789",
            email="alice@example.com"
        )

    def test_str_representation(self):
        self.assertIn("Alice Smith", str(self.driver))
        self.assertIn("PERMANENT", str(self.driver))

    def test_valid_email(self):
        self.assertTrue(self.driver.is_valid_email())

    def test_invalid_email(self):
        driver = Driver(
            driver_id=2,
            name="Bob",
            cpf="11122233344",
            driver_type="TEMPORARY",
            phone="(11)98765-4321",
            email="bob[at]mail"
        )
        self.assertFalse(driver.is_valid_email())


if __name__ == '__main__':
    unittest.main()

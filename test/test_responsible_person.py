import unittest

from manager.responsible_person import ResponsiblePerson



class TestResponsiblePerson(unittest.TestCase):
    def setUp(self):
        self.person = ResponsiblePerson(
            responsible_id=1,
            location_id=101,
            name="Carlos Silva",
            phone="(62)91234-5678",
            email="carlos@email.com"
        )

    def test_str_representation(self):
        self.assertIn("Carlos Silva", str(self.person))
        self.assertIn("ID: 1", str(self.person))

    def test_valid_email(self):
        self.assertTrue(self.person.has_valid_email())

    def test_invalid_email(self):
        self.person.email = "carlos.email.com"
        self.assertFalse(self.person.has_valid_email())

if __name__ == "__main__":
    unittest.main()

import unittest
from datetime import datetime
from crud_db.cargo_vehicle_crud import CargoVehicleCRUD
from manager.cargo_vehicle import CargoVehicle


class TestCargoVehicleCRUD(unittest.TestCase):
    
    def setUp(self):
        """Método chamado antes de cada teste"""
        self.manager = CargoVehicleCRUD()
        self.vehicle_1 = CargoVehicle(
            vehicle_id=1,
            vehicle_type_id=101,
            brand="Mercedes-Benz",
            vehicle_description="Caminhão baú",
            plate="ABC1D23",
            chassis="MB1234567890XYZ",
            model_year=datetime.now().year,
            manufacture_year=datetime.now().year - 1,
            cargo_capacity=12.0
        )
        self.vehicle_2 = CargoVehicle(
            vehicle_id=2,
            vehicle_type_id=102,
            brand="Scania",
            vehicle_description="Caminhão tanque",
            plate="XYZ4E56",
            chassis="SCN9876543210QWE",
            model_year=datetime.now().year,
            manufacture_year=datetime.now().year - 2,
            cargo_capacity=15.5
        )
    
    def test_create_vehicle(self):
        """Testa se o veículo é criado corretamente"""
        self.manager.create_vehicle(self.vehicle_1)
        self.assertEqual(len(self.manager.vehicles), 1)
        self.assertEqual(self.manager.vehicles[0].vehicle_id, 1)
        self.assertEqual(self.manager.vehicles[0].brand, "Mercedes-Benz")
    
    def test_read_vehicles(self):
        """Testa a leitura dos veículos"""
        self.manager.create_vehicle(self.vehicle_1)
        self.manager.create_vehicle(self.vehicle_2)
        with self.assertLogs(level='INFO') as log:
            self.manager.read_vehicles()
        self.assertIn("Caminhão baú", log.output[0])  # Verifica a descrição do veículo

    def test_update_vehicle(self):
        """Testa a atualização de um veículo"""
        self.manager.create_vehicle(self.vehicle_1)
        self.manager.update_vehicle(1, brand="Mercedes-Benz Atualizada", cargo_capacity=13.0)
        updated_vehicle = self.manager.vehicles[0]
        self.assertEqual(updated_vehicle.brand, "Mercedes-Benz Atualizada")
        self.assertEqual(updated_vehicle.cargo_capacity, 13.0)

    def test_delete_vehicle(self):
        """Testa a exclusão de um veículo"""
        self.manager.create_vehicle(self.vehicle_1)
        self.manager.create_vehicle(self.vehicle_2)
        self.manager.delete_vehicle(2)
        self.assertEqual(len(self.manager.vehicles), 1)
        self.assertEqual(self.manager.vehicles[0].vehicle_id, 1)
    
    def test_update_vehicle_not_found(self):
        """Testa a tentativa de atualizar um veículo que não existe"""
        self.manager.create_vehicle(self.vehicle_1)
        with self.assertLogs(level='ERROR') as log:
            self.manager.update_vehicle(3, brand="Não Existe")
        self.assertIn("🚫 Veículo com ID 3 não encontrado.", log.output[0])

    def test_delete_vehicle_not_found(self):
        """Testa a tentativa de excluir um veículo que não existe"""
        self.manager.create_vehicle(self.vehicle_1)
        with self.assertLogs(level='ERROR') as log:
            self.manager.delete_vehicle(3)
        self.assertIn("🚫 Veículo com ID 3 não encontrado.", log.output[0])


if __name__ == "__main__":
    unittest.main()

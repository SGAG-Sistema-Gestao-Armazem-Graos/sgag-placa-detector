import unittest
from decimal import Decimal
from datetime import datetime

from manager.stock_history import StockHistory


class TestStockHistory(unittest.TestCase):
    def setUp(self):
        self.stock = StockHistory(
            stock_history_id=1,
            location_id=10,
            cargo_id=20,
            movement_id=30,
            update_datetime=datetime(2025, 4, 10, 14, 0),
            initial_quantity=Decimal('100.00'),
            current_quantity=Decimal('130.00'),
            quantity_in=Decimal('50.00'),
            quantity_out=Decimal('20.00')
        )

    def test_compute_current_quantity(self):
        expected = Decimal('130.00')
        result = self.stock.compute_current_quantity()
        self.assertEqual(result, expected)

    def test_str_representation(self):
        self.assertIn("StockHistory(ID: 1", str(self.stock))


if __name__ == "__main__":
    unittest.main()

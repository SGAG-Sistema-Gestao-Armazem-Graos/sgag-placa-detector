from datetime import datetime
from decimal import Decimal
from typing import Optional

class StockHistory:
    """
    Represents the historical stock record of a cargo at a specific location.

    Attributes:
        stock_history_id (int): Unique identifier for the stock history entry.
        location_id (int): ID of the location.
        cargo_id (int): ID of the cargo.
        movement_id (int): ID of the related movement.
        update_datetime (datetime): Date and time of the update.
        initial_quantity (Decimal): Quantity of cargo at the beginning.
        current_quantity (Decimal): Current quantity of cargo.
        quantity_in (Decimal): Quantity of cargo received (in).
        quantity_out (Decimal): Quantity of cargo dispatched (out).
    """

    def __init__(
        self,
        stock_history_id: int,
        location_id: int,
        cargo_id: int,
        movement_id: int,
        update_datetime: datetime,
        initial_quantity: Decimal,
        current_quantity: Decimal,
        quantity_in: Decimal,
        quantity_out: Decimal
    ):
        self.stock_history_id = stock_history_id
        self.location_id = location_id
        self.cargo_id = cargo_id
        self.movement_id = movement_id
        self.update_datetime = update_datetime
        self.initial_quantity = initial_quantity
        self.current_quantity = current_quantity
        self.quantity_in = quantity_in
        self.quantity_out = quantity_out

    def __str__(self):
        return (
            f"StockHistory("
            f"ID: {self.stock_history_id}, Location ID: {self.location_id}, Cargo ID: {self.cargo_id}, "
            f"Movement ID: {self.movement_id}, Updated: {self.update_datetime}, "
            f"Initial Qty: {self.initial_quantity}, Current Qty: {self.current_quantity}, "
            f"Qty In: {self.quantity_in}, Qty Out: {self.quantity_out})"
        )

    def compute_current_quantity(self) -> Decimal:
        """
        Computes the current quantity based on initial, in, and out quantities.

        Returns:
            Decimal: The recalculated current quantity.
        """
        return self.initial_quantity + self.quantity_in - self.quantity_out

# Manual test block
#if __name__ == "__main__":
#    stock = StockHistory(
#        stock_history_id=1,
#        location_id=101,
#        cargo_id=202,
#        movement_id=303,
#        update_datetime=datetime.now(),
#        initial_quantity=Decimal('100.00'),
#        current_quantity=Decimal('130.00'),
#        quantity_in=Decimal('50.00'),
#        quantity_out=Decimal('20.00')
#    )

#    print(stock)
#    print("Recalculated current quantity:", stock.compute_current_quantity())

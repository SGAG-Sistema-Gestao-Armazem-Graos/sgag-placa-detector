class Load:
    """
    Represents cargo weight information.

    Attributes:
        load_id (int): Unique identifier of the cargo.
        initial_total_weight (float): Initial total weight.
        final_total_weight (float): Final total weight.
    """

    def __init__(self, load_id: int, initial_total_weight: float, final_total_weight: float):
        self.load_id = load_id
        self.initial_total_weight = initial_total_weight
        self.final_total_weight = final_total_weight

    def weight_difference(self):
        """Returns the difference between initial and final weights."""
        return self.initial_total_weight - self.final_total_weight

    def __str__(self):
        return (
            f"Load(ID: {self.load_id}, "
            f"Initial Weight: {self.initial_total_weight}, "
            f"Final Weight: {self.final_total_weight})"
        )


# Quick test (only runs when this file is executed directly)
#if __name__ == "__main__":
#    load = Load(
#        load_id=1,
#        initial_total_weight=1000.0,
#        final_total_weight=950.5
#    )
#    print(load)
#    print("Weight difference:", load.weight_difference())

class GrainLoadType:
    """
    Represents a specific type of grain load.

    Attributes:
        grain_load_type_id (int): Unique ID for the grain load type.
        grain_type_id (int): ID of the grain type.
        load_id (int): ID of the related load.
        grain_moisture (int): Grain moisture percentage.
        initial_weight (float): Initial grain weight.
        final_weight (float): Final grain weight.
    """

    def __init__(self, grain_load_type_id: int, grain_type_id: int, load_id: int,
                 grain_moisture: int, initial_weight: float, final_weight: float):
        self.grain_load_type_id = grain_load_type_id
        self.grain_type_id = grain_type_id
        self.load_id = load_id
        self.grain_moisture = grain_moisture
        self.initial_weight = initial_weight
        self.final_weight = final_weight

    def lost_weight(self):
        """Calculates the weight lost during the process."""
        return self.initial_weight - self.final_weight

    def __str__(self):
        return (
            f"GrainLoadType(ID: {self.grain_load_type_id}, Type: {self.grain_type_id}, "
            f"Load: {self.load_id}, Moisture: {self.grain_moisture}%, "
            f"Initial: {self.initial_weight}, Final: {self.final_weight})"
        )


#if __name__ == "__main__":
#    sample = GrainLoadType(
#        grain_load_type_id=1,
#        grain_type_id=3,
#        load_id=2,
#        grain_moisture=14,
#        initial_weight=500.0,
#        final_weight=480.5
#    )
#    print(sample)
#    print("Lost weight:", sample.lost_weight())

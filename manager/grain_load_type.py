from manager.grain_type import GrainType
from manager.load import Load

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

    def __init__(self, grain_load_type_id: int, grain_type_id: GrainType, load_id: Load,
                 grain_moisture: int, initial_weight: float, final_weight: float):
        self.grain_load_type_id = grain_load_type_id
        self.grain_type_id = grain_type_id
        self.load_id = load_id
        self.grain_moisture = grain_moisture
        self.initial_weight = initial_weight
        self.final_weight = final_weight

    # Getters
    def get_grain_load_type_id(self) -> int:
        return self.grain_load_type_id

    def get_grain_type_id(self) -> int:
        return self.grain_type_id

    def get_load_id(self) -> int:
        return self.load_id

    def get_grain_moisture(self) -> int:
        return self.grain_moisture

    def get_initial_weight(self) -> float:
        return self.initial_weight

    def get_final_weight(self) -> float:
        return self.final_weight

    # Other methods
    def lost_weight(self) -> float:
        """Calculates the weight lost during the process."""
        return self.initial_weight - self.final_weight

    def __str__(self):
        return (
            f"GrainLoadType(ID: {self.grain_load_type_id}, Type: {self.grain_type_id}, "
            f"Load: {self.load_id}, Moisture: {self.grain_moisture}%, "
            f"Initial: {self.initial_weight}, Final: {self.final_weight})"
        )
    
# if __name__ == "__main__":
#     sample = GrainLoadType(
#         grain_load_type_id=1,
#         grain_type_id=3,
#         load_id=2,
#         grain_moisture=14,
#         initial_weight=500.0,
#         final_weight=480.5
#     )

#     print(sample)
#     print("Peso perdido:", sample.lost_weight())
#     print("ID do tipo de carga:", sample.grain_load_type_id)
#     print("ID do tipo de grão:", sample.grain_type_id)
#     print("ID da carga:", sample.load_id)
#     print("Umidade do grão:", sample.grain_moisture)
#     print("Peso inicial:", sample.initial_weight)
#     print("Peso final:", sample.final_weight)

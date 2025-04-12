class GrainType:
    """
    Represents a specific type of grain.

    Attributes:
        grain_type_id (int): Unique identifier for the grain type.
        name (str): Name of the grain type.
        ideal_moisture (int): Ideal moisture percentage for the grain.
        observations (str): Additional notes or observations about the grain type.
    """

    def __init__(self, grain_type_id: int, name: str, ideal_moisture: int, observations: str):
        self.grain_type_id = grain_type_id
        self.name = name
        self.ideal_moisture = ideal_moisture
        self.observations = observations

    # Getters
    def get_grain_type_id(self) -> int:
        return self.grain_type_id

    def get_name(self) -> str:
        return self.name

    def get_ideal_moisture(self) -> int:
        return self.ideal_moisture

    def get_observations(self) -> str:
        return self.observations

    def __str__(self):
        return (
            f"GrainType(ID: {self.grain_type_id}, Name: {self.name}, "
            f"Ideal Moisture: {self.ideal_moisture}%, Observations: {self.observations})"
        )


# if __name__ == "__main__":
#     sample_grain_type = GrainType(
#         grain_type_id=1,
#         name="Corn",
#         ideal_moisture=14,
#         observations="Common in summer crops"
#     )
    
#     print(sample_grain_type)
#     print("ID:", sample_grain_type.get_grain_type_id())
#     print("Nome:", sample_grain_type.get_name())
#     print("Umidade ideal:", sample_grain_type.get_ideal_moisture())
#     print("Observações:", sample_grain_type.get_observations())

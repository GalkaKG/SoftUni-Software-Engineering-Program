from project.software.software import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
        self.capacity_consumption = floor(capacity_consumption + (capacity_consumption * 0.50))
        self.memory_consumption = floor(memory_consumption / 2)


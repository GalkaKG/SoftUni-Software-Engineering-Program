from project.software.software import Software
from math import floor


class ExpressSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Express", capacity_consumption, memory_consumption)
        self.memory_consumption = floor(memory_consumption * 2)

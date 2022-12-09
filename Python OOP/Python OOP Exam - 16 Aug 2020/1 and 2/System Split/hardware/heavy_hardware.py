from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)
        self.capacity = capacity * 2
        self.memory = floor(memory * 0.75)

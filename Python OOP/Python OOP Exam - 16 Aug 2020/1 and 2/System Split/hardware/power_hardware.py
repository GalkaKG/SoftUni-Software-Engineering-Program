from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)
        self.capacity = floor(capacity * 0.25)
        self.memory = memory + floor(memory * 0.75)

     

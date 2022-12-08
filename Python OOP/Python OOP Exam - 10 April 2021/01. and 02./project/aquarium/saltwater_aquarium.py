from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    capacity = 25

    def __init__(self, name: str):
        super().__init__(name, self.capacity)

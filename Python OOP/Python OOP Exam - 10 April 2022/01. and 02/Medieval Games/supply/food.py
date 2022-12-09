from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)

    def details(self):
        return f"Food: {self.name}, {self.energy}"

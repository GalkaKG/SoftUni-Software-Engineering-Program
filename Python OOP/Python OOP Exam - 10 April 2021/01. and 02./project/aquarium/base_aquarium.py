from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value
        
    def calculate_comfort(self):
        sum_comfort = 0
        for decoration in self.decorations:
            sum_comfort += decoration.comfort
        return sum_comfort

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity"

        fish_type = fish.__class__.__name__
        if fish_type in ["FreshwaterFish", "SaltwaterFish"]:
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f'{self.name}:\n'
        if not self.fish:
            result += f'Fish: none\n'
        else:
            result += f'Fish: {" ".join([f.name for f in self.fish])}' + "\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def _find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def _find_decoration(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        else:
            return "Invalid aquarium type."

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        else:
            return "Invalid decoration type."

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self._find_aquarium(aquarium_name)
        decoration = self._find_decoration(decoration_type)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)

            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self._find_aquarium(aquarium_name)
        if not aquarium:
            return

        if aquarium.capacity == len(aquarium.fish):
            return "Not enough capacity."

        fish = None
        aquarium_type = aquarium.__class__.__name__
        message = "Water not suitable."

        if fish_type == "FreshwaterFish":
            if aquarium_type == "FreshwaterAquarium":
                fish = FreshwaterFish(fish_name, fish_species, price)
            else:
                return message
        elif fish_type == "SaltwaterFish":
            if aquarium_type == "SaltwaterAquarium":
                fish = SaltwaterFish(fish_name, fish_species, price)
            else:
                return message
        else:
            return f"There isn't a fish of type {fish_type}."

        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self._find_aquarium(aquarium_name)
        if not aquarium:
            return
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self._find_aquarium(aquarium_name)
        if not aquarium:
            return

        total_sum = 0
        for fish in aquarium.fish:
            total_sum += fish.price
        for decoration in aquarium.decorations:
            total_sum += decoration.price

        return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

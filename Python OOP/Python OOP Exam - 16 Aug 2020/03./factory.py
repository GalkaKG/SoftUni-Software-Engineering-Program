from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}  # key: name of the ingredient and value: quantity of the ingredient

    @abstractmethod
    def add_ingredient(self, type, quantity):
        """Add products to the factory"""
        pass

    @abstractmethod
    def remove_ingredient(self, type, quantity):
        """Remove products from the factory"""
        pass

    def can_add(self, value):
        return self.capacity - sum(self.ingredients.values()) - value >= 0

    def __repr__(self):
        result = ""
        result += f"Factory name: {self.name} with capacity {self.capacity}.\n"
        for ingredient in self.ingredients:
            result += f"{ingredient}: {self.ingredients[ingredient]}\n"
        return result

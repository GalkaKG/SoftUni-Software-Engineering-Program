from .factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def add_ingredient(self, product_type, product_quantity):
        if product_type in self.valid_ingredients:
            if self.can_add(product_quantity):
                if product_type not in self.ingredients:
                    self.ingredients[product_type] = 0
                self.ingredients[product_type] += product_quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, product_type, product_quantity):
        if product_type in self.ingredients:
            if self.ingredients[product_type] - product_quantity >= 0:
                self.ingredients[product_type] -= product_quantity
            else:
                raise ValueError("Ingredients quantity cannot be less than zero")
        else:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients

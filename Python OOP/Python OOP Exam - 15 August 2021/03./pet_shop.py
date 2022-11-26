class PetShop:
    def __init__(self, name: str):
        self.name = name
        self.food = {}
        self.pets = []

    def add_food(self, name: str, quantity: float):
        if quantity <= 0:
            raise ValueError('Quantity cannot be equal to or less than 0')

        if name not in self.food:
            self.food[name] = 0
        self.food[name] += quantity
        return f"Successfully added {quantity:.2f} grams of {name}."

    def add_pet(self, name: str):
        if name not in self.pets:
            self.pets.append(name)
            return f"Successfully added {name}."
        raise Exception("Cannot add a pet with the same name")

    def feed_pet(self, food_name: str, pet_name: str):
        if pet_name not in self.pets:
            raise Exception(f"Please insert a valid pet name")

        if food_name not in self.food:
            return f'You do not have {food_name}'

        if self.food[food_name] < 100:
            self.add_food(food_name, 1000.00)
            return "Adding food..."

        self.food[food_name] -= 100
        return f"{pet_name} was successfully fed"

    def __repr__(self):
        return f'Shop {self.name}:\n' \
               f'Pets: {", ".join(self.pets)}'

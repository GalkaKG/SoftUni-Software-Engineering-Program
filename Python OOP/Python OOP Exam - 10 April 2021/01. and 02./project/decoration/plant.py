from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    comfort = 5
    price = 10

    def __init__(self):
        super().__init__(self.comfort, self.price)

from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, model: str, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def minimum_speed(self):
        return 250

    @property
    def maximum_speed(self):
        return 450

from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def _find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [c.model for c in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))
        elif car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))
        else:
            return
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if driver_name not in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_car = None
        for car in self.cars:
            if type(car).__name__ == car_type and not car.is_taken:
                available_car = car

        driver = [d for d in self.drivers if d.name == driver_name][0]

        if not available_car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = available_car
            available_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {available_car.model}."

        driver.car = available_car
        available_car.is_taken = True
        return f"Driver {driver_name} chose the car {available_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if race_name not in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_name not in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."
    
     def start_race(self, race_name: str):
        race = self._find_race(race_name)
        if race not in self.races:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        fastest_drivers = []
        counter = 0
        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit):
            if counter == 3:
                break
            driver.number_of_wins += 1
            fastest_drivers.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            counter += 1

        return '\n'.join(fastest_drivers)

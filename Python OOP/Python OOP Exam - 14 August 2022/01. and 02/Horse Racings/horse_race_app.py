from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def _find_horse(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def _find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def _find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self._find_horse(horse_name)

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self._find_jockey(jockey_name)

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey(jockey_name)
        horse = None

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for h in reversed(self.horses):
            if not h.is_taken and h.__class__.__name__ == horse_type:
                horse = h
                break

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self._find_race(race_type)
        jockey = self._find_jockey(jockey_name)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self._find_race(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        highest_speed = 0

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is" \
               f" {winner.name}! Winner's horse: {winner.horse.name}."

      

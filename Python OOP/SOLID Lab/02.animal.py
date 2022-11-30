# OCP
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Chicken(Animal):
    def make_sound(self):
        return "Peow"


class Pig(Animal):
    def make_sound(self):
        return "Gruh"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken(), Pig()]
animal_sound(animals)

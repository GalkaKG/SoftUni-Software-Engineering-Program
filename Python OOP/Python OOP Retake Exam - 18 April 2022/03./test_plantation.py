from project.plantation import Plantation

# from testing.plantation import Plantation
from unittest import TestCase


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(20)

    def test_init_proper_initialization(self):
        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_if_less_than_zero_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_if_already_hired_raise_error(self):
        self.plantation.hire_worker("Ivan")

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(f"Ivan successfully hired.", result)
        self.assertEqual(1, len(self.plantation.workers))

    def test_len_return_count_plants(self):
        self.assertEqual(0, self.plantation.plants.__len__())

        self.plantation.plants = {"Ivan": ["plant1", "plant2"]}
        self.assertEqual(2, self.plantation.__len__())

        self.plantation.plants = {"Ivan": ["plant1", "plant2"], "Gosho": ["plant3", "plant4"]}
        self.assertEqual(4, self.plantation.__len__())

    def test_planting_worker_does_not_exist_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Ivan", "plant1")

        self.assertEqual(f"Worker with name Ivan is not hired!", str(error.exception))

    def test_planting_when_plantation_is_full(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {"Ivan": ["a", "b", "c", "d", "e", "1", "2", "1", "a", "a",
                                           "j", "g", "k", "l", "m", "b", "c", "n", "h"]}
        self.plantation.planting("Ivan", "k")
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Ivan", "asd")

        self.assertEqual("The plantation is full!", str(error.exception))

    def test_planting_worker_exist_and_successfully_planted(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {"Ivan": ["a"]}
        result = self.plantation.planting("Ivan", "flower")

        self.assertEqual(f"Ivan planted flower.", result)
        self.assertEqual({"Ivan": ["a", "flower"]}, self.plantation.plants)

    def test_planting_wrong_dict_assigment(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.pl.planting('Martin', 'carrots')
        self.assertEqual(len(self.pl.plants['Martin']), 2)

    def test_planting_successfully_first_plant_for_that_worker(self):
        self.plantation.hire_worker("Ivan")
        result = self.plantation.planting("Ivan", "flower")

        self.assertEqual(f"Ivan planted it's first flower.", result)

    def test_str_if_its_proper(self):
        self.plantation.plants = {"Ivan": ["a", "b"], "Gosho": ["asd"]}
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Gosho")

        result = f"Plantation size: 20\nIvan, Gosho\nIvan planted: a, b\nGosho planted: asd"

        self.assertEqual(result, self.plantation.__str__())

    def test_str_without_workers(self):
        result = f"Plantation size: 20\n"
        self.assertEqual(result, self.plantation.__str__())

    def test_repr_if_proper_represents(self):
        self.plantation.hire_worker("Ivan")
        result = f'Size: 20\nWorkers: Ivan'

        self.assertEqual(result, self.plantation.__repr__())

    def test_repr_if_proper_represents_without_workers(self):
        result = f'Size: 20\nWorkers: '

        self.assertEqual(result, self.plantation.__repr__())





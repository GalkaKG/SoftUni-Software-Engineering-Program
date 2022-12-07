from project.pet_shop import PetShop
from unittest import TestCase


class PetShopTests(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Shop")

    def test_init(self):
        self.assertEqual("Shop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_negative_quantity_or_equal_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("meet", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("meet", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_add_name_to_food_dict(self):
        self.pet_shop.add_food("meet", 5)
        self.assertEqual({"meet": 5}, self.pet_shop.food)

    def test_add_food_sum_quantity_of_food_return_correct_message(self):
        self.pet_shop.food = {"meet": 10}
        result = self.pet_shop.add_food("meet", 20)

        self.assertEqual(f"Successfully added 20.00 grams of meet.", result)
        self.assertEqual({"meet": 30}, self.pet_shop.food)

    def test_add_pet_if_not_exist(self):
        result = self.pet_shop.add_pet("Tomy")

        self.assertEqual(f"Successfully added Tomy.", result)
        self.assertEqual(["Tomy"], self.pet_shop.pets)

    def test_add_pet_if_already_exist_raise_error(self):
        self.pet_shop.pets = ["Tomy"]

        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet("Tomy")

        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_feed_pet_if_pet_not_exist_raise_error(self):
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet("meet", "Tomy")

        self.assertEqual(f"Please insert a valid pet name", str(error.exception))

    def test_feed_pet_dont_have_of_that_name_food(self):
        self.pet_shop.add_pet("Tomy")
        result = self.pet_shop.feed_pet("meet", "Tomy")

        self.assertEqual(f'You do not have meet', result)

    def test_add_food_if_quantity_is_under_100_add_it(self):
        self.pet_shop.add_pet("Tomy")
        self.pet_shop.add_food("meet", 90)

        result = self.pet_shop.feed_pet("meet", "Tomy")

        self.assertEqual("Adding food...", result)
        self.assertEqual({"meet": 1090}, self.pet_shop.food)

    def test_add_food_when_successfully_added(self):
        self.pet_shop.add_pet("Tomy")
        self.pet_shop.add_food("meet", 120)

        result = self.pet_shop.feed_pet("meet", "Tomy")

        self.assertEqual(f"Tomy was successfully fed", result)
        self.assertEqual({"meet": 20}, self.pet_shop.food)

    def test_repr_if_correct_represent(self):
        self.pet_shop.add_pet("Tomy")
        self.pet_shop.add_pet("Cat")

        result = f'Shop {self.pet_shop.name}:\n' \
            f'Pets: Tomy, Cat'

        self.assertEqual(result, self.pet_shop.__repr__())


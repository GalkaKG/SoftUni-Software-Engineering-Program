from project.toy_store import ToyStore
from unittest import TestCase


class ToyStoreTests(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_init_if_is_proper(self):
        expected = {"A": None,
                    "B": None,
                    "C": None,
                    "D": None,
                    "E": None,
                    "F": None,
                    "G": None,
                    }
        result = self.toy_store.toy_shelf
        self.assertEqual(expected, result)

    def test_add_toy_if_shelf_not_exist_raise_error(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("key", "toy")

        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_add_toy_if_toy_name_is_already_in_the_shelf_raise_error(self):
        self.toy_store.add_toy("A", "toy1")
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "toy1")

        self.assertEqual("Toy is already in shelf!", str(error.exception))

    def test_add_toy_if_shelf_is_already_taken_raise_error(self):
        self.toy_store.add_toy("A", "toy1")

        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "toy2")

        self.assertEqual("Shelf is already taken!", str(error.exception))

    def test_add_toy_if_add_is_successful(self):
        result = self.toy_store.add_toy("A", "toy1")

        self.assertEqual("Toy:toy1 placed successfully!", result)

        result_shelf = self.toy_shelf = {
            "A": "toy1",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(result_shelf, self.toy_store.toy_shelf)

    def test_remove_toy_if_shelf_not_exist_raise_error(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("key", "toy1")

        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_remove_toy_if_toy_not_exist_raise_error(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("A", "toy1")

        self.assertEqual("Toy in that shelf doesn't exists!", str(error.exception))

    def test_remove_toy_if_is_successful_removed(self):
        self.toy_store.add_toy("A", "toy1")
        result = self.toy_store.remove_toy("A", "toy1")

        self.assertEqual("Remove toy:toy1 successfully!", result)

        result_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(result_shelf, self.toy_store.toy_shelf)
        

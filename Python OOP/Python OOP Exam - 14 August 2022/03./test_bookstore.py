from project.bookstore import Bookstore

# from testing.bookstore import Bookstore
from unittest import TestCase


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.book_store = Bookstore(100)

    def test_init(self):
        self.assertEqual(100, self.book_store.books_limit)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)

    def test_books_limit_value_is_zero_or_negative_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = -1

        self.assertEqual(f"Books limit of -1 is not valid", str(error.exception))

    def test_len_count_books_available_in_store(self):
        self.book_store.receive_book("Matrix", 10)
        self.book_store.receive_book("The beach", 30)

        self.assertEqual(40, self.book_store.__len__())

    def test_receive_book_if_there_is_no_space_in_the_store(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book("Matrix", 101)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_if_there_is_enough_space_in_the_store(self):
        self.book_store.receive_book("Matrix", 20)
        self.assertEqual({"Matrix": 20}, self.book_store.availability_in_store_by_book_titles)

        self.book_store.receive_book("The beach", 30)
        self.assertEqual({"Matrix": 20, "The beach": 30}, self.book_store.availability_in_store_by_book_titles)

        self.book_store.receive_book("The beach", 30)
        self.assertEqual({"Matrix": 20, "The beach": 60}, self.book_store.availability_in_store_by_book_titles)

    def test_receive_book_take_new_availability_of_that_book(self):
        book_title = "Matrix"
        new_book_store = Bookstore(100)
        new_book_store.receive_book(book_title, 20)

        result = new_book_store.receive_book(book_title, 20)

        self.assertEqual(f"40 copies of {book_title} are available in the bookstore.", result)

    def test_sell_book_if_the_book_is_not_in_the_store(self):
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("The matrix", 10)

        self.assertEqual(f"Book The matrix doesn't exist!", str(error.exception))

    def test_sell_book_not_enough_copies_of_that_book_raise_error(self):
        self.book_store.receive_book("The matrix", 20)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("The matrix", 50)

        self.assertEqual(f"The matrix has not enough copies to sell. Left: 20", str(error.exception))

    def test_sell_book_successfully_sell_it(self):
        self.book_store.receive_book("The matrix", 50)

        self.assertEqual(f"Sold 20 copies of The matrix", self.book_store.sell_book("The matrix", 20))

        self.assertEqual({"The matrix": 30}, self.book_store.availability_in_store_by_book_titles)

    def test_str_if_has_books(self):
        book_name = "The matrix"

        result = f"Total sold books: 50\nCurrent availability: 20\n " \
                 f"- The matrix: 20 copies"

        self.book_store.receive_book(book_name, 70)
        self.book_store.sell_book(book_name, 50)

        self.assertEqual(result, self.book_store.__str__())

    def test_str_if_not_books(self):
        book_name = "The matrix"

        result = f"Total sold books: 50\nCurrent availability: 0\n - The matrix: 0 copies"

        self.book_store.receive_book(book_name, 50)
        self.book_store.sell_book(book_name, 50)

        self.assertEqual(result, self.book_store.__str__())

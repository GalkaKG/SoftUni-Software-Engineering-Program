from typing import Dict


class Bookstore:
    def __init__(self, books_limit: int):
        self.books_limit = books_limit
        self.availability_in_store_by_book_titles: Dict[str, int] = {}
        self.__total_sold_books: int = 0

    @property
    def total_sold_books(self):
        return self.__total_sold_books

    @property
    def books_limit(self):
        return self.__books_limit

    @books_limit.setter
    def books_limit(self, value: int):
        # the books limit cannot be equal or below zero
        if value <= 0:
            raise ValueError(f"Books limit of {value} is not valid")
        self.__books_limit = value

    # count the total number of books (copies) in the bookstore
    def __len__(self):
        count_books = 0
        for number_of_books in self.availability_in_store_by_book_titles.values():
            count_books += number_of_books
        return count_books

    def receive_book(self, book_title: str, number_of_books: int):
        # if there is not enough space in the bookstore
        if len(self) + number_of_books > self.books_limit:
            raise Exception("Books limit is reached. Cannot receive more books!")

        # if there is enough space in the bookstore
        if book_title not in self.availability_in_store_by_book_titles:
            self.availability_in_store_by_book_titles[book_title] = 0
        self.availability_in_store_by_book_titles[book_title] += number_of_books

        # take the new availability of that book copies and return the result
        total_number = self.availability_in_store_by_book_titles[book_title]
        return f"{total_number} copies of {book_title} are available in the bookstore."

    def sell_book(self, book_title: str, number_of_books: int):
        # if the book is not available in the bookstore
        if book_title not in self.availability_in_store_by_book_titles:
            raise Exception(f"Book {book_title} doesn't exist!")

        # if there is not enough copies of that book to sell
        if number_of_books > self.availability_in_store_by_book_titles[book_title]:
            books_left = self.availability_in_store_by_book_titles[book_title]
            raise Exception(f"{book_title} has not enough copies to sell. Left: {books_left}")

        # if can sell successfully
        self.availability_in_store_by_book_titles[book_title] -= number_of_books
        self.__total_sold_books += number_of_books
        return f"Sold {number_of_books} copies of {book_title}"

    def __str__(self):
        result = [f"Total sold books: {self.total_sold_books}"]
        result.append(f'Current availability: {len(self)}')
        for book_title, number_of_copies in self.availability_in_store_by_book_titles.items():
            result.append(f" - {book_title}: {number_of_copies} copies")
        return '\n'.join(result)

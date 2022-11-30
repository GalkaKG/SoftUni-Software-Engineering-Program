# SRP


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Book title {self.title} from {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        pass

    def find_book(self, title):
        try:
            return [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book not found"


library = Library()

for num in range(1, 21):
    book = Book(f"Title {num}", f"Author {num}")
    library.add_book(book)

print(*library.books, sep="\n")
print(library.find_book("Title 7"))

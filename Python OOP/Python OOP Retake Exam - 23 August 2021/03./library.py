class Library:
    def __init__(self, name):
        self.name = name
        self.books_by_authors = {}
        self.readers = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty string!")
        self.__name = value

    def add_book(self, author, title):
        if author not in self.books_by_authors:
            self.books_by_authors[author] = []
        if title not in self.books_by_authors[author]:
            self.books_by_authors[author].append(title)

    def add_reader(self, name):
        if name not in self.readers:
            self.readers[name] = []
        else:
            return f"{name} is already registered in the {self.name} library."

    def rent_book(self, reader_name, book_author, book_title):
        if reader_name not in self.readers:
            return f"{reader_name} is not registered in the {self.name} Library."
        if book_author not in self.books_by_authors:
            return f"{self.name} Library does not have any {book_author}'s books."
        if book_title not in self.books_by_authors[book_author]:
            return f"""{self.name} Library does not have {book_author}'s "{book_title}"."""
        self.readers[reader_name].append({book_author: book_title})
        book_title_index = self.books_by_authors[book_author].index(book_title)
        del self.books_by_authors[book_author][book_title_index]

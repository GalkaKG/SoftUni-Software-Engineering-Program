class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        output = f'Username: {self.username}, Age: {self.age}\n'
        output += 'Liked movies:\n'
        if self.movies_liked:
            for movie in self.movies_liked:
                output += movie.details() + '\n'
        else:
            output += 'No movies liked.\n'
        output += 'Owned movies:\n'
        if self.movies_owned:
            for movie in self.movies_owned:
                output += movie.details() + '\n'
        else:
            output += 'No movies owned.'
        return output



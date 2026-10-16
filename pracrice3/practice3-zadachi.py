"""Задачи: книги, электронные книги и вывод информации."""

# 1, 3, 4
from abc import ABC, abstractmethod
from datetime import datetime


class Printable(ABC):
    """Интерфейс для объектов, которые умеют печатать информацию."""

    @abstractmethod
    def print_info(self):
        """Печатает информацию об объекте."""
        pass


class Book(Printable):
    """Книга с названием, автором и годом издания."""

    def __init__(self, title, author, year):
        """Создаёт книгу."""
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Возвращает строку с информацией о книге."""
        return (
            f"Книга - {self.title}, автор - {self.author}, "
            f"год - {self.year}"
        )

    def print_info(self):
        """Печатает информацию о книге."""
        print(self.info())

    def __str__(self):
        """Возвращает информацию о книге."""
        return self.info()

    def __eq__(self, other):
        """Сравнивает книги по названию."""
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        """Возвращает возраст книги в годах."""
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        """Пересчитывает год издания по возрасту."""
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        """Создаёт книгу из строки вида 'название;автор;год'."""
        title, author, year = data.split(";")
        return cls(title, author, int(year))


book_cats = Book("Путешествия котов", "Лорд де Кот", 2000)
print(book_cats.info())
print(book_cats.age)
book_cats.print_info()
book_fishs = Book.from_string("Путешествия рыб;Барон фон Карась;2001")
print(book_fishs)
print(book_cats == book_fishs)


# 2
class Ebook(Book):
    """Электронная книга с форматом."""

    def __init__(self, title, author, year, format):
        """Создаёт электронную книгу с форматом файла."""
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """Возвращает информацию о книге вместе с форматом."""
        return (
            f"Книга - {self.title}, автор - {self.author}, "
            f"год - {self.year}, формат - {self.format}"
        )


book_dogs = Ebook("Путешествия собачек", "Барон Догвиль", 2001, "Электронный")
print(book_dogs.info())

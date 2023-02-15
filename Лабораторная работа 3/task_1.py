class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    """'Бумажная книга"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError('Страницы должны быть типа int')
        if new_pages <= 0:
            raise ValueError('Страницы должны быть положительным числом')
        self._pages = new_pages

class AudioBook(Book):
    """'Аудиокнига"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError('Длительность должна быть типа float')
        if new_duration <= 0:
            raise ValueError('Длительность должна быть положительным числом')
        self._duration = new_duration

if __name__ == '__main__':
    paper = PaperBook('Онегин', 'Пушкин', 666)
    print(paper)
    audio = AudioBook('Онегин', 'Пушкин', 777.77)
    print(audio)
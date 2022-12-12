# TODO Написать 3 класса с документацией и аннотацией типов
class Box:
    def __init__(self, a: float, b: float, c: float)->None:
        if not a:
            TypeError(" нет длины")
        if a<0:
            raise ValueError("отрицательная длина")
        if not b:
            raise TypeError(" нет ширины")
        if b<0:
            raise ValueError("отрицательная ширина")
        if not c:
            raise TypeError(" нет высоты")
        if c<0:
            raise ValueError("отрицательная высота")
        self.a=a
        self.b=b
        self.c=c
    def more_long(self, d)->float:
        ...
    def less_high(self, e)->float:
        ...
class Tovar:
    def __init__(self, price: float, sale: float) -> None:
        self.price = price
        self.sale = sale
    def inflation(self, nadbavka)->float:
        ...
    def halyava(self, economy)->float:
        ...
class Car:
    def __init__(self, massa: int, speed: float )->None:
        self.massa = massa
        speed = 40
        self.yskorenie(speed)
    def yskorenie(self, speed)->float:
        ...
    """ 
    >>> car=Car(800, 40)
    >>> car.yskorenie(90)
    """
    def ballast(self,ves)->int:
        ...
import doctest
if __name__ == "__main__":

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

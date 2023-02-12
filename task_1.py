from typing import Union


class Fly:
    """
    Базовый класс Самолет

    :param color: цвет фюзеляжа самолета, str
    :param model: название модели самзика, str
    :param fly_weight: масса без пассажиров и груза в тоннах, int or float
    :param max_speed: максимальная скорость самзика в км/ч, int

    :raise: TypeError, неправильный типу
    :raise: ValueError,  значение нереальное

    """
    def __init__(self, model: str, color: str, fly_weight: Union[int, float], max_speed: int):
        """ Валидация атрибутов объекта класса Самолет """
        if not isinstance(model, str):
            raise TypeError("The model should be a string")
        self._model = model

        if not isinstance(color, str):
            raise TypeError("The color should be a string")
        self._color = color

        if not isinstance(fly_weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if fly_weight <= 0:
            raise ValueError("The weight should be positive")
        self._fly_weight = fly_weight

        if not isinstance(max_speed, int):
            raise TypeError("The max speed should be an int")
        if max_speed <= 0:
            raise ValueError("The max speed should be positive")
        self._max_speed = max_speed

    def __str__(self) -> str:
        return f'Самолет {self._color} {self._model}. Масса: {self._fly_weight} тонн. Макс. скор: {self._max_speed}.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}модель={self._model!r}, (цвет={self._color!r}, масса={self._fly_weight}, макс. скор={self._max_speed})'

    # Защищаем базовые аргументы и даём возможность перезаписи
    # Модель, как в примере с автором книги, менять запрещаем. Остальные менять можно.
    @property
    def model(self) -> str:
        """ получаем модель самолета """
        return self._model

    @property
    def color(self) -> str:
        """ получаем цвет самолета """
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        """ дадим новый цвет """
        if not isinstance(new_color, str):
            raise TypeError("The color should be a string")
        self._color = new_color

    @property
    def weight(self) -> int or float:
        """ установим массу """
        return self._fly_weight

    @weight.setter
    def weight(self, new_weight: Union[int, float]) -> None:
        """ новая масса """
        if not isinstance(new_weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if new_weight <= 0:
            raise ValueError("The weight should be positive")
        self._fly_weight = new_weight

    @property
    def max_speed(self) -> int:
        """ макс скорость """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int) -> None:
        if not isinstance(new_max_speed, int):
            raise TypeError("The max speed should be an int")
        if new_max_speed <= 0:
            raise ValueError("The max speed should be positive")
        self._max_speed = new_max_speed

    def max_kinetic_energy(self) -> float:
        """
        максимальная кинетическая энергия в джоулях.
        Наследуется в неизменном виде дочерними классами.
        """
        return (self._fly_weight * (self.max_speed / 3.6) ** 2) / 2

    def fuel_consumption(self) -> float:
        """
        расход в тоннах/час
        Этот метод может быть переопределен в дочерних классах для расчета расхода топлива
        иным образом.
        """
        return None

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        """
         максимальная грузоподъемность самолета в тоннах.
        грузоподъемность рассчитывается как разница между максимально допустимой массой
        и его собственной массой (без пассажиров и груза).

        :param max_weight: максимально допустимая масса в тоннах, int or float

        """
        # Параметр max_weight указан здесь, а не в __init__, чтобы передавать его только тогда, когда нужно
        if not isinstance(max_weight, tuple([int, float])):
            raise TypeError("The max weight should be an int or float")
        if max_weight <= 0:
            raise ValueError("The max weight should be positive")
        self.max_weight = max_weight
        return self.max_weight - self._fly_weight


class Plane_passenger(Fly):
    """
    Дочерний класс пассажирский самолет

    :param body_type: количество двигателей, int

    """
    def __init__(self, model, color, vehicle_weight, max_speed, body_type: int):  # аннотацию типов убрал, чтобы меньше дублировать код
        super().__init__(model, color, vehicle_weight, max_speed)  # вызываем конструктор родительского класса для его расширения
        if not isinstance(body_type, int):
            raise TypeError("The body type should be a int")
        self.body_type = body_type

    def __str__(self) -> str:
        return f'{super().__str__()} Body type: {self.body_type}.'  # наследуем и дополняем __str__

    def __repr__(self) -> str:  # а вот метод __repr__ придется перегружать из-за одной скобки
        return f'{self.__class__.__name__}(модель={self._model!r}, цвет={self._color!r}, вес={self._fly_weight}, макс. скорость={self._max_speed}, количество двигателей={self.body_type!r})'

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        """ Допустим, для сверхлегкого самолета грузоподъёмность хотим возвращать не в тоннах,
         а в килограммах """
        super(Plane_passenger, self).calculate_payload(max_weight)
        return (self.max_weight - self._fly_weight) * 1000


class Cargo_plane(Fly):
    """
    Дочерний класс Грузовой самолет

    :param fuel_tank: возможность добавить топливные баки ( да или нет), bool

    """
    def __init__(self, color, model, vehicle_weight, max_speed, fuel_tank: bool):
        super().__init__(color, model, vehicle_weight, max_speed)
        if not isinstance(fuel_tank, bool):
            raise TypeError("The fuel_tank availability should be a string")
        self.fuel_tank = fuel_tank

    def __str__(self) -> str:
        return f'{super().__str__()} возможность навесить топливные баки: {self.fuel_tank}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(цвет={self._color!r}, модель={self._model!r}, вес={self._fly_weight}, максимальная скороть={self._max_speed}, топливный бак={self.fuel_tank})'

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        super(Cargo_plane, self).calculate_payload(max_weight)
        return self.max_weight - self._fly_weight / 2  # просто для примера


if __name__ == "__main__":
    fly = Fly('Антонов', 'желтый', 2000, 1500)
    print(fly)

    passenger = Plane_passenger('кукурузник', 'белый', 4, 280, 1)
    print(passenger)
    print("Payload:", passenger.calculate_payload(5), "кг")

    cargo_plane = Cargo_plane('ИЛ-86', 'белый', 300, 800, False)
    print(cargo_plane)
    print("Максимальная кинетическая энергия:", cargo_plane.max_kinetic_energy())  # наследуемый метод
    print("перегруз:", cargo_plane.calculate_payload(450))  # перегружаемый метод
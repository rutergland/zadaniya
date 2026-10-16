"""Практика 2: виды транспорта."""


class Transport:
    """Базовый транспорт с названием."""

    def __init__(self, name):
        """Создаёт транспорт с названием."""
        self.name = name

    def description(self):
        """Возвращает описание транспорта."""
        return f"Транспорт - {self.name}"


class Car(Transport):
    """Автомобиль с цветом."""

    def __init__(self, name, color):
        """Создаёт автомобиль с названием и цветом."""
        self.color = color
        super().__init__(name)

    def description(self):
        """Возвращает описание автомобиля."""
        return f"Автомобиль {self.name}, цвет: {self.color}"


class Plane(Transport):
    """Самолёт с максимальной высотой полёта."""

    def __init__(self, name, max_heights):
        """Создаёт самолёт с названием и максимальной высотой."""
        self.max_heights = max_heights
        super().__init__(name)

    def description(self):
        """Возвращает описание самолёта."""
        return (
            f"Самолёт {self.name}, "
            f"максимальная высота полёта: {self.max_heights}"
        )


class Ship(Transport):
    """Корабль с длиной."""

    def __init__(self, name, length):
        """Создаёт корабль с названием и длиной."""
        self.length = length
        super().__init__(name)

    def description(self):
        """Возвращает описание корабля."""
        return f"Корабль {self.name}, длина: {self.length}"


car = Car("VAZ", "чёрный")
plane = Plane("Boeing", 16_000)
ship = Ship("Hyundai", 150)
print(car.description())
print(plane.description())
print(ship.description())

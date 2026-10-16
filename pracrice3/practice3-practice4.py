"""Практика 4: симулятор космического корабля."""


class SpaceShip:
    """Космический корабль: топливо, корпус и скорость."""

    def __init__(self, name, fuel, shell, speed):
        """Создаёт корабль с топливом, корпусом и скоростью."""
        self.name = name
        self.fuel = fuel
        self.shell = shell
        self.speed = speed

    def set_speed(self, speed):
        """Устанавливает скорость корабля."""
        self.speed = speed

    def damage(self, damage):
        """Уменьшает прочность корпуса, не опуская её ниже нуля."""
        self.shell -= damage
        if self.shell < 0:
            self.shell = 0

    def __str__(self):
        """Возвращает строку с состоянием корабля."""
        return (
            f"{self.name}: топливо {self.fuel}, "
            f"корпус {self.shell}, скорость {self.speed}"
        )


class CrewMember:
    """Член экипажа: здоровье, навыки и роль."""

    def __init__(self, name, role, skills, health):
        """Создаёт члена экипажа."""
        self.name = name
        self.health = health
        self.skills = skills
        self.role = role

    def damage(self, damage):
        """Уменьшает здоровье, не опуская его ниже нуля."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def __str__(self):
        """Возвращает строку с именем, ролью и здоровьем."""
        return f"{self.name} ({self.role}): здоровье {self.health}"


class Mission:
    """Миссия с целью, ресурсами и событиями."""

    def __init__(self, goal, resources, events):
        """Создаёт миссию."""
        self.goal = goal
        self.resources = resources
        self.events = events

    def start(self, ship, crew):
        """Запускает миссию и применяет события к кораблю и экипажу."""
        print(f"Миссия: {self.goal}")
        for event in self.events:
            if event == "авария":
                ship.damage(30)
                for member in crew:
                    member.damage(10)
                print("Авария, корпус и экипаж повреждены")
            elif event == "астероиды":
                ship.damage(20)
                print("Столкновение с астероидом, корпус повреждён")


ship = SpaceShip("Муха", 100, 100, 0)
cleaner = CrewMember("Вася", "уборщик", "уборка", 100)
pilot = CrewMember("Петя", "пилот", "пилотирование", 100)
mission = Mission(
    "Долететь до Луны", {"пища": 100, "кислород": 100}, ["авария", "астероиды"]
)

ship.set_speed(50)
mission.start(ship, [pilot, cleaner])

print(ship)
print(cleaner)
print(pilot)

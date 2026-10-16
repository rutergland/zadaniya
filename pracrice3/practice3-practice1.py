"""Практика 1: расчёт зарплат сотрудников разных должностей."""


class Employee:
    """Сотрудник с базовой зарплатой."""

    def __init__(self, id, name, base_money):
        """Создаёт сотрудника с id, именем и базовой зарплатой."""
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self):
        """Возвращает зарплату сотрудника."""
        return self.base_money


class Manager(Employee):
    """Менеджер: зарплата с бонусом."""

    def __init__(self, id, name, base_money, bonus):
        """Создаёт менеджера с бонусом."""
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self):
        """Возвращает базовую зарплату плюс бонус."""
        return self.base_money + self.bonus


class Developer(Employee):
    """Разработчик: зарплата зависит от числа проектов."""

    def __init__(self, id, name, base_money, project_sum):
        """Создаёт разработчика с количеством проектов."""
        super().__init__(id, name, base_money)
        self.project_sum = project_sum

    def calculate_salaries(self):
        """Возвращает базовую зарплату плюс оплату за проекты."""
        return self.base_money + self.project_sum * 10_000


emp_alex = Employee(0, "Alex", 50_000)
manager_ivan = Manager(1, "Ivan", 50_000, 10_000)
dev_eva = Developer(2, "Eva", 50_000, 5)

print(emp_alex.calculate_salaries())
print(manager_ivan.calculate_salaries())
print(dev_eva.calculate_salaries())

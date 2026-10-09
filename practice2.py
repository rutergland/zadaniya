"""
practice2.py

Простой калькулятор, который может складывать и делить

Автор: Александр
Версия: 1.0.0
Дата создания: 09.10.2026
"""

import numpy


def add_numbers(a: float, b: float) -> float:
    """
    Складывает два числа.

    Args:
        a (float): Первое число
        b (float): Второе число

    Returns:
        float: Сумма a и b

    Example:
        >>> add_numbers(2, 3)
        5
    """
    return a + b


def divide(a, b):
    """
    Делит первое число на второе.

    Args:
        a (float): Первое число
        b (float): Второе число

    Returns:
        float: Частное от деления a на b

    Raises:
        ValueError: Если b равно нулю

    Example:
        >>> divide(6, 3)
        2.0
    """
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    return a / b

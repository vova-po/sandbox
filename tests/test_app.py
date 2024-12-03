import pytest
from sandbox import add_numbers

# Тест для перевірки коректності додавання
def test_add_numbers():
    # Тест 1: звичайне додавання
    result = add_numbers(3, 5)
    assert result == 8  # 3 + 5 має бути 8

    # Тест 2: перевірка з від'ємними числами
    result = add_numbers(-3, 5)
    assert result == 2  # -3 + 5 має бути 2

    # Тест 3: додавання двох від'ємних чисел
    result = add_numbers(-3, -5)
    assert result == -8  # -3 + -5 має бути -8

    # Тест 4: додавання з нулем
    result = add_numbers(0, 5)
    assert result == 5  # 0 + 5 має бути 5

    # Тест 5: додавання великих чисел
    result = add_numbers(1000000, 2000000)
    assert result == 3000000  # 1000000 + 2000000 має бути 3000000

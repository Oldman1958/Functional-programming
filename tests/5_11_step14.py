"""
Декоратор counting_calls
Реализуйте декоратор counting_calls,
который будет подсчитывать количество вызовов оригинальной функции.

После декорирования при помощи counting_calls у функции должен появиться атрибут call_count,
который отслеживает текущее количество вызовов.
"""

from functools import wraps


def counting_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Увеличиваем счётчик перед вызовом оригинальной функции
        wrapper.call_count += 1
        return func(*args, **kwargs)
        # Инициализируем атрибут счётчика

    wrapper.call_count = 0
    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print(add.call_count)
print(add(30, 5))
print(add.call_count)


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add(10, b=20))
print(add(30, 5))
print(add(3, 5))
print(add(4, 5))
print('Количество вызовов =', add.call_count)
print(add(11, 5))
print('Количество вызовов =', add.call_count)

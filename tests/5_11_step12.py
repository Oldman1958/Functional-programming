"""
Декоратор reverse.
Реализуйте декоратор reverse, который сделает так,
чтобы декорированная функция принимала все свои позиционные аргументы в обратном порядке.
Именованные аргументы должны игнорироваться декоратором reverse.

Также нужно сохранить информацию о декорируемой функции.
"""

from functools import wraps


def reverse(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # Изменяем порядок позиционных аргументов
        reversed_args = args[::-1]
        # Вызываем оригинальную функцию с обратным порядком аргументов
        return func(*reversed_args)


    return inner


@reverse
def get_max_index(*args):
    if not args:
        return None
    max_index = 0
    for i in range(len(args)):
        if args[i] > args[max_index]:
            max_index = i
    return max_index


print(get_max_index(1, 2, 3, 4, 5))
print(get_max_index(3, 4, 1, 5, 2))
print(get_max_index(5, 3, 4, 1, 2))
print(get_max_index.__name__)


def get_average(*args, **kwargs):
    summa = sum(args) + sum(kwargs.values())
    count = len(args) + len(kwargs)
    return summa / count


print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
# декорируем
get_average = reverse(get_average)
print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))

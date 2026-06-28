"""
Декоратор explicit_args.
Реализуйте декоратор explicit_args, который не позволяет запускать оригинальную функцию,
если были переданы позиционные аргументы.
Декоратор explicit_args должен выводить фразу

Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений

и предотвращать запуск оригинальной функции
"""
from functools import wraps

def explicit_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args:
            print("Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений")
            return None
        return func(**kwargs)
    return inner


@explicit_args
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


print(add(10, 20))


@explicit_args
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


print(add(a=10, b=20))


@explicit_args
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


print(add(10, b=20))
print(add.__name__)
print(add.__doc__)

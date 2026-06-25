"""
Сохраняем имя и docstring
Отредактируйте код так,
чтобы сохранялись оригинальное имя и док строка декорируемой функции
"""

from functools import wraps  # Импортировал декоратор wraps


def upper(func):
    @wraps(func)  # Добавил декоратор wraps
    def inner(*args, **kwargs):
        """
        Внутренняя функция декоратора
        """
        return func(*args, **kwargs).upper()

    return inner


@upper
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate.__name__)
print(concatenate.__doc__.strip())

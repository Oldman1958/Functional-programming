"""
Декоратор add_args
Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения:
строку «begin» в начало аргументов, строку «end» в конец.
Также декоратор должен сохранить первоначальное имя декорируемой функции и ее строку документации
"""

import copy
from functools import wraps


def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        copied_args = copy.deepcopy(args)
        copied_kwargs = copy.deepcopy(kwargs)
        new_args = ('begin',) + args + ('end',)
        return func(*new_args, **copied_kwargs)

    return wrapper


@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(concatenate('my', 'name is', 'Artem'))
print(concatenate.__name__)
print(concatenate.__doc__.strip())

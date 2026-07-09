"""
Декоратор pass_arguments
Ваша задача написать параметризированный декоратор pass_arguments,
который принимает произвольное количество именованных и позиционных аргументов
и пробрасывает их дополнительно к аргументам, которые передаются при вызове оригинальной функции
"""

from functools import wraps


def pass_arguments(*args, **kwargs):
    def decorator(func):
        @wraps(func)
        def inner(*args_dec, **kwargs_dec):
            new_args = args_dec + args
            new_kwargs = kwargs_dec | kwargs
            return func(*new_args, **new_kwargs)

        return inner

    return decorator


@pass_arguments(1, 2, 3)
def add(*values):
    return sum(values)


print(add(5, 4, 6))


@pass_arguments(s='Когда', w='-', r='нибудь!')
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))

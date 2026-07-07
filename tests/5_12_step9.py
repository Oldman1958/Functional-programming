"""
Декоратор monkey_patching - 2
Ваша задача переписать декоратор monkey_patching.
Ранее он заменял значения всех переданных аргументов при вызове оригинальной функции
следующим образом:

    ➕ значение каждого позиционного аргумента заменяется на строку «Monkey»

    ➕ значение каждого именованного аргумента заменяется на строку «patching»

Теперь необходимо завести параметры arg и kwarg,
при помощи которых можно влиять на значения,
которые будут проставляться в позиционные и именованные аргументы.
Параметры arg и kwarg являются необязательными для передачи,
их значения по умолчанию «Monkey» и «patching» соответственно.
"""

from functools import wraps


def monkey_patching(arg="Monkey", kwarg="patching"):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            new_args = (arg,) * len(args)
            new_kwargs = {key: kwarg for key in kwargs}
            return func(*new_args, **new_kwargs)

        return inner

    return decorator


@monkey_patching(arg='Super')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)


@monkey_patching(kwarg='Duper')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)


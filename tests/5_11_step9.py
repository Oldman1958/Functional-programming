"""
Декоратор no_side_effects_decorator
Напишите декоратор no_side_effects_decorator,
который защищает от побочных эффектов при работе функции — то есть не допускает
изменения переданных аргументов.

Особенно важно защититься от таких побочных эффектов,
как изменение изменяемых объектов, например списков или словарей.

📌 Ваша задача — сделать так, чтобы функция, обёрнутая в декоратор no_side_effects_decorator,
не могла изменить переданные в неё объекты.
При этом функция должна работать корректно и возвращать нужный результат.
"""
import copy
from functools import wraps


def no_side_effects_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        copied_args = copy.deepcopy(args)
        copied_kwargs = copy.deepcopy(kwargs)
        return func(*copied_args, **copied_kwargs)

    return wrapper


@no_side_effects_decorator
def add_element(data, element):
    data.append(element)
    return data


my_list = [1, 2, 3]
print('Результат вызова =', add_element(my_list, 4))
print('Результат вызова =', add_element(my_list, 5))
print(my_list)
print(add_element.__name__)


@no_side_effects_decorator
def add_element(data, key, value=None):
    data[key] = value
    return data


my_dict = {1: 'Hello', 2: 'World'}
print('Результат вызова =', add_element(my_dict, 3))
print('Результат вызова =', add_element(my_dict, 4, 'four'))
print(my_dict)
print(add_element.__name__)

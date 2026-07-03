"""
Декоратор counting_calls - 2
Усовершенствуем ранее созданный декоратор counting_calls,
добавив отслеживание переданных аргументов при каждом вызове.

Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список,
в который будут сохраняться все переданные аргументы в момент вызова в виде словаря.
Каждый словарь должен иметь два ключа: args и kwargs для сохранения соответствующих аргументов.
"""

from functools import wraps


def counting_calls(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Увеличиваем счётчик перед вызовом оригинальной функции
        wrapper.call_count += 1
        wrapper.calls.append({'args': args, 'kwargs': kwargs})
        return func(*args, **kwargs)
        # Инициализируем атрибут счётчика
    wrapper.calls = []
    wrapper.call_count = 0
    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])

"""
Функция-применитель
Напишите функцию apply, которая принимает функцию и итерируемый объект (например, список)
и применяет функцию к каждому элементу итерируемого объекта.

В качестве ответа функция apply должна вернуть список из вычисленных значений.
"""


def apply(func, obj):
    result = [func(i) for i in obj]
    return result


def square(num):
    return num ** 2


print(apply(square, [5, 7, 0, 3]))


def repeater(value, n=5):
    return str(value) * n


print(apply(repeater, ['Hi', True, 0, [1, 2]]))

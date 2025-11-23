"""
Множественное вычисление
Затем создайте функцию compute, которая принимает список функций и произвольное количество значений.
Функция compute должна применить каждую функцию к каждому значению в переданном порядке
и сформировать из полученных значений новый список, который и будет возвращаться в качестве ответа.
"""


def compute(functions, *args):
    result = [func(i) for func in functions for i in args]
    return result


def square(num):
    return num ** 2


def inc(num):
    return num + 1


def dec(num):
    return num - 1


print(compute([square, inc, dec], 10))


def square(num):
    return num ** 2


def inc(num):
    return num + 1


def dec(num):
    return num - 1


print(compute([inc, dec, square], 10, 20, 30, 40))

"""
Множественное вычисление-2
Затем создайте функцию compute, которая принимает список функций и произвольное количество значений.
Функция compute должна применить последовательно в переданном порядке все функции сразу к каждому значению
и сформировать из полученных значений новый список, который и будет возвращаться в качестве ответа.
"""


def compute(functions, *args):
    result = []
    for i in args:
        for func in functions:
            i = func(i)
        result.append(i)
    return result


def square(num):
    return num ** 2


def inc(num):
    return num + 1


def dec(num):
    return num - 1


print(compute([inc, square, dec], 10, 20, 30, 40))

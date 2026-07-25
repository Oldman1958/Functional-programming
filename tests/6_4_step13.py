"""
Напишите функцию filter_numbers, которая принимает список целых чисел и возвращает новый список,
который состоит только из четных чисел входного списка или из тех, которые по модулю больше 100.
"""


def filter_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0 or abs(x) > 100, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7]
print(filter_numbers(numbers))

numbers = [-100, 2, -300, -400, 5, -60, -61, -101, 101]
print(filter_numbers(numbers))

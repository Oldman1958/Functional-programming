"""
Напишите функцию increase_3, которая принимает список целых чисел.

Функция  increase_3 должна увеличить каждый элемент входного списка втрое,
сформировать из этих значений кортеж и вернуть в качестве результата.
"""


def increase_3(numbers):
    return tuple(x * 3 for x in numbers)


numbers = [16, -1, 8, 6, -5, -9, 22, 26, 7, -10]
print(increase_3(numbers))

numbers = [1238, 16, -53, -59, 10]
print(increase_3(numbers))

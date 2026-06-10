"""
Фильтрация
Напишите функцию filter_list, которая принимает функцию f и список lst.

Функция f обязательно должна проверять определенное условие и возвращать булев тип.

Задача функции filter_list состоит в том, чтобы вернуть новый список, составленный из элементов входного lst,
отфильтрованных согласно функции f.
"""

def filter_list(f, lst):
    return [elem for elem in lst if f(elem)]



def is_even(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_list(is_even, numbers)  # берем только четные
print(even_numbers)


def is_positive(num):
    return num > 0


numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_list(is_positive, numbers)  # берем только положительные
print(positive_numbers)
